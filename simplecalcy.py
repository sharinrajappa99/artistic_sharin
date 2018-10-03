#program for simple calculator

i=int(input("Enter value of i: "))
j=int(input("Enter value of j: "))
o=input("what do you want to do? +,-,x,/: ")

def add():
	return i+j
def sub():
    return i-j
def mult():
    return i*j
def divide():
    return i/j

if(o=='+'):
    print("addition=",add())
elif(o=='-'):
    print("subtraction=",sub())
elif(o=='x'):
    res=mult(i,j)
    print("multiplication=",mult())
elif(o=='/'):
    print("division=",divide())
