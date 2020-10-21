"""
Demonstrate sort operations algorithms.

PDB Module Docs: https://docs.python.org/3/library/pdb.html
"""
import pdb

def selectionSort(listObj):
    """

    :param listObj: A list object whose contents gotta be sorted in ascending order.
    :type listObj: List object
    """
    # set initial index for later iteration
    suffixStart = 0

    print('"listObj" contains:',listObj)
    print(f'"listObj" length is: {len(listObj)}')

    while suffixStart != len(listObj):

        for i in range(suffixStart,len(listObj)):

            if listObj[i] < listObj[suffixStart]:
                # swap elements position
                listObj[suffixStart], listObj[i] = listObj[i], listObj[suffixStart]

                print(f'suffix = {suffixStart}, i = {i}:',listObj)

        # increment suffix start
        suffixStart += 1

pdb.runcall(selectionSort,[3,9,0])



