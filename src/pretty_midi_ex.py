import pretty_midi
import librosa.display
import matplotlib.pyplot as plt
import numpy as np




def plot_piano_roll(pm, start_pitch, end_pitch, fs=100):
	librosa.display.specshow(pm.get_piano_roll(fs)[start_pitch:end_pitch],
							hop_length=1, sr=fs, x_axis='time', y_axis='cqt_note',
							fmin=pretty_midi.note_number_to_hz(start_pitch))


pm = pretty_midi.PrettyMIDI('bwv772.mid')
plt.figure(figsize=(8,4))

fs = 100
start_pitch = 0
end_pitch = 88
plot_piano_roll(pm, start_pitch, end_pitch, fs=fs)

# plt.show()

data = pm.get_piano_roll(fs)[start_pitch:end_pitch]
print(data.shape)

mean_value = np.mean(data,axis=0)
print(mean_value)
# plt.plot(mean_value)

plt.colorbar()
plt.show()