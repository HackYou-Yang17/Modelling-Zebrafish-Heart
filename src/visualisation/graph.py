import matplotlib.pyplot as plt


def plot_properties(dict, model=""):
    """Plot energy and magnetization evolution."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
    
    ax1.plot(dict['energy'])
    ax1.set_ylabel('Energy')
    ax1.grid(True, alpha=0.3)

    ax2.plot(dict['magnetisation'])
    ax2.set_ylabel('Magnetization')
    ax2.set_xlabel('Saved Frame Index')
    ax2.grid(True, alpha=0.3)

    params = dict['params']
    plt.suptitle(f"{model.capitalize()} Model: L={params['size']}, T={params['T']:.2f}, "
                f"bias={params['bias']}")
    plt.tight_layout()
    plt.show()