from visualisation.utilities import load_data
from pathlib import Path
import os


if __name__ == "__main__":
    while True:
        filename = None
        try:
            filename = input("\nEnter a filename for visualisation:\n")
            model_data, model = load_data(filename)
            file_path = Path(__file__).parent.joinpath(
                "data", filename.split("_")[0] + "_data", filename + ".npz"
            )
            break
        except:
            print(
                "Filename does not exist, is incorrect, or the file does not work. "
                + "Please try again"
            )
        finally:
            if filename == None:
                raise SystemExit

    file_size = os.path.getsize(file_path) / 1024**2  # In megabytes

    if model != "ising":
        vortices = model_data[1]
        # print calculated vortices for models
        data = model_data[0]
    params = data["params"]

    print("\nParameters: ")
    for param, value in params.items():
        print(f"{param}: {value}")

    print("\nNumber of frames: ")
    print(len(data["data"]))

    print("\nDate saved (YYYY_MM_DD): ")
    print(filename[-26:-16])

    print("\nTime saved: ")
    print(filename[-16:-7])

    print("\nFile size: ")
    print(f"{file_size:.2f} MB")
