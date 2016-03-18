clear
% initial parameters
xSun = [0 0 0]';
x0 = [1 0 0]';
v0 = [0 1 0]';
h = 1E-5;
maxStep = 1E5;
xi = x0;
vi = v0;

%%
% verlet
n = 1;
while(n < maxStep)
    ri = abs(xi - xSun);
    ai = -4*3.1415^2./ri;    
    xi_1 = xi + h*vi + h^2/2*ai;
    ri_1 = abs(xi_1 - xSun);
    ai_i = -4*3.1415^2./ri_1;
    vi_1 = vi + h/2*(ai_1+ai);    
    
    n = n+1;
end
xi_1