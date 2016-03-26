classdef myData
   properties
      Data = 0;
   end
   methods
      function obj = addData(obj,val)
%          newData = obj.Data + val;
%          obj.Data = newData;
           obj.Data = obj.Data + val;
      end
   end
end