from generate_img import generate_binary_image
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


def add_image_to_gif(best_image,images):
    plt.subplot(1,1,1)
    plt.imshow(best_image, cmap='gray')
    plt.axis('off')
    plt.gca().set_facecolor('white')
    img = io.BytesIO()
    plt.savefig(img,format='png')
    img.seek(0)
    images.append(imageio.imread(img))
    plt.close()    

def make_gif(images,output_folder):
    imageio.mimsave(os.path.join(output_folder,'gif_output.gif'), images, duration=0.1)

def draw_image(image,output_folder):
    plt.subplot(1,1,1)
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.savefig(os.path.join(output_folder,'image.png'))
    plt.close()


def draw_energy(energies,output_folder):
    plt.plot(energies,color = 'goldenrod')
    plt.xlabel('Iteration')
    plt.ylabel('Energy')
    plt.title('Energy vs. Iteration')
    plt.savefig(os.path.join(output_folder,'energy_plot.png'))
    plt.close()


def draw_temperature(temperatures,output_folder):
    plt.plot(temperatures,color ='orangered')
    plt.xlabel('Iteration')
    plt.ylabel('Temperature')
    plt.title('Temperature vs. Iteration')
    plt.savefig(os.path.join(output_folder,'temp_plot.png'))
    plt.close()