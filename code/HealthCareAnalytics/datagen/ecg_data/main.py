import pylab
import scipy.signal as signal
import numpy
numpy.set_printoptions(suppress=True) #prevent numpy exponential
                                   #notation on print, default False

print('Simulating heart ecg')

# The "Daubechies" wavelet is a rough approximation to a real,
# single, heart beat ("pqrst") signal
pqrst = signal.wavelets.daub(10)

# Add the gap after the pqrst when the heart is resting.
samples_rest = 10
zero_array = numpy.zeros(samples_rest, dtype=float)
pqrst_full = numpy.concatenate([pqrst,zero_array])

# Plot the heart signal template
pylab.plot(pqrst_full)
pylab.xlabel('Sample number')
pylab.ylabel('Amplitude (normalised)')
pylab.title('Heart beat signal Template')
# pylab.show()

# Simulated Beats per minute rate
# For a health, athletic, person, 60 is resting, 180 is intensive exercising
bpm = 60
bps = bpm / 60 # 1.0

# Simumated period of time in seconds that the ecg is captured in
capture_length = 10 # seconds

# Caculate the number of beats in capture time period
# Round the number to simplify things
num_heart_beats = int(capture_length * bps)

# Concatonate together the number of heart beats needed
ecg_template = numpy.tile(pqrst_full , num_heart_beats)
ecg_template_for_10_secs = ecg_template

# Plot the heart ECG template
pylab.plot(ecg_template)
pylab.xlabel('Sample number')
pylab.ylabel('Amplitude (normalised)')
pylab.title('Heart ECG Template')
# pylab.show()

# Add random (gaussian distributed) noise
noise = numpy.random.normal(0, 0.01, len(ecg_template))
ecg_template_noisy = noise + ecg_template

print(f"len(pqrst) {len(pqrst)} ")
print(f"len(pqrst_full) {len(pqrst_full)} with samples_rest = {samples_rest} for heart resting")
print(f"bps {bps} heart beat per second")
print(f"capture_length {capture_length} seconds")
print(f"num_heart_beats int(capture_length * bps) = {num_heart_beats} heart beats")
print(f"ecg_template_for_10_secs {len(ecg_template_for_10_secs)} ::: includes 10 for noisy (resting heartbeat)")
print(f"ecg_template_noisy {len(ecg_template_noisy)}")

# Plot the noisy heart ECG template
pylab.plot(ecg_template_noisy)
pylab.xlabel('Sample number')
pylab.ylabel('Amplitude (normalised)')
pylab.title('Heart ECG Template with Gaussian noise')
# pylab.show()


# Simulate an ADC by sampling the noisy ecg template to produce the values
# Might be worth checking nyquist here
# e.g. sampling rate >= (2 * template sampling rate)
sampling_rate = 50.0
num_samples = sampling_rate * capture_length
# print(f"num_samples {num_samples}")
# ecg_sampled = signal.resample(ecg_template_noisy, num_samples)

# Scale the normalised amplitude of the sampled ecg to whatever the ADC
# bit resolution is
# note: check if this is correct: not sure if there should be negative bit values.
adc_bit_resolution = 1024
ecg =  adc_bit_resolution * ecg_template_noisy

# Plot the sampled ecg signal
pylab.plot(ecg)
pylab.xlabel('Sample number')
pylab.ylabel('bit value')
pylab.title('%d bpm ECG signal with gaussian noise sampled at %d Hz' %(bpm, sampling_rate) )
# pylab.show()

print('saving ecg values to file')
print(len(ecg))
# print(ecg)
numpy.savetxt("ecg_values.csv", ecg, delimiter=",")
print('Done')