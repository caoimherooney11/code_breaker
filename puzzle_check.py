import numpy as np

def check(puzzle, clue_index, code):
    def permute(arr, num_dig):
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
            num_common = (1*np.isin(all_codes_new, clue2)).sum(axis=1)
            all_codes_new = all_codes_new[num_common==2]
            
            # remove all codes that have clue digits in correct place
            clue2_rp = repeat(clue2,all_codes_new.shape[0])
            diff = all_codes_new - clue2_rp
            all_codes_new = all_codes_new[~np.any(diff==0,axis=1)]

        ##### check Clue 3 (one correct wrong place)
        elif indx==2:
            clue3 = puzzle[k]
            # remove all codes that do not contain exactly one digits of clue 3
            num_common = (1*np.isin(all_codes_new, clue3)).sum(axis=1)
            all_codes_new = all_codes_new[num_common==1]
            
            # remove all codes that have clue digit in correct place
            clue3_rp = repeat(clue3,all_codes_new.shape[0])
            diff = all_codes_new - clue3_rp
            all_codes_new = all_codes_new[~np.any(diff==0,axis=1)]

        ##### check Clue 4 (one correct right place)
        elif indx==3:
            clue4 = puzzle[k]
            # remove all codes that do not contain exactly one digits of clue 4
            num_common = (1*np.isin(all_codes_new, clue4)).sum(axis=1)
            all_codes_new = all_codes_new[num_common==1]
            
            # keep only codes that have clue digit in correct place
            clue4_rp = repeat(clue4,all_codes_new.shape[0])
            diff = all_codes_new - clue4_rp
            all_codes_new = all_codes_new[np.any(diff==0,axis=1)]



    if all_codes_new.shape[0]==1:
        return True
    else:
        return False
    
