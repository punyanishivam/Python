import math

def foursum_divisors(nums):
    
    sum_ = 0
    
    for num in nums:
        divisors = set()
        for i in range(1, math.floor(math.sqrt(num))+1):
            if num % i == 0:
                divisors.add(num//i)
                divisors.add(i)
            if len(divisors) > 4:
                break
                
        if len(divisors) == 4:
            sum_ += sum(divisors)
            
    return sum_


print(foursum_divisors([21,4,7]))
