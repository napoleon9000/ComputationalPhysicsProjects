import numpy as np

# Energy

def cEnergy(quant, mode):
    # mode == 1: AU
    # mode == 2: SI
    # J -> AU
    ratio = 1.651e-21
    if mode == 1:
        quant1 = quant/ratio
    if mode == 2:
        quant1 = quant*ratio
    return quant1


def cMass(quant, mode):
    # mode == 1: AU
    # mode == 2: SI
    # au -> AU
    ratio = 1
    if mode == 1:
        quant1 = quant/ratio
    if mode == 2:
        quant1 = quant*ratio
    return quant1


def cLength(quant, mode):
    # mode == 1: AU
    # mode == 2: SI
    # A -> AU
    ratio = 1
    if mode == 1:
        quant1 = quant/ratio
    if mode == 2:
        quant1 = quant*ratio
    return quant1


def cTemperature(quant, mode):
    # mode == 1: AU
    # mode == 2: SI
    # K -> AU
    ratio = 119.735
    if mode == 1:
        quant1 = quant/ratio
    if mode == 2:
        quant1 = quant*ratio
    return quant1


def cTime(quant, mode):
    # mode == 1: AU
    # mode == 2: SI
    # ps -> AU
    ratio = 1.00224e-1
    if mode == 1:
        quant1 = quant/ratio
    if mode == 2:
        quant1 = quant*ratio
    return quant1


def cForce(quant, mode):
    # mode == 1: AU
    # mode == 2: SI
    # eV/A -> AU
    ratio = 1.032e-2
    if mode == 1:
        quant1 = quant/ratio
    if mode == 2:
        quant1 = quant*ratio
    return quant1


def cPressure(quant, mode):
    # mode == 1: AU
    # mode == 2: SI
    # Pa -> AU
    ratio = 0.16536
    if mode == 1:
        quant1 = quant/ratio
    if mode == 2:
        quant1 = quant*ratio
    return quant1


def cVelocity(quant, mode):
    # mode == 1: AU
    # mode == 2: SI
    # m/s -> AU
    ratio = 997.765
    if mode == 1:
        quant1 = quant/ratio
    if mode == 2:
        quant1 = quant*ratio
    return quant1

def cDiffCoeff(quant, mode):
    # mode == 1: AU
    # mode == 2: SI
    # m/s^2 -> AU
    ratio = 9.955e15
    if mode == 1:
        quant1 = quant/ratio
    if mode == 2:
        quant1 = quant*ratio
    return quant1


