# BOILERPLATE STUFF
from tkinter import *
import math

# creating the canvas for the app
app = Tk()
app.title("n-body problem")
c = Canvas(app,height="700",width="700")
c.pack()

# program specific code starts here
class particle():
    def __init__(self,startPos,startVel,charge,id):
        self.position = startPos
        self.velocity = startVel
        self.charge = charge
        self.id = id
        self.radius = 2
        self.drawParticle(charge)

    def drawParticle(self,charge):
        if charge == -1:
            colour = "#FF0000"
        elif charge == 0:
            colour = "#AA00AA"
        else:
            colour = "#0000FF"

        c.create_rectangle(self.position[0]-self.radius,self.position[1]-self.radius,self.position[0]+self.radius,self.position[1]+self.radius,tag="body"+str(self.id)+"Circle",fill=colour)
        #c.create_line(self.position[0],self.position[1],self.position[0]+self.velocity[0],self.position[1]+self.velocity[1],fill="blue",tag="body" + str(self.id) + "Arrow",arrow="last")

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

# creating a bunch of particles
particles = []
particles.append(particle([100,300],[0,0],-1,1))
particles.append(particle([100,400],[0,0],1,2))
particles.append(particle([200,300],[0,0],-1,3))
particles.append(particle([200,400],[0,0],-1,4))
particles.append(particle([300,300],[0,0],1,5))
particles.append(particle([300,400],[0,0],-1,6))
particles.append(particle([400,300],[0,0],-1,7))
particles.append(particle([400,400],[0,0],1,8))
particles.append(particle([500,300],[0,0],-1,9))
particles.append(particle([500,400],[0,0],-1,10))
particles.append(particle([600,300],[0,0],1,11))
particles.append(particle([600,400],[0,0],-1,12))

# makes the program run forever, or until it is closed
while True:
    deltaTime = 0.0005

    for i in particles:
        for x in particles:
            if i.id != x.id:



mainloop()
