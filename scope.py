'''x=10
def show():
    global y
    y=30
    print(x)
    print(y)
show()
print(x)
print(y)'''
x=20
def show():
    x=50
    global y
    y=90
#   y=70 # it will create error
    print(x)
    print(globals()['x'])
show()
print(x)
print(y)

