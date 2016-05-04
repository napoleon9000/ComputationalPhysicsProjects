filename = 'Ar_log10_50.txt';
dataStr = readList(filename);
data = str2num(dataStr(3:end,:));
range = 1:50;
pRange = 30:50;
plotIdx = 7;
% time     ke      pe    etot  momentum diffCoeff temp 
figure
plot(data(range,1), (data(range,plotIdx)))
% semilogy(data(:,1), (data(:,6)))
meanT = mean(data(pRange,plotIdx));
stdT = std(data(pRange,plotIdx));
text(3,meanT,[num2str(meanT), ' K ± ' num2str(stdT)])
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
meanT = mean(data(pRange,plotIdx));
stdT = std(data(pRange,plotIdx));
text(3,meanT,[num2str(meanT), ' K ± ' num2str(stdT)])


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
meanT = mean(data(pRange,plotIdx));
stdT = std(data(pRange,plotIdx));
text(3,meanT,[num2str(meanT), ' K ± ' num2str(stdT)])


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
meanT = mean(data(pRange,plotIdx));
stdT = std(data(pRange,plotIdx));
text(3,meanT,[num2str(meanT), ' K ± ' num2str(stdT)])
legend('50','60','100','150')
title('Temperature vs simulation time')
xlabel('Simulation time/ps')
ylabel('Temperature/K');