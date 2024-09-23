import time
name = input('Enter your name: ')
recenttime = time.strftime('%H:%M:%S')
Recenttime = int(time.strftime('%H'))
c= name.title()
if(4<=Recenttime<12):
    print('GOOD MORNING,',c,'its, ',recenttime,"A.M")
elif(12>=Recenttime<17):
    print('GOOD EVENING,',c,'its, ',recenttime,"P.M")
else:
    print('GOOD NIGHT,',c,'its, ',recenttime,"P.M")
