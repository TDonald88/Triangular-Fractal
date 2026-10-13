
import numpy as np
import matplotlib.pyplot as plt

print("aight")

AnkersX = np.array([0, 5, 2.5])  # X coordinates of the triangle's vertices
AnkersY = np.array([0, 0, 4.33])  # Y coordinates of the triangle's vertices

plt.plot(AnkersX, AnkersY, 'bo', markersize = 0.5)  # Plot the triangle
plt.show()






