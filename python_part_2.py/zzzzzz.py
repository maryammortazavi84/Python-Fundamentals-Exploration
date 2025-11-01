class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        return Cat(self.name + "-" + other.name, 0)

    def __str__(self):
        return f"{self.name} ({self.age} years old)"

cat1 = Cat("Luna", 3)
cat2 = Cat("Milo", 2)
kitten = cat1 + cat2
print(kitten)
