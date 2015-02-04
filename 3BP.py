from tkinter import *
import math
import time

global running
running = False
global bodies
bodies = []
gravityConstant = 500

# SIMULATION EDITOR
selector = Tk()
selector.title("Simulation editor")
selector.geometry("300x475")
selectorApp = Frame(selector)
selectorApp.grid()

# Functions for the simulation editor
def createBody():
    bodies.append(body([scaleXAxis.get(),scaleYAxis.get()],[scaleXVelocity.get(),scaleYVelocity.get()],int(entryMass.get()),len(bodies)))
    c.create_oval(bodies[len(bodies)-1].position[0]-5,
                          bodies[len(bodies)-1].position[1]-5,
                          bodies[len(bodies)-1].position[0]+5,
                          bodies[len(bodies)-1].position[1]+5,
                          tag="body"+str(bodies[len(bodies)-1].id)+"Circle",
                          fill=entryColour.get())
    c.update()

def removeBody():
    if len(bodies) > 0:
        c.delete("body"+bodies[bodies[len]-1].id+"Circle")
        bodies.remove(bodies[len(bodies)-1])
        c.update()

def toggleSim():
    try:
        if running == True:
            running = False
        else:
            running = True
            runSimulation()
    except:
        running = True
        runSimulation()

# Defining the widgits for the app and their functions
labelIntroduction = Label(selector,text="Remove/add bodies. Start or stop the simulation.")
labelIntroduction.grid()

# All the sliders for the position of the next body and for the time frame
scaleTimeSlider = Scale(selector,orient="horizontal",from_="-5",to="5",resolution=0.5,length="300",label="Time scale")
scaleTimeSlider.grid()
scaleXAxis = Scale(selector,orient="horizontal",from_="0",to="700",resolution="10",length="300",label="Position X")
scaleXAxis.grid()
scaleYAxis = Scale(selector,orient="horizontal",from_="0",to="700",resolution="10",length="300",label="Position Y")
scaleYAxis.grid()
scaleXVelocity = Scale(selector,orient="horizontal",from_="-50",to="50",resolution="1",length="300",label="Speed X")
scaleXVelocity.grid()
scaleYVelocity = Scale(selector,orient="horizontal",from_="-50",to="50",resolution="1",length="300",label="Speed Y")
scaleYVelocity.grid()

#Widgets for selecting the mass of the next body and colour
labelMass = Label(selector,text="Mass")
labelMass.grid()
entryMass = Entry(selector,width="4")
entryMass.grid()
labelColour = Label(selector,text="Colour")
labelColour.grid()
entryColour = Entry(selector,width="10")
entryColour.grid()
buttonAddNewBody = Button(selector,text="Add body",command=createBody)
buttonAddNewBody.grid()
buttonRemoveLastBody = Button(selector,text="Remove last body",command=removeBody)
buttonRemoveLastBody.grid()

#Widget for toggling the simulation. Should default to off
buttonToggleSim = Button(selector,text="Toggle simulation",command=toggleSim)
buttonToggleSim.grid()

# SIMULATION
canvasApp = Tk()
canvasApp.title("N-Body Problem")
c = Canvas(canvasApp,height="700",width="700")
c.pack()

# Defines the body object. It will store the position and velocity vector for the body, aswell as its mass and the ability to calculate specific values.
class body:
    # This is the function that runs when the object is instantiated.
    def __init__(self,startPosition,startVelocity,mass,id):
        self.position = startPosition
        self.velocity = startVelocity
        self.mass = mass
        self.id = id

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

# Makes the program run forever (or until it is closed)

def runSimulation():
    while running:
        # Gets the time frame to multiply by and sets the frame values
        deltaTime =  float(scaleTimeSlider.get())*0.0005
        # Goes through all bodies
        for i in bodies:
            # Calculates the accelaration for all of the bodies before moving them
            for x in bodies:
                if i.id != x.id:
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
            '''
            if i.position[0] < 0 or i.position[0] > 700:
                i.velocity[0] *= -1
            if i.position[1] < 0 or i.position[1] >700:
                i.velocity[1] *= -1
            '''
        # Moving all of the bodies after calculations
        for i in range(len(bodies)):
            # Moves the canvas object and the bodies coordinates
            c.move("body" + str(i.id) + "Circle",bodies[i].velocity[0]*deltaTime,bodies[i].velocity[1]*deltaTime)
            bodies[i].position = [bodies[i].position[0] + bodies[i].velocity[0]*deltaTime,
                                            bodies[i].position[1] + bodies[i].velocity[1]*deltaTime]
        c.update()
        #time.sleep(2)


mainloop()
