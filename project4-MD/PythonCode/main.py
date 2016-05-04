import numpy as np
from MD_Class import *

# myCell = Atom(200, [157.8, 157.8, 157.8], 39.948, 1, 5.260, 1)
# myCell = Atom(10, [20, 20, 20], 39.948, 1, 5.260, 2)
myCell = Atom(1, [20, 20, 20], 39.948, 1, 5.405, 2)
# myCell.addAtom(2,[0.1, 1, 1],[0, 0, 0], 40,1)
# myCell.addAtom(3,[20-3.7, 1, 1],[0, 0, 0], 40,1)
# myCell.totNumberOfAtom = 3
myCell.assignTemperture(20)
# myCell.printStructure()
s = MDSystem()
s.addStructure(myCell)
s.setDump('trajTest.xyz', 10, 3)
s.setLog('Ar_logTest.txt', 10, 1)
# print myCell.cellLength
# print s.PBC_distance(np.array([19, 1, 1]), np.array([3.0, 1, 1]))
# print s.force(3.5)
s.nve(0.01, 1)
# myCell.printStructure()
# myCell.showStructures()
# print s.force(3.8)
# print cTemperature(s.temperature(), 2)
# print myCell.cellLength

#
# # myCell = Atom(10, [20, 20, 20], 39.948, 1, 5.260, 2)
# myCell2 = Atom(1, [20, 20, 20], 39.948, 1, 5.405, 2)
# # myCell.addAtom(2,[0.1, 1, 1],[0, 0, 0], 40,1)
# # myCell.addAtom(3,[20-3.7, 1, 1],[0, 0, 0], 40,1)
# # myCell.totNumberOfAtom = 3
# myCell2.assignTemperture(20)
# # myCell2.printStructure()
# s2 = MDSystem()
# s2.addStructure(myCell2)
# s2.setDump('traj2.xyz', 20, 3)
# s2.setLog('Ar_log2.txt', 20, 1)
# # print myCell.cellLength
# # print s.PBC_distance(np.array([19, 1, 1]), np.array([3.0, 1, 1]))
# # print s.force(3.5)
# s.nve(0.001, 2)
