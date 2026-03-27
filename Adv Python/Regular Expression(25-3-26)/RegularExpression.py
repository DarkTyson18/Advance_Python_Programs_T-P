import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

#The findall() function

#Return a list containing every occurrence of "ai":
#If no matches are found, an empty list is returned:

txt = "The rain in Spain"
pattern="ai"
x = re.findall(pattern, txt)
print(x)



#The search() Function

#The search() function searches the string for a match, and returns a Match object if there is a match.
#If no matches are found, the value None is returned:
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

