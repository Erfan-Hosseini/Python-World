import os
import imageio

file_list = sorted(os.listdir("Assignment 8/Gif/images"))

IMAGES = []

for name in file_list:
    path = "Assignment 8/Gif/images/" + name
    image = imageio.imread(path)
    IMAGES.append(image)

imageio.mimsave("Assignment 8/Gif/my_gif.gif", IMAGES)