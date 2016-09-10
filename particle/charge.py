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
    def __init__(self,startPos,startVel,mass,charge,id):
        self.position = startPos
        self.velocity = startVel
        self.charge = charge
        self.id = id
        self.radius = 2
        self.drawParticle(charge)
        self.mass = mass

    def drawParticle(self,charge):
        if charge < 0:
            colour = "#FF0000"
        elif charge == 0:
            colour = "#00FF00"
        else:
            colour = "#0000FF"

        c.create_rectangle(self.position[0]-self.radius,self.position[1]-self.radius,self.position[0]+self.radius,self.position[1]+self.radius,tag="body"+str(self.id)+"Circle",fill=colour)
        c.create_line(self.position[0],self.position[1],self.position[0]+self.velocity[0],self.position[1]+self.velocity[1],fill="blue",tag="body" + str(self.id) + "Arrow",arrow="last")

    def updateMovement(self,deltaTime):
        c.move("body" + str(self.id) + "Circle",self.velocity[0]*deltaTime,self.velocity[1]*deltaTime)
        c.coords("body" + str(self.id) + "Arrow",self.position[0],self.position[1],self.position[0]+self.velocity[0],self.position[1]+self.velocity[1])
        self.position = [self.position[0] + self.velocity[0]*deltaTime,
                         self.position[1] + self.velocity[1]*deltaTime]


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

def destroy(i,x):
    # deleting the current displayed rectangles
    c.delete("body" + str(particles[i].id) + "Circle")
    c.delete("body" + str(particles[x].id) + "Circle")
    c.delete("body" + str(particles[i].id) + "Arrow")
    c.delete("body" + str(particles[x].id) + "Arrow")

    # creating the new particle, then removing old ones
    newParticle = particle(particles[i].position,
                  [(particles[i].velocity[0]*particles[i].mass + particles[x].velocity[0]*particles[x].mass)/(particles[i].mass + particles[x].mass),
                   (particles[i].velocity[1]*particles[i].mass + particles[x].velocity[1]*particles[x].mass)/(particles[i].mass + particles[x].mass)],
                  particles[i].mass + particles[x].mass,
                  particles[i].charge + particles[x].charge,
                  len(particles)-2)

    # x MUST be destroyed first otherwise the indexes of the elements all change
    particles.pop(x)
    particles.pop(i)
    particles.append(newParticle)


# creating a bunch of particles
particles = []
particles.append(particle([50,320],[0,0],1,1,0))
particles.append(particle([150,320],[0,0],1,-2,1))
particles.append(particle([250,520],[0,0],1,-1,2))
particles.append(particle([350,320],[11,1],1,-1,3))
particles.append(particle([450,320],[0,0],2,1,4))
particles.append(particle([550,320],[0,0],1,-2,5))
particles.append(particle([50,380],[13,6],1,1,6))
particles.append(particle([150,380],[0,0],1,4,7))
particles.append(particle([250,370],[0,0],1,-1,8))
particles.append(particle([350,380],[10,3],1,1,9))
particles.append(particle([450,380],[0,0],1,-1,10))
particles.append(particle([550,380],[0,0],1,-1,11))

kConstant = 1000

# makes the program run forever, or until it is closed
while True:
    deltaTime = 0.005
    # coloumbs law:
    # F = k * q * Q / r^2

    for indexI,i in enumerate(particles):
        for indexX,x in enumerate(particles):
            if i.id != x.id:
                if calcDistance(i.position,x.position) < i.radius + x.radius and x.charge * i.charge < 0:
                    destroy(indexI,indexX)

                distance = calcDistance(i.position,x.position)
                if distance == 0:
                    distance += 0.001
                F = 0-(kConstant*i.charge*x.charge)/(distance**2)

                # calculating the direction of the force and therefore the force vector
                deltaX = x.position[0] - i.position[0]
                deltaY = x.position[1] - i.position[1]
                thetaRad = math.atan2(deltaX,deltaY)

                # calculating x and y force components, then accelaration
                Fx = math.sin(thetaRad) * F
                Fy = math.cos(thetaRad) * F
                Ax = Fx*i.mass
                Ay = Fy*i.mass

                # Calculate final velocity vector by using v=u+at
                i.velocity[0] += Ax*deltaTime
                i.velocity[1] += Ay*deltaTime

    # Moving all of the bodies after calculations
    for i in range(len(particles)):
        particles[i].updateMovement(deltaTime)
    c.update()

mainloop()
