import numpy as np

# generate all numbers from [1,10] (will subtract 1 at end to make [0,9])
n = np.arange(1,11)
# generate random code
code = np.random.choice(n, 3, replace=False)
mats = []
clues = []

# matrix tuples
wrong_place = [[0,1], [0,2], [1,0], [1,2], [2,0], [2,1]]
right_place = [[0,0], [1,1], [2,2]]

def nothing_correct():
    mat1 = np.zeros((3,3)) 
    mats.append(mat1)
    clues.append(" nothing is correct")

def two_correct_wrong_place():
    mat2 = np.zeros((3,3))
    select = np.random.choice(range(len(wrong_place)), 1, replace=False)
    indx1 = wrong_place[select[0]]; 
    wrong_place.remove(indx1)
    temp_list = wrong_place.copy()
    for j in range(len(wrong_place)):
        if (wrong_place[j][0]==indx1[0]) or (wrong_place[j][1]==indx1[1]):
            temp_list.remove(wrong_place[j])

    select = np.random.choice(range(len(temp_list)), 1, replace=False)
    indx2 = temp_list[select[0]]
    wrong_place.remove(indx2)
    
    mat2[indx1[0]][indx1[1]] = 1
    mat2[indx2[0]][indx2[1]] = 1
    mats.append(mat2)
    clues.append(" two digits are correct but in the wrong place")

def one_correct_wrong_place(index=None):
    mat3 = np.zeros((3,3)) 
    wrong_place_temp = wrong_place.copy()
    if index != None:
        for j in range(len(wrong_place)):
            if all(i!=index for i in wrong_place[j]):
                wrong_place_temp.remove(wrong_place[j])

    select = np.random.choice(range(len(wrong_place_temp)), 1, replace=False)

    indx = wrong_place_temp[select[0]]
    wrong_place.remove(indx)
    
    mat3[indx[0]][indx[1]] = 1
    mats.append(mat3)
    clues.append(" one digit is correct but in the wrong place")

def one_correct_right_place(index=None):
    mat4 = np.zeros((3,3))
    if index != None:
        for j in range(len(right_place)):
            if all(i!=index for i in right_place[j]):
                right_place.remove(tuples[j])

    select = np.random.choice(range(len(right_place)), 1, replace=False)
    indx = right_place[select[0]]
    right_place.remove(indx)
    
    mat4[indx[0]][indx[1]] = 1
    mats.append(mat4)
    clues.append(" one digit is correct and in the correct place")

def sum_columns(mats):
    sums = np.zeros(3)
    for i in range(len(mats)):
        sums = sums + np.sum(mats[i],axis=1)

    return sums

    
# Clue 1: nothing is correct
nothing_correct()
# Clue 2: two digits are correct but in the wrong spots
two_correct_wrong_place()
# Clue 3: one digit correct but in the wrong place
one_correct_wrong_place()
# Clue 4: one digit is correct and in the right place
one_correct_right_place()
# Clue 5
sums = sum_columns(mats)
print(sums)
if np.any(sums==0):
    indx = np.where(sums==0)[0][0]
    one_correct_wrong_place(index=indx)
else:
    one_correct_wrong_place()
 
# Construct matrix of code digits 
puzzle = np.dot(mats,code)

# Generate array of remaining digits
other = np.delete(n,code-1)

# Randomly choose digits for missing puzzle entries
rank=0
while rank!=5:
    for i in range(puzzle.shape[0]):
        options = other
        for j in range(puzzle.shape[1]):
            if puzzle[i,j] not in code:
                temp = np.random.choice(options)
                puzzle[i,j] = temp
                options = np.setdiff1d(options,temp)

    # Generate matrix of ones and zeros to determine which numbers appear in each clue
    M = np.ones((5,10))
    for i in range(5):
        for j in range(10):
            if j in puzzle[i,:]:
                M[i,j] = 2

    rank = np.linalg.matrix_rank(M)

# subtract 1 to make puzzle and code between [0,9]
puzzle = puzzle-1
code = code-1

# jumble up clues
order = [0,1,2,3,4]
np.random.shuffle(order)

print('\n')
for i in range(5):
    print(puzzle[order[i],:], clues[order[i]])
print('\n')
input("Press Enter for answer...")
print('\n')
print(code)
print('\n')






# Currently this does not give a unique answer. An answer always exists but sometimes more than one solution exists. 
# How can we ensure uniqueness?

