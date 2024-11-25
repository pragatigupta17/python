
num = int(input("Enter the number of terms in the Fibonacci series: "))
a=0
b =1
print("Fibonacci Series:")
for _ in range(num):
    print(a, end=" ")  
    a, b = b, a + b  
