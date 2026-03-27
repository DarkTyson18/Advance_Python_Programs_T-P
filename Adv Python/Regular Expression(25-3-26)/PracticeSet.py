#1
li=[1,2,3,4,5]
print("Largest element : ",max(li))

#2
num=2
if num&1==0:
    print("Even")
else:
    print("Odd")


if (num//2)*2==num:
    print("Even with div and mul")
else:
    print("Odd with div and mul")


#3
str1="shashi"
reversed_string = "".join(reversed(str1))
print("Reversed string:", reversed_string)

#4
num=123
sum=0
while num>0:
    sum += num%10
    num //=10

print("sum of digit : ",sum)

#5
str1="mom"
str2 = "".join(reversed(str1))
if str1==str2: print("Palindrome")
else: print("Not palindrome")