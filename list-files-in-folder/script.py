import os

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
        




def list_of_files_in_folder(folder_list):
    try:
        files = os.listdir(folder_list)
        return files,None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"


if __name__ == "__main__":
    main()
        
        
