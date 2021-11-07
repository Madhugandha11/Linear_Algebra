def add(l):
    answer=0
    for i in l:
        answer= answer + i
    return answer

def sub(a,b):
    answer=0
    answer = a - b
    return answer

def multi(l):
    answer=1
    for i in l:
        answer= answer*i
    return answer

def division(a,b):
    answer=1
    answer = a/b
    return answer

print("LETS DO SOME BASIC CALCULATIONS")
print("WHAT DO YOU WANNA DO?")
print("1.ADDITION \n2.SUBTRACTION \n3.MULTIPLICATION \n4.DIVISION ")
choice = int(input("CHOOSE YOUR OPTION"))
if(choice == 1):
    print("Enter your values for addition")
    l=[]
    n = int(input("enter the number of elements"))
    for i in range(0,n):
        element = int(input())
        l.append(element)
    result = add(l)
    print("Your answer is: ",result)
elif(choice ==2):
    print("Enter two values for substraction")
    a=int(input("Your first value:"))
    b=int(input("Your second value:"))
    result = sub(a,b)
    print("Your answer is: ",result)
elif(choice==3):
    print("Enter your values for multiplication")
    l=[]
    n = int(input("enter the number of elements"))
    for i in range(0,n):
        element = int(input())
        l.append(element)
    result = multi(l)
    print("Your answer is: ",result)
elif(choice==4):
    print("Enter two values for division")
    a=int(input("Your first value:"))
    b=int(input("Your second value:"))
    result = division(a,b)
    print("Your answer is: ",result)
else:
    print("Enter the right choice") 

