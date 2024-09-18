import random 

rannum = random.randint(1,100)

while True:
    userno = int (input ("guess the no:"))
    if (userno==rannum):
        print ("correct you won")
        break
    elif (userno<rannum):
        print ("geess biger no")
    else:
        print ("geess small no")

print ("-----game over bro------")
