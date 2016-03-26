clear
clear class
h = 0.001;
maxStep = 4;
Earth = planet('Earth',1.5e-6,[1,0,0],[0,6.28,0]);
Jupiter = planet('Jupiter',9.5e-4,[5.20 0 0],[0 2.04 0]);
S = solarSystem;
S = S.addPlanet(Earth);
S = S.addPlanet(Jupiter);
S = S.godSettings(h, maxStep);

%%
while(S.currentStep < maxStep)
    S.verlet;
end
S.show;