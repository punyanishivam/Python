def productExceptSelf(nums):
        
    prod = 1
    answer = []
    
    for i in range(len(nums)):
        answer.append(prod)
        prod *= nums[i]
        
    prod = 1
    
    for i in range(len(nums)-1, -1, -1):
        answer[i] *= prod
        prod *= nums[i]

    return answer


print(productExceptSelf([1,2,3,4]))
