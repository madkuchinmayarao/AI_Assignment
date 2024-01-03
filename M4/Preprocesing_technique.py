import cv2
import matplotlib.pyplot as plt

# Function to resize an image
def resize_image(image, new_size):
    resized_image = cv2.resize(image, new_size)
    return resized_image

# Function to convert an image to grayscale
def convert_to_grayscale(image):
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return grayscale_image

# Read an example image
image_path = "M4/AIML_4MT20AI017_M CHINMAYA RAO.JPG"
original_image = cv2.imread(image_path)

# Display the original image
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")

# Resize the image to (150, 150)
resized_image = resize_image(original_image, (150, 150))
plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
plt.title("Resized Image")

# Convert the image to grayscale
grayscale_image = convert_to_grayscale(original_image)
plt.subplot(1, 3, 3)
plt.imshow(grayscale_image, cmap="gray")
plt.title("Grayscale Image")

plt.show()


# EXPLANATION

# 1.Resizing:
#   The resize_image function uses OpenCV's resize function to resize the image to a new size specified by the new_size parameter.

# 2.Grayscale Conversion:
#   The convert_to_grayscale function uses OpenCV's cvtColor function to convert the color image to grayscale. The cv2.COLOR_BGR2GRAY flag indicates the color conversion.