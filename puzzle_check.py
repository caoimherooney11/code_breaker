import numpy as np

def check(puzzle, clue_index):
    """
    Checks whether puzzle has unique solution

    Parameters
    ----------
    puzzle : ndarray 
        Puzzle matrix
    clue_index : array of int
        Indicator for which clue applies to each row of puzzle matrix

    Returns
    -------
    Boolean True/False as to whether puzzle has unique solution
    """

    def permute(arr, num_dig):
        """ 
        Creates list of all possible 3-digit codes where every code digit is unique

        Parameters
        ----------
        arr : ndarray 
            Array of possible digits of codes
        num_dig : int
            Number of digits in code

        Returns
        -------
        List of all possible 3-digit codes where every code digit is unique
        """

        num_perm = 1
        for j in range(num_dig):
            num_perm *= len(arr)-j

        permutations = np.zeros((num_perm, num_dig))
        n=0
        for i in range(len(arr)):
            for j in range(len(arr)):
                for k in range(len(arr)):
                    if (i!=j and j!=k and i!=k):
                        permutations[n][0] = arr[i]
                        permutations[n][1] = arr[j]
                        permutations[n][2] = arr[k]
                        n=n+1
        return permutations
    
    def repeat(clue, n):
        return np.stack([clue for _ in range(n)], axis=0)

    def filter_num_digits(all_codes, clue, num_digits):
        num_common = (1*np.isin(all_codes, clue)).sum(axis=1)
        return all_codes[num_common==num_digits]

    def filter_digit_loc(all_codes, clue, action='remove'):
        clue_rp = repeat(clue, all_codes.shape[0])
        diff = all_codes - clue_rp
        if action=='remove':
            return all_codes[~np.any(diff==0,axis=1)]
        elif action=='keep':
            return all_codes[np.any(diff==0,axis=1)]

    all_codes = permute(range(1,11), 3)

    for k,indx in enumerate(clue_index):
        ##### check Clue 1 (nothing correct)
        if indx==0:
            clue1 = puzzle[k]
            all_codes_new = all_codes.copy()
            for i in range(3):
                # remove all codes that contain any digit of clue 1
                all_codes_new = all_codes_new[~np.any(all_codes_new==clue1[i], axis=1)]

        ##### check Clue 2 (two correct wrong place)
        elif indx==1:
            clue2 = puzzle[k]
            # remove all codes that do not contain two digits of clue 2
            all_codes_new = filter_num_digits(all_codes_new, clue2, 2)  
            # remove all codes that have clue digits in correct place
            all_codes_new = filter_digit_loc(all_codes_new, clue2, 'remove')

        ##### check Clue 3 (one correct wrong place)
        elif indx==2:
            clue3 = puzzle[k]
            # remove all codes that do not contain exactly one digits of clue 3
            all_codes_new = filter_num_digits(all_codes_new, clue3, 1)  
            # remove all codes that have clue digit in correct place
            all_codes_new = filter_digit_loc(all_codes_new, clue3, 'remove')

        ##### check Clue 4 (one correct right place)
        elif indx==3:
            clue4 = puzzle[k]
            # remove all codes that do not contain exactly one digits of clue 4
            all_codes_new = filter_num_digits(all_codes_new, clue4, 1)  
            # keep only codes that have clue digit in correct place
            all_codes_new = filter_digit_loc(all_codes_new, clue4, 'keep')

    if all_codes_new.shape[0]==1:
        return True
    else:
        return False
    
