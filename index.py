nums = [2,43,45,56,7,8,9,-33,44,45,5,6,45,66,45,]
# index , index(element,startvalue,endvalue)
a=nums.index(45)
print(a)
b=nums.index(45,a+1)
print(b)
c=nums.index(45,b+1)
print(c)
d=nums.index(45,c+1)
print(d)

'''INDEX---> index() return index value of element passed, 
           we can give maximum of 3 parameter in index()
           in first parameter , u have to pass the element itself,
           second and third are optional parameter, if element is not found in list it throw error(exception).'''
#           second --> start
#           third  -->end(excluded)

# COUNT---> it return the frequency of list no. means how many times a no. is present in list
a=nums.count(2)
print(a)
a=nums.count(45)
print(a)

#SORT() -->it convert list in desscending to asscending order
# None return, inplace fuction , no need of extra list(object)  
nums.sort()
print(nums)
nums.sort(reverse=True) #asscending to desscending
print(nums)
# INPLACE FUNCTION --> are the functions in which no extra object has been created 