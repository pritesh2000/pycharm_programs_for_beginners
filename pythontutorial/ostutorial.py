import os
print(dir(os))
print(os.getcwd())          # Get Current working directory
# os.chdir("C://")
# print(os.getcwd())
# f = open("pritesh.txt")
print(os.listdir())         # Return list of directory
print(os.listdir("C://"))   # Return list of given directory
# os.mkdir("An")            # Create folder 1 run this only os.mkdir("An/that")       # Create sub folder comment
# above then run os.mkdir("This/there")      # Through an error because there is no "This folder" but you want to
# make sub folder in it.
# os.makedirs("This/that")    # Crate both folder and sub-folder together
# os.rename("temp.txt", "beginner.txt")
print(os.environ.get("path"))
print(os.path.join("C://", "beginner.txt"))     # Remove unnecessary slash
print(os.path.exists("C://"))
print(os.path.isfile("C://"))
