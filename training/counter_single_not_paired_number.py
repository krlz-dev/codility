def solution(A):
    pairs={}
    not_pair_value = 0

    for value in A:
        pairs[value] = pairs.get(value,0) + 1

    for pair,counter in pairs.items():
        if counter == 1:
            not_pair_value = pair

    return not_pair_value

# ^ operator is XOR in python, pairs in XOR cancel each other to 0 then only the unpair value will be set to result
def solution(A):
    result = 0

    for num in A:
        result ^= num 

    return result