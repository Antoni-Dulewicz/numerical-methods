import numpy as np
import numpy.fft as fft
from PIL import Image
from numpy import rot90
import os

RED = (255, 0, 0)
BLUE = (0, 0, 255)

def invert_image(image):
    return Image.eval(image, lambda x: 255 - x)

def save_image(image, filename):
    image.save(filename)

def to_gray(image):
    return image.convert('L')

def to_rgb(image):
    return image.convert('RGB')

def dft(image):
    image_arr = np.asarray(image)
    dft_arr = fft.fft2(image_arr)

    #np.abs oblicza modul liczby zespolonej (pierwiastek z sumy kwadratow czesci rzeczywistej i urojonej)
    #np.log oblicza logarytm z liczby bo roznice miedzy modulami sa duze
    module = np.log(np.abs(dft_arr))
    #skalujemy modul do przedzialu [0, 255]
    module /= module.max()
    module = 255 * module

    module = module.astype(np.uint8)
    module = Image.fromarray(module)


    #np.angle oblicza faze (kat) liczby zespolonej
    # dodajemy pi, aby faza byla z przedzialu [0, 2*pi] a nie [-pi, pi]
    phase = (np.angle(dft_arr) + np.pi)
    #skalujemy faze do przedzialu [0, 255]
    phase *= 255 / (2 * np.pi)

    phase = phase.astype(np.uint8)
    phase = Image.fromarray(phase)

    return module, phase

def calculate_correlation(image1,image2,norm = True):
    image1_arr = np.asarray(image1)
    image2_arr = np.asarray(image2)

    h,w = image1_arr.shape

    rotated = rot90(image2_arr, 2)

    tmp1 = fft.fft2(image1_arr)
    tmp2 = fft.fft2(rotated,(h,w))

    result = fft.ifft2(tmp1*tmp2)
    
    #leave only real values
    result = np.real(result)

    if norm:
        result /= np.max(np.abs(result))

    return result

def save_correlation(correlation,filename):
    correlation = np.abs(correlation)
    correlation = 255 * correlation
    correlation = correlation.astype(np.uint8)
    correlation = Image.fromarray(correlation)
    correlation.save(filename)


def highlight_correlated_elements(image_arr, correlation, percentage,color):
    elements = []
    w,h = correlation.shape

    for i in range(w):
        for j in range(h):
            if correlation[i,j] > percentage:
                elements.append((i,j))

    result = image_arr.copy()

    for y, x in elements:
        for height in range(0, 4):
            for width in range(-9, 0):
                    result[y + height, x + width] = color

    result_image = Image.fromarray(result)
    return result_image

def find_pattern(folder_path,image_path, pattern_path, percentage,color):

    A = Image.open(image_path)

    if folder_path == 'images/fishes':
        A_gray = to_gray(A)
        A_color = to_rgb(A)
    else:
        A_inv = invert_image(A)
        A_gray = to_gray(A_inv)
        A_color = to_rgb(A_gray)
        save_image(A_gray, os.path.join(folder_path, 'galia_gray.png'))
        

    module,phase = dft(A_gray)    

    save_image(module, os.path.join(folder_path, 'module.png'))
    save_image(phase, os.path.join(folder_path, 'phase.png'))

    if folder_path == 'images/fishes':
        pattern = Image.open(pattern_path)
        pattern_gray = to_gray(pattern)
    else:
        pattern = Image.open(pattern_path)
        pattern_inv = invert_image(pattern)
        pattern_gray = to_gray(pattern_inv)
        

    save_image(pattern_gray, os.path.join(folder_path, 'pattern_gray.png'))

    correlation = calculate_correlation(A_gray, pattern_gray)
    save_correlation(correlation, os.path.join(folder_path, 'correlation.png'))

    highlighted = highlight_correlated_elements(np.asarray(A_color), correlation,percentage,color)
    save_image(highlighted, os.path.join(folder_path, 'highlighted.png'))


find_pattern('images/fishes','images/fishes/fishes.png','images/fishes/fish1.png',0.95,RED)
#find_pattern('images/galia','images/galia/galia.png','images/galia/e.png',0.95,RED)


