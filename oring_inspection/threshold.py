import numpy as np

# What this file does
# Computes the histogram of pixel intensity values in the image, which is used for Otsu

def otsu_threshold(histogram, total_pixels):

    # Calculates the total sum of pixel intensity values
    sum_total = 0
    for t in range(256):
        sum_total += t * histogram[t]

    sum_background = 0
    weight_background = 0
    max_variance = 0
    threshold = 0

    # Goes through all possible threshold values to find the one that maximizes the between-class variance
    for t in range(256):

        # Updates background weight and sum
        weight_background += histogram[t]

        # If background weight is zero, skip to next threshold
        if weight_background == 0:
            continue
        
        # Calculates foreground weight
        weight_foreground = total_pixels - weight_background

        # If foreground weight is zero, break the loop as we have processed all pixels
        if weight_foreground == 0:
            break

        # Updates background sum
        sum_background += t * histogram[t]

        # Calculates mean intensity for background and foreground
        mean_background = sum_background / weight_background

        # Calculates mean intensity for foreground
        mean_foreground = (sum_total - sum_background) / weight_foreground

        # Calculates between-class variance
        variance_between = weight_background * weight_foreground * (mean_background - mean_foreground) ** 2
        
        # Updates maximum variance and corresponding threshold
        if variance_between > max_variance:
            max_variance = variance_between
            threshold = t

    return threshold
 
   # Applies the given threshold to the image to create a binary image
def apply_threshold(image, threshold):
      
       # Initialises binary image with zeros
    binary = np.zeros_like(image, dtype=np.uint8)

     # Gets the number of rows and columns in the image
    rows, cols = image.shape

        # Applies threshold to each pixel in the image
    for r in range(rows):
        for c in range(cols):

            if image[r, c] < threshold:
                binary[r, c] = 1
            else:
                binary[r, c] = 0

    return binary