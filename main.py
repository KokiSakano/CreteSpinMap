import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

from module import GenerateSpinState

# save path
# train test data
npy_path = "./result//"
# spin map
spin_map_path = "./result/"


# lattice size
N = 32

# number of data (square lattice)
count = 100

# tempreturelist
T_list = np.linspace(0.1, 5.5, count)

# make gif which write spin state trainsition
def create_spinmap_gif(data, T, save_path):
    save_path = save_path + "squarelattice.gif"
    fig = plt.figure()

    def Plot(num):
        plt.cla()
        plt.imshow(data[num])
        plt.title("temperature:" + str(T[num]))

    anim = FuncAnimation(fig, Plot, frames=100)
    anim.save(save_path, writer='imagemagick')


# call module GSS
GSS = GenerateSpinState.GSS(N, T_list)

# create spin map
X_train = GSS.calc_each_tempreture()

# create gif
create_spinmap_gif(X_train, T_list, spin_map_path)
