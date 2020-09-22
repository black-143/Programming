'''https://leetcode.com/problems/single-number/'''

def SingleNumber(nums):
	a = nums[0]
	for i in range(1,len(nums)):
	       a ^= nums[i]
	return a

nums = list(map(int,input().split()))
print(SingleNumber(nums))