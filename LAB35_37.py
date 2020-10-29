#Lab 35
import numpy as np
import matplotlib.pyplot as plotter
class chargedParticle():
    elementaryCharge=1.60e-19
    epsilon_0=8.85e-12
    def __init__(self,location,charge):
        self.location=location
        self.charge=charge
    def chargeNumberCalculator(self):
        chargeNumber=self.charge/self.elementaryCharge
        return chargeNumber
    
    def distanceCalculator(self,locationOfInterest):
        distanceVector=locationOfInterest-self.location
        distance=np.linalg.norm(distanceVector)
        directionVector=distanceVector/distance
        return directionVector, distance
    def electricFieldCalculator(self,locationOfInterest):
        prefactors=1/4/np.pi/self.epsilon_0
        directionVector, distance = self.distanceCalculator(locationOfInterest)
        electricField=prefactors*self.charge/(distance**2)*directionVector
        return electricField
    def electricPotentialforPlotting(self,plottingX,plottingY):
        prefactors=1/4/np.pi/self.epsilon_0
        distance=np.sqrt((plottingX-self.location[0]**2+(plottingY-self.location[1])**2))
        electricPotential=prefactors*self.charge/distance
        return electricPotential
    def electricFieldforPlotting(self,plottingX,plottingY):
        prefactors=1/4/np.pi/self.epsilon_0*self.charge
        distancesquared=(plottingX-self.location[0])**2+(plottingY-self.location[1])**2
        eX,eY = prefactors*self.charge*(plottingX-self.location[0])/distancesquared,prefactors*self.charge*(plottingY-self.location[1])/distancesquared
        return eX,eY
origin=np.array([0,0,0])
electron=chargedParticle(origin,-1.60e-19)
print(electron.charge)
print(electron.location)
origin1=np.array([0,0,1])
proton=chargedParticle(origin1,1.60e-19)
print(proton.charge)
print(proton.location)
print(electron.chargeNumberCalculator())
print(proton.chargeNumberCalculator())
LocOfInterest=np.array([2,0,0])
electronFi=electron.electricFieldCalculator(LocOfInterest)
protonFi=proton.electricFieldCalculator(LocOfInterest)
print('Enet',electronFi + protonFi)
#Charge Distrib 1
Q1=chargedParticle(origin,1*(10**-9))
Q2=chargedParticle(np.array([.10,0,0]),1*(10**-9))
print('Table',Q1.electricFieldCalculator(np.array([-.05,0,0])))
print(Q2.electricFieldCalculator(np.array([-.05,0,0])))
print(Q1.electricFieldCalculator(np.array([-.05,0,0]))+Q2.electricFieldCalculator(np.array([-.05,0,0])))
#Char Distrib 2
Q1_=chargedParticle(np.array([.05,0,0]),1*(10**-9))
Q2_=chargedParticle(np.array([.15,0,0]),1*(10**-9))
Q3_=chargedParticle(np.array([.10,0,0]),1*(10**-9))
print(Q1_.electricFieldCalculator(origin))
print(Q2_.electricFieldCalculator(origin))
print(Q3_.electricFieldCalculator(origin))
print(Q1_.electricFieldCalculator(origin)+Q2_.electricFieldCalculator(origin)+Q3_.electricFieldCalculator(origin))
#Char Distrib 3
Q1_=chargedParticle(np.array([-.05,-.05,0]),1*(10**-9))
Q2_=chargedParticle(np.array([.05,-.05,0]),1*(10**-9))
print(Q1_.electricFieldCalculator(origin))
print(Q2_.electricFieldCalculator(origin))
print(Q1_.electricFieldCalculator(origin)+Q2_.electricFieldCalculator(origin))
#Char Distrib 4
Q1_=chargedParticle(np.array([-.05,-.05,0]),1*(10**-9))
Q2_=chargedParticle(np.array([.05,-.05,0]),1*(10**-9))
Q3_=chargedParticle(np.array([0,-.05,0]),1*(10**-9))
print(Q1_.electricFieldCalculator(origin))
print(Q2_.electricFieldCalculator(origin))
print(Q3_.electricFieldCalculator(origin))
print(Q1_.electricFieldCalculator(origin)+Q2_.electricFieldCalculator(origin)+Q3_.electricFieldCalculator(origin))
#Day 2 (Lab 36)
d=-5e-2
L=10e-2
Q=10e-9
numberOfPieces=10
LocationOfPieces=np.linspace(0,L,numberOfPieces)
electricFieldAtP=[0,0,0]
dQ=Q/numberOfPieces
for x in LocationOfPieces:
    littleChargedParticle=chargedParticle(np.array([x,0,0]),dQ)
    electricFieldAtP+=littleChargedParticle.electricFieldCalculator(np.array([d,0,0]))
