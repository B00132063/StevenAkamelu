# Main file for the O-ring inspection project
# This file loads the images, calls the functions from the other files to process the images,
import os
import time
import cv2 as cv

# Imports the functions from the other files
from histogram import compute_histogram
from threshold import otsu_threshold, apply_threshold
from morphology import closing
from connected_components import connected_components, extract_largest_region
from analysis import classify_oring


def process_image(image_path, output_path):

    # Starts the timer before processing begins
    start_time = time.time()

    # Loads the image in grayscale
    image = cv.imread(image_path, 0)

    # Checks if the image was loaded correctly
    if image is None:
        print("Error: Image not found ->", image_path)
        return

    # Computes the histogram of the grayscale image
    hist = compute_histogram(image)

    # Finds the threshold using Otsu's method
    threshold = otsu_threshold(hist, image.shape[0] * image.shape[1])

    # Applies thresholding to create a binary image
    binary = apply_threshold(image, threshold)

    # Applies morphology to clean the binary image
    cleaned = closing(binary)

    # Labels all connected foreground regions
    labels, region_sizes = connected_components(cleaned)

    # Extracts the largest connected region
    oring = extract_largest_region(labels, region_sizes)

    # Classifies the O-ring as PASS or FAIL
    result, features = classify_oring(oring)

    # Stops the timer after processing is complete
    end_time = time.time()

    # Calculates total processing time
    processing_time = end_time - start_time

    # Converts grayscale image to BGR so coloured text can be added
    output_image = cv.cvtColor(image, cv.COLOR_GRAY2BGR)

    # Adds the PASS or FAIL result to the image
    cv.putText(output_image, "Result: " + result, (10, 25),
               cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Adds the threshold value to the image
    cv.putText(output_image, "Threshold: " + str(threshold), (10, 50),
               cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    # Adds the processing time to the image
    cv.putText(output_image, "Time: " + str(round(processing_time, 4)) + " s", (10, 75),
               cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 150, 0), 2)

    # Adds the hole area to the image
    cv.putText(output_image, "Hole area: " + str(features["hole_area"]), (10, 100),
               cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 150, 150), 1)

    # Adds the aspect ratio to the image
    cv.putText(output_image, "Aspect ratio: " + str(round(features["aspect_ratio"], 3)), (10, 120),
               cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 150, 150), 1)

    # Saves the final output image
    cv.imwrite(output_path, output_image)

    # Prints useful information in the terminal
    print("Image:", image_path)
    print("Threshold =", threshold)
    print("Regions found =", region_sizes)
    print("Result =", result)
    print("Features =", features)
    print("Processing time =", round(processing_time, 4), "seconds")
    print("----------------------------------------")


def main():

    # Creates an output folder if it does not already exist
    os.makedirs("outputs", exist_ok=True)

    # Loops through all 15 O-ring images
    for i in range(1, 16):

        # Creates the input image path
        image_path = f"images/Oring{i}.jpg"

        # Creates the output image path
        output_path = f"outputs/result_Oring{i}.jpg"

        # Processes the image
        process_image(image_path, output_path)


if __name__ == "__main__":
    main()