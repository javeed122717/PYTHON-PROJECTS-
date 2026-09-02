import time
class Calculator:
    def __init__ (self)->None:
        print("Calculator has been initialized")
        print("Menu will be displayed in 3 seconds")
    def add(self , *args: int)->int:
        return sum(args)
    def sub(self , *args: int)->int:
        r=args[0]
        for i in args[1:]:
            r-=i
        return r
    def mul(self , *args: int)->int:
        r=1
        for i in args:
            r*=i
        return r
    def div(self , *args: int)->float:
        r=args[0]
        for i in args[1:]:
            r/=i
        return r
    def get_args(self)->list:
        args=[]
        n=int(input("Enter the number of arguements:"))
        for i in range(n):
            h=int(input(f'Enter the {i+1} element:'))
            args.append(h)
        return args
k=Calculator()
for i in range(3):
    print(f"'{i+1}' second...")
    time.sleep(1)
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5.Change arguements\n6.Exit\n")
args=[]
f=0
args=k.get_args()
while f==0:
    c=int(input("Enter your choice of selection:"))
    if c==1:
        print("Result=",k.add(*args))
    elif c==2:
        print("Result=",k.sub(*args))
    elif c==3:
        print("Result=",k.mul(*args))
    elif c==4:
        print("Result=",k.div(*args))
    elif c not in[1,2,3,4,5,6]:
        print("Inavlid choice try again")
    elif c==6:
        print("Exiting the operation")
        f=1
    elif c==5:
        args=k.get_args()
        print("Arguments changed successfully")
    else:
        print('some mystical error occured')
    
         
        