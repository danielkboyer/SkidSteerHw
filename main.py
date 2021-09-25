import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


#for part two add Vx and Vy velocity graph, add theta direction
#

length = .5
width = .3

colors = ['r', 'g', 'b', 'm', 'y']
LINEWIDTH=2
t_updateTime = .01




fig = plt.figure()
ax = fig.add_subplot(3,4,(1,4))

ax_2 = fig.add_subplot(3,4,5)
ax_3 = fig.add_subplot(3,4,6)
ax_4 = fig.add_subplot(3,4,7)
ax_5 = fig.add_subplot(3,4,8)

ax_6 = fig.add_subplot(3,4,9)
ax_7 = fig.add_subplot(3,4,10)
ax_8 = fig.add_subplot(3,4,11)
ax_9 = fig.add_subplot(3,4,12)
ax.title.set_text("part 1 (x,y)")

ax_2.title.set_text("Skid 5X5 (x,y)")
ax_3.title.set_text("Skid 5X5 (time,xVel) Wrld")
ax_4.title.set_text("Skid 5X5 (time,yVel) Wrld")
ax_5.title.set_text("Skid 5X5 (time,Theta)")

ax_6.title.set_text("Swedish 5X5 (x,y)")
ax_7.title.set_text("Swedish 5X5 (time,xVel) Wrld")
ax_8.title.set_text("Swedish 5X5 (time,yVel) Wrld")
ax_9.title.set_text("Swedish 5X5 (time,Theta)")
part_a_command_list = [(5,1,1.5),(3,-1,-1.5),(8,.8,-2),(10,2,2)]

#.235 is a 90 degree angle
ninety_turn_angle = width*np.pi/4




def Get5v5():
    commandList = []
    leftTurnAngle = ninety_turn_angle
    rightTurnAngle = -ninety_turn_angle
    endRange = (int)(5/width)
    for i in range(0,endRange):
        commandList.append((5,1,1))
        commandList.append((1,leftTurnAngle,rightTurnAngle))
        commandList.append((width,1,1))
        commandList.append((1,leftTurnAngle,rightTurnAngle))
        leftTurnAngle *= -1
        rightTurnAngle *= -1
    commandList.append((5,1,1))
    return commandList

part_b_command_list = Get5v5()
command_lists = [(ax, part_a_command_list),(ax_2,part_b_command_list)]

commandNumber = 0
for commandList in command_lists:
    x = 0 
    y = 0
    alphaSkid = 0

    graph = commandList[0]
    totalTime = 0
    xVel = 0
    yVel = 0
    for i,command in enumerate(commandList[1]):
        
        xSkidList =[]
        ySkiList =[]

        thetaList = []
        timeThetaList = []

        xVelocityList = []
        yVelocityList = []

        

        
        for dt in np.arange(0.0, command[0],t_updateTime):
            totalTime += t_updateTime
            xSkidList = np.append(xSkidList,x)
            ySkiList = np.append(ySkiList,y)

            xVelocityList = np.append(xVelocityList,xVel)
            yVelocityList = np.append(yVelocityList,yVel)
            timeThetaList = np.append(timeThetaList,totalTime)
            thetaList = np.append(thetaList,alphaSkid)

            xVel = (-(command[2] + command[1])/2) * np.sin(alphaSkid)
            yVel = ((command[2] + command[1])/2) * np.cos(alphaSkid)
            alphaSkidVel =  (command[2]-command[1])/width
            alphaSkid += alphaSkidVel * t_updateTime
            x +=  xVel * t_updateTime
            y +=  yVel * t_updateTime
            

        
    #label=f'Duration={command[0]}, LVel={command[1]}, RVel={command[2]}'
        graph.plot(xSkidList, ySkiList, colors[i%len(colors)], linewidth=LINEWIDTH)
        #ax_2.plot(xSwedishList,ySwedishList, colors[i], linewidth=LINEWIDTH)
        graph.spines['left'].set_position('zero')
        graph.spines['right'].set_color('none')
        graph.spines['bottom'].set_position('zero')
        graph.spines['top'].set_color('none')
        if commandNumber == 1:
            ax_3.plot(timeThetaList, xVelocityList, colors[i%len(colors)], linewidth=LINEWIDTH)
            #ax_2.plot(xSwedishList,ySwedishList, colors[i], linewidth=LINEWIDTH)
            ax_3.spines['left'].set_position('zero')
            ax_3.spines['right'].set_color('none')
            ax_3.spines['bottom'].set_position('zero')
            ax_3.spines['top'].set_color('none')

            ax_4.plot(timeThetaList, yVelocityList, colors[i%len(colors)], linewidth=LINEWIDTH)
            #ax_2.plot(xSwedishList,ySwedishList, colors[i], linewidth=LINEWIDTH)
            ax_4.spines['left'].set_position('zero')
            ax_4.spines['right'].set_color('none')
            ax_4.spines['bottom'].set_position('zero')
            ax_4.spines['top'].set_color('none')

            ax_5.plot(timeThetaList, thetaList, colors[i%len(colors)], linewidth=LINEWIDTH)
            #ax_2.plot(xSwedishList,ySwedishList, colors[i], linewidth=LINEWIDTH)
            ax_5.spines['left'].set_position('zero')
            ax_5.spines['right'].set_color('none')
            ax_5.spines['bottom'].set_position('zero')
            ax_5.spines['top'].set_color('none')
    commandNumber+=1


