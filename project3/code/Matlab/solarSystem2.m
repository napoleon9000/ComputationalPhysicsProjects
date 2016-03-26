classdef solarSystem2
   properties
      Data = 0;
      list = [];
   end
   methods
      function obj = addData(obj,val)
%          newData = obj.Data + val;
%          obj.Data = newData;
           obj.Data
           obj.Data = obj.Data + 1;
           obj.list = val.name;
      end
   end
end