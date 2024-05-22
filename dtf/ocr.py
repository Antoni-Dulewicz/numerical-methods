from imgd_analysis import invert_image, to_gray, to_rgb,calculate_correlation
import os
from PIL import Image
from level import Level
import numpy as np

percentege_per_letter = {'a': 0.90, 'b': 0.90, 'c': 0.90, 'd': 0.92,
                            'e': 0.90, 'f': 0.95, 'g': 0.90, 'h': 0.95,
                            'i': 0.90, 'j': 0.90, 'k': 0.90, 'l': 0.90,
                            'm': 0.92, 'n': 0.92, 'o': 0.90, 'p': 0.90,
                            'q': 0.90, 'r': 0.90, 's': 0.90, 't': 0.93, 
                            'u': 0.90, 'v': 0.90, 'w': 0.90, 'x': 0.90,
                            'y': 0.90, 'z': 0.90}

def correlation_wout_norm(A_gray,letter_gray):
    highest_correlation = calculate_correlation(letter_gray, letter_gray,False)
    correlation = calculate_correlation(A_gray, letter_gray,False)
    correlation /= np.max(np.abs(highest_correlation))

    return correlation

def create_alphabet(alphabet_path):
    easy_to_read_short = {}
    easy_to_read_long = {}
    medium_to_read = {}
    hard_to_read = {}



    for letter_filename in os.listdir(alphabet_path):
        letter = letter_filename.split('.')[0]
        letter_img = Image.open(os.path.join(alphabet_path, letter_filename))
        letter_img_inv = invert_image(letter_img)
        letter_img_gray = to_gray(letter_img_inv)

        
        if letter in ['a','b','d','e','f','k','n','s','t','x','z']:
            easy_to_read_short[letter] = letter_img_gray
            
        elif letter in ['g','j','p','q','y']:
            easy_to_read_long[letter] = letter_img_gray

        elif letter in ['m','o','r','w','h']:
            medium_to_read[letter] = letter_img_gray

        else:
            hard_to_read[letter] = letter_img_gray
        
    
    return easy_to_read_short,easy_to_read_long,medium_to_read,hard_to_read

def find_elements(correlation,letter):
    elements = []
    w,h = correlation.shape

    for i in range(w):
        for j in range(h):
            if correlation[i,j] > percentege_per_letter[letter]:
                elements.append((i,j))
    
    return elements

def line_already_exists(y,lines):
    for line in lines:
        if abs(line - y) < 3:
            return line
    return 0
    

def space_taken(text,given_letter):

    for letter in text:
        if abs(letter[1][0] - given_letter[1][0]) < 8 and abs(letter[1][1] - given_letter[1][1]) < 8:
            return True
    return False

def add_letter(correlation,letter,text,lines):

    elements = find_elements(correlation,letter)


    for y,x in elements:
        line = line_already_exists(y,lines)
        if not line:
            lines.append(y)
        else:
            y = line
        
        if not space_taken(text,(letter,(x,y))):
            text.append((letter,(x,y)))
            
  
    return text
        

def adjust_text(text,lines):
    text.sort(key=lambda x: (x[1][1],x[1][0]))

    for i in range(len(text)-1):
        print(text[i][0],end='')
        if text[i+1][1][1] != text[i][1][1]:
            print('\n',end='')
        elif abs(text[i+1][1][0] - text[i][1][0]) > 17:
            print(' ',end='')



def image_to_text(image_path,alphabet_path):

    easy_to_read_short,easy_to_read_long,medium_to_read,hard_to_read = create_alphabet(alphabet_path)

    A = Image.open(image_path)
    A_inv = invert_image(A)
    A_gray = to_gray(A_inv)

    text = []
    lines = []


    for letter in easy_to_read_short:    
        correlation = correlation_wout_norm(A_gray,easy_to_read_short[letter])
        add_letter(correlation,letter,text,lines)
        
    for letter in easy_to_read_long:
        correlation = correlation_wout_norm(A_gray,easy_to_read_long[letter])
        add_letter(correlation,letter,text,lines)

    for letter in medium_to_read:
        correlation = correlation_wout_norm(A_gray,medium_to_read[letter])
        add_letter(correlation,letter,text,lines)

    for letter in hard_to_read:
        correlation = correlation_wout_norm(A_gray,hard_to_read[letter])
        add_letter(correlation,letter,text,lines)


    adjust_text(text,lines)
        

#image_to_text('images/FE/FE2.png','images/FE/characters')
#image_to_text('images/FE/FE3.png','images/FE/characters')
#image_to_text('images/FE/FE4.png','images/FE/characters')
#image_to_text('images/FE/FE.png','images/FE/characters')
image_to_text('images/FE/wonderwall.png','images/FE/characters')

