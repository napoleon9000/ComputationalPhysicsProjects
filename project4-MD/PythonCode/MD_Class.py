import numpy as np





class System:

    timestep = 1
    cellLength = []

    def __init__(self):
        self.atoms = []

    def force(self, distance):
        print "force"

    def PBC_distance(self, x1, x2):
        # Read cellLength from self.cellLength
        print "PBC"

    def creatCell(self, H):
        self.cellLength = H
        print "H = ", H

    def addAtom(self, current_atoms):
        self.atoms.append(current_atoms)

    def verlet(self):
        # Read positions and velocity
        # Apply verlet
        # Update position, velocity and time step

    def dump(self, mode):
        # write output file
        # mode = 1: position 2: position + velocity 3: position + velocity + force



class Atom:

    def addAtom(self, idx, position, velocity,  mass):
        self.idx.append = idx
        self.position.append = position
        self.mass = mass
        self.velocity = velocity

    def createFCC(self, numberOfAtom, cellLength):
        print cellLength
    def createRand(self, numberOfAtom, cellLength):
        print cellLength
    def __init__(self, numberOfAtom, cellLength, mode):
        # remove momentum at the same time
        N = numberOfAtom
        if(mode == 1):
            Atom.createFCC(self, numberOfAtom, cellLength)
        if(mode == 2):
            Atom.createRand(self, numberOfAtom, cellLength)

        print N


