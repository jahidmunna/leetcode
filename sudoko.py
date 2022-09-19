from collections import Counter
from typing import List


def row_correct(sudoku: List[List], row_no: int):
    values = sudoku[row_no]

    # remove 0 from values
    values = list(filter(lambda x: x != 0, values))
    # now count the existing values how many time each of them exist
    count = Counter(values)
    # get the most number that any values form 1-9 appears
    most_frequency = count.most_common()[0][1]
    '''
    if most_frequency ==1 means all the values are appeared exactly once,  
    Multiple times otherwise!
    '''
    return most_frequency == 1


sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(row_correct(sudoku, 0))  # True
print(row_correct(sudoku, 1))  # False
