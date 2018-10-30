q=4.52;
qo=1.5;

wo=111753;
R1=82e3;
C1=444e-12;
C2=444e-12;

% wo=141306;
% r1=47e3;
% c=680e-12;

alpha=(qo-q)/(-2*q*qo^2);
K=alpha/(1+alpha);

r=1/(3*C1*wo);
a=r/R1;
R2=9*r;
R3=r/(1-a);
r6=k*r;
r7=(1-k)*r;
g=R3*R2*C1/((K-1)*R1*R3*(C1+C2)+K*(R1+R3)*R2*C2);