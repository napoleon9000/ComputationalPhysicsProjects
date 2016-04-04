classdef solarSystem
    %SOLARSYSTEM create the class for solar system
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
        fixSun = 0;
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
                if(obj.fixSun == 1)
                    obj.x(:,1,step+1) = 0;
                end
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
        
        function obj = plotE(obj,mode)
            %% plot the Energy
            % mode: 1:KE 2:PE 3:sum of KE 4:sum of PE 5:total E
            KE = zeros(obj.numOfPlanet,round(obj.maxStep/obj.h)+1);
            PE = KE;
            for i = 1:obj.numOfPlanet
                KE(i,:) = 0.5*obj.m(i)*sum(squeeze(obj.v(:,i,:)).*squeeze(obj.v(:,i,:)));
                for j = 1:obj.numOfPlanet
                   if(i~=j)
                       rVector = squeeze(obj.x(:,i,:))-squeeze(obj.x(:,j,:));
                       r = sqrt(sum(rVector.*rVector));
%                        figure
%                        plot(r)
                       PE(i,:) = PE(i,:)-2*pi.^2*obj.m(i)*obj.m(j)./r;
                   end
                end
            end
            for i = 1:length(mode)
                figure
                hold on
                box on
                grid on
                if(mode(i) == 1)                
                    legendText = [];
                    for j = 1:obj.numOfPlanet
                        plot(KE(j,:));
                        legendText = char(legendText,obj.listOfPlanet(j+1,:));
                    end
                    legendText(1,:) = [];
                    title('The kinectic Energy vs time');
                    legend(legendText);
                end
                if(mode(i) == 2)                    
                    plot(sum(KE));
                    title('The total kinectic Energy vs time');
                end
                if(mode(i) == 3)          
                    legendText = [];
                    for j = 1:obj.numOfPlanet
                        plot(PE(j,:));
                        legendText = char(legendText,obj.listOfPlanet(j+1,:));
                    end
                    legendText(1,:) = [];
                    title('The potential Energy vs time');
                    legend(legendText);
                end
                if(mode(i) == 4)                    
                    plot(sum(PE));
                    title('The total potential Energy vs time');
                end
                if(mode(i) == 5)                    
                    plot(sum(PE)+sum(KE));
                    title('The total Energy vs time');
                end
            end
        end
    end
end

