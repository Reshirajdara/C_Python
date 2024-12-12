# Global variable
global_var = "I am a global variable"

def global_example():
    global global_var  # Declaring to modify the global variable
    global_var = "I have been modified globally"
    print(global_var)

def local_example():
    local_var = "I am a local variable"  # Local variable
    print(local_var)

def nonlocal_example():
    outer_var = "I am in the outer function"
    
    def inner_function():
        nonlocal outer_var  # Using nonlocal to modify the variable from outer scope
        outer_var = "I have been modified in the inner function"
        print(outer_var)
    
    print("Before calling inner_function:", outer_var)
    inner_function()
    print("After calling inner_function:", outer_var)

# Call the functions
print("Global variable before modification:", global_var)
global_example()
print("Global variable after modification:", global_var)

local_example()

print("\nDemonstrating nonlocal variables:")
nonlocal_example()
