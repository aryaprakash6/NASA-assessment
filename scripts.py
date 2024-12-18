import kagglehub
import os
import pandas as pd
import plotly.express as px

# Step 1: Download the dataset
dataset_path = kagglehub.dataset_download("patrickfleith/nasa-battery-dataset")
print("Dataset downloaded to:", dataset_path)

# Step 2: Define the path to the cleaned_dataset folder
cleaned_dataset_path = os.path.join(dataset_path, 'cleaned_dataset')

# Step 3: List all files in the cleaned_dataset folder
files_in_cleaned_dataset = os.listdir(cleaned_dataset_path)
print("Files in the cleaned_dataset folder:", files_in_cleaned_dataset)

# Step 4: Define the correct folder containing metadata.csv or other relevant files
file_name = "metadata.csv"  # Replace this if other files are needed
file_path = os.path.join(cleaned_dataset_path, file_name)

# Step 5: Check if the file exists and load the dataset
if os.path.exists(file_path):
    print(f"File found: {file_path}")
else:
    print(f"File not found at: {file_path}")
    exit()

df = pd.read_csv(file_path)
print("Dataset Loaded Successfully")
print(df.head())

# Step 6: Generate plots for the given parameters
# Plot Battery Impedance over Charge/Discharge Cycles (using uid as Cycle Index)
fig_impedance = px.line(
    df, 
    x="uid", 
    y="Re", 
    title="Battery Impedance (Re) Over Charge/Discharge Cycles",
    labels={"uid": "Cycle Index", "Re": "Battery Impedance (Re)"},
)
fig_impedance.show()
fig_impedance.write_image("battery_impedance_plot.png")

# Plot Electrolyte Resistance (Re) over Cycles
fig_re = px.line(
    df, 
    x="uid", 
    y="Re", 
    title="Electrolyte Resistance (Re) Over Charge/Discharge Cycles",
    labels={"uid": "Cycle Index", "Re": "Electrolyte Resistance"},
)
fig_re.show()
fig_re.write_image("electrolyte_resistance_plot.png")

# Plot Charge Transfer Resistance (Rct) over Cycles
fig_rct = px.line(
    df, 
    x="uid", 
    y="Rct", 
    title="Charge Transfer Resistance (Rct) Over Charge/Discharge Cycles",
    labels={"uid": "Cycle Index", "Rct": "Charge Transfer Resistance"},
)
fig_rct.show()
fig_rct.write_image("charge_transfer_resistance_plot.png")


