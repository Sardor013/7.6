#1-https://www.codewars.com/kata/5b047875de4c7f9af800011b/train/python
'''def sentence(dict_list):
    key_value = [(int(key), value) for d in dict_list for key, value in d.items()]

    sorted_s = sorted(key_value, key=lambda x: x[0])

    sorted_values = [value for i, value in sorted_s]

    return ' '.join(sorted_values)'''



#2-https://www.codewars.com/kata/5417423f9e2e6c2f040002ae/train/python
'''def digitize(n):
    return [int(digit) for digit in str(n)]'''


#3-https://www.codewars.com/kata/59557b2a6e595316ab000046/train/python
'''def convert_hash_to_array(hash):
    return [[key, value] for key, value in hash.items()]'''


#4-https://www.codewars.com/kata/53d2697b7152a5e13d000b82/train/python
'''def copy_list(l):
    if not isinstance(l, list):
        raise TypeError("The provided input is not a list")
    return l.copy()'''


#5-https://www.codewars.com/kata/59b44d00bf10a439dd00006f/train/python
'''def add(numbers):
    if not isinstance(numbers, list):
        raise TypeError("The provided input is not a list")
    
    result = []
    current_sum = 0
    for number in numbers:
        current_sum += number
        result.append(current_sum)
    
    return result'''