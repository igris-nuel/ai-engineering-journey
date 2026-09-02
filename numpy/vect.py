import numpy as np
import matplotlib.pyplot as plt

def plot_vectors(list_v, list_label, list_color):
    _, ax = plt.subplots(figsize=(10, 10))
    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)
    
    # Corrected range boundaries to include +10
    ax.set_xticks(np.arange(-10, 11))
    ax.set_yticks(np.arange(-10, 11))
    
    # Fixed syntax error in the axis limits
    plt.axis([-10, 10, -10, 10])
    
    for i, v in enumerate(list_v):
        # Flatten the vector to 1D for easier handling
        v_flat = v.flatten()
        
        # Fixed sign notation logic for text offsetting
        sgn = 0.4 * np.sign(v_flat)
        
        # Quiver needs starting points (0,0) to plot vectors from the origin
        plt.quiver(0, 0, v_flat[0], v_flat[1], angles='xy', scale_units='xy', scale=1, color=list_color[i])
        
        # Placed text at the tip of the vector arrow
        ax.text(v_flat[0] + sgn[0], v_flat[1] + sgn[1], list_label[i], fontsize=14, color=list_color[i])
        
    plt.grid()
    plt.gca().set_aspect("equal")
    plt.show()

# --- Execution ---

# 1. Single Vector
v = np.array([[1],[3]])
# plot_vectors([v], [f"$v$"], ["black"])

# 2. Vector Addition
w = np.array([[4],[-1]])
plot_vectors([v, w, v + w], [f"$v$", f"$w$", f"$v + w$"], ["black", "black", "red"])

print("Norm of a vector v is", np.linalg.norm(v))