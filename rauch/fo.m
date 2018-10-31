close all;
s=tf('s');
Ha=(s/(q*wo))/(s^2/wo^2+s/(wo*q)+1);
Hb=(s/(q*wob))/(s^2/wob^2+s/(wob*q)+1);
H=Ha*Hb*(1+5e3/4.7e3)
w=100:100:400e3;
[mag,pha]=bode(H,w);
mag=squeeze(mag);
pha=squeeze(pha);

figure;
%rectangle('Position',[19025, -80, 2e3, 79.01])
semilogx(w/(2*pi),20*log10(mag));
hold on
semilogx(freq,mag);
semilogx(freqsim,magsim);
title('Bode de Magnitud');
grid on
ylabel('Magnitud [dB]');
xlabel('Frecuencia [Hz]');
hold off 
legend('Teórico','Medido','Simulado');
axis([1e3 50e3 -80 10]);

figure;
semilogx(w/(2*pi),pha);
hold on
semilogx(freq,pha2);
semilogx(freqsim,phasim);
title('Bode de Fase');
grid on
ylabel('Fase [grados]');
xlabel('Frecuencia [Hz]');
legend('Teórico','Medido','Simulado');
axis([1e3 50e3 -250 200]);
hold off