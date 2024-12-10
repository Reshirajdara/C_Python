class MathOperations:
    multiplier = 2

    @staticmethod
    def add(a, b):
        """
        Static method to perform addition.
        Does not depend on the class or instance.
        """
        return a + b

    @classmethod
    def multiply_with_class_variable(cls, value):
        """
        Class method to perform multiplication using a class variable.
        Depends on the class and can access or modify class attributes.
        """
        return value * cls.multiplier


# Using the static method
result_add = MathOperations.add(5, 7)
print(f"Static Method - Addition Result: {result_add}")

# Using the class method
result_multiply = MathOperations.multiply_with_class_variable(10)
print(f"Class Method - Multiplication Result: {result_multiply}")

# Modifying the class variable and using the class method again
MathOperations.multiplier = 5
new_result_multiply = MathOperations.multiply_with_class_variable(10)
print(f"Class Method (After Update) - Multiplication Result: {new_result_multiply}")
