import pickle
import numpy as np

with open("data/sim_vision_reach/demos_13.pkl", "r") as input_file:
    tmp = pickle.load(input_file)

print("\nType of pkl file:")
print(type(tmp))
print("\nKeys of pkl file:")
for key, value in tmp.items():
    if type(value) is np.ndarray:
        print("{} \t\t - Type: {} \t\t - Size: {}".format(key, type(value), np.array(value).shape))
    elif type(value) is list:
        print("{} \t - Type: {} \t\t\t\t - Size: {}".format(key, type(value), len(value)))
        print("\tItems in {}: {}".format(key, value))
