import numpy as np
from numpy import linalg as LA
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager


# Set the font dictionaries (for plot title and axis titles)
title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'normal',
              'verticalalignment':'bottom'} # Bottom vertical alignment for more space
axis_font = {'fontname':'Arial', 'size':'16'}

# Set the font properties (for use in legend)
font_path = 'C:\Windows\Fonts\Arial.ttf'
font_prop = font_manager.FontProperties(fname=font_path, size=14)

class solarsystem:

    count = 0

    def __init__(self):
        self.planets = []

    def add(self, a_planet):
        self.planets.append(a_planet)
        solarsystem.count += 1

    def showPlanet(self):
        for a_planet in self.planets:
            print a_planet.name

    def compilePlanet(self):
        y_i = np.zeros([solarsystem.count,7])
        ii = 0
        for a_planet in self.planets:
            y_i[ii,6] = a_planet.mass
            y_i[ii,5] = a_planet.vz
            y_i[ii,4] = a_planet.vy
            y_i[ii,3] = a_planet.vx
            y_i[ii,2] = a_planet.z
            y_i[ii,1] = a_planet.y
            y_i[ii,0] = a_planet.x
            ii += 1
        return y_i

    def force(self, x, y, z, Mothers):
        G = 4*np.pi**2
        distance = x**2 + y**2 + z**2
        F = G*Mothers/distance**1.5
        return F

    def forceperi(self, vec,i):
        G = 4*np.pi**2
        r = (vec[i,0]**2 + vec[i,1]**2 + vec[i,2]**2)**0.5
        c = 63241.5418464 #AU/yr
        L = LA.norm(np.cross([vec[i,0],vec[i,1],vec[i,2]],[vec[i,3],vec[i,4],vec[i,5]]))
        F = G*vec[i,6]/r**2*(1+(3*L**2/(r**2*c**2)))
        return F


    def kinetic(self, vec, i):
        KE = 0.5*vec[i,6]*(vec[i,3]**2+vec[i,4]**2+vec[i,5]**2)
        return KE

    def potential(self, vec, i):
        G = 4*np.pi**2
        PE = -2*G*vec[i,6]/(vec[i,0]**2+vec[i,1]**2+vec[i,2]**2)**0.5
        return PE

    def angMomentum(self, vec, i):
        L = LA.norm(np.cross([vec[i,0],vec[i,1],vec[i,2]],[vec[i,3],vec[i,4],vec[i,5]]))
        return L


    def positionPlot3D(self, position):
        plt.figure()
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        for i in range(solarsystem.count):
            ax.plot(position[i,0], position[i,1],position[i,2])
        plt.show()

    def positionPlot(self, position):
        plt.figure()
        for i in range(solarsystem.count):
            plt.plot(position[i,0], position[i,1])
        plt.xlabel("X", **axis_font)
        plt.ylabel("Y", **axis_font)
        plt.title("Trajectory", **title_font)
        plt.tick_params(axis = 'x', labelsize = 15)
        plt.tick_params(axis = 'y', labelsize = 15)
        plt.show()

    def distance(self, vec, i):
        d = (vec[i,0]**2 + vec[i,1]**2 + vec[i,2]**2)**0.5
        return d


    def KEPlot(selfself, KE, h, tmax):
        plt.figure()
        m = range(int(tmax/h)+1)
        for i in range(solarsystem.count):
            if i != 0:
                plt.plot(m, KE[i]+KE[0])
        plt.xlabel("Time steps", **axis_font)
        plt.ylabel("Kinetic Energy", **axis_font)
        plt.title("Kinetic Energy", **title_font)
        plt.tick_params(axis = 'x', labelsize = 15)
        plt.tick_params(axis = 'y', labelsize = 15)
        plt.show()

    def PEPlot(self, PE, h, tmax):
        plt.figure()
        m = range(int(tmax/h)+1)
        for i in range(solarsystem.count):
            if i != 0:
                plt.plot(m, PE[i]+PE[0])
        plt.xlabel("Time steps", **axis_font)
        plt.ylabel("Potential Energy", **axis_font)
        plt.title("Potential Energy", **title_font)
        plt.tick_params(axis = 'x', labelsize = 15)
        plt.tick_params(axis = 'y', labelsize = 15)
        plt.show()


    def distancePlot(self, distance, h, tmax):
        plt.figure()
        m = range(int(tmax/h)+1)
        for i in range(solarsystem.count):
            if i != 0:
                plt.plot(m, distance[i])
        plt.xlabel("Time steps", **axis_font)
        plt.ylabel("Distance from origin (A.U.)", **axis_font)
        plt.title("Distance from origin", **title_font)
        plt.tick_params(axis = 'x', labelsize = 15)
        plt.tick_params(axis = 'y', labelsize = 15)
        plt.show()

    def LPlot(self, L, h, tmax):
        plt.figure()
        m = range(int(tmax/h)+1)
        for i in range(solarsystem.count):
            plt.plot(m, L[i])
        plt.xlabel("Time steps", **axis_font)
        plt.ylabel("Angular Momentum", **axis_font)
        plt.title("Angular Momentum", **title_font)
        plt.tick_params(axis = 'x', labelsize = 15)
        plt.tick_params(axis = 'y', labelsize = 15)
        plt.show()

