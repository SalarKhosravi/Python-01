# Step 1: Create a new file
# ----------------------------------------------------------
try:
    file = open("projects/myfile.txt", "x")  # "x" mode for creating a new file
    file.write("This is a newly created file.")  # Write initial text
    print("File created successfully.")
except FileExistsError:
    print("File already exists.")
finally:
    file.close()





# Step 2: Open and read the file content
# ----------------------------------------------------------
with open("projects/myfile.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)    






# Step 3: Write new content to the file (overwrites any existing content)
# ----------------------------------------------------------
with open("projects/myfile.txt", "w") as file:
    file.write("This is new content that overwrites the previous text.")







# Step 4: Append content to the file
# ----------------------------------------------------------
with open("projects/myfile.txt", "a") as file:
    file.write("\nThis line is appended to the file.")








# Step 5: Read the file line by line
# ----------------------------------------------------------
with open("projects/myfile.txt", "r") as file:
    for line in file:
        print(line, end="")  # end="" prevents extra newlines







# Step 6: Delete the file
# ----------------------------------------------------------
import os
if os.path.exists("projects/myfile.txt"):
    os.remove("projects/myfile.txt")
    print("File deleted.")
else:
    print("File does not exist.")




