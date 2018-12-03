#tic tac toe
a=['1','2','3','4','5','6','7','8','9']

def printboard() :
	print( '\n-----')
	print('|' + a[0] + '|' + a[1] + '|' + a[2] + '|')
	print('-----')
	print('|' + a[3] + '|' + a[4] + '|' + a[5] + '|')
	print('-----')
	print('|' + a[6] + '|' + a[7] + '|' + a[8] + '|')
	print('-----\n')

p1 = True

while(True):
	printboard()
	#player 1 plays
	if p1:
		p = input("player 1,you have to choose your place : ")
		if p in a:
			a[int(p)-1] = 'x'
			p1 = not p1
	#player 2 plays
	else:
		p = input("player 2,you have to choose your place : ")	
		if p in a:
			a[int(p)-1] = '0'
			p1 = not p1
	#check for rows
	for i in(0,3,6):
		if(a[i]==a[i+1] and a[i]==[i+2]):
			print("game ends");
			printboard()
			exit()
	#check for columns
	for i in range(3):
		if(a[i]==a[i+3] and a[i]==a[i+6]):
			print("game ends")
			printboard()
			exit()
	#check for diagonal(from left to right)
		if(a[0]==a[4] and a[0]==a[8]):
			print("game ends")
			printboard()
			exit()
	#check for diagonal(from right to left)
		if(a[2]==a[4] and a[2]==a[6]):
			printboard()
			



	