def Get5V5Swedish():
    commandList = []
    endRange = (int)(5/width/2)
    for i in range(0,endRange):
        commandList.append((0,1,5))
        commandList.append((1,0,width))
        commandList.append((0,-1,5))
        commandList.append((1,0,width))

    commandList.append((0,1,5))
    return commandList
        
swedishWheelsCommand = Get5V5Swedish()

x = 0 
y = 0
alphaSkid = 0

totalTime = 0
xVel = 0
yVel = 0
for i,command in enumerate(swedishWheelsCommand):
    
    xSkidList =[]
    ySkiList =[]

    thetaList = []
    timeThetaList = []

    xVelocityList = []
    yVelocityList = []

    

    
    for dt in np.arange(0.0, command[2],t_updateTime):
        totalTime += t_updateTime
        xSkidList = np.append(xSkidList,x)
        ySkiList = np.append(ySkiList,y)

        xVelocityList = np.append(xVelocityList,xVel)
        yVelocityList = np.append(yVelocityList,yVel)
        timeThetaList = np.append(timeThetaList,totalTime)
        thetaList = np.append(thetaList,alphaSkid)

        xVel = command[0]
        yVel = command[1]
        alphaSkidVel =  0
        alphaSkid += alphaSkidVel * t_updateTime
        x +=  xVel * t_updateTime
        y +=  yVel * t_updateTime


    ax_6.plot(xSkidList, ySkiList, colors[i%len(colors)], linewidth=LINEWIDTH)
    #ax_2.plot(xSwedishList,ySwedishList, colors[i], linewidth=LINEWIDTH)
    ax_6.spines['left'].set_position('zero')
    ax_6.spines['right'].set_color('none')
    ax_6.spines['bottom'].set_position('zero')
    ax_6.spines['top'].set_color('none')
   
    ax_7.plot(timeThetaList, xVelocityList, colors[i%len(colors)], linewidth=LINEWIDTH)
    #ax_2.plot(xSwedishList,ySwedishList, colors[i], linewidth=LINEWIDTH)
    ax_7.spines['left'].set_position('zero')
    ax_7.spines['right'].set_color('none')
    ax_7.spines['bottom'].set_position('zero')
    ax_7.spines['top'].set_color('none')

    ax_8.plot(timeThetaList, yVelocityList, colors[i%len(colors)], linewidth=LINEWIDTH)
    #ax_2.plot(xSwedishList,ySwedishList, colors[i], linewidth=LINEWIDTH)
    ax_8.spines['left'].set_position('zero')
    ax_8.spines['right'].set_color('none')
    ax_8.spines['bottom'].set_position('zero')
    ax_8.spines['top'].set_color('none')

    ax_9.plot(timeThetaList, thetaList, colors[i%len(colors)], linewidth=LINEWIDTH)
    #ax_2.plot(xSwedishList,ySwedishList, colors[i], linewidth=LINEWIDTH)
    ax_9.spines['left'].set_position('zero')
    ax_9.spines['right'].set_color('none')
    ax_9.spines['bottom'].set_position('zero')
    ax_9.spines['top'].set_color('none')

plt.ioff()
plt.show()
        
    
                                