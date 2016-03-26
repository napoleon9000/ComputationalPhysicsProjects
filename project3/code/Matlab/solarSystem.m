classdef solarSystem
    %SOLARSYSTEM Summary of this class goes here
    %   Detailed explanation goes here
    
    properties        
        xSun = [0 0 0]';
        mEarth = 1.5E-6;
        h = 0.001;
        maxStep = 3;
        numOfPlanet
        listOfPlanet 
        m
        x
        v
        currentStep = 1;
        tracjectory
    end
    properties (Access = private)
        
    end
    methods
        function obj = solarSystem()
            obj.numOfPlanet = 0; 
            tracjectory = [];
        end
        function obj = godSettings(obj, h, maxStep)
            obj.h = h;
            obj.maxStep = maxStep;
        end
        function obj = addPlanet(obj, planet)
            obj.numOfPlanet = obj.numOfPlanet + 1;
            obj.listOfPlanet = char(obj.listOfPlanet,planet.name);   
            i = obj.numOfPlanet;
            obj.m(i) = planet.mass;
            obj.x(:,i) = planet.position';
            obj.v(:,i) = planet.velocity';
        end   
        function obj = verlet(obj)
            % Add the original position
            if(obj.currentStep == 1)
                obj.add2Trac(obj.x,1)
            end
            % For each planet,
            for i = 1:obj.numOfPlanet
                xi = obj.x(:,i);
                vi = obj.v(:,i);
                % Calculate a from Sun
                rS = xi - obj.xSun;
                ai = -4*3.1415^2./norm(rS.*rS.*rS).*rS;
                % Calculate a from other planet
                for j = 1:obj.numOfPlanet
                    % Excluding itself
                    if(j~=i)
                        rj = xi - obj.x(:,j);
                        aj = -4*3.1415^2*obj.m(j)/norm(rj.*rj.*rj).*rj;
                        ai = ai + aj;
                    end
                    
                end
                
                xi_1 = xi + obj.h*vi + obj.h^2/2*ai;                
                obj.x(:,i) = xi_1;
            end
            % Record the tracjectory
            obj.currentStep = obj.currentStep + 1;
            obj.add2Trac(obj.x,obj.currentStep)
            
            % Again, for each planet, calculate ai+1 from xi+1,
            for i = 1:obj.numOfPlanet
                xi = obj.x(:,i);
                % Calculate a from Sun
                rS = xi - obj.xSun;
                ai_1 = -4*3.1415^2./norm(rS.*rS.*rS).*rS;
                % Calculate a from other planet
                for j = 1:obj.numOfPlanet
                    % Excluding itself
                    if(j~=i)
                        rj = xi - obj.x(:,j);
                        aj = -4*3.1415^2*obj.m(j)/norm(rj.*rj.*rj).*rj;
                        ai_1 = ai_1 + aj;
                    end
                    
                end
                vi_1 = vi + obj.h/2*(ai_1+ai);
                obj.v(:,i) = vi_1;
            end
                       
        end
        function obj = add2Trac(obj,position,t)
            obj.tracjectory(:,:,t) = position;
        end
        function obj = show(obj)
            hold on
            for i = 1:obj.numOfPlanet
                plot3(obj.tracjectory(1,i,:),obj.tracjectory(2,i,:),obj.tracjectory(3,i,:));
            end
        end
    end
end

