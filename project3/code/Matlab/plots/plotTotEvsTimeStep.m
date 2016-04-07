h = [0.001, 0.01 0.03 0.05 0.1];
error = [2.960885-2.960845 2.9609-2.9605 2.961-2.959 2.961-2.953 2.96-2.89];
plot(log10(h),log10(error),'o-');
title('Absolute error accumulated in 100 years vs time step')
xlabel('log(h^2)');
ylabel('log(error)');