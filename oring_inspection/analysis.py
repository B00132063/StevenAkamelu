import numpy as np

# What this file does 
# Counts how mnay white pixels are in the region, finds the bounding box, fills holes, and classifies the O-ring as PASS or FAIL based on these features.


# Counts the number of foreground pixels in the region
def region_area(region):

    # Adds up all the white pixels in the binary region
    area = np.sum(region)

    return area


# Finds the bounding box of the region
def bounding_box(region):

    # Gets the positions of all white pixels
    rows, cols = np.where(region == 1)

    # If no white pixels are found, return zeros
    if len(rows) == 0 or len(cols) == 0:
        return 0, 0, 0, 0

    # Finds the smallest and largest row values
    min_row = np.min(rows)
    max_row = np.max(rows)

    # Finds the smallest and largest column values
    min_col = np.min(cols)
    max_col = np.max(cols)

    return min_row, min_col, max_row, max_col


# Fills holes inside the binary region
def fill_holes(region):

    # Gets the number of rows and columns in the image
    rows, cols = region.shape

    # Creates a copy of the region
    filled = region.copy()

    # Creates the inverse image
    inverse = 1 - region

    # Creates a visited image filled with zeros
    visited = np.zeros_like(region, dtype=np.uint8)

    # Creates a stack for flood fill
    stack = []

    # Adds all border pixels that belong to the background
    for r in range(rows):
        if inverse[r, 0] == 1:
            stack.append((r, 0))
        if inverse[r, cols - 1] == 1:
            stack.append((r, cols - 1))

    # Adds top and bottom border pixels that belong to the background
    for c in range(cols):
        if inverse[0, c] == 1:
            stack.append((0, c))
        if inverse[rows - 1, c] == 1:
            stack.append((rows - 1, c))

    # Marks all background pixels connected to the border
    while stack:

        # Takes one pixel from the stack
        r, c = stack.pop()

        # Skips the pixel if it is outside the image
        if r < 0 or r >= rows or c < 0 or c >= cols:
            continue

        # Skips the pixel if it was already visited
        if visited[r, c] == 1:
            continue

        # Skips the pixel if it is not background in the inverse image
        if inverse[r, c] == 0:
            continue

        # Marks the pixel as visited
        visited[r, c] = 1

        # Adds 4-connected neighbours
        stack.append((r + 1, c))
        stack.append((r - 1, c))
        stack.append((r, c + 1))
        stack.append((r, c - 1))

    # Any background pixel not visited is a hole
    for r in range(rows):
        for c in range(cols):
            if inverse[r, c] == 1 and visited[r, c] == 0:
                filled[r, c] = 1

    return filled


# Measures the size of the hole inside the O-ring
def hole_area(region):

    # Fills the hole inside the region
    filled = fill_holes(region)

    # Calculates the number of pixels added by filling
    hole_pixels = np.sum(filled) - np.sum(region)

    return hole_pixels


# Classifies the O-ring as PASS or FAIL
def classify_oring(region):

    # Calculates the area of the O-ring region
    area = region_area(region)

    # Finds the bounding box
    min_row, min_col, max_row, max_col = bounding_box(region)

    # Calculates width and height of bounding box
    width = max_col - min_col + 1
    height = max_row - min_row + 1

    # Avoids division by zero
    if height == 0:
        aspect_ratio = 0
    else:
        aspect_ratio = width / height

    # Measures the hole area
    hole = hole_area(region)

    # Starts by assuming the O-ring passes
    result = "PASS"

    # If there is almost no hole, the ring may be broken
    if hole < 200:
        result = "FAIL"

    # If the shape is too stretched, it may be defective
    if aspect_ratio < 0.8 or aspect_ratio > 1.2:
        result = "FAIL"

    # Stores useful values for printing and debugging
    features = {
        "area": int(area),
        "hole_area": int(hole),
        "aspect_ratio": float(aspect_ratio),
        "bounding_box": (int(min_row), int(min_col), int(max_row), int(max_col))
    }

    return result, features