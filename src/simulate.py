from modelling.ising_model import Ising_Model
from modelling.xy_model import Xy_Model
from modelling.symmetric_models import Nematic_Model
from modelling.symmetric_models import Quartic_Model
from modelling.quadratic_model import Quadratic_Model


def run_model(params, model_name, model):
    if model_name == "ising":
        params.__delitem__("S")
    curr_mdl = model(**params)
    curr_mdl.run(steps=100000, save_every=625)  # save_every = L**2
    curr_mdl.save_data(params, model_name + "_data")


if __name__ == "__main__":
    params = {
        "size": 25,
        "T": 2.0,  # Temperature
        "J": 1.0,  # Coupling strength
        "bias": 0.7,  # For asymmetric proposal
        "S": 0.3,  # Gaussian width
    }

    models = {
        "ising": Ising_Model,
        "xy": Xy_Model,
        "nematic": Nematic_Model,
        "quartic": Quartic_Model,
        "quadratic": Quadratic_Model,
    }

    while True:
        m_name = None
        try:
            m_name = input("\nEnter model:\n").lower()
            model = models[m_name]
            break
        except KeyError as e:
            print(f"{e}. Model does not exist, please try again")
        finally:
            if m_name == None:
                raise SystemExit

    run_model(params, m_name, model)
