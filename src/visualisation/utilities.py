from pathlib import Path
import sys
import numpy as np


def load_data(filename=None):
    model = filename.split("_")[0]

    if filename == None:
        sys.exit("No filename entered. Exiting...")
    file_path = Path(__file__).parent.parent.joinpath(
        "data", f"{model + "_data"}", filename + ".npz"
    )
    file = np.load(file_path, allow_pickle=True)
    model_data = give_data(file, model)
    return model_data, model


def give_data(file, model):
    model_data = {
        "data": file["data_history"],
        "energy": file["energy_history"],
        "magnetisation": file["mag_history"],
        "params": file["params"].item(),
    }

    if model != "ising":
        vortices = calculate_vortices(model_data)
        return model_data, vortices
    return model_data


def calculate_vortices(model_data):
    pass
