# sample the images from this image folder
import os
import random 

sample_file = open("sample_output.txt", "a")
image_path = os.path.abspath("./")
image_lists = [ f for f in os.listdir(image_path) if f.endswith(".png") ]

sample_numbers = int(0.7*len(image_lists))

image_samples = random.sample(image_lists, sample_numbers)

for image in image_samples:
    print(os.path.join(image_path, image), file = sample_file)
    