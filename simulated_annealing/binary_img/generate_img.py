from copy import deepcopy
import numpy as np
import random


def generate_new_image(img):
    new_img = deepcopy(img)
    n,m = img.shape
    x = random.randint(0, n-1)
    y = random.randint(0, m-1)

    x1 = random.randint(0,n-1)
    y1 = random.randint(0,m-1)

    while x1 == x and y1 == y:
        x1 = random.randint(0,n-1)
        y1 = random.randint(0,m-1)

    new_img[x1][y1],new_img[x][y] = new_img[x][y],new_img[x1][y1]

    return new_img



def generate_binary_image(n, density):
    image = np.zeros((n, n), dtype=int)

    num_white_points = int(n * n * (1 - density))

    white_indices = np.random.choice(n * n, num_white_points, replace=False)

    image.ravel()[white_indices] = 1
    
    return image
