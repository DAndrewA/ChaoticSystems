# Chaotic Systems
This repository is where I will be coding solutions to chaotic systems - one's where slight variations in initial conditions can lead to wildly varying results.

# 3BodyProblem
Solving a three body problem using physics, python and - hopefully - javascript.

The python script is running in python 3.4 using TKinter. Each frame, for every body, it calculates the force on it between all of the other bodies, turns that into a vector and then changes the current vector by the new one. After all of the calculations are done, the bodies are moved - ready for the next frame.

This simulates the way in which 3 (or in this case, n) celestial bodies can be gravitationally bound to each other. Often, the orbits created aren't stable and as more bodies are taken into account stability in the system becomes less and less likely.
However, this doesn't simulate collisions, orbital decay and many of the values which are universal constants have been changed in order to make the program easier to use.

# Dual pendulum
Solving the chaotic system whereby two or more pendulums are connected in series and thus affect each others trajectories.
