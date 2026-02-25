#Sets - Practice question

#1. find common element between two list using set
A = [1, 2, 3, 4,5]
B = [3, 4, 5, 6]
s = set()
common = []

for i in A:
    s.add(i)

for j in B:
    if j in s:
        common.append(j)

print("Common elements:", common)


#2. Remove duplicate words from a sentence using set
sentence = input("Enter a sentence: ")

words = sentence.split()
seen = set()
result = ""

for word in words:
    if word not in seen:
        result = result + word + " "
        seen.add(word)

print("Sentence without duplicate words:")
print(result)


#3. check two strings are anagrams using sets and logic
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) != len(s2):
    print("Not anagrams")
else:
    is_anagram = True
    for ch in s1:
        if s1.count(ch) != s2.count(ch):
            is_anagram = False
            break

    if is_anagram:
        print("Strings are anagrams")
    else:
        print("Strings are not anagrams")


#4. find element present in the first list but not in second using set
ls1=[1,2,3,4,5,6]
ls2=[4,5,6,7,8]
temp1=set(ls1)
temp2=set(ls2)
print(list(temp1-temp2))

#5. check if all character in a string are unique using set
str = input("Enter a string: ")
unique=True
seen = set()
result = ""

# remove spaces -- if we nned to perform on sentences
#s1 = s1.replace(" ", "").lower()
#s2 = s2.replace(" ", "").lower()

for word in str:
    if word not in seen:
        seen.add(word)
    else:
        unique=False
        break

if unique:
    print("String contain unique characters")
else:
    print("String NOT contain unique characters")

#count number of distinct element in a list using set
lis=[1,2,3,3,4,5,5,5,5,5]
repeated=[]
seen=[]
for i in lis:
    if lis.count(i)!=1 and i not in seen:
        repeated.append(i)
        seen.append(i)

set1=set(lis)
set2=set(repeated)
print("Distinct element in list are : ",(set1-set2))


#find syemmetric difference between two set without built in method

#remove common character from two string using set
s1 = input("Enter first string: ")#hello
s2 = input("Enter second string: ")#hel

set1 = set(s1)#helo
set2 = set(s2)#hel

common = set1 & set2#hel

result1 = ""
result2 = ""

for ch in s1:
    if ch not in common:
        result1 += ch

for ch in s2:
    if ch not in common:
        result2 += ch

print("String 1 after removing common characters:", result1)
print("String 2 after removing common characters:", result2)

#check if one set is subset of another without sing built in function


#find repeated element in a list ising set
lis=[1,2,3,3,4,5,5,5,5,5]
repeated=[]
seen=[]
for i in lis:
    if lis.count(i)!=1 and i not in seen:
        repeated.append(i)
        seen.append(i)

print("Distinct element are : ",repeated)