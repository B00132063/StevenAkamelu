import numpy as np

# What this file does
# Computes the histogram of pixel intensity values in the image, which is used for Otsu

def compute_histogram(image):
    # Computing histogram with 256 bins for pixel intensity values
    histogram = np.zeros(256)
    
    # Iterate through each pixel in the image and update the histogram
    for row in image:
        for pixel in row:
            histogram[pixel] += 1
        
    return histogram

