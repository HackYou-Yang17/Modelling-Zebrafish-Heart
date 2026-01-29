from modelling.ising_model import Ising_Model
from modelling.xy_model import Xy_Model
from modelling.symmetric_models import Nematic_Model
from modelling.symmetric_models import Quartic_Model
from modelling.quadratic_model import Quadratic_Model
import pyglet as pig


def load_model():
    return True


def draw_actin():
    return True


def run_movie():
    return True


if __name__ == "__main__":#
    if load_model():
        print("Model has been loaded")
    if draw_actin():
        print("Actin has been drawn")
    if run_movie():
        pass

# Generate the model as an interactive visualisation