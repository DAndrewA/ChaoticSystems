'''
This is a test bed for the dual pendulum program.
It will only contain one pendulum that will swing around a pivot P.
This is to get what needs to be done to accelarate the mass sorted before attempting the dual pendulum system.
'''
from tkinter import *
import math
import time

app = Tk()
app.title("Pendulum")
c = Canvas(app,height="700",width="700")
c.pack()

# CONSTANTS
density = 100
gravity = 0.5
deltaTime = 0.005

class Pendulum:
    # Mass is the mass of the pendulum, which affects how it accelarates
    # Radius is the distance between the pivot and point mass
    # startAngle (in RADIANS) is the angle from being vertically downwards that the mass will start at
    # startVelocity is the speed with which the pendulum is travelling. It is a one dimensional value, +ve being clockwise
    def __init__(self,mass,radius,startAngle,startVelocity):
        self.mass = mass
        self.radius = radius
        self.angle = startAngle
        self.velocity = startVelocity
        self.position = [0,0]
        self.getPosition()
        self.drawPendulum()

    def getPosition(self):
        # x = rsin(theta)
        # y = rcos(theta)
        x = self.radius * math.sin(self.angle)
        y = self.radius * math.cos(self.angle)
        # differentiates between different y values as cosine repeats every pi degrees
        if self.angle < -math.pi/2 and self.angle > math.pi/2:
            y = -y
        self.position = [x,y]

    def drawPendulum(self):
        volume = self.mass * density
        self.width = (volume/((4/3)*math.pi))**(1/3)

        c.create_oval(350+ self.position[0]-self.width,350+ self.position[1]-self.width,350+ self.position[0]+self.width,350+ self.position[1]+self.width,fill="blue",tag="p")

p = Pendulum(10,200,math.pi/2,0)

# Where the code runs. Calculates the forces acting upon the pendulum, then applies them
while True:
    # tangent is the angle that is tangential to
    # Force A component runs tangential to radius
    # Force B component runs parrallel to radius, is cancelled out by tension
    pTangent = math.pi - (p.angle + math.pi/2)
    fA = gravity * math.cos(pTangent)
    fB = gravity * math.sin(pTangent)

    #p.tension = fB
    p.velocity += fA* deltaTime
    # CALCULATES NEW ANGLE FOR p
    newAngle = p.angle - (p.velocity*deltaTime/p.radius)
    p.angle = newAngle
    p.getPosition()

    c.coords("p",350+ p.position[0]-p.width,350+ p.position[1]-p.width,350+ p.position[0]+p.width,350+ p.position[1]+p.width)
    c.update()

mainloop()
