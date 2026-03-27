#wap to take a string input from the user and print it in reverse
s = input("Enter a string to reverse it ")
rev = s[::-1]
print(rev)


#wap to count the number of lower case and upper case character in a string
s = input("Enter a string to count its lower and upper case ")

lower = 0
upper = 0

for ch in s:
    if 'a' <= ch <= 'z':
        lower += 1
    elif 'A' <= ch <= 'Z':
        upper += 1

print("Lowercase:", lower)
print("Uppercase:", upper)

#wap to check whether a given string contain only digit
s = input("Enter a string check whether it contain only digit or not ")

only_digits = True
for ch in s:
    if ch < '0' or ch > '9':
        only_digits = False
        break

if only_digits:
    print("String contains only digits")
else:
    print("String does not contain only digits")


#wap to replace all spaces in a string with underscore(_).
s = input("Enter a string to replace all the space swith the underscore ")

result = ""
for ch in s:
    if ch == ' ':
        result += '_'
    else:
        result += ch

print(result)


#wap to count the frequency of each character in a string 
s = input("Enter the String to count the frequency of each character ")
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for key in freq:
    print(key, ":", freq[key])


#wap to find first and last occurence of a character in a string
s = input("Enter a string ")
ch = input("Enter the character to find its first and last occurence ")

first = -1
last = -1

for i in range(len(s)):
    if s[i] == ch:
        if first == -1:
            first = i
        last = i

print("First:", first)
print("Last:", last)

#wap to remove all the vowels in a given string
s = input("Enter a string to remove all the vowels from it ")
result = ""

for ch in s:
    if ch not in "aeiouAEIOU":
        result += ch

print(result)

#wap to check whether two string are anagrams of each other.

#wap to capitalize the first letter of each word in a string

#wap to check whether a given string is palindrome without usin built-in reverse function.
s = input("Enter a string to check palindrome ")

left = 0
right = len(s) - 1
palindrome = True

while left < right:
    if s[left] != s[right]:
        palindrome = False
        break
    left += 1
    right -= 1

if palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")
