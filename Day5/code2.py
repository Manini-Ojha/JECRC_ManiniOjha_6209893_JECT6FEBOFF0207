# we're using c python
# we have jpython which works with java binary files
# we have iron python
# we have distributions like anaconda

#def func_name(formal args/parameter):  ->function  declaration
#   //statement block

#func_name  ->function accessing, reference of memory is returned
#func_name(actual args)  ->function calling, function's task is executed

#operators,copy operation, datatypes

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

'''

#[11,15,7,2], target=9

def twoSum(collection,target):
    for i in range(0,len(collection)-1):
        for j in range(i+1,len(collection)):
            if(collection[i]+collection[j]==target):
                return [i,j]
    return -1

length=int(input("length of collection "))
collection=[]
for i in range (length):
    item=int(input("enter element"))
    collection.append(item)
    
target=int(input("enter target "))
print(twoSum(collection,target))
