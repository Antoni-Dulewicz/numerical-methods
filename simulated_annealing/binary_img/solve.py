from generate_img import generate_binary_image,generate_new_image
from draw_image import draw_image,draw_energy,draw_temperature,clear_output_folder,add_image_to_gif,make_gif
from finding_energies import find_energy
from energytype import Energytype
import numpy as np
from copy import deepcopy



def simulated_annealing(img_size, density, max_iter, initial_temp, final_temp,reheat_temp, cooling_rate,energy_type,output_folder = 'output'):

    clear_output_folder(output_folder)

    starting_img = generate_binary_image(img_size, density)
    current_img = deepcopy(starting_img)
    best_img = deepcopy(current_img)



    E = find_energy(current_img,energy_type)
    best_E = E

    stuck_count = 0
    reheat_rate = initial_temp/0.3
    target = 0

    images = []
    energies = []
    temparatures = []

    temparature = initial_temp
    
    for i in range(max_iter):
        if i%10000 == 0 :
            print("Iteration "+str(i)+", temparature: "+str(temparature)+", current score:"+str(E)+"  Best score: "+str(best_E))

        if E == target:
            break

        if temparature < final_temp:
            break

        if stuck_count > 15000 or temparature < reheat_temp:
            tmp = temparature*reheat_rate
            print("Program is stuck - rehating from: " + str(temparature) + "to: " + str(tmp))
            temparature *= reheat_rate
            current_img = generate_binary_image(img_size,density)
            stuck_count = 0


        new_img = generate_new_image(current_img)
        new_E = find_energy(new_img,energy_type)
        
        if new_E < E or np.random.rand() < np.exp((E - new_E) / temparature):
            current_img = deepcopy(new_img)
            E = new_E
            if new_E < find_energy(best_img,energy_type):
                best_E = new_E
                best_img = deepcopy(new_img)
                add_image_to_gif(best_img,images)
            stuck_count = 0
            energies.append(E) 
           
        temparatures.append(temparature)    
        temparature *= cooling_rate
        stuck_count += 1

    draw_energy(energies,output_folder)
    draw_temperature(temparatures,output_folder)
    draw_image(best_img,output_folder)
    make_gif(images,output_folder)
    return best_img

#img1 = simulated_annealing(10, 0.5, 50000, 10, 0.000000001,0.001, 0.9999,Energytype.FOUR,'output_fours')
#img2 = simulated_annealing(10, 0.5, 50000, 10, 0.000000001,0.001, 0.9999,Energytype.EIGHT,'output_eights')
#img3 = simulated_annealing(30, 0.5, 1100000, 10, 0.000000001,0.001, 0.9999,Energytype.CORNERS,'output_corners')
#img3 = simulated_annealing(10, 0.5, 100000, 10, 0.000000001,0.001, 0.9999,Energytype.BOTH_CORNERS,'output_corners')


