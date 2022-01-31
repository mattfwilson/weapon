import random

def find_dups():
    lst = ['common', 'uncommon', 'rare', 'very rare', 'epic', 'legendary']
    output_lst = []
    while len(output_lst) < 3:
        weightedRoll = random.choices(lst, weights=[60, 42, 28, 18, 10, 2])
        for i in weightedRoll:
            if i not in output_lst:
                output_lst.append(i)
    return output_lst

testRoll = find_dups()
print(testRoll)