def file_update(file_path, key, value): # Function to update a specific key in a configuration file
    # Read the original file

    with open(file_path,'r') as file: # Open the file in read mode
        lines = file.readlines() # Read all lines into a list
    # Update the specific key
    
    with open(file_path, 'w') as file: # Open the file in write mode
        for line in lines: # Iterate through each line
            if key in line: # Check if the line contains the key to be updated
                file.write(key + " = " + value + "\n") # Write the updated key-value pair
            else: # If the line does not contain the key
                file.write(line) # Write the line as it is

file_update('./server.conf', "MAX_CONNECTIONS", "1000") # Call the function to update the MAX_CONNECTIONS key in the server.conf file
