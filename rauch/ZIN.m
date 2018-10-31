close all;
s=tf('s');
Zin=(s^2*R1*C2^2*R2*R3+s*R1*R3*(C2+C1)+R1+R3)/(s^2*C2*C1*R3*R2+s*R3*(C2+C1)+1);
%Zin=(s^2*R1*R2*R3*r*(1-k)*C1+s*(2*R1*R2*r*(1-k)-r*k*(R1*R2-R3*R2))*C1+r*(1-k)*(R1+R2))/(s^2*R2*R3*r*(1-k)*C2+s*r*(2*R2*(1-k)-R2*k)+r*(1-k));
w=100:100:400e3;
[mag,pha]=bode(Zin,w);
mag=squeeze(mag);
pha=squeeze(pha);

figure;
%rectangle('Position',[19025, -80, 2e3, 79.01])
%semilogx(w/(2*pi),mag);
hold on
%semilogx(freqsim,magsim);
semilogx(f,10.^(m./20));
title('Módulo de Impedancia de entrada');
grid on
ylabel('Impedancia [Ohm]');
xlabel('Frecuencia [Hz]');
hold off 
legend('Teórico','Simulado','Medido');
axis([1e3 50e3 0 100e3]);

figure;
%semilogx(w/(2*pi),pha);
hold on
semilogx(f,p);
%semilogx(freqsim,fasesim);
title('Fase de Impedancia de Entrada');
grid on
ylabel('Fase [grados]');
xlabel('Frecuencia [Hz]');
legend('Teórico','Simulado','Medido');
axis([1e3 50e3 -250 200]);
hold off