#functions

a=int(input("enter the value of a"))
b=int(input("enter the value of b"))


def add():
	c=a+b
	return c

def sub():
	c=a-b
	return c

def multi():
	c=a*b
	return c

def div():
	c=a/b
	return c

print("addition of a and b",add())
print("subtraction of a and b", sub())
print("multiplication of and b", multi())
print("division of a and b", div())

