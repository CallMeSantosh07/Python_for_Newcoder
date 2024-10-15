import os 

path = "C:\\Users\\SANTOSH\\OneDrive\\Desktop\\folder"  # Use raw string to avoid escape sequence issues

if os.path.exists(path):  # Call os.path.exists with path as an argument
    print("Location exists")
    if os.path.isfile(path):
        print("This os file!")
    elif os.path.isdir(path):
        print("This is folder")
else:
    print("Location does not exist")
