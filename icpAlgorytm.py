import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import KDTree
#import open3d as o3d
import time



def createBoxPoints():

    """
    generates points on the surface of a three-dimensional box
    """

    points = []
    for x in np.linspace(0, 1, 10):
        for y in np.linspace(0, 1, 10):
            points.append([x, y, 0])
            points.append([x, y, 1])
            points.append([0, x, y])
            points.append([1, x, y])
            points.append([x, 0, y])
            points.append([x, 1, y])

    return np.unique(points, axis=0)

#def createShape():

