import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import KDTree
#import open3d as o3d
import time



def createBoxPoints():
    boxPoints = []
    """Generowanie pudełka trzywymiarowego (próba)"""
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



def transformPointCloud(points, R, t):
    return np.dot(points, R.T) + t


def addNoise(points, noise_level=0.02):
    """ Szum Gaussa jako symulacja """
    noise = np.random.normal(0, noise_level, points.shape)



def paintClouds(source, target, title="Wizualizacja chmur punktów"):
    """ Wizualizacja chmury punktów"""



#def runICP(...):





def main():






if __name__ == "__main__":
    main()