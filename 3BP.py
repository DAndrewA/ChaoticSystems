from Tkinter import *
import math
import time

app = Tk()
c = Canvas(app,height="500",width="500")
c.pack()

# Defines the body object. It will store the position and velocity vector for the body, aswell as its mass and the ability to calculate specific values.
class body:
    # This is the function that runs when the object is instantiated.
    def __init__(self,startPosition,startVelocity,mass):
        self.position = startPosition
        self.velocity = startVelocity
        self.mass = mass

    # Calculates the speed of the body by using its vector and pythagoras' theorum.
    def calculateSpeed(self):
        self.speed = math.sqrt(self.velocity[0]**2 + self.velocity[1]**2)

# Calculates the distance between two points. This will be used for getting the distance from a body to the COG.
def calcDistance(pos1,pos2):
    distanceV = []
    # Takes the biggest smallest one from the biggest one
    if pos1[0] > pos2[0]:
        distanceV[0] = pos1[0] - pos2[0]
    else:
        distanceV[0] = pos2[0] - pos1[0]

    if pos1[1] > pos2[1]:
        distanceV[1] = pos1[1] - pos2[1]
    else:
        distanceV[1] = pos2[1] - pos1[1]

    distance = math.sqrt(distanceV[0]**2 + distanceV[1]**2)
    return distance

# Claculates the position of the centre of gravity - COG
def calcCOG(bodies):
    # Sets the values for the COG's mass and x,y position
    COGx = 0
    COGy = 0
    COGm = 0
    # Iterates through bodies and adds a weighted average of their positions to get a mass accurate COG
    for i in range(len(bodies)):
        COGx += bodies[i].position[0]*bodies[i].mass
        COGy += bodies[i].position[1]*bodies[i].mass
        COGm += bodies[i].mass
    # Divides the values by the overall mass to get the weighted average
    COGx = COGx / COGm
    COGy = COGy / COGm
    return [COGx,COGy,COGm]

# Calculates the difference in time between the current frame and the previous one (and sets the time for the previous frame as the current time)
def calcDeltaTime():
    timeFromLastFrame = time.time() - lastFrame
    lastFrame = time.time()
    return timeFromLastFrame

# Instantiating the objects and setting their positions and velocities
body1 = body([430,210],[-50,-30],100)
body2 = body([50,150],[80,40],100)
body3 = body([300,450],[20,-50],50)

# Drawing the bodies onto the canvas
c.create_oval(body1.position[0]-5,body1.position[1]-5,body1.position[0]+5,body1.position[1]+5,tag="body1Circle",fill="green")
c.create_oval(body2.position[0]-5,body2.position[1]-5,body2.position[0]+5,body2.position[1]+5,tag="body2Circle",fill="blue")
c.create_oval(body3.position[0]-5,body3.position[1]-5,body3.position[0]+5,body3.position[1]+5,tag="body3Circle",fill="red")

global lastFrame = time.time()

# Makes the program run forever (or until it is closed)
while True:
    deltaTime = calcDelatTime()
    b1NewPos = []
    b2NewPos = []
    b3NewPos = []
    # Calculates the movements of the first body
    COG1 = calcGOG([body2,body3])
    b1Distance = calcDistance(body1.position,COG1)
        # CALCULATE THE FORCE, THEN INTERPOLATE, THEN REPEAT

    c.update()


mainloop()
