import numpy as np

# generate all numbers from [1,10] (will subtract 1 at end to make [0,9]
n = np.arange(1,11)
# generate random code
code = np.random.choice(n, 3, replace=False)


# Clue 1: digit 2 is in the correct (2nd) spot
mat1 = np.zeros((3,3)) 
mat1[1,1] = 1

# Clue 2: nothing is correct
mat2 = np.zeros((3,3)) 

# Clue 3: digit 3 is in the wrong (2nd) spot
mat3 = np.zeros((3,3))
mat3[1,2] = 1; 
 
# Clue 4: digit 1 is in the correct (1st) spot
mat4 = np.zeros((3,3))
mat4[0,0] = 1; 

# Clue 5: digits 2 and 3 are in the wrong (3rd and 2nd) spots
mat5 = np.zeros((3,3))
mat5[1,2] = 1; mat5[2,1] = 1; 

# Construct matrix of correct digits 
mat = [mat1,mat2,mat3,mat4,mat5]
puzzle = np.dot(mat,code)

# Generate array of remaining digits
other = np.delete(n,code)
# Choose 6 of these (i.e. remove one from this list which will not feature in puzzle)
other = np.random.choice(other, 6, replace = False)

# Randomly choose digits for missing puzzle entries
for i in range(puzzle.shape[0]):
    options = other
    for j in range(puzzle.shape[1]):
        if puzzle[i,j] not in code:
            temp = np.random.choice(options)
            puzzle[i,j] = temp
            options = np.setdiff1d(options,temp)


print(puzzle-1)
input("Press Enter for answer...")
print(code-1)


# Currently this does not give a unique answer. An answer always exists but sometimes more than one solution exists. 
# How can we ensure uniqueness?

