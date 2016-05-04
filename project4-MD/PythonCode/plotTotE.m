filename = 'Ar_log10_50.txt';
dataStr = readList(filename);
data = str2num(dataStr(3:end,:));
range = 1:50;
plotIdx = 4;
% time     ke      pe    etot  momentum diffCoeff temp 
figure
plot(data(range,1), (data(range,plotIdx)))
% semilogy(data(:,1), (data(:,6)))
box on
grid on
hold on
% axis([0 5 -1 0])

filename = 'Ar_log_60.txt';
dataStr = readList(filename);
data = str2num(dataStr(3:end,:));
% time     ke      pe    etot  momentum diffCoeff temp 
% figure
% semilogy(data(:,1), (data(:,6)))
plot(data(range,1), (data(range,plotIdx)))
box on
grid on
hold on

filename = 'Ar_log9_100.txt';
dataStr = readList(filename);
data = str2num(dataStr(3:end,:));
% time     ke      pe    etot  momentum diffCoeff temp 
% figure
% semilogy(data(:,1), (data(:,6)))
plot(data(range,1), (data(range,plotIdx)))
box on
grid on
hold on

filename = 'Ar_log8_150.txt';
dataStr = readList(filename);
data = str2num(dataStr(3:end,:));
% time     ke      pe    etot  momentum diffCoeff temp 
% figure
% semilogy(data(:,1), (data(:,6)))
plot(data(range,1), (data(range,plotIdx)))
box on
grid on
hold on

legend('50','60','100','150','Location','NorthWest')
title('Total energy vs simulation time')
xlabel('Simulation time/ps')
ylabel('Total energy/J');