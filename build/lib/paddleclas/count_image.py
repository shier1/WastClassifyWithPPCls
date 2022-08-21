import matplotlib.pyplot as plt
import numpy as np
import json
import os

with open('dataset/garbage_1/garbage_label.json', 'r') as f:
    json_label = json.load(f)

root_path = './dataset/garbage_1'
num_dict = []

for key, val in json_label.items():
    image_dir_path = os.path.join(root_path, key)
    num_dict.append(len(os.listdir(image_dir_path)))

print(num_dict)
# plt.hist(num_dict, bins=len(num_dict))
# plt.show()