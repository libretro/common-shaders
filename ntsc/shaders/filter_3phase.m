T = 3.9;
beta = 0.50;
tt = -22.5 : 22.5;

% Cosine windows reduce ringing artifacts.
cosine_window = cos(pi * beta * tt / T) ./ (1 - (2 * beta * tt).^2 / (T * T));
luma = (1 / T) * sinc(tt / T) .* cosine_window .* kaiser(length(tt), 4.0)';
luma = conv(luma, [1 0 0 1] / 2);

T = 12.2;
beta = 0.50;
tt = -22.5 : 22.5;

% Cosine windows reduce ringing artifacts.
cosine_window = cos(pi * beta * tt / T) ./ (1 - (2 * beta * tt).^2 / (T * T));
chroma = (1 / T) * sinc(tt / T) .* cosine_window .* kaiser(length(tt), 4.0)';
chroma = conv(chroma, [1 0 0 1] / 2);

close all;
figure(1);
freqz(luma, 1, 16 * 1024);

figure(2);
stem(luma);

figure(3);
freqz(chroma, 1, 16 * 1024);

file = fopen('ntsc-decode-filter-3phase.inc', 'w');
fprintf(file, '#define TAPS 24\n');
fprintf(file, 'const float luma_filter[TAPS + 1] = float[TAPS + 1](\n');
fprintf(file, '   %.9f,\n', luma(1 : 24));
fprintf(file, '   %.9f);\n\n', luma(25));

fprintf(file, 'const float chroma_filter[TAPS + 1] = float[TAPS + 1](\n');
fprintf(file, '   %.9f,\n', chroma(1 : 24));
fprintf(file, '   %.9f);\n', chroma(25));
fclose(file);
