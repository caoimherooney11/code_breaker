import numpy as np

def check(puzzle):
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

    # check Clue 1 (nothing correct)
    clue1 = puzzle[0]
    all_codes_new = all_codes.copy()
    for i in range(3):
        # remove all codes that contain any digit of clue 1
        all_codes_new = all_codes_new[~np.any(all_codes_new==clue1[i], axis=1)]

    # check Clue 2 (two correct wrong place)
    clue2 = puzzle[1]
    clue2 = permute(clue2,3)
    for i in range(len(clue2)):
        clue2_rp = repeat(clue2[i],all_codes_new.shape[0])
        diff1 = all_codes_new - clue2_rp
    #clue1_check = diff1[~np.any(diff1==0,axis=1)]
    import IPython; IPython.embed()
    diff1[np.where(diff1!=0)]=1
    check1 = np.sum(diff1,axis=1)



    import IPython; IPython.embed()
