classdef planet
    %PLANET stores data of different planets
    %   
    
    properties 
        position
        velocity
        mass
        name
    end
    
    methods
        function obj = planet(pName, pMass, pPosition, pVelocity)
            obj.name = pName;
            obj.position = pPosition;
            obj.velocity = pVelocity;
            obj.mass = pMass;
        end
            
    end
    
end

