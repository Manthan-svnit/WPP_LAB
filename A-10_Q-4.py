import numpy as np

N = int(input("Enter number of points (N >= 10): "))  
if N < 10:
    raise ValueError("N must be at least 10.")

cartesian_points = np.random.uniform(-10, 10, (N, 2))  # Generate (x, y) pairs

x, y = cartesian_points[:, 0], cartesian_points[:, 1]
r = np.sqrt(x**2 + y**2)  # Compute radius
theta = np.arctan2(y, x)  # Compute angle (radians)

polar_points = np.column_stack((r, theta))  # Combine into Nx2 array

print("\nCartesian Coordinates:\n", cartesian_points)
print("\nPolar Coordinates (r, θ in radians):\n", polar_points)
