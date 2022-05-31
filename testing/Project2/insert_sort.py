from typing import List, Any, Dict



def insertion_sort(data: List[Any]) -> None:
    """
    Sorts a list using the popular method Insertion Sort
    :param data: the given list which needs to be sorted!!
    """

    length = len(data) # length of list passed in
    if length == 0:
        return data
    for i in range(1, length):
        key = data[i]
        j = i-1
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key


