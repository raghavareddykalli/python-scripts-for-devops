
Below is the step-by-step explanation of the code: 

```bash
import os
```
- This line imports the os module, which lets you interact with the operating system (like listing files in a folder).

```bash
def main():
    folders_list = input("Enter the list of files with space in between: ").split()
    for folder_list in folders_list:
        files, error = list_of_files_in_folder(folder_list)
        if files:
            print(f"Files in '{folder_list}': {files}")
            for file in files:
                print(file)
        else:
            print(f"Error in '{folder_list}': {error}")
```

- The main() function is the main part of the program.
- It asks the user to enter folder names, separated by spaces.
- It splits the input into a list called folders_list.
- For each folder in that list:
  - It calls list_of_files_in_folder() to get the files in that folder.
  - If files are found, it prints the folder name and the list of files, then prints each file name individually.
  - If there’s an error (like the folder doesn’t exist), it prints an error message.
 
```bash
def list_of_files_in_folder(folder_list):
    try:
        files = os.listdir(folder_list)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"
```

- This function tries to list all files in a given folder.
- It covers the exceptional cases using the try-except concept in Python.
- If successful, it returns the list of files and None for error.
- If the folder doesn’t exist, it returns None and an error message.
- If you don’t have permission to access the folder, it returns None and a different error message.

```bash
if __name__ == "__main__":
main()
```

- This checks if the script is being run directly (not imported).
- If so, it calls the main() function to start the program.

## Summary:
The script asks you for folder names, lists the files in each folder, and handles errors if a folder doesn’t exist or you don’t have permission.
