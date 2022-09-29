def hourglassSum(arr):
    max = -float('inf')
    sum = 0
    for x in range(1, 5):
        for y in range(1, 5):
            sum = 0
            sum += arr[x][y]
            sum += arr[x-1][y-1] + arr[x-1][y] + arr[x-1][y+1]
            sum += arr[x+1][y-1] + arr[x+1][y] + arr[x+1][y+1]
        
            if sum>max:
                max = sum
        
    
    return max 