import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Step 1: Load the depth image
image_path = 'test_out_depth.jpg'  # Path to the depth image
depth_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Load as grayscale

# Step 2: Normalize the depth values (optional, but useful for better visualization)
Z = depth_image.astype(np.float32)
Z = Z / 255.0  # Normalized to range between 0 and 1

# Step 3: Generate grid coordinates
height, width = Z.shape
X, Y = np.meshgrid(np.arange(width), np.arange(height))

# Step 4: Downsample for better mesh (optional)
# To speed up rendering, downsample the points if the image is too large
downsample_rate = 5  # Adjust downsample rate for performance vs. quality
X = X[::downsample_rate, ::downsample_rate]
Y = Y[::downsample_rate, ::downsample_rate]
Z = Z[::downsample_rate, ::downsample_rate]

# Step 5: Create a figure with subplots for image and 3D plot
fig = plt.figure(figsize=(16, 8))

# Left subplot: Original depth image
ax1 = fig.add_subplot(1, 2, 1)
ax1.imshow(depth_image)
ax1.set_title('Original Depth Image')
ax1.axis('off')  # Turn off axis for better visualization

# Right subplot: 3D wireframe plot
ax2 = fig.add_subplot(1, 2, 2, projection='3d')

# Step 6: Plot wireframe mesh
ax2.plot_wireframe(X, Y, Z, color='darkblue', linewidth=0.5)

# Step 7: Configure the plot for better visualization
ax2.set_title('3D Depth Wireframe Mesh')
ax2.set_xlabel('X-axis')
ax2.set_ylabel('Y-axis')
ax2.set_zlabel('Depth')

# Step 8: Show both plots
plt.tight_layout()
plt.show()
