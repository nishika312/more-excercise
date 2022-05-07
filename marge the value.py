list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
k=[]
i=0
while i<len(list2):
    list1.append(list2[i])
    j=0
    while j<len(list1):
        if list1[j] not in k:
            k.append(list1[j])
        j=j+1
    i=i+1
print(k)
    
            
