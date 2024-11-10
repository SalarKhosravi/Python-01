import os

myfolderDir = os.path.join(os.getcwd(), "projects/myfolder")
myfilePath = os.path.join(myfolderDir, "myfile.txt")



# Create folder if there is no folder here
if not os.path.exists(myfolderDir):
#   os.system(f'mkdir {myfolderDir}')
  os.mkdir(myfolderDir)
  print('1- created the directory')
else:
  print("1- The directory does exist")




# Create the file if it doesn't exist
if not os.path.exists(myfilePath):
    with open(myfilePath, 'w') as file:
        file.write("Initial file creation.\n")
    print("2- Created the file")
else:
    print("2- The file already exists")




# Open the file to write additional content and read it
with open(myfilePath, 'r+') as file:
    file.write('this is code from project 10\n')
    file.seek(0)  # Move to the start of the file for reading
    print("File contents after writing:")
    print(file.readline())