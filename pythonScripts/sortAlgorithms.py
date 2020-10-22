"""
Demonstrate sort operations algorithms.

Recommended reads:

PDB Module Docs: https://docs.python.org/3/library/pdb.html

"Bubble vs Selection vs Insertion" sorting comparison: https://bit.ly/3dUwozO

How to Sort Arrays in Python: https://bit.ly/37Hr1mz
"""
import pdb

def selectionSort(listObj):
    """
    Sort "listObj" elements in ascending order.

    :param listObj: A list object whose contents gotta be sorted in ascending order.
    :type listObj: List object
    """
    # set initial list position to progressively work upon.
    absPosition = 0
    # store "listObj" length
    listLength = len(listObj)

    # print helper msg to stdout
    print('\n "listObj" contains:',listObj)
    print(f'\n "listObj" length is: {listLength}')

    # execute loop until it goes up to "listObj" length: the loop's gonna
    # be executed on all List elements.
    while absPosition != listLength:

        print(f'\n SETTING listObj[{absPosition}] value:')

        # for each "absPosition" value iterate over all remaining list elements
        # whose index is greater than or equal to "absPosition".
        for indexValue in range(absPosition,listLength):
            # print helper msg to stdout
            print(f'\n is {listObj[indexValue]} < {listObj[absPosition]}? {listObj[indexValue] < listObj[absPosition]}')

            # is the current element the least value not already sorted?
            if listObj[indexValue] < listObj[absPosition]:
                # swap elements position
                listObj[absPosition], listObj[indexValue] = listObj[indexValue], listObj[absPosition]

                print(f'\n "listObj" now is: {listObj}.')

        # increment absolute list position
        absPosition += 1

# selectionSort([1,0,2])

# pdb.runcall(selectionSort,[3,9,0])

"""----------------------------------------------------------------------------
    Merge-Sort algorithm below.
----------------------------------------------------------------------------"""

def merge(left, right, compare):
    """
    """
    # initialize result as an empty list
    result = []
    # store list objects length
    leftLength = len(left)
    rightLength = len(right)

    # initialize indexes for iteration
    leftIndex, rightIndex = 0,0

    while leftIndex < leftLength and rightIndex < rightLength:
        
        if compare(left[leftIndex], right[rightIndex]) == True:

            result.append(left[leftIndex])
            # increment left index counter
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            # increment right index counter
            rightIndex += 1

    # 
    while (leftIndex < leftLength):
        result.append(left[leftIndex])
        leftIndex += 1

    while (rightIndex < rightLength):
        result.append(right[rightIndex])
        rightIndex += 1

    return result

def mergeSort(listObj, compare = lambda x, y: x < y):

    if len(listObj) < 2:
        return listObj[:]
    else:
        middle = len(listObj) // 2
        left = mergeSort(listObj[:middle],compare)
        right = mergeSort(listObj[middle:],compare)

        return merge(left, right, compare)

# print(mergeSort([2,1,4,5,3]))

pdb.runcall(mergeSort,[2,1,4,5,3])



