import numpy as np

# What this file does 
# Finds all connected regions in the binary image and extracts the largest one, which should correspond to the O-ring.

# Finds all connected regions in the binary image
def connected_components(binary):

    # Gets the number of rows and columns in the image
    rows, cols = binary.shape

    # Creates a label image filled with zeros
    labels = np.zeros_like(binary, dtype=np.int32)

    # Starts the first region label at 1
    current_label = 1

    # Creates a dictionary to store region sizes
    region_sizes = {}

    # Loops through every pixel in the image
    for r in range(rows):
        for c in range(cols):

            # Checks if the pixel is foreground and not labeled yet
            if binary[r, c] == 1 and labels[r, c] == 0:

                # Creates a stack and puts the starting pixel into it
                stack = [(r, c)]

                # Starts counting the size of this region
                region_size = 0

                # Keeps going until there are no more connected pixels to check
                while stack:

                    # Takes one pixel from the stack
                    rr, cc = stack.pop()

                    # Skips the pixel if it is outside the image
                    if rr < 0 or rr >= rows or cc < 0 or cc >= cols:
                        continue

                    # Skips the pixel if it is background
                    if binary[rr, cc] == 0:
                        continue

                    # Skips the pixel if it is already labeled
                    if labels[rr, cc] != 0:
                        continue

                    # Gives the pixel the current region label
                    labels[rr, cc] = current_label

                    # Increases the size of the current region
                    region_size += 1

                    # Adds the 4 neighbouring pixels to the stack
                    stack.append((rr + 1, cc))
                    stack.append((rr - 1, cc))
                    stack.append((rr, cc + 1))
                    stack.append((rr, cc - 1))

                # Stores the size of the current region
                region_sizes[current_label] = region_size

                # Moves to the next label number
                current_label += 1

    return labels, region_sizes


# Extracts the largest connected region from the label image
def extract_largest_region(labels, region_sizes):

    # If no regions were found, return an empty image
    if len(region_sizes) == 0:
        return np.zeros_like(labels, dtype=np.uint8)

    # Finds the label number of the largest region
    largest_label = max(region_sizes, key=region_sizes.get)

    # Creates a blank binary image for the output region
    largest_region = np.zeros_like(labels, dtype=np.uint8)

    # Gets the number of rows and columns
    rows, cols = labels.shape

    # Loops through every pixel
    for r in range(rows):
        for c in range(cols):

            # Checks if the pixel belongs to the largest region
            if labels[r, c] == largest_label:

                # Sets that pixel to foreground
                largest_region[r, c] = 1

    return largest_region