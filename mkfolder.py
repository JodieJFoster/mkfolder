import os

#Prompts user for number of folders to create
def number_of_folders():
    while True:
        try: 
            folders_int = int(input("How many folders would you like to create? \n"))
            print(folders_int, "folders will be created for you")
            return folders_int
        except ValueError:
            print("Invalid input. Please enter a number of folders to create \n")

# Prompts user for where they would like the folders to be created
def path_of_folders():
    while True:
        try:
            folders_path = str(input("Where would you like the folders to be created? \n"))
            print("Folders will be created in", folders_path)
            return folders_path
        except ValueError:
            print("Invalid path. Please select a valid path to create folders \n")


#Create folders based on users inputs
n_folder = number_of_folders()
folder_path = path_of_folders()

try:
    for i in range(n_folder):
        folder_name = "Week " + str(i)
        folder_full_path = os.path.join(folder_path, folder_name)
        os.makedirs(folder_full_path)
except OSError as e:
    print("error in creating folders")


