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