# input from the user to roll the dice
i=0
import random 
while i<5:
	a=str(input("enter r to roll the dice and q to quit"))
	if(a=='r'):
		print(random.randint(1,6))
	else:
		print("exit")
		break
    
