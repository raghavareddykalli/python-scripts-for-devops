import os # This import is necessary to use os.listdir

def main(): # Main function to execute the script
    # Prompt user for a list of folders
    folders_list = input("Enter the list of folders with space in between: ").split() # Split input into a list
    # Iterate through each folder in the list
    for folder in folders_list: # Get each folder from the list
        # Call the function to list files in the folder
        files, error = list_of_files_in_folder(folder)
        if files: # If files are found, print them
            print(f"Files in '{folder}': {files}")
            for file in files: # Iterate through each file in the folder
                print(file) # Print each file name
        else: # If there is an error, print the error message
            print(f"Error in '{folder}': {error}")


def list_of_files_in_folder(folder): # Function to list files in a given folder
    # Try to list files in the specified folder
    try:
        files = os.listdir(folder)
        return files,None # Return the list of files and no error
    # Handle exceptions if the folder does not exist or permission is denied
    except FileNotFoundError:
        return None, "Folder not found" # Return None and an error message if folder not found
    except PermissionError:
        return None, "Permission denied" # Return None and an error message if permission is denied


if __name__ == "__main__": # Check if the script is being run directly
    main() # Call the main function to execute the script
        
        
