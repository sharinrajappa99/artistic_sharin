#snakesandladders
import random
count=0
def myroll():
       return random.randint(1,6)
while(count<=100):
       n=input("press r to roll the dice")
       if(n=='r'):
               r=myroll()
               count=count+r
               print("u got",r)
               print("new position is",count)
               if(count==8):
                      count=37
                      print("you climbed the ladder")
               elif(count==11):
                      count=2
                      print("snake has bitten you")
               elif(count==13):
                      count=34
                      print("you climbed the ladder")
               elif(count==25):
                      count=4
                      print("snake has bitten you")             
               elif(count==38):
                      count=9
                      print("snake has bitten you")
               elif(count==40):
                      count=68
                      print("you climbed the ladder") 
               elif(count==52):
                      count=81
                      print("you climbed the ladder")
               elif(count==65):
                      count=46
                      print("snake has bitten you")
               elif(count==76):
                      count=97
                      print("you climbed the ladder")
               elif(count==89):
                      count=70
                      print("snake has bitten you")
               elif(count==93):
                      count=64
                      print("snake has bitten you")
               elif(count>100):
                      print("count is beyond 100")
                      count==count-r
               elif(count==100):
                      print("congratulations!you won")
                      break      

