def quick_sort(list):
    """Функция быстрой сортировки списков"""
    length = len(list)
    if length <= 1:
        return list
    else:
        last_element = list.pop()

    elements_smaller = []
    elements_bigger = []

    for item in list:
        if item > last_element:
            elements_bigger.append(item)
        else:
            elements_smaller.append(item)

    return quick_sort(elements_smaller) + [last_element] + quick_sort(elements_bigger)
