import tensorflow as tf
import librosa
import matplotlib.pyplot as plt
import librosa.display
import numpy as np

from tqdm import tqdm
import os
import pickle
# print(os.getcwd())

# mfcc = pickle.load(open('mfcc_male_voices.pkl', 'rb'))

pluto = librosa.load('pluto.mp3')

D = librosa.stft(pluto[0])
log_power = librosa.power_to_db(D**2, ref=np.max)
librosa.display.specshow(log_power, x_axis='time', y_axis='linear')
plt.colorbar()
plt.show()
exit()

test = mfcc[1][:][:50]

fig, ax = plt.subplots()
img = librosa.display.specshow(mfcc[2], x_axis='time', ax=ax)
img = librosa.display.specshow(mfcc[1], x_axis='time', ax=ax)
# fig.colorbar(img, ax=ax)
ax.set(title='MFCC')
plt.show()
# for i in range(10):
#     print(mfcc[i].shape)