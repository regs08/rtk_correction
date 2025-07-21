
import matplotlib.pyplot as plt

def plot_before_after(original_coords, corrected_coords):
    plt.figure(figsize=(10, 6))
    plt.scatter(
        [p[0] for p in original_coords],
        [p[1] for p in original_coords],
        label='Original',
        c='red',
        s=10
    )
    plt.scatter(
        [p[0] for p in corrected_coords],
        [p[1] for p in corrected_coords],
        label='Corrected',
        c='green',
        s=10
    )
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Before and After GPS Correction")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("output/before_after_plot.png")
    plt.close()
