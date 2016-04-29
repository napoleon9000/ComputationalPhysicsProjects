import numpy as np
from MD_Class import *

myCell = Atom(10, [5, 5, 5], 40, 1, 1)
# myCell.printStructure()
myCell.assignTemperture(300)
myCell.printStructure()
s = MDSystem()
s.addStructure(myCell)
s.setDump('traj.xyz', 1000, 1)
s.nve(1000, 100000)
myCell.printStructure()