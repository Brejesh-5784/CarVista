# CHECK WHETHER DATASET IS FOUND OR NOT !!! 
import os

file_path = " #PATH FOR YOUR DATASET "  # Replace with the correct path

if os.path.exists(file_path):
    print("File found!")
else:
    print("File not found!")
