# Sort strings by length, identify palindromes, and replace spaces with hyphens using list
# comprehension.


words = ["mom", "hello world", "python", "level", "data science"]

sorted_words = sorted(words, key=len)
print(sorted_words)


palindromes = [w for w in words if w.replace(" ", "") == w.replace(" ", "")[::-1]]
print(palindromes)

modified = [w.replace(" ", "-") for w in words]
print(modified)

