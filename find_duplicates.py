import random

def find_dups():
    lst = ['Common', 'Uncommon', 'Rare', 'Very rare', 'Epic', 'Legendary']
    output_lst = []
    while len(output_lst) < 2:
        weightedRoll = random.choices(lst, weights=[40, 30, 18, 12, 8, 2])
        for i in weightedRoll:
            if i not in output_lst:
                output_lst.append(i)
    return output_lst

testRoll = find_dups()
print(testRoll)