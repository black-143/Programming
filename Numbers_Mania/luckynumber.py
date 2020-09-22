'''Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.'''
from collections import Counter
def findLucky(arr):
    arr.sort()
    dic = Counter(arr)
    num = -1
    for i in dic:
        if dic[i] == i:
            num = i
    return num


print(findLucky([2,2,3,4])) #The only lucky number in the array is 2 because frequency[2] == 2.

print(findLucky([1,2,2,3,3,3])) #1, 2 and 3 are all lucky numbers, return the largest of them.