#end parameter
print("welcome" , end=" ")
print("to",end=" ")
print("python classes")
#-----------------------
#sep parameter
print("welcom","to","python",sep="$")

#-----------------------------------------
#indent
#to define block in python we use indent,
#it is equivalent to {} in c++,
#    python ----> indent


print("left most cornor uuyhdcdshhskcsdhfshfhdscdschdshfi\
       chgfhfgjkhkhjlkhhiuhhkhh\
       bjhhhukkjhkjhkjhjbkjhkjhih\
       ghuhikhhhihiu")
print("aaaaaaaa"
      "hcdhvckzdcvlskdjiuds"
      "jdnckdschids")

#--------------------------
#if body takes automatic space in next line

if True:
    print("if body")


#tokens:---------------------------------------------
#smallest unit of code which has a meaning to translate
#there are five type of token
'''1. keywords --- reserve words there are 35 keywords None,True,False,while,for,break, return etc
keywords are the reserverd words which has a special meaning to compiler predefine words three keywords are written in capital letter True,False,None)
'''
import keyword
print(keyword.kwlist)
print("count",len(keyword.kwlist))
'''2. identifier --- to identify the component of program uniquly we use identifire. 
5 rules of idenifire - 1. first character start with alphabet + underscore
                       2. Remaining -> alphabet + underscore + digit
                               #valid -> a100abc , _abc ,Break = 1879
                               #invalid -> 100abc
                       3. no keywords are allowed
                       4. no whitespace --> area rectangle
                       5. name should be relevent readable (subject_marks)
                       
 3. literal--> this is objects stored in memory to perform operation .
              fruit = "mango" # string literal
              int = 90 # int literal
              list1 = [2,3,4,5,] # int lirtals
 
 4. secial symbols(delimiter) --> puncuators ([],{},(),:,;,"",)
 5. operators --> (and,or,not,+,-,%,*,&,>,<,)  when ever want to perform any operation we have to use some operator
                      a=90 # a,b and c are operand by the help of them we perform operations
                      b=80 # c= a+b
                      print(24%5) --4
                      print(5%24) --5
                      *note--> modulous operator is used in cyclic process just like 'watch' '''
print("PRAGATI")    # heres are three 3 tokens in this print function
# print() identifire 
#"welcome" literals(string)
# #comment



