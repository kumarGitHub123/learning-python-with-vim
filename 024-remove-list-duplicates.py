numbers = [1, 7, 2, 5, 7, 8, 5, 9, 4]
for number in numbers:
    if numbers.count(number) > 1:
        numbers.remove(number)
print(numbers)

# Another way of doing it
numbers2 = [1, 7, 2, 5, 7, 8, 5, 9, 4]
uniques = []
for number in numbers2:
    if number not in uniques:
        uniques.append(number)
print(uniques)
