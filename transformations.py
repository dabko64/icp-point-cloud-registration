import numpy as np

def rotation_matrix_x(angle_deg):
    angle = np.radians(angle_deg)

    return np.array([
        [1, 0, 0],
        [0, np.cos(angle), -np.sin(angle)],
        [0, np.sin(angle),  np.cos(angle)]
    ])


def rotation_matrix_y(angle_deg):
    angle = np.radians(angle_deg)

    return np.array([
        [np.cos(angle), 0, np.sin(angle)],
        [0, 1, 0],
        [-np.sin(angle), 0, np.cos(angle)]
    ])