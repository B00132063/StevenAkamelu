import numpy as np  

# What this file does
# Implements morphological operations like dilation and erosion, which are used to clean up the binary image by

 # Function to perform dilation on a binary image
def dilate(binary):                    

    # Get the number of rows and columns in the image
    rows, cols = binary.shape 

    # Create a new empty image with the same size as the input          
    output = np.zeros_like(binary)      

    # Loop through every row of the image
    for r in range(rows):   
        # Loop through every column of the image           
        for c in range(cols):          

            value = 0                   

            # Check neighbouring rows around the pixel
            for dr in [-1, 0, 1]:      
                # Check neighbouring columns around the pixel
                for dc in [-1, 0, 1]:   

                    # Calculates the row index of the neighbour pixel
                    rr = r + dr        
                    # Calculates the column index of the neighbour pixel 
                    cc = c + dc        

                    # Check that the neighbour is still inside the image
                    if 0 <= rr < rows and 0 <= cc < cols:

                        # If any neighbour pixel is foreground (1)
                        if binary[rr, cc] == 1:

                            # Sets the output pixel to foreground
                            value = 1  

            # Stores the new value in the output image
            output[r, c] = value      

    # Returns the dilated image
    return output                      


# Function to perform erosion on a binary image
def erode(binary):                    

    rows, cols = binary.shape           # Get image size
    output = np.zeros_like(binary)      # Create a new empty image

    for r in range(rows):               # Loop through every row
        for c in range(cols):           # Loop through every column

            value = 1                   # Start by assuming the pixel will stay foreground

            for dr in [-1, 0, 1]:       # Check neighbouring rows
                for dc in [-1, 0, 1]:   # Check neighbouring columns

                    rr = r + dr         # Neighbour row position
                    cc = c + dc         # Neighbour column position

                    # If neighbour goes outside the image
                    if rr < 0 or rr >= rows or cc < 0 or cc >= cols:
                        value = 0       # Set pixel to background

                    # If neighbour is background
                    elif binary[rr, cc] == 0:
                        # Set pixel to background
                        value = 0      

            # Store the result pixel in output image
            output[r, c] = value       

    # Return the eroded image
    return output                       

# Function to perform closing operation
def closing(binary, iterations=1):    

    # Make a copy of the original binary image
    result = binary.copy()              

    # Repeat dilation the number of times specified
    for _ in range(iterations):        

        # Apply dilation to expand foreground pixels
        result = dilate(result)        

    # Repeat erosion the number of times specified
    for _ in range(iterations): 

         # Apply erosion to shrink the region back  
        result = erode(result)         

    # Return the cleaned binary image
    return result                      