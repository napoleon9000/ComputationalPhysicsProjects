data2 = [91.2 61.3 36.4 26.0];
data1 = [150 100 60 50];
plot(fliplr(data1), fliplr(data1./data2),'o-')
axis([50 150 1 2])
title('Ratio between T and T_i')
hold on
box on
grid on
data3 = [114.2 67.9 37.0 30.9];
plot(fliplr(data1), fliplr(data1./data3),'o-')