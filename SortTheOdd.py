def sort_array(source_array):
    
    dicty = {}
    odds = []
    
    for i in range(len(source_array)):
        if source_array[i] % 2 == 0 or source_array[i] == 0:
            dicty.update({source_array[i]:i})
        else:
            odds.append(source_array[i])

    print(dicty)
    
    odds = sorted(odds)
    
    for i in range(len(odds)):
        dicty.update({odds[i]:source_array[i]})
        print(dicty)
        
    result = [0] * len(source_array)
    
    for key, value in dicty.items():
        result[value] = key
        
    return result

print(sort_array([5, 3, 2, 8, 1, 4]))