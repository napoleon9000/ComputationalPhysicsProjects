import numpy as np
import random
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy.linalg as lg


class MDSystem:

    structure = []
    timestep = 1.0
    dynamic = 0
    simulationTime = 0
    currentTime = 1
    dumpFilename = []
    dumpInterval = 0
    dumpMode = 0

    def __init__(self):
        # Dynamic: 1: NVE
        self.atoms = []

    def nve(self, timestep, simulationTime):
        print 'nve'
        self.timestep = timestep
        self.simulationTime = simulationTime
        while self.currentTime < simulationTime:
            self.verlet()
            if (self.dumpMode != 0) & (np.mod(self.currentTime, self.dumpInterval) == 0):
                self.dump()
            self.currentTime += 1



    def force(self, distance):
        epsilon = 993.3   # 1.65 * 10^-21 J.
        sigma = 3.4
        f = 4*epsilon*((sigma/distance)**12-(sigma/distance)**6)
        return f

    def PBC_distance(self, x1, x2):
        # Read cellLength from self.cellLength
        cellLength = self.structure.cellLength
        distance = abs(x1 - x2)
        correctD = np.zeros((3))
        for i in [0, 1, 2]:
            correctD[i] = math.floor(2*distance[i]/cellLength[i])*cellLength[i]
        distance = distance - correctD
        return lg.norm(distance)

    def checkPBC(self):
        cellLength = self.structure.cellLength
        for i in xrange(0, self.structure.totNumberOfAtom, 1):
            currentPosition = self.structure.position[i, :]
            for j in [0, 1, 2]:
                self.structure.position[i, j] -= math.floor(currentPosition[j]/cellLength[j])*cellLength[j]

    def addStructure(self, newStructure):
        self.structure = newStructure

    def verlet(self):
        # Read positions and velocity
        # Apply verlet
        # Update position, velocity and time step
        # print 'verlet'
        h = self.timestep/1e9
        self.updataForce()
        # updata position from current velocity and force
        position_1 = self.structure.position
        for i in xrange(0, self.structure.totNumberOfAtom, 1):
            position_1[i, :] = self.structure.position[i, :] + h*self.structure.velocity[i, :] + h*h/2/self.structure.mass[i]*self.structure.force[i, :]
            # print h*h/2/self.structure.mass[i]*self.structure.force[i, :]
        self.checkPBC()

    def setDump(self, filename, interval, mode):
        # mode = 1: position 2: position + velocity 3: position + velocity + force
        self.dumpFilename = filename
        self.dumpInterval = interval
        self.dumpMode = mode

    def dump(self):
        # write output file
        f = open(self.dumpFilename, 'a')
        f.write(str(self.structure.totNumberOfAtom))
        f.write('\n')
        f.write('Atom. timestep:')
        f.write(str(self.currentTime))
        f.write('\n')
        if self.dumpMode == 1:
            for i in xrange(0, self.structure.totNumberOfAtom, 1):
                f.write(str(self.structure.element[i]))
                f.write(str(self.structure.position[i, :]))
                f.write('\n')

        print 'dump', self.currentTime

    def updataForce(self):
        # evaluate force from current position
        for i in xrange(0, self.structure.totNumberOfAtom, 1):
            for j in xrange(i+1, self.structure.totNumberOfAtom, 1):
                atomDistance = self.structure.position[i, :] - self.structure.position[j, :]
                atomDirection = atomDistance/lg.norm(atomDistance)
                atomForce = self.force(self.PBC_distance(self.structure.position[i, :], self.structure.position[j, :]))
                self.structure.force[i, :] = atomForce*atomDirection
                self.structure.force[j, :] = -self.structure.force[i, :]

class Atom:
    cellLength = []
    totNumberOfAtom = 0
    position = np.array([0, 0, 0])
    velocity = np.array([0, 0, 0])
    force = np.array([0, 0, 0])
    idx = np.array([0])
    mass = np.array([0])
    element = np.array([0])

    def addAtom(self, newIdx, newPosition, newVelocity,  newMass, newElement):
        #  print self.idx
        #  print newIdx
        self.idx = np.vstack([self.idx, newIdx])
        self.position = np.vstack([self.position, newPosition])
        self.mass = np.vstack([self.mass, newMass])
        self.velocity = np.vstack([self.velocity, newVelocity])
        self.force = np.vstack([self.force, [0, 0, 0]])
        self.element = np.vstack([self.element, newElement])
        # print self.position
        # self.idx.append(newIdx)
        # self.position.append(newPosition)
        # self.mass.append(newMass)
        # self.velocity.append(newVelocity)

    def createFCC(self, numberOfAtom, mass):
        self.totNumberOfAtom = numberOfAtom

    def createRand(self, numberOfAtom, element, mass):

        for i in xrange(0, numberOfAtom, 1):
            # print i
            # print [random.uniform(0, self.cellLength[1]), random.uniform(0, self.cellLength[2]), random.uniform(0, self.cellLength[3])]
            # print mass
            self.totNumberOfAtom += 1
            Atom.addAtom(self, i+1, [random.uniform(0, self.cellLength[0]), random.uniform(0, self.cellLength[1]), random.uniform(0, self.cellLength[2])], [0.0, 0.0, 0.0], mass, element)

    def __init__(self, numberOfAtom, cellLength, mass, element, mode):
        # unit: cell length: A, mass: g/mol
        N = numberOfAtom
        self.cellLength = cellLength
        if mode == 2:
            Atom.createFCC(self, numberOfAtom, element, mass)
        if mode == 1:
            Atom.createRand(self, numberOfAtom, element, mass)
            self.idx = np.delete(self.idx,0)
            self.mass = np.delete(self.mass,0)
            self.position = np.delete(self.position,0, axis=0)
            self.velocity = np.delete(self.velocity,0, axis=0)
            self.force = np.delete(self.force,0, axis=0)
            self.element = np.delete(self.element, 0, axis=0)
        # print N

    def printStructure(self):
        print 'id mass x y z vx vy vz fx fy fz'
        for i in xrange(0,self.totNumberOfAtom, 1):
            print self.idx[i], self.mass[i], self.position[i], self.velocity[i], self.force[i]
    def showStructures(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for i in xrange(0, self.totNumberOfAtom, 1):
            ax.scatter(self.position[i, 0], self.position[i, 1], self.position[i, 2])
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        plt.show()


    def assignTemperture(self, t):
        # print 'Assign temperature'
        kE = 3.0/2*1.38E-23*t*self.totNumberOfAtom
        kEcurrent = 0
        for i in xrange(0, self.totNumberOfAtom,1):
            nv = 0
            self.velocity[i, :] = [random.random()-0.5, random.random()-0.5, random.random()-0.5]
            # print self.velocity
            # print self.mass[i]
            # print nv
            kEcurrent += 0.5 * self.mass[i] * lg.norm(self.velocity[i,:])
        kEcurrent /= self.totNumberOfAtom * 6.023E23
        # print 'kEcurrent = ', kEcurrent
        # print 'kE = ', kE
        # print 'ratio = ', math.sqrt(kE / kEcurrent)
        self.velocity *= math.sqrt(kE / kEcurrent)