print(electricFieldAtP)
#36.1
d1=5e-2
L1=10e-2
Q1=5e-9
numberOfPieces1=10
LocationOfPieces1=np.linspace(0,L,numberOfPieces1)
electricFieldAtP1=[0,0,0]
dQ1=Q1/numberOfPieces1
for x in LocationOfPieces1:
    littleChargedParticle1=chargedParticle(np.array([x,0,0]),dQ1)
    electricFieldAtP1+=littleChargedParticle1.electricFieldCalculator(np.array([d1,0,0]))
print(electricFieldAtP1)
electricFieldAtP11=[0,0,0]
#36.2
R=10e-2
NumberofPieces=10
xLocationsOnRings=R*np.cos(np.linspace(np.pi/2,-np.pi/2,NumberofPieces))
ylocationsOnRings=R*np.sin(np.linspace(np.pi/2,-np.pi/2,NumberofPieces))
dQ2=(5e-9)/NumberofPieces
for x,y in zip(xLocationsOnRings,ylocationsOnRings):
 # ex 36.3
  littleChargedSphere=chargedParticle(np.array([x,y,0]),dQ2)
  electricFieldAtP11+=littleChargedSphere.electricFieldCalculator(np.array([R,0,0]))
print(electricFieldAtP11)
print("%error",(np.sqrt((2.167e4)**2+(5.414e-1)**2)-np.sqrt((4.690e3)**2+(1.506e-12)**2))/np.sqrt((2.167e4)**2+(5.414e-1)**2)*100)
#Day3 (Lab 37)
from matplotlib.patches import Circle

nx=100
ny=100
x=np.linspace(-1,1,nx)
y=np.linspace(-1,1,ny)
X,Y=np.meshgrid(x,y)
R=10e-2
numberOfPieces=100
Q=5e-9
xLocationsOnRing=R*np.cos(np.linspace(np.pi/2,-np.pi/2,numberOfPieces))
yLocationsOnRing=R*np.sin(np.linspace(np.pi/2,-np.pi/2,numberOfPieces))
dq=Q/numberOfPieces

Ex,Ey=np.zeros((ny,nx)),np.zeros((ny,nx))
potential=np.zeros((ny,nx))
fig=plotter.figure()
plot1=fig.add_subplot(121)
plot2=fig.add_subplot(122)
charge_colors={True:'#aa0000', False: '#0000aa'}
for x,y in zip(xLocationsOnRing,yLocationsOnRing):
    littleChargedParticle=chargedParticle(np.array([x,y]),dq)
    ex,ey=littleChargedParticle.electricFieldforPlotting(X,Y)
    Ex+=ex
    Ey+=ey
    potential+=littleChargedParticle.electricPotentialforPlotting(X,Y)
    plot1.add_artist(Circle(littleChargedParticle.location,0.01,color=charge_colors[littleChargedParticle.charge>0]))
    plot2.add_artist(Circle(littleChargedParticle.location,0.01,color=charge_colors[littleChargedParticle.charge>0]))
color=np.log(np.sqrt(Ex**2+Ey**2))
plot1.streamplot(X,Y,Ex,Ey,color=color,linewidth=1,cmap=plotter.cm.inferno,density=3,arrowstyle='->',arrowsize=1)
plot2.contour(X,Y,potential,1000,levels=np.linspace(np.min(potential),np.max(potential)*0.1,1000),cmap=plotter.cm.inferno,linewidth=1,density=3)
plot1.set_title('Electric Field')
plot1.set_xlabel('$x$')
plot1.set_ylabel('$y$')
plot1.set_xlim(-1,1)
plot1.set_ylim(-1,1)
plot1.set_aspect('equal')
plot2.set_title('Potential')
plot2.set_xlabel('$x$')
plot2.set_ylabel('$y%')
plot2.set_xlim(-1,1)
plot2.set_ylim(-1,1)
plot2.set_aspect('equal')
plotter.show()


#Since we are going from pi/2 - -pi/2 the ring would go downward
#From a far distance the potential will appear as a point particle