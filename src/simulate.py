from modelling.ising_model import Ising_Model
from modelling.xy_model import Xy_Model
from modelling.nematic_model import Nematic_Model
from modelling.quartic_model import Quartic_Model


def run_model(params, model_name, model):
    if model_name == "ising":
        params.__delitem__("S")
    elif model_name == "quartic":
        params['J4'] == 1
    curr_mdl = model(**params)
    curr_mdl.run(steps=100000, save_every=2500) # save_every = L**2
    curr_mdl.save_data(params, model_name + "_data")


if __name__ == "__main__":
    params = {
        'size': 50,
        'T': 2.0,   # Temperature
        'J': 1.0,   # Coupling strength
        'bias': 0.7,
        'S': 0.3, # G-width
        }

    models = {
        'ising': Ising_Model,
        'xy': Xy_Model,
        'nematic': Nematic_Model,
        'quartic': Quartic_Model,
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
