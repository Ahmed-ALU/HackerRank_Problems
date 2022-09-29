def dynamicArray(n, queries):
    # Write your code here
    #array
    answer = []
    arr = []
    arr2 =[]
    length = n
    qlength = str(queries[0])[1:-1].split(",")[1]
    if qlength.startswith(' '):
        qlength = qlength[1:]
    qlength = int(qlength)

    for i in range(length):
        arr.append([])
    # for i2 in range(qlength+1):
    #     arr2.append([])
    #var
    lastAnswer = 0
        
    # for row in arr2[1:]:
    for row in queries[1:]:
        if row[0] == 1:
            index = (row[1]^lastAnswer)%length
            arr[index].append(row[2])
        elif row[0] == 2:
            index = (row[1]^lastAnswer)%length
            lastAnswer =  arr[index][row[2]%len(arr[index])] # check if size is the same as the len
            answer.append(lastAnswer)
    
            
    return answer

# print(dynamicArray('2 5', '1 0 5\n1 1 7\n1 0 3\n2 1 0\n2 1 1')) 
l = [[100, 100], [1, 910205855, 303787404], [1, 710990379, 16287945], [2, 249491964, 116338582], [1, 862995909, 267690725], [1, 874625610, 100042133], [1, 83989594, 716350279], [1, 505517714, 790911666], [1, 348464997, 463299210], [1, 712698899, 814096174], [1, 444401220, 103180274], [1, 47171291, 386422094]]
print(dynamicArray(100, l)) 

# print(str(int(22))[0])


print()
