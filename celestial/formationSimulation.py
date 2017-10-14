from tkinter import *
import random
import math
import time

app = Tk()
app.title("Formation Simulation")
c = Canvas(app,height="1000",width="1000")
c.pack()

# the universal length and mass scalars, the gravitational constant and the time frame through which each calculation is performed
GConst = 1
dT = 1
lScalar = 1
mScalar = 1

# the number of blocks spanning the simulation space
blockNumber = 10

# defines the class that manages the running of the program and the blocks
class Manager():
    # grid: a 2d array containing the blocks in use in the simulation
    def __init__(self,grid=[]):

# defines the block class, which define a region containing particles
class Block():
    # position: the relative coordinates of the top left corner of the block
    # length: the relative length of the block
    # particles: an array containing the particles within the confines of the block
    def __init__(self,position,length,particles=[]):
        self.position = position
        self.length = length
        self.particles = particles
        self.mass,self.COG = self.findCOG()

    def findCOG(self):
        moment = [0,0]
        totalMass = 0
        for p in self.particles:
            moment[0] += p.position[0]*p.mass
            moment[1] += p.position[1]*p.mass
            totalMass += p.mass
        COG = [moment[0]/totalMass,moment[1]/totalMass]
        return totalMass,COG

# defines the particles that will occupy the simulation
class Particle():
    def __init__(self,startPos,startVel,id,mass=1):
        self.position = startPos
        self.velocity = startVel
        self.id = id
        self.mass = mass

mainloop()
