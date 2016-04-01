classdef solarSystem
    %SOLARSYSTEM Summary of this class goes here
    %   Detailed explanation goes here
    
    properties        
        mEarth = 1.5E-6;
        h = 0.001;
        maxStep = 3;
        numOfPlanet
        listOfPlanet 
        m
        x   % x(3,planetyIdx,timeStep)
        v
        currentStep = 1;
        dispFlag = 0;
    end
    properties (Access = private)
        
    end
    methods
        function obj = solarSystem()
            obj.numOfPlanet = 0; 
        end
        function obj = godSettings(obj, h, maxStep)
            obj.h = h;
            obj.maxStep = maxStep;
        end
        function obj = addPlanet(obj, planet)
            obj.numOfPlanet = obj.numOfPlanet + 1;
            obj.listOfPlanet = char(obj.listOfPlanet,planet.name);   
            i = obj.numOfPlanet;
            simulationSteps = round(obj.maxStep/obj.h);
            obj.m(i) = planet.mass;
            obj.x(:,i,1) = planet.position';
            obj.x(:,i,simulationSteps) = [0 0 0]';
            obj.v(:,i,1) = planet.velocity';
            obj.v(:,i,simulationSteps) = [0 0 0]';
            
        end   
        function obj = verlet(obj)
            % For each planet,
            
            ai = zeros(3,obj.numOfPlanet);
            ai_1 = ai;
            step = obj.currentStep;
            if(mod(obj.maxStep,step) == 1000)
                disp(step)
            end
            for i = 1:obj.numOfPlanet
                xi = obj.x(:,i,step);
                vi = obj.v(:,i,step);
                if(obj.dispFlag == 1)
                    disp(['step:' num2str(obj.currentStep)])
                    disp(['i = ' num2str(i)])
                end
                % Calculate a
                ai(:,i) = 0;
                % Calculate a from all planet
                for j = 1:obj.numOfPlanet
                    % Excluding itself
                    if(j~=i)
                        rj = xi - obj.x(:,j,step);
                        aj = -4*pi^2*obj.m(j)/(norm(rj).^2).*rj/norm(rj);
                        ai(:,i) = ai(:,i) + aj;
                        if(obj.dispFlag == 1)
                            disp(['xi = ' num2str(xi')])
                            disp(['xj = ' num2str(obj.x(:,j)')])
                            disp(['rj = ' num2str(rj')])
                        end
                    end
                    
                end
                
                xi_1 = xi + obj.h*vi + obj.h^2/2*ai(:,i);
                if(obj.dispFlag == 1)
                    disp(['xi = ' num2str(xi')])
                    disp(['vi = ' num2str(vi')])
                    disp(['ai = ' num2str(ai(:,i)')])
                    disp(['xi_1 = ' num2str(xi_1')])
                end
%                 disp(obj)
                obj.x(:,i,step+1) = xi_1;
            end
            % Record the tracjectory           
%             obj = obj.add2Trac(obj.x,obj.currentStep);
            
            % Again, for each planet, calculate ai+1 from xi+1,
            for i = 1:obj.numOfPlanet
                xi = obj.x(:,i,step+1);
                if(obj.dispFlag == 1)
                    disp(['step:' num2str(obj.currentStep)])
                    disp(['i = ' num2str(i)])
                end
                % Calculate a
                ai_1(:,i) = 0;
                % Calculate a from all planet
                for j = 1:obj.numOfPlanet
                    % Excluding itself
                    if(j~=i)
                        rj = xi - obj.x(:,j,step);
                        aj = -4*pi^2*obj.m(j)/(norm(rj).^2).*rj/norm(rj);
                        ai_1(:,i) = ai_1(:,i) + aj;
                    end
                    
                end
                vi_1 = obj.v(:,i,step) + obj.h/2*(ai_1(:,i)+ai(:,i));
                obj.v(:,i,step+1) = vi_1;
                if(obj.dispFlag == 1)
                    disp(['ai_1 = ' num2str(ai_1(:,i)')])
                end
            end
            obj.currentStep = obj.currentStep + 1;
                       
        end
%         function obj = add2Trac(obj,position,velocity,planetyIdx,t)
%             obj.x(:,planetyIdx,t) = position;
%             obj.v(:,planetyIdx,t) = velocity;
%         end
        function obj = show(obj)
            
            clf
            legendText = [];
            hold on
            axis equal
            grid on
            plotH = zeros(1,obj.numOfPlanet);
            plotColor = zeros(obj.numOfPlanet,3);
            tracSize = obj.currentStep;
            for i = 1:obj.numOfPlanet
%                 disp(i)
                
                positionX = reshape(obj.x(1,i,1:tracSize),1,tracSize);
                positionY = reshape(obj.x(2,i,1:tracSize),1,tracSize);
                positionZ = reshape(obj.x(3,i,1:tracSize),1,tracSize);
                plotH(i) = plot3(positionX, positionY, positionZ);
                plotColor(i,:) = get(plotH(i),'Color');
                legendText = char(legendText,obj.listOfPlanet(i+1,:));
            end
            legendText(1,:) = [];
            legend(legendText);
            for i = 1:obj.numOfPlanet
%                 scatter3(obj.x(1,i,obj.currentStep),obj.x(2,i,obj.currentStep),obj.x(3,i,obj.currentStep),40,plotH(i).Color);
%                 plotH
%                 plotH(i).Color
                plotH1 = scatter3(obj.x(1,i,obj.currentStep),obj.x(2,i,obj.currentStep),obj.x(3,i,obj.currentStep),40);
                set(plotH1,'CData',plotColor(i,:));
            end
            
            title(['Simulation of solar system. Current time: ' num2str(obj.h*tracSize)]);
        end
        function obj = plotE(obj)
            figure
            hold on
            box on
            grid on
            for i = 1:obj.numOfPlanet
                KE = 0.5*obj.m(i)*norm(obj.v)^2;
                plot(KE);
            end
        end
        function obj = plotDist(obj)
            
        end
    end
end

