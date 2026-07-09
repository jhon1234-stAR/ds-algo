### selection sort
# time complexity: O(n^2)
# traverse through all elements in the array

mylist = [423,342,432,5,2,4,53,543,5,3,45,3,53,5,3,53,5]

for i in range(len(mylist)):
    miniElement = mylist[i]
    minilocation = i
    for j in range(i + 1, len(mylist)):
        if miniElement > mylist[j]:
            miniElement = mylist[j]
            minilocation = j
    mylist[i], mylist[minilocation] = mylist[minilocation], mylist[i]
    
print(mylist)
