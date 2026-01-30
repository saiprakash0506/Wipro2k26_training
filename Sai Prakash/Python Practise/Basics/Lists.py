num1=65
print(num1)

nums=[45,87,21,23,99]
print(nums)

print(nums[0]) #indexing 
print(nums[::-1]) #reversing a list with slicing

print(nums[-1])

names=['navin',"saiprakash","reddy",0.2,433,True]
print(names)

mix=[nums,names]
print(mix)
print(mix[0])
print(len(mix[1]))
print(mix[1][1])

mix=nums+names
print(mix)

nums.append(32) #at the end
print(nums)

print(nums.count(23))
print(nums.index(23))
nums.insert(0,44)
nums.remove(99) 
nums.pop()
nums.pop(2)
print(nums)

# del(nums)
# print(nums)



nums=["sai","prakash"]
nums.extend([1,2,3,4,5])
print(nums)

nums[1]="reddy"
print(nums)

# nums.sort() #but it should only have int or str, not both 
print(nums)

print(min(nums))
print(max(nums))
print(sum(nums))