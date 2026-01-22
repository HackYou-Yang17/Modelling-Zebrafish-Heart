import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib import ticker


def animate_ising(model_data, model="", frame_skip=0, interval=50):
    data = model_data['data'][::frame_skip] if frame_skip != 0 else model_data['data']
    params = model_data['params']
    fig, ax = plt.subplots()

    if model == "ising":
        im = ax.imshow(data[0], cmap='RdYlBu', vmin=-1, vmax=1)
        plt.colorbar(im, label='Spin', ticks=[-1, 1])
    else:
        def pi_formatter(i, pos):
            value = np.round(i / np.pi, 4)  # multiple of π
            if value == 0:
                return "0"
            elif value == 1:
                return r"$\pi$"
            else:
                return rf"${value}\pi$"

        im = ax.imshow(data[0], cmap='hsv', vmin=0, vmax=2*np.pi)
        cbar = plt.colorbar(im, label='Angle', ticks=[0, np.pi, 2*np.pi])
        cbar.ax.yaxis.set_major_formatter(ticker.FuncFormatter(pi_formatter))

    def update(frame):
        im.set_array(data[frame])
        ax.set_title(f"{model.capitalize()} Model, L = {params['size']}, T = {params['T']:.2f}")
        return im,
    
    ani = FuncAnimation(fig, update, frames=len(data), 
                       interval=interval, blit=True)
    plt.show()
    return ani

