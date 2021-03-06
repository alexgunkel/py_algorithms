

def insertion_sort(list_of_sortable):
    result = []
    for sortable in list_of_sortable:
        length = len(result)
        result[length:] = [sortable]
        while length > 0 and result[length-1] > result[length]:
            result[length-1], result[length] = result[length], result[length-1]
            length = length-1
    return result
