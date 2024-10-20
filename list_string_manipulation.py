# 1.  List and String Manipulation (5 points)
#     Write a function `reverse_even_strings(strings: list)` that takes a list of strings and returns a new list where all strings with even lengths are reversed. Strings with odd lengths should remain unchanged.

#     Example:
#     Input: ["data", "science", "is", "fun"]
#     Output: ['atad', 'science', 'si', 'fun']

#This function is used to reverse the string with even length
def reverse_even_strings(strings: list):
    reversed_string = [
        s[::-1] if len(s)%2 == 0 
        else s[::] for s in strings
        ]
    return reversed_string

input_data = ['data', 'science', 'is','fun']
print(reverse_even_strings(input_data))
