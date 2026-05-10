import numpy as np


def generateCubePoints(n_points=1000, size=1.0, noise=0.0):

    points = np.random.uniform(-size, size, (n_points, 3))

    if noise > 0:
        points += np.random.normal(0, noise, points.shape)

    return points