def derivative(dat, de, n):
    for i in range(n):
        acc_x  = 0.0
        acc_y = 0.0
        acc_z = 0.0
        for j in range(n):
            if i != j:
            #if i!= 0:
                mod_force = SS.force(dat[j,0]-dat[i,0], dat[j,1]-dat[i,1], dat[j,2]-dat[i,2], dat[j,6])
                #mod_force = SS.forceperi(dat,1)
                acc_x += mod_force*(dat[j,0]-dat[i,0])
                acc_y += mod_force*(dat[j,1]-dat[i,1])
                acc_z += mod_force*(dat[j,2]-dat[i,2])
        de[i,3] = acc_x
        de[i,4] = acc_y
        de[i,5] = acc_z
    for i in range(n):
        de[i,0] = dat[i,3]
        de[i,1] = dat[i,4]
        de[i,2] = dat[i,5]


def sum_matrix(results, coeff_one, first, coeff_two, second, n):
    for i in range(n):
        for j in range(6):
            results[i,j] = coeff_one*first[i,j] + coeff_two*second[i,j]
        results[i,6] = first[i,6]


def solverRK4(h, tmax):
    y_temp = np.zeros([solarsystem.count, 7])
    position = np.zeros((solarsystem.count,7,int(tmax/h)+1))
    KE = np.zeros((solarsystem.count, int(tmax/h)+1))
    PE = np.zeros((solarsystem.count, int(tmax/h)+1))
    L = np.zeros((solarsystem.count, int(tmax/h)+1))
    distance = np.zeros((solarsystem.count, int(tmax/h)+1))
    k1 = np.zeros([solarsystem.count, 7])
    k2 = np.zeros([solarsystem.count, 7])
    k3 = np.zeros([solarsystem.count, 7])
    k4 = np.zeros([solarsystem.count, 7])
    y_i = SS.compilePlanet()
    t = 0.0
    n=0

    while t < tmax:
        derivative(y_i, k1, solarsystem.count)
        sum_matrix(y_temp, 1, y_i, 0.5*h, k1, solarsystem.count)
        derivative(y_temp, k2, solarsystem.count)
        sum_matrix(y_temp, 1, y_i, 0.5*h, k2, solarsystem.count)
        derivative(y_temp, k3, solarsystem.count)
        sum_matrix(y_temp, 1, y_i, h, k3, solarsystem.count)
        derivative(y_temp, k4, solarsystem.count)

        for i in range(solarsystem.count):
                for j in range(6):
                    y_i[i,j] = y_i[i,j] + h*(k1[i,j] + 2*k2[i,j] + 2*k3[i,j] + k4[i,j])/6
                    position[i,j,n] = y_i[i,j]
                    distance[i,n] = SS.distance(y_i,i)
                    KE[i,n] = SS.kinetic(y_i,i)
                    PE[i,n] = SS.potential(y_i,i)
                    PE[0,n] = SS.potential(y_i,i)/y_i[i,6]*y_i[0,6]
                    L[i,n] = SS.angMomentum(y_i,i)
        t += h
        n += 1

# fixing minor bugs
    position[:,:,int(tmax/h)] = position[:,:,int(tmax/h)-1]
    KE[:,int(tmax/h)] = KE[:,int(tmax/h)-1]
    PE[:,int(tmax/h)] = PE[:,int(tmax/h)-1]
    distance[:,int(tmax/h)] = distance[:,int(tmax/h)-1]
    L[:,int(tmax/h)] = L[:,int(tmax/h)-1]

    return [position, KE, PE, distance, L]






