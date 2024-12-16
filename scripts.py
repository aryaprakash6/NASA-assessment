import kagglehub

# Download the dataset
dataset_path = kagglehub.dataset_download("patrickfleith/nasa-battery-dataset")
print("Dataset downloaded to:", dataset_path)

import os

# Define the path to the cleaned_dataset folder
cleaned_dataset_path = os.path.join(dataset_path, 'cleaned_dataset')

# List all files in the cleaned_dataset folder
files_in_cleaned_dataset = os.listdir(cleaned_dataset_path)
print("Files in the cleaned_dataset folder:", files_in_cleaned_dataset)

import os

# Define the correct folder containing metadata.csv
file_name = "metadata.csv"
file_path = os.path.join(dataset_path, "cleaned_dataset", file_name)  # Adjust folder if needed

# Check if the file exists
if os.path.exists(file_path):
    print(f"File found: {file_path}")
else:
    print(f"File not found at: {file_path}")

import pandas as pd

# Load the CSV
df = pd.read_csv(file_path)
print("Dataset Loaded Successfully")
print(df.head())

import os

for root, dirs, files in os.walk(dataset_path):
    print(f"Directory: {root}")
    print(f"Subdirectories: {dirs}")
    print(f"Files: {files}")

