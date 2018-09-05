# Python 3

import pickle
import numpy as np
import os
from PIL import Image

pkl_path = "data/sim_push/demos_1.pkl"
gif_path = "data/sim_push/object_1/cond0.samp0.gif"

print("Opening file '{}'".format(pkl_path))
with open(pkl_path, "rb") as pkl_file:
    tmp = pickle._Unpickler(pkl_file)
    tmp.encoding = 'latin1'
    input_file = tmp.load()

print("\nType of pkl file: {}".format(type(input_file)))

print("\nKeys of pkl file:")
for key, value in input_file.items():
    if type(value) is np.ndarray:
        print("{} \t\t - Type: {} \t\t - Size: {}".format(key, type(value), np.array(value).shape))
    elif type(value) is list:
        print("{} \t - Type: {} \t\t\t\t - Size: {}".format(key, type(value), len(value)))
        print("\tItems in {}: {}".format(key, value))
    elif type(value) is str:
        print("{} \t\t - Type: {} \t\t\t\t - Elements: {}".format(key, type(value), value))
    else:
        print("Unknown type: {}".format(type(value)))


frame = Image.open(gif_path)
nframes = 0
while frame:
    nframes += 1
    try:
        frame.seek(nframes)
    except EOFError:
        break;

sample_rate = 10 # pictures taken at 10Hz
print("\nGif has {} frames".format(nframes))
print("The demonstration took {} seconds".format(nframes/sample_rate))