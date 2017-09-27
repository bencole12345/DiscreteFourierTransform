import cmath


def dft(source, sample_rate):
    """
    Calculates the Discrete Fourier Transform of an the passed array of samples.
    """

    n = len(source)
    output_complex = []

    for f in range(0, int(n/2)):
        if f % 10 == 0:
            print("Testing %ihz..." % f)
        real_sum = 0
        imaginary_sum = 0
        for t in range(0, n):
            argument = -2 * cmath.pi * t * f / n
            real_sum += source[t] * cmath.cos(argument) / sample_rate
            imaginary_sum += source[t] * cmath.sin(argument) / sample_rate
        output_complex.append(complex(real_sum, imaginary_sum))

    output = list(map(lambda z: abs(z), output_complex))
    return output


def generate_sinusoidal_wave(frequency, phase, amplitude, sample_rate, duration):
    output = []
    for i in range(duration * sample_rate):
        t = i / sample_rate
        angle = frequency * 2 * cmath.pi * t + phase
        output.append((amplitude * cmath.sin(angle)).real)
    return output


def test():
    frequency = 5
    phase = 0
    amplitude = 1
    sample_rate = 440
    duration = 1
    wave = generate_sinusoidal_wave(frequency, phase, amplitude, sample_rate, duration)
    for i in wave:
        print(i)
    print("=" * 80)
    wave_transformed = dft(wave, sample_rate)
    for i in range(len(wave_transformed)):
        print("Amplitude at %ihz: %f" % (i, wave_transformed[i]))


if __name__ == "__main__":
	test()
