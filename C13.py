# Define a metaclass
class Meta(type):
    # Overriding the __new__ method to customize class creation
    def __new__(cls, name, bases, dct):
        print(f"Creating class: {name}")
        
        # Add a custom attribute to all classes created by this metaclass
        dct['custom_attribute'] = "I was added by Meta!"
        
        # Enforce a rule: Ensure all classes have a 'greet' method
        if 'greet' not in dct:
            raise TypeError(f"Class {name} must define a 'greet' method")
        
        return super().__new__(cls, name, bases, dct)

# Define a class using the metaclass
class MyClass(metaclass=Meta):
    def greet(self):
        return "Hello from MyClass!"

# Attempt to create a class without a 'greet' method
# This will raise a TypeError due to the rule enforced by Meta
try:
    class InvalidClass(metaclass=Meta):
        pass
except TypeError as e:
    print(e)

# Instantiate and use MyClass
obj = MyClass()
print(obj.greet())  # Output from the 'greet' method
print(obj.custom_attribute)  # Access the custom attribute added by the metaclass
