import oops

def mat():
    a=int(input("Enter the Num 1:"))
    b=int(input("Enter the Num 2:"))


    cal=oops.Calci()

    print(cal.add(a,b))
    print(cal.substract(a,b))
    print(cal.multi(a,b))
    print(cal.div(a,b))

mat()