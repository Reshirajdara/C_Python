class Example:
    def __init__(self, name, value):
        """Dunder method for object initialization"""
        self.name = name
        self.value = value

    def __str__(self):
        """Dunder method to return a string representation of the object"""
        return f"Example(name={self.name}, value={self.value})"

    def __repr__(self):
        """Dunder method for the official string representation"""
        return f"Example({repr(self.name)}, {repr(self.value)})"

    def __add__(self, other):
        """Dunder method to handle addition of two Example objects"""
        if isinstance(other, Example):
            return Example(self.name + other.name, self.value + other.value)
        raise TypeError("Unsupported operand type for +")

    def __len__(self):
        """Dunder method to get the length of the name attribute"""
        return len(self.name)

    def __eq__(self, other):
        """Dunder method to compare two Example objects for equality"""
        return self.name == other.name and self.value == other.value


# Using the Example class
obj1 = Example("Alpha", 10)
obj2 = Example("Beta", 20)

print(str(obj1))  # __str__ method
print(repr(obj2))  # __repr__ method

# Adding two objects
obj3 = obj1 + obj2
print(f"Combined Object: {obj3}")

# Checking equality
print(f"Objects are equal: {obj1 == obj2}")

# Getting the length of the name
print(f"Length of name in obj1: {len(obj1)}")
