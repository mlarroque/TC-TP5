%semilogx(w/(2*pi),pha);
semilogx(f,fa);
%semilogx(freqsim,fasesim);
title('Impedancia de Salida');
grid on
ylabel('Fase [grados]');
xlabel('Frecuencia [Hz]');
%legend('Te�rico','Simulado','Medido');
axis([1e3 50e3 0 180]);