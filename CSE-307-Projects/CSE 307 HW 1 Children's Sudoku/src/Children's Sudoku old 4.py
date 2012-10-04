
# Childrens Sudoku Solver (CSE 307 Assignment 1)
# Written by Arjun G. Menon (SBID: 106335011)

matrix = []
size = 6
bw = 3
bh = 2

zones = []

def construct_zones():
    # (There are 18 zones in total.)
    # First 6 zones - the rows
    for i in range(1, size+1):
        zones.append(map((lambda j: elem(i, j)), range(1, 6+1)))
    # Second 6 zones - the columns
    for j in range(1, size+1):
        zones.append(map((lambda i: elem(i, j)), range(1, 6+1)))
    # Third 6 zones - the boxes
    for i in range(3):
        for j in range(2):
            first_box = [(1,1), (1,2), (1,3),
                         (2,1), (2,2), (2,3)]
            zones.append(map((lambda e: elem(*e)), map((lambda x: (2*i + x[0], 3*j + x[1])), first_box)))

def reduce(el):
    did_something = False
    for ex in el:
        if len(matrix[ex]) == 1:
            for ey in el:
                if len(matrix[ey]) > 1:
                    try:
                        matrix[ey].remove(matrix[ex][0])
                        did_something = True
                    except ValueError:
                        pass
    return did_something
                    
def reduce_all():
    actions = 0
    for each in zones:
        if reduce(each):
            actions += 1
    return actions > 0

def solve():
    while True:        
        if not reduce_all():
            break

def elem(i, j):
    if i > 0 and j > 0:
        return (i-1)*size + (j-1)
    else:
        print "Error: invalid argument to function elem(i, j)"
        raise ValueError
    
def feed(x):
    if x == '-':
        matrix.append(range(1, size+1))
    elif x >= str(1) and x <= str(size):
        matrix.append([int(x)])

#
# Pretty printers:
#
       
def display_matrix():
    for i in range(1, size+1):
        for j in range(1, size+1):
            print matrix[elem(i, j)],
        print ""

def display_result():
    for i in range(1, size+1):
        for j in range(1, size+1):
            symbol = '-'
            length = len(matrix[elem(i, j)])
            if length == 1:
                symbol = str(matrix[elem(i, j)][0])
            elif length > 1:
                symbol = '*'
            print symbol,
        print ""

#
# File access sequence:
#

file = open("input.txt")

for line in file:
    for k in line:
        feed(k)

construct_zones()
solve()
display_result()
