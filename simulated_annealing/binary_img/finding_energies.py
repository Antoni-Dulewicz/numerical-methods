from energytype import Energytype


def find_energy(img,energy_type):
    height, width = img.shape 
    energy = 0

    if energy_type == Energytype.FOUR:
        for i in range(height):
            for j in range(width):
                current_color = img[i][j]
                """ if img[i][j] == current_color: """    
                for x,y in [(0,1),(1,0),(-1,0),(0,-1)]:
                    if i+x >= 0 and i+x < height and j+y >= 0 and j+y < width:
                        energy += 1 if img[i+x][j+y] != current_color else 0
                
                for x,y in [(-1,-1),(1,1),(-1,1),(1,-1)]:
                    if i+x >= 0 and i+x < height and j+y >= 0 and j+y < width:
                        energy += 1 if img[i+x][j+y] == current_color else 0
                

    elif energy_type == Energytype.EIGHT:
        for i in range(height):
            for j in range(width):
                current_color = img[i][j]
                """ current_color = 1
                if img[i][j] == current_color: """
                for x,y in [(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]:
                    if i+x >= 0 and i+x < height and j+y >= 0 and j+y < width:
                        energy += 1 if img[i+x][j+y] != current_color else 0
    elif energy_type == Energytype.CORNERS:
        for i in range(height):
            for j in range(width):
                
                current_color = 1
                if img[i][j] == current_color:

                    for x,y in [(-1,-1),(1,1)]:
                        if i+x >= 0 and i+x < height and j+y >= 0 and j+y < width:
                            energy += 1 if img[i+x][j+y] != current_color else 0
                    
                    for x,y in [(-1,1),(1,-1)]:
                        if i+x >= 0 and i+x < height and j+y >= 0 and j+y < width:
                            energy += 1 if img[i+x][j+y] == current_color else 0
    else:
        for i in range(height):
            for j in range(width):
                
                current_color = 1
                if img[i][j] == current_color:

                    for x,y in [(-1,-1),(1,1),(-1,1),(1,-1)]:
                        if i+x >= 0 and i+x < height and j+y >= 0 and j+y < width:
                            energy += 1 if img[i+x][j+y] != current_color else 0
                            
                    for x,y in [(0,1),(1,0),(-1,0),(0,-1)]:
                        if i+x >= 0 and i+x < height and j+y >= 0 and j+y < width:
                            energy += 1 if img[i+x][j+y] == current_color else 0

    
    return energy


