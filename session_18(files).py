# files
# --------------------------------------------------
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# create a file
# f = open("myfile.txt", "x")
# f.close()


# read the whole file 
# --------------------------------------------------
# f = open("demofile.txt", "r")
# print(f.read())
# print(f.read(5))
# f.close()


# read a file line by line
# --------------------------------------------------
# f = open("demofile.txt", "r")
# print(f.readline())

# for x in f:
#   print(x)
# f.close()



# Write a file with content
# --------------------------------------------------
# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()


# f = open("demofile2.txt", "r")
# print(f.read())
# f.close()



# Delete a file
# --------------------------------------------------
# import os
# os.remove("demofile.txt")


# Delete a file if exist
# --------------------------------------------------
# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")


# Delete Folder
# --------------------------------------------------
# import os
# os.rmdir("myfolder")









# OS
# print current directory address
# --------------------------------------------------
# import os
# print(os.getcwd())


# create file in this directory
# --------------------------------------------------
# import os

# Define the file path
# file_path = os.path.join(os.getcwd(), 'new_file.txt')

# Create and open the file in write mode
# with open(file_path, 'w') as file:
#     file.write("Hello, this is a new file!")

# print(f"File created at: {file_path}")


# rename / remove a file
# --------------------------------------------------
# os.rename('old_file.txt', 'new_file.txt')
# os.remove('new_file.txt')


# list file and folders
# --------------------------------------------------
# print(os.listdir())


# create and delet a folder
# --------------------------------------------------
# os.mkdir('new_directory')
# os.rmdir('new_directory')


# if a file exist
# --------------------------------------------------
# print(os.path.exists('session_16,17(modules).py'))




# Run a shell command
# --------------------------------------------------
# import time
# os.system('echo hello')
# time.sleep(3)
# os.system('clear')
