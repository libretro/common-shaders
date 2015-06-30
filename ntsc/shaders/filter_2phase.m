T = 5.6;
beta = 0.50;
tt = -32 : 32;

% Cosine windows reduce ringing artifacts.
cosine_window = cos(pi * beta * tt / T) ./ (1 - (2 * beta * tt).^2 / (T * T));

luma = (1 / T) * sinc(tt / T) .* cosine_window .* kaiser(65, 1.0)';

chroma = gausswin(65);
chroma = chroma / sum(chroma);

close all;
figure(1);
freqz(luma);

figure(2);
stem(luma);

figure(3);
freqz(chroma);

file = fopen('ntsc-decode-filter-2phase.inc', 'w');
fprintf(file, '#define TAPS 32\n');
fprintf(file, 'const float luma_filter[TAPS + 1] = float[TAPS + 1](\n');
fprintf(file, '   %.9f,\n', luma(1 : 32));
fprintf(file, '   %.9f);\n\n', luma(33));

fprintf(file, 'const float chroma_filter[TAPS + 1] = float[TAPS + 1](\n');
fprintf(file, '   %.9f,\n', chroma(1 : 32));
fprintf(file, '   %.9f);\n', chroma(33));
fclose(file);
