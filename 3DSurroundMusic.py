# import
import numpy as np
import librosa

# def


def n_phase_sin(sample_rate, time, freq, n_phase):
    sine_waves = []
    x = np.arange(sample_rate*time)
    for idx in range(n_phase):
        sine_waves.append(
            np.sin(2*np.pi*freq*(x/sample_rate)+idx*np.pi/n_phase))
    return sine_waves


def make_stereo_music(source_path, sample_rate, destination_path, n_phase, freq=0.03):
    print('Compute')
    y, sample_rate = librosa.load(source_path, sample_rate)
    time = len(y)/sample_rate
    sine_waves = n_phase_sin(sample_rate, time, freq, n_phase)
    y = np.vstack((y*s for s in sine_waves))
    librosa.output.write_wav(
        destination_path, np.asfortranarray(y), sample_rate)
    print('Finish')


if __name__ == "__main__":
    source_path = 'test.wav'
    sample_rate = 44100
    destination_path = 'test.wav'
    make_stereo_music(source_path, sample_rate, destination_path, 2)
