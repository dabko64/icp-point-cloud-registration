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



def transformPointCloud(points, R, t):
    return np.dot(points, R.T) + t


def addNoise(points, noise_level=0.02):
    """gaussian noise as a simulation"""
    noise = np.random.normal(0, noise_level, points.shape)
    return points + noise



def nearestNeighbors(source, target):
    """
    finds the nearest target point for every source point
    """

    tree = KDTree(source)
    dist, ind = tree.query(target)

    return dist, ind


def bestFitTransform(source, target):
    centroid_source = np.mean(source, axis=0)
    centroid_target = np.mean(target, axis=0)

    source_centered = source - centroid_source
    target_centered = target - centroid_target

    covariance_matrix = source_centered.T @ target_centered

    U, _, Vt = np.linalg.svd(covariance_matrix)

    rotation_matrix = Vt.T @ U.T

    if np.linalg.det(rotation_matrix) < 0:
        Vt[-1, :] *= -1
        rotation_matrix = Vt.T @ U.T

        translation_vector = centroid_target - rotation_matrix @ centroid_source

        return rotation_matrix, translation_vector


#def paintClouds(source, target, title="point cloud visualization"):