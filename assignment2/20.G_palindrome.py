# Define function is_palindrome

def is_palindrome_rec(str, p, q):
    if p > q:
        return True
    elif str[p] != str[q]:
        return False
    else:
        # Recursion
        return is_palindrome_rec(str, p+1, q-1)


# Help function that initializes the recursive function
def is_palindrome(str):
    p = 0
    q = len(str) - 1
    return is_palindrome_rec(str, p, q)


text = input("Enter a text:")
s = text.lower()           # All letters converted to lower letters
converted_text = ""
for ch in s:
    asc = ord(ch)                # ASCII code
    if 97 <= asc <= 122:         # lower case in ASCII code
        converted_text += ch

print(f"'{text}'' is palindrime: {is_palindrome(converted_text)}")
