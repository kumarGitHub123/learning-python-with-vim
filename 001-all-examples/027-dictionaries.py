customer = {
    "name": "Manuel Alaminos",
    "age": 30,
    "is_verified": True
}

print(customer["name"])
print(customer.get("age"))
print(customer.get("birthday", "Nov 1 1986"))

customer["name"] = "Elias Alaminos"
print(customer["name"])
customer["hair_colour"] = "Dark"
print(customer["hair_colour"])



