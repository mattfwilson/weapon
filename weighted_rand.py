import random

nums = [34, 23, 57, 63, 3, 17, 98]
print(lambda num: num + 2 for num in nums)

class WeightedRandomizer:
    def __init__ (self, weights):
        self.__max = .0
        self.__weights = []
        for value, weight in weights.items ():
            self.__max += weight
            self.__weights.append ( (self.__max, value) )

    def random (self):
        r = random.random () * self.__max
        for ceil, value in self.__weights:
            if ceil > r: return value

weights = {'A': 1.0, 'B': 1.0, 'C': 18.0}

wr = WeightedRandomizer(weights)

results = {'A': 0, 'B': 0, 'C': 0}
for i in range (10000):
    results [wr.random () ] += 1

print(f'After 10000 rounds the distribution is: {results}')
