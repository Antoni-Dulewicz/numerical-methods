import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def compress_img(U,S,VT,image,k):
    height,width = image.shape
    cmp_img = []

    for i in range(height):
        row = []
        for j in range(width):
            pixel_val = 0
            for z in range(k):
                pixel_val += U[i][z]*S[z]*VT[z][j]
            row.append(pixel_val)
        cmp_img.append(row)
    
    return np.array(cmp_img)

def solve():
    img = Image.open('lena.png').convert('L')

    img.show()
    I = np.array(img)

    U,S,VT = np.linalg.svd(I)

    differences = []

    for k in [10,50,100]:
        I_alfa = compress_img(U,S,VT,I,k)
        I_alfa = Image.fromarray(I_alfa.astype('uint8'))
        diff = np.linalg.norm(I-I_alfa)
        differences.append(diff)
        I_alfa.show()
    
    plt.plot([10,50,100],differences)
    plt.xlabel('k')
    plt.ylabel('difference')
    plt.show()

    

solve()
