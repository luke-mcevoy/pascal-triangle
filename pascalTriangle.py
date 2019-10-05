#Luke McEvoy
#10/2/18
#I pledge my honor I have abided by the Stevens Honor System


def pascal_row(R):
#base case for when the row is 0
    if R == 0:
        return [1]
#base case for when the row is 1
    elif R == 1:
        return [1, 1]
#base case for when the row is >= 2
    elif R >= 2:
    #return [1, actual calculations, 1]
        return [1] + helper2(pascal_row(R-1)) +[1]

def helper2(L):
#if the length of the words are 1 or [], return []
    if len(L) == 1 or len(L) == []:
        return []
    #add the first part of list and second part of list, recursively call
    return [ L[0] + L[1] ] + helper2(L[1:])


def pascal_triangle(R):
    if R == 0:
        return [[1]]
    #recursive call to move down one and add the current rows value to future calls
    return pascal_triangle(R-1) + [pascal_row(R)]


def test_pascal_row():
    assert pascal_row(4) == [1, 4, 6, 4, 1]
    assert pascal_row(6) == [1, 6, 15, 20, 15, 6, 1]
    assert pascal_row(8) == [1, 8, 28, 56, 70, 56, 28, 8, 1]
    assert pascal_row(10) == [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]

def test_pascal_triangle():
    assert pascal_triangle(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert pascal_triangle(2) == [[1], [1, 1], [1, 2, 1]]
    assert pascal_triangle(3) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    assert pascal_triangle(1) == [[1], [1, 1]]




    
    
    
