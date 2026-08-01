numbers = [11,22,33,44,55,66,77,88,99]

target = int(input(" what number r u looking for:"))

start = 0
end = len(numbers)-1

flage=False

while start<=end:
    mid = (start+end)//2
    #floor division-> // uf we divide 5 with 2 -> ans is 2.5 but when u do // we get 2
    if numbers[mid]==target:
        flag=True
        break
    elif numbers[mid]<target:
        end = mid + 1
    else:
        start = mid - 1
        

if flag == False:
    print("not found")