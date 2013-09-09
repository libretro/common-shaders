T = 1.8;
beta = 0.50;
tt = -16 : 16;

% Cosine windows reduce ringing artifacts.
cosine_window = cos(pi * beta * tt / T) ./ (1 - (2 * beta * tt).^2 / (T * T));

prefilt = (1 / T) * sinc(tt / T) .* cosine_window .* kaiser(33, 2.0)';

figure(1);
freqz(prefilt);
figure(2);
stem(prefilt);

file = fopen('ntsc-pass2-prefilter.inc', 'w');
fprintf(file, '#define TAPS 16\n');
fprintf(file, 'const float filter[TAPS + 1] = float[TAPS + 1](\n');
fprintf(file, '   %.9f,\n', prefilt(1 : 16));
fprintf(file, '   %.9f);\n', prefilt(17));
fclose(file);


