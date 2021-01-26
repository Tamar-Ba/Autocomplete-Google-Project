def remove_duplicates(lst):
    for index, item in enumerate(lst):
        for index2, item2 in enumerate(lst):
            if index != index2 and item == item2:
                lst.remove(item2)
    return lst
