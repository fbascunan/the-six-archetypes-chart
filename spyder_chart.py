# This script generates a spyder chart based on information taken from the book "The Archetype Effect" by James Root.

import matplotlib.pyplot as plt
import numpy as np

def create_spyder_chart(data, labels, title):
    """
    Creates a spyder chart.

    Args:
        data (list): A list of numerical values for each category.
        labels (list): A list of strings representing the labels for each category.
        title (str): The title of the chart.
    """
    num_vars = len(labels)

    # Compute angle for each axis
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # The plot is made circular, so we need to complete the loop
    data += data[:1]
    angles += angles[:1]

    # Initialize the spyder plot
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    # Draw one axe per variable + add labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([10, 20, 30, 40, 50], ["10", "20", "30", "40", "50"], color="grey", size=7)
    plt.ylim(0, 50)

    # Plot data
    ax.plot(angles, data, linewidth=1, linestyle='solid', label="Archetype Profile")

    # Fill area
    ax.fill(angles, data, 'b', alpha=0.1)

    # Add a title
    plt.title(title, size=11, color='blue', y=1.1)

    # Save the plot to a file
    plt.savefig("spyder_chart.png")
    print("Spyder chart saved to spyder_chart.png")

if __name__ == '__main__':
    # Example Data (replace with actual data from the book)
    archetype_labels = [
        "Innocent", "Orphan", "Warrior", "Caregiver", 
        "Seeker", "Lover", "Destroyer", "Creator", 
        "Ruler", "Magician", "Sage", "Jester"
    ]
    # These are placeholder values.
    archetype_values = [30, 25, 40, 35, 20, 45, 10, 50, 25, 30, 40, 15] 

    chart_title = "My Archetype Profile"

    create_spyder_chart(archetype_values, archetype_labels, chart_title)
