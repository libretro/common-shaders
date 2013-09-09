T = 4.1;
beta = 0.45;
tt = -24 : 24;

% Cosine windows reduce ringing artifacts.
cosine_window = cos(pi * beta * tt / T) ./ (1 - (2 * beta * tt).^2 / (T * T));

luma = (1 / T) * sinc(tt / T) .* cosine_window .* kaiser(49, 1.0)';

chroma = gausswin(49);
chroma = chroma / sum(chroma);

close all;
figure(1);
freqz(luma);

figure(2);
stem(luma);

figure(3);
freqz(chroma);

file = fopen('ntsc-decode-filter-3phase.inc', 'w');
fprintf(file, '#define TAPS 24\n');
fprintf(file, 'const float luma_filter[TAPS + 1] = float[TAPS + 1](\n');
fprintf(file, '   %.9f,\n', luma(1 : 24));
fprintf(file, '   %.9f);\n\n', luma(25));

fprintf(file, 'const float chroma_filter[TAPS + 1] = float[TAPS + 1](\n');
fprintf(file, '   %.9f,\n', chroma(1 : 24));
fprintf(file, '   %.9f);\n', chroma(25));
fclose(file);
