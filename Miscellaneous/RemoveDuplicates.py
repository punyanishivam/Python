def array_dupliacte(arr):
    dict_arr = {}
    for i in arr:
        if i in dict_arr:
            value = dict_arr.get(i)
            value = value+1
            dict_arr.update({i: value})
        else:
            dict_arr.update({i: 1})

    list1 = []
    for i in dict_arr.keys():
        list1.append(i)
    return list1


arr = [1, 2, 1, 3, 2, 5, 4, 5]
result = array_dupliacte(arr)
print(result)
