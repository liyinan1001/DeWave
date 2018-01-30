import glob
import librosa
import os
import numpy as np
from constant import *

def audio_clip(data_dir, N, low, high, duration, output_dir):
  speakers = glob.glob(os.path.join(data_dir, "*.sph"))
  for i in range(len(speakers)):
    p = os.path.join(output_dir, str(i))
    if not os.path.exists(p):
      os.makedirs(p)
    y, _ = librosa.load(speakers[i], sr=SAMPLING_RATE)
    for j in range(N):
      k = int(np.random.randint(low, high, size=1))
      librosa.output.write_wav(os.path.join(p, str(j)) + ".wav", 
        y[k*SAMPLING_RATE : (k+duration)*SAMPLING_RATE], SAMPLING_RATE)

if __name__ == "__main__":
  # generate training and validation datasets
  audio_clip("data", 2, 60, 600, 5, "data/train")
  audio_clip("data", 2, 605, 725, 5, "data/val")
