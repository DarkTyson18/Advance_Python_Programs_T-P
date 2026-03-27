#In Python, regular sets are mutable. This means you can add or remove elements from a set
#Frozen Set is a (Immutable Set)

# Creating sets
s = {1, 2, 3}
s2 = set([3, 4, 5])
empty = set()   # note: {} creates a dict
print(s,s2,empty)


print("\n\n")

s.add(10)# add single element
print(s)    
       
s.update([20, 30])# add multiple elements
print(s) 

s.remove(2)# removes, throws error if not exists 
print(s)     

s.discard(100)# removes, no error if not exists 
print(s)  

s.pop()# removes random element
print(s)    

s.clear()# removes all elements
print(s)             

print("\n\n")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))# A-B, should present in A but not in B
print(B.difference(A))# B-A, should present in B but not in A   

print("\n")
#In form of operators
print(A | B)   # union
print(A & B)   # intersection
print(A - B)   # difference
print(A ^ B)   # symmetric difference


fs = frozenset([1, 2, 3])
#fs.add(4)   ERROR (not allowed)


print(len(A))   # length of the  set
print(3 in A)   # membership operator
print(3 not in A)


a = {"mango","ram",True,1}#set important property
print(a)

#--------------------------------------------------------------------------------------------------------

