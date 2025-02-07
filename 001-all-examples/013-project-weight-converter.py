weight = int(input("Your weight "))
unit = input("Did you enter (L)bs or (K)g ?: ")

if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
elif unit.upper() == "K":
    converted = weight / 0.45
    print(f"You are {converted} pounds")
else:
    print("You didn't enter a correct letter")




