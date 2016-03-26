clear
% initial parameters
xSun = [0 0 0]';
x0 = [1 0 0]';
v0 = [0 6.3 0]';
h = 0.001;
mEarth = 1.5E-6;
max_t = 3;
maxStep = round(max_t/h);
xi = x0;
vi = v0;

%initial variables
tracjectory = zeros(3,maxStep);
velocity = tracjectory;
acceleration = tracjectory;
tracjectory(:,1) = x0;
velocity(:,1) = v0;
ri = abs(xi - xSun);
acceleration(:,1) = -4*3.1415^2./norm(ri.*ri).*ri;
% verlet loop
n = 1;
while(n < maxStep)
    % verlet
    ri = xi - xSun;
    ai = -4*3.1415^2./norm(ri.*ri.*ri).*ri;
    
    xi_1 = xi + h*vi + h^2/2*ai;
    ri_1 = xi_1 - xSun;
    ai_1 = -4*3.1415^2./norm(ri_1.*ri_1.*ri_1).*ri_1;
    vi_1 = vi + h/2*(ai_1+ai);
    % write data
    tracjectory(:,n+1) = xi_1;
    velocity(:,n+1) = vi_1;
    acceleration(:,n+1) = ai_1;
    % move to next step
    xi = xi_1;
    vi = vi_1;    
    n = n+1;
end
% subplot(1,3,1)
% hold on
% plot(tracjectory(1,:),tracjectory(2,:),'*')
% title('Tracjectory');
% scatter(tracjectory(1,1),tracjectory(2,1),'r','filled')
% axis([-1.5 1.5 -1.5 1.5])
% %axis equal
% subplot(1,3,2)
% hold on
% plot(velocity(1,:),velocity(2,:),'*')
% scatter(velocity(1,1),velocity(2,1),'r','filled')
% title('Velocity');
% subplot(1,3,3)
% hold on
% plot(acceleration(1,:),acceleration(2,:),'*')
% scatter(acceleration(1,1),acceleration(2,1),'r','filled')
% title('Acceleration');
hold on
box on
grid on
plot3(tracjectory(1,:),tracjectory(2,:),tracjectory(3,:),'*')
title('Tracjectory');
scatter3(tracjectory(1,1),tracjectory(2,1),tracjectory(3,1),'r','filled')
axis([-1.5 1.5 -1.5 1.5])
axis equal
