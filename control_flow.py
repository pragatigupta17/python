''' CONTROL FLOW 
     1) sequantial control flow - it excute every line of code
     2) conditional control flow - it takes limitation like which lines we want to execute we can excute , 
     there are types of condition statement ---
           1)if ,
           2)if-else,
           3)if-elseif,
           4)if-elseif-else.

     3) iterative/looping control flow - it execute at least at one time, some type of looping
           1)While loop -(infinite-time execution) 
           2)for loop - (final-time execution)
     4) transfer statement - 1)continue,
                             2)break,
                             3)pass'''
# --------------------------------------------------------------------------------------#
'''flow chart - if else
                statement 1
                    |
                    |
                statement2
                     |
                     |
                if (condition)------T
                      |             |
                      | F        statement3
                statement4          |    
                      |             |
                      |             |    
                      ---------------  
                      |
                      |
                statement5 (final statement)  '''
# SYNTAX OF IF-ELSE
x=10
y=20
if x==y:
    print("both are equql")
else:
    print("hello")
                    
# SYNTAX OF if-elif-else
a=int (input("enter 1st value"))
print("1.add\n 2.sub\n 3.div\n 4.multiply")
n=int(input("enter your choice no."))
b=int (input("enter 2nd value"))
if n==1:
    print(a+b)
elif n==2:
    print(a-b)
elif n==3:
    print(a/b)
elif n==4:
    print(a*b)
else:
    print("plese enter correct no")



                            
                            