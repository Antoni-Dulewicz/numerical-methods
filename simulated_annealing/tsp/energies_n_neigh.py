from swaptype import Swaptype
from copy import deepcopy
import numpy as np

def distance_between_points(a,b):    
    return np.linalg.norm(a-b)


def find_energy(circut,points):
    energy = 0
    v = len(circut)
    for i in range(len(circut)-1):
        u = circut[i]
        v = circut[i+1]
        energy += distance_between_points(points[u],points[v])
    
    return energy

def arbitrary_swap(circut):
    cp_circut = deepcopy(circut)    
    x,y = np.random.choice(range(1,len(circut)-1), size=2, replace=False)
    
    cp_circut[x],cp_circut[y]=cp_circut[y],cp_circut[x]

    return cp_circut


def consecutive_swap(circut):
    cp_circut = deepcopy(circut)
    x = np.random.randint(0,len(circut)-2)
    y = x + 1

    cp_circut[x],cp_circut[y]=cp_circut[y],cp_circut[x]
    return cp_circut

def generate_neighbour(circut,swap_type):
    if swap_type == Swaptype.ARBITRARY:
       return arbitrary_swap(circut)
    else:
        return consecutive_swap(circut)

    
    
def generate_first_circut(points):
    points_num = len(points)
    route = np.random.permutation(range(points_num))
    circut = np.append(route,route[0])
    return circut

