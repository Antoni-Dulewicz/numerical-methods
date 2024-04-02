import matplotlib.pyplot as plt
import imageio.v2 as imageio
import os
import io

def clear_output_folder(output_folder):
    if os.path.exists(output_folder):
        for file_name in os.listdir(output_folder):
            os.remove(os.path.join(output_folder,file_name))
    else:
        os.mkdir(output_folder)


def add_image_to_gif(best_route,points,images):
    best_points = points[best_route]
    plt.plot(best_points[:,0], best_points[:,1], 'limegreen')
    plt.scatter(best_points[:,0], best_points[:,1], color='purple')
    plt.title('Best path found by simulated annealing algorithm')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.gca().set_facecolor('white')
    img = io.BytesIO()
    plt.savefig(img,format='png')
    img.seek(0)
    images.append(imageio.imread(img))
    plt.close()    

def plot_energy_function(output_folder,energies):
    plt.plot(energies, color = 'goldenrod')
    plt.title('Energy characteristic function')
    plt.xlabel('Number of iterations')
    plt.ylabel('Energy')
    plt.savefig(os.path.join(output_folder,'energy_plot.png'))
    plt.close()

def plot_temp_function(output_folder,temparatures):
    plt.plot(temparatures, color ='orangered')
    plt.title('Temp. function')
    plt.xlabel('Number of iterations')
    plt.ylabel('Temparature')
    plt.savefig(os.path.join(output_folder,'temparature_plot.png'))
    plt.close()

def create_graph_png(output_folder,best_route,points):

    best_points = points[best_route]
    plt.plot(best_points[:, 0], best_points[:, 1], 'limegreen')
    plt.scatter(best_points[:, 0], best_points[:, 1], color='purple')
    plt.title('Best path found by simulated annealing algorithm')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.savefig(os.path.join(output_folder,'graph_output.png'))
    plt.close()

def make_gif(output_folder,images):
    imageio.mimsave(os.path.join(output_folder,'gif_output.gif'), images, duration=2.0)