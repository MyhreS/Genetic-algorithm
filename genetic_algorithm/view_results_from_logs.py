import matplotlib.pyplot as plt
import numpy as np

"""
Loads data from a file and plots in in graphs. Manual filename,label, title and color input. 
"""

def load_data(filename):
    with open(filename, "r") as f:
        data = [eval(line) for line in f]

        # To numpy arrays.
        data_numpy = []
        for array in data:
            data_numpy.append(np.array(array))
        return data_numpy

def plot_graphs(data):
    plt.plot(range(len(data[0])), data[0], color="red", label="High mutation rate")
    plt.plot(range(len(data[1])), data[1], color="blue", label="Low mutation rate")
    plt.plot(range(len(data[2])), data[2], color="green", label="Middle mutation rate")

    plt.title("Best fitness: 100 generations, 100 bit length")

    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.legend()
    plt.show()


best = load_data("logs/best.txt")
plot_graphs(best)














"""
# Load the data from best.txt file and plot each line as a graph.
with open("logs/best.txt", "r") as f:
    for line in f:
        line = line.strip()
        # Remove the brackets and split the string into a list.
        line = line[1:-1]
        line = line.split(",")
        line = [float(i) for i in line]
        plt.plot(line)
        plt.title("Best fitness")
        plt.xlabel("Generation")
        plt.ylabel("Fitness")
        plt.show()
"""