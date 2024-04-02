from plots import clear_output_folder,add_image_to_gif,plot_energy_function,plot_temp_function,create_graph_png,make_gif
from energies_n_neigh import find_energy,generate_neighbour,generate_first_circut
import points_generator as pg
from swaptype import Swaptype
from copy import deepcopy
import numpy as np


def tsp(points,swap_type,initial_temp,end_temp,cooling_rate,max_iter,output_folder = 'output'):

    clear_output_folder(output_folder)

    curr_circut = generate_first_circut(points)
    best_circut = deepcopy(curr_circut)

    E = find_energy(curr_circut,points)
    best_E = E

    stuck_count = 0
    reheat_rate = initial_temp

    images = []
    energies = []
    temparatures = []

    temparature = initial_temp

    for i in range(max_iter):

        if i%10000 == 0 :
            print("Iteration "+str(i)+", temparature: "+str(temparature)+", current score:"+str(E)+"  Best score: "+str(best_E))

        if temparature < end_temp:
            break

        if stuck_count > 10000 or temparature < 0.01:
            tmp = temparature *reheat_rate
            print("Program is stuck - rehating from: " + str(temparature) + "to: " + str(tmp))
            temparature *= reheat_rate
            curr_circut = generate_first_circut(points)
            stuck_count = 0  

        new_circut = generate_neighbour(curr_circut,swap_type)
        new_E = find_energy(new_circut,points)

        if np.random.rand() < np.exp((E - new_E) / temparature):
            curr_circut = deepcopy(new_circut)
            E = new_E
            if new_E < find_energy(best_circut,points):
                best_circut = deepcopy(new_circut)
                add_image_to_gif(best_circut,points,images)
                best_E = new_E
            stuck_count = 0
            energies.append(E)
        
        temparatures.append(temparature)
        temparatures.append(temparature)
        temparature *= cooling_rate
        stuck_count += 1
    
    plot_energy_function(output_folder,energies)
    plot_temp_function(output_folder,temparatures)
    make_gif(output_folder,images)
    create_graph_png(output_folder,best_circut,points)



points = pg.generate_uniform(20)

tsp(points,Swaptype.ARBITRARY,10,0.000001,0.99,100000,'output_u')

