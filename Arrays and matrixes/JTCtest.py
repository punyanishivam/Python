"""
Takes input an array of numbers. The numbers in the input array can be negative, positive, decimal and in any order.

Re arrange numbers in the array as follows

a1 <= a2 >= a3 <= a4 >= ...

Returns the array with re-arranged numbers as defined in Step 2.

"""

def arrange(nums):
    nums.sort()
    result=[]

    for i in range(len(nums) // 2):
        result.append(nums[i])
        result.append(nums[-i -1])
    
    if len(nums)%2:
        result.append(nums[len(nums) // 2])
    
    return result



# Time complexity = O(N logN) - because of sorting
# Space complexity = O(N) - because of output array (i.e result)

testcases = [[1, 11, 1, 10, 3, 9, 4, 7, 5], [], [0, -1, 2, 3], [-1, -1, 2, -2], [1, 2, 3, 4, 5]]

for testcase in testcases:
    print(arrange(testcase))