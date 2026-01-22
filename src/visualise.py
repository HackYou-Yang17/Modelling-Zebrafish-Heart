import visualisation.animate as ani
import visualisation.graph as plot
from visualisation.utilities import load_data


if __name__ == "__main__":
    while True:
        filename = None
        try:
            filename = input("\nEnter a filename for visualisation:\n")
            data, model = load_data(filename)
            break
        except:
            print("Filename does not exist, is incorrect, or the file does not work. " +\
                  "Please try again")
        finally:
            if filename == None:
                raise SystemExit

    if model != "ising":
        vortices = data[1]
        data = data[0]
    if ani.animate_ising(data, model):
        print("Animation complete")
    if plot.plot_properties(data, model):
        print("Plot complete")
