n = 1000;
r1 = normrnd(0,1,n,1);
r2=normrnd(0,1,n,1);
z=r1.^2+r2;
hist(z,-3.75:.5:3.75);
xlim([-4 4]);
title('1000 Simulated N(0,1) Random Values');
xlabel('Z');
ylabel('Frequency');