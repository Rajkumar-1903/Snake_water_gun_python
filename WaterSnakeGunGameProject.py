import random

def swg(comp,mine):
    if (comp==mine):
        return None
    if(comp =='s' and mine =='g'):
        return True
    elif(comp=='w' and mine =='s'):
        return True
    elif(comp=='g' and mine == 'w'):
        return True
    else:
        return False


choice = ('s','w','g')
comp = random.randint(0,2)
comp = choice[comp]
mine = input("choose either s for snake,w for water or g for gun:")

win = swg(comp,mine)
print(f"You choose {mine} and the Computer choose {comp}")
if win is None:
    print("Match drawn")
if win:
    print("You won!")
else:
    print("you loose:(")