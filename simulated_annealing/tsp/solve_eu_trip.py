from plots import clear_output_folder,add_image_to_gif,plot_energy_function,plot_temp_function
from energies_n_neigh import find_energy,generate_neighbour,generate_first_circut
from points_generator import generate_europe_capitals
from swaptype import Swaptype
from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import os

def tsp_for_eu_trip(points,swap_type,initial_temp,end_temp,cooling_rate,max_iter,europe_capitals,output_folder = 'output_eu_trip'):

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

        
        temparatures.append(temparature)
        energies.append(E)
        temparatures.append(temparature)
        temparature *= cooling_rate
        stuck_count += 1


    plot_energy_function(output_folder,energies)
    plot_temp_function(output_folder,temparatures)
    max_lat = max([coord[0] for coord in europe_capitals.values()])
    min_lat = min([coord[0] for coord in europe_capitals.values()])
    max_lon = max([coord[1] for coord in europe_capitals.values()])
    min_lon = min([coord[1] for coord in europe_capitals.values()])
    plt.figure(figsize=(10, 8))
    ax = plt.axes(projection=ccrs.PlateCarree())

    # Set the extent to focus on Europe
    ax.set_extent([-10, 40, 35, 70], crs=ccrs.PlateCarree())

    # Draw coastlines and countries
    ax.coastlines(resolution='10m')
    ax.add_feature(cfeature.BORDERS, linestyle=':', edgecolor='gray')
    ax.add_feature(cfeature.LAND, facecolor='white')

    for capital, (lat, lon) in zip(europe_capitals.keys(), points):
        ax.plot(lon * (max_lon - min_lon) + min_lon, lat * (max_lat - min_lat) + min_lat, 'ro', transform=ccrs.PlateCarree(), markersize=6)  # Add dots
        ax.text(lon * (max_lon - min_lon) + min_lon, lat * (max_lat - min_lat) + min_lat, capital, transform=ccrs.PlateCarree(), fontsize=9, ha='right', va='bottom', color='blue')

    for i in range(len(best_circut) - 1):
        start_lat, start_lon = points[best_circut[i]]
        end_lat, end_lon = points[best_circut[i + 1]]
        ax.plot([start_lon * (max_lon - min_lon) + min_lon, end_lon * (max_lon - min_lon) + min_lon],
                [start_lat * (max_lat - min_lat) + min_lat, end_lat * (max_lat - min_lat) + min_lat],
                transform=ccrs.PlateCarree(), color='green')

    # Connect the last city to the first city to complete the cycle
    start_lat, start_lon = points[best_circut[-1]]
    end_lat, end_lon = points[best_circut[0]]
    ax.plot([start_lon * (max_lon - min_lon) + min_lon, end_lon * (max_lon - min_lon) + min_lon],
            [start_lat * (max_lat - min_lat) + min_lat, end_lat * (max_lat - min_lat) + min_lat],
            transform=ccrs.PlateCarree(), color='green')

    plt.title('European trip plan')
    plt.savefig(os.path.join(output_folder,'graph_output.png'))
    plt.close()

points,eu_capitals = generate_europe_capitals()


tsp_for_eu_trip(points,Swaptype.ARBITRARY,10,0.000001,0.99999,1600000,eu_capitals)