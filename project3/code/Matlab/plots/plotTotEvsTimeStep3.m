h = [0.001, 0.01 0.03 0.05 0.1];
error = [2.85227-2.85218 2.8523-2.8514 2.8525-2.8495 2.8525-2.848 2.852-2.842];
figure
plot(log10(h),log10(error),'o-');
title('Absolute error accumulated in 100 years vs time step')
xlabel('log(h^2)');
ylabel('log(error)');