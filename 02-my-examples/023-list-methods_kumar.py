numbers = [5, 2, 1, 5, 7, 4]
numbers.append(20)
print(numbers)

numbers.insert(0, 10)
print(numbers)

numbers.remove(5)
print(numbers)

print(numbers.count(5))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
numbers.append(10)
print(numbers2)

print(50 in numbers)

numbers.pop()
print(numbers)

print(numbers.index(2))

numbers.clear()
print(numbers)


