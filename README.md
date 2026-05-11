# ICP Point Cloud Registration

## Contributors

This project was created by:

- [@dabko64](https://github.com/dabko64)
- [@karolinaa05](https://github.com/karolinaa05)
- [@karolinaflorek10](https://github.com/karolinaflorek10)

## Project description

This project presents a custom implementation of the Iterative Closest Point (ICP) algorithm for 3D point cloud registration.

The main goal of the project is to show how two point clouds can be aligned by estimating the transformation between them. The algorithm works iteratively by finding corresponding points, calculating the best rotation and translation, and applying the transformation until convergence.

The project also includes a comparison with the ready-to-use ICP implementation from the Open3D library.

## Main features

- Generating custom 3D point clouds
- Applying rotation and translation to a point cloud
- Finding nearest neighbours using KDTree
- Estimating transformation using SVD
- Iterative ICP algorithm
- Error analysis in each iteration
- RMSE calculation
- Visualization before and after registration
- Comparison with Open3D ICP

## Technologies

- Python
- NumPy
- SciPy
- Matplotlib
- Open3D

## Algorithm steps

1. Generate or load a source point cloud.
2. Create a transformed target point cloud.
3. Find nearest neighbours between both point clouds.
4. Estimate rotation and translation using SVD.
5. Apply the transformation to the source cloud.
6. Repeat the process until convergence.
7. Visualize and compare the results.

## Visualizations

The project includes visualizations of:

- point cloud before alignment
- point cloud after alignment
- ICP convergence
- RMSE error in each iteration
- comparison between custom ICP and Open3D ICP


## Status

Project in progress.
