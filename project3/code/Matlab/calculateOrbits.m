clear
clc
clear class

movieFlag = 0;
h = 1e-6;    % time step
movieInt = 10;   
maxStep = 1;  % years?
Sun = planet('Sun',1,[0,0,0],[0,0,0]);
Sun2 = planet('Sun2',1,[0,5,0],[5,0,0]);
Sun3 = planet('Sun3',1,[5,0,0],[0,5,0]);
Mercury = planet('Mercury',1.2e-7,[0.39,0,0],[0,9.96,0]);
Venus = planet('Venus',2.4e-6,[0.72,0,0],[0,7.36,0]);
Earth = planet('Earth',1.5e-6,[1,0,0],[0,6.28,0]);
Mars = planet('Mars',3.3e-7,[1.52,0,0],[0,5.06,0]);
Jupiter = planet('Jupiter',9.5e-4,[5.20 0 0],[0 3.04 0]);
Saturn = planet('Saturn',2.75e-4,[9.54,0,0],[0,2.04,0]);
Uranus = planet('Uranus',4.4e-5,[19.19,0,0],[0,1.43,0]);
Neptune = planet('Neptune',5.1e-5,[30.06,0,0],[0,1.14,0]);
Pluto = planet('Pluto',5.6e-9,[39.53,0,0],[0,0.99,0]);

Moon = planet('Moon',(7.347/1.989)*1e-8,[1.00256955529 0 0],[0 (1+1.022/30)*6.28 0]);


% Add planets
S = solarSystem;
S = S.godSettings(h, maxStep);
S = S.addPlanet(Sun);
% S = S.addPlanet(Mercury);
% S = S.addPlanet(Venus);
S = S.addPlanet(Earth);
% S = S.addPlanet(Mars);
% S = S.addPlanet(Jupiter);
% S = S.addPlanet(Saturn);
% S = S.addPlanet(Uranus);
% S = S.addPlanet(Neptune);
% S = S.addPlanet(Pluto);
S = S.addPlanet(Moon);
% S = S.addPlanet(Sun2);
% S = S.addPlanet(Sun3);


% S = S.verlet;
%% Run
step = 1;
while(S.currentStep*h <= maxStep)
    S = S.verlet;
    if(mod(step,movieInt) == 0&& movieFlag == 1)
        S.show;
        pause(0.01)
    end
    if(mod(step,1000) == 0)
        disp(S.currentStep*h/maxStep)
    end
    step = step + 1;
end
S.show;