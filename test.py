#1) reversed 
'''num=int(input("enter a number:"))
reversed_num = int (str(num)[::-1])
print("reversed digits:",reversed_num)'''

# 2)range even
'''num= int(input("enter no:"))
my_range=range(2,num,2)
print(list(my_range))'''

#3)leap year
'''year=int(input("enter your year:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 100 == 0): 
    print("leap year")
else:
    print("NOT a leap year")'''
#4) factorial
num=int(input("enter an number:"))
factorial=1
i=1
while i<=num:
    factorial *= i
    i +=1
print("factorial=",factorial)
      
