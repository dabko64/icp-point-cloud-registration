import numpy as np
from shapes import generateCubePoints
from shapes import generateSpherePoints
from shapes import generateRubberDuckPoints


cube = generateCubePoints(n_points=1000, size=1.0, noise=0.01)
sphere = generateSpherePoints(n_points=1000, radius=1.0, noise=0.01)
duck = generateRubberDuckPoints(n_points=4000, noise=0.01)

print("Cube:", cube.shape)
print("Sphere:", sphere.shape)
print("Duck:", duck.shape)
print(duck[:5])