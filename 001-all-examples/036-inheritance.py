class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    # Python doesn't like empty objects, so we can just add pass to do nothing with it atm
    #pass
    def bark(self):
        print("wough")


class Cat(Mammal):
    def be_annoying(self):
        print("miauuu")


dog = Dog()
dog.walk()
dog.bark()

cat = Cat()
cat.be_annoying()

