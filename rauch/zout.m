%semilogx(w/(2*pi),pha);
semilogx(f,10.^(m./20));
%semilogx(freqsim,fasesim);
title('Impedancia de Salida');
grid on
ylabel('Modulo [Ohms]');
xlabel('Frecuencia [Hz]');
%legend('Teórico','Simulado','Medido');
%axis([1e3 50e3 -250 200]);