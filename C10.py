def is_palindrome(s):
    return s == s[::-1]
    
input_string = input("Enter a string: ")
 
if is_palindrome(input_string):
   print("Palindrome")
else:
   print("Not a palindrome")