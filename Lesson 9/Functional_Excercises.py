### Practical Exercises
"""
celsius = [12,3,8,9]
1. **Transforming Data:** Use `map` to convert a list of temperatures from Celsius to Fahrenheit.


names = ['john','alyssa']
2. **Filtering Data:** Use `filter` to extract names starting with a particular letter from a list.


numbers[1,2,3,4,5]
3. **Aggregating Data:** Use `reduce` to calculate the total of a list of numbers.
"""

celsius = [12, 3, 8, 9]
fahrenheit = list(map(lambda x: x * 9 / 5 + 32, celsius))
print(fahrenheit)

names = ['john', 'alyssa']
filtered_names = list(filter(lambda name: name.startswith('a'), names))
print(filtered_names)

from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)

