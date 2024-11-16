while True:
    print("1.Add\n 2.Sub\n 3.Div\n 4.Multi\n 5.off")
    n=int(input("enter any no:"))

    x=[1,2,3,4]
    if n in x:
        x=int(input("enetr 1st no:"))
        y=int(input("enter 2nd no:"))
        if n==1:
           print("Addition=",x+y)
        elif n==2:
            print("Subtract",x-y)
        elif n==3:
            print("Division",x/y)
        elif n==4:
            print("Multiply",x*y)
    elif n==5:
        break
    else:
        print("Enter right no:")


                            
