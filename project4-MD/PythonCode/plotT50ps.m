filename = 'Ar_log9_100.txt';
dataStr = readList(filename);
data = str2num(dataStr(3:end,:));
range = 1:400;
plotIdx = 7;
% time     ke      pe    etot  momentum diffCoeff temp 
figure
plot(data(range,1), (data(range,plotIdx)))
% semilogy(data(:,1), (data(:,6)))
box on
grid on
hold on
% axis([0 5 -1 0])


title('Temperature vs simulation time')
xlabel('Simulation time/ps')
ylabel('Temperature/K');