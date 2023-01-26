from matplotlib import pyplot as plt
import random
import numpy as np

def main():
    # until user types "end"
    while True:
        # generate a random rgb value in form: [xxx, xxx, xxx]
        rgb = generate_rgb()
        # create an axes with the facecolor of the rgb value generated
        plot_clr(rgb)
        
        label = input(f"Colour label: {rgb} ")
        
        # check if user wants to end the program
        if label == "end":
            break
        # if not then write the users input to the dataset
        else:
            write_to_dataset(rgb,label)

# generates three random integers in range 255 and appends them to a 
# list which is returned   
def generate_rgb():
    rgb = []
    for i in range(3):
        rgb.append(random.randint(0,255))
    return rgb

# converts rgb values from form 0-255 --> 0-1
def normalise_rgb(rgb):
    clist = np.array(rgb)
    clist_max = max(clist)
    return clist / clist_max

# create an axes with the facecolor of the rgb value generated
def plot_clr(rgb):
    plt.plot([0,1],[0,1])
    ax = plt.axes()
    ax.set_facecolor(normalise_rgb(rgb))
    plt.show(block=False) 

# write a new line to "dataset.csv" containing values for:
# red, green, blue, rgb, label  
def write_to_dataset(rgb, label):
    with open("dataset.csv","a") as clrs:
        formatted_str = f"{rgb[0]},{rgb[1]},{rgb[2]},{rgb[0]} {rgb[1]} {rgb[2]},{label}".strip()
        clrs.write(formatted_str + "\n")

if __name__ == "__main__":
    main()