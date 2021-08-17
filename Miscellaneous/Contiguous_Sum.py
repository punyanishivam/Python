def contiguousSum(arr, k):
    currSum = 0
    start = 0
    
    i = 1
    while i <= len(arr):
        while currSum > k and start < i - 1:
            currSum -= arr[start]
            start += 1
        
        if currSum == k:
            return True
        
        if i < len(arr):
            currSum += arr[i]
        i += 1
            
    
    
    
    
    
    
    
    
    
    
    
    
    
arr = [1, 2, 3, 4, 5]
k = 9
print(contiguousSum(arr, sum))