from tkinter import *
import math
import time

app = Tk()
app.title("n-body problem")
c = Canvas(app,height="700",width="700")
c.pack()

# Defines the body object. It will store the position and velocity vector for the body, aswell as its mass and the ability to calculate specific values.
density = 2.5
class body:
    # This is the function that runs when the object is instantiated.
    def __init__(self,startPosition,startVelocity,mass,id,colour):
        self.position = startPosition
        self.velocity = startVelocity
        self.mass = mass
        self.id = id
        self.status = 1
        self.drawBody(colour)

    def drawBody(self,colour):
        volume = density*self.mass
        # allowing for negative masses
        if volume < 0:
            volume *= -1

        self.radius =  (volume/((4/3)*math.pi))**(1/3)
        c.create_oval(self.position[0]-self.radius,self.position[1]-self.radius,self.position[0]+self.radius,self.position[1]+self.radius,tag="body"+str(self.id)+"Circle",fill=colour)
        c.create_line(self.position[0],self.position[1],self.position[0]+self.velocity[0],self.position[1]+self.velocity[1],fill="blue",tag="body" + str(self.id) + "Arrow",arrow="last")

    def updateMovement(self,deltaTime):
        # Moves the canvas object and the bodies coordinates
        c.move("body" + str(self.id) + "Circle",self.velocity[0]*deltaTime,self.velocity[1]*deltaTime)
        c.coords("body" + str(self.id) + "Arrow",self.position[0],self.position[1],self.position[0]+self.velocity[0],self.position[1]+self.velocity[1])
        self.position = [self.position[0] + self.velocity[0]*deltaTime,
                                        self.position[1] + self.velocity[1]*deltaTime]

    # never actually used as a function
    def checkCollision(self,other):
        if self.mass > other.mass:
            return
        else:
            distance = calcDistance(self.position,other.position)-(self.radius)
            if distance - other.radius < 0:
                self.velocity[0] = (self.velocity[0]*self.mass)+(other.velocity[0]*other.mass)/(self.mass+other.mass)
                self.velocity[1] = (self.velocity[1]*self.mass)+(other.velocity[1]*other.mass)/(self.mass+other.mass)
                self. mass += self.mass

                other.mass = 0
                other.velocity = [0,0]
                #other.position = [other.id*(-200),-200]
                other.status = 0

# Calculates the distance between two points. This will be used for getting the distance from a body to the COG.
def calcDistance(pos1,pos2):
    distanceV = []
    # Takes the biggest smallest one from the biggest one
    if pos1[0] > pos2[0]:
        distanceV.append(pos1[0] - pos2[0])
    else:
        distanceV.append(pos2[0] - pos1[0])

    if pos1[1] > pos2[1]:
        distanceV.append(pos1[1] - pos2[1])
    else:
        distanceV.append(pos2[1] - pos1[1])

    distance = math.sqrt(distanceV[0]**2 + distanceV[1]**2)
    return distance

# Instantiating the objects and setting their positions and velocities
# body([position],[velocity],mass,id,colour)
body1 = body([350,350],[0,0],150,0,"#FF0000")
body2 = body([150,350],[10,20],250,1,"#0000FF")
body3 = body([550,350],[-10,-20],250,2,"#00FF00")
body4 = body([350,150],[-30,0],150,3,"#FF00FF")
body5 = body([350,550],[30,0],150,4,"#FFFF00")
'''
body6 = body([594.3375,600],[0,0],1300,5,"#00FFFF")
body7 = body([300,550],[20,15],5000,6,"#FFFFFF")
body8 = body([70,650],[-20,5],3000,7,"black")
'''
#global lastFrame
#lastFrame = time.time()
gravityConstant = 500

# Makes the program run forever (or until it is closed)
while True:
    # Updates the bodies variable with the current objects
    bodies = [body1,body2,body3,body4,body5]#,body6,body7,body8]
    # Gets the time frame to multiply by and sets the frame values
    deltaTime =  0.0005
    # Goes through all bodies
    for i in bodies:
        # Calculates the accelaration for all of the bodies before moving them
        for x in bodies:
            if i.id != x.id and i.status == 1:
                COG = x.position
                # Force = G * ((M1*M2)/distance^2)
                F = gravityConstant*((i.mass*x.mass)/(calcDistance(COG,i.position)**2))
                # Break down force into x and y components
                        # THE INTERNET IS A REALLY USEFULL THING
                # Calculate angle theta with equation in equation sheet
                deltaX = COG[0] - i.position[0]
                deltaY = COG[1] - i.position[1]
                thetaRad = math.atan2(deltaX,deltaY)
                # Using trig.
                Fx = math.sin(thetaRad)*F
                Fy = math.cos(thetaRad)*F
                # Calculating x and y accelaration
                Ax = Fx/i.mass
                Ay = Fy/i.mass
                # Calculate final velocity vector by using v=u+at
                i.velocity[0] += Ax*deltaTime
                i.velocity[1] += Ay*deltaTime

                #Checking for collision witht the other body
                #i.checkCollision(x)

        '''
        if i.position[0] < 0 or i.position[0] > 700:
            i.velocity[0] *= -1
        if i.position[1] < 0 or i.position[1] >700:
            i.velocity[1] *= -1
        '''
    # Moving all of the bodies after calculations
    for i in range(len(bodies)):
        bodies[i].updateMovement(deltaTime)
    c.update()
    #time.sleep(2)


mainloop()