class planet:

    def __init__(self, name, mass, x, y, z, vx, vy, vz):
        self.name = name
        self.mass = mass
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

Sun = planet('Sun', 1.0,  3.771026244390675E-03,  2.043097224215272E-03, -1.627192490003819E-04
                    , -3.77E-05, 2.55E-03, -2.71E-06)
Mercury = planet('Mercury', 1.66051E-07, 1.863515519979501E-01,  2.548065003154470E-01,  3.740439308464503E-03
                    , -2.840110528355240E-02*365.25, 1.762706954908617E-02*365.25, 4.045318985205311E-03*365.25)
Venus = planet('Venus', 2.44827E-06,  6.402610421995966E-01, -3.487130058678541E-01, -4.170129005991170E-02
                    , 9.643270647275807E-03*365.25, 1.763763269124911E-02*365.25, -3.147583648494046E-04*365.25)
Earth = planet('Earth', 3.0033E-06,  -9.722793854254226E-01, -2.136194298311388E-01, -1.524486237461527E-04
                    , 1.25E+00,	-6.16E+00, 3.77E-04)
Mars = planet('Mars', 3.22774E-07, -1.273888286335226E+00, -9.345650995929446E-01,  1.156708511527438E-02
                    , 8.796919824227780E-03*365.25, -1.008219489094120E-02*365.25, -4.273358411290152E-04*365.25)
Jupiter = planet('Jupiter', 0.000954533, -5.343374723296717E+00,  9.499090356431010E-01,  1.155500089211299E-01
                    , -1.408034735202547E-03*365.25, -7.074583503958680E-03*365.25,  6.088651310975759E-05*365.25)
Saturn = planet('Saturn', 0.000285797,  -3.257658796800622E+00, -9.469829247085269E+00, 2.943053689076774E-01
                    , 4.969350447804316E-03*365.25, -1.831261754069796E-03*365.25, -1.661687950774069E-04*365.25)
Uranus = planet('Uranus', 4.36552E-05,  1.874773642797683E+01,  6.878729814152105E+00, -2.173332521506558E-01
                    ,-1.383418038561912E-03*365.25, 3.509051475538068E-03*365.25, 3.101068527811424E-05*365.25)
Neptune = planet('Neptune',5.15E-05, 2.805523791636490E+01, -1.050433698717797E+01, -4.302448968580886E-01,
                     1.079523475180545E-03*365.25,  2.958063165703507E-03*365.25, -8.594624381715380E-05*365.25)
Pluto = planet('Pluto', 6.57265E-09, 8.819727426071946E+00, -3.186049668958540E+01, 8.580737574573666E-01,
                    3.083142612945824E-03*365.25, 1.793117968432260E-04*365.25, -9.202762004669122E-04*365.25)
Europa = planet('Europa', 2.41232E-08,-5.338855447506378E+00,  9.500633366380398E-01,  1.156289216566137E-01
                    , -1.711494459181975E-03*365.25,  7.843001860038034E-04*365.25,  4.022198889849470E-04*365.25)
Triton = planet('Triton', 1.07968E-08, 2.805371779129888E+01, -1.050375893119152E+01, -4.285190271950739E-01,
                2.562399432164993E-03*365.25,  4.908194332505412E-03*365.25,  5.669721037418506E-04*365.25)

SS = solarsystem()

SS.add(Sun)              #0
#SS.add(Earth)            #1
#SS.add(Mercury)         #2
#SS.add(Venus)           #3
#SS.add(Mars)            #4
#SS.add(Jupiter)         #5
#SS.add(Saturn)          #6
#SS.add(Uranus)          #7
SS.add(Neptune)         #8
#SS.add(Pluto)           #9
#SS.add(Europa)          #10
SS.add(Triton)


[h,tmax] = [0.01,100000]

[position, KE, PE, distance, L] = solverRK4(h, tmax)
#SS.positionPlot(position)
#SS.positionPlot3D(position)
#SS.KEPlot(KE, h, tmax)
#SS.PEPlot(PE, h, tmax)
#SS.distancePlot(distance, h, tmax)
#SS.LPlot(L,h, tmax)

plt.plot(range(int(tmax/h)+1),position[2,1])
plt.show()