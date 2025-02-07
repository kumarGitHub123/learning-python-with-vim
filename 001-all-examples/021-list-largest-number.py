numbers = [1, 9, 2, 8, 3, 7, 4, 6, 5]
highest = max(numbers)
print(highest)


highest_2 = numbers[0]
for number in numbers:
    if number > highest_2:
        highest_2 = number
print(highest_2)

