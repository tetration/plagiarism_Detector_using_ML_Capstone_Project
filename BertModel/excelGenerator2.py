# Import pandas library to work with excel files
import pandas as pd

# Read the original excel file into a dataframe
df = pd.read_excel("plagiarism_results.xlsx")

# Define the name of the column to match
column_name = "Level"

# Get the unique values in the column
values = df[column_name].unique()

# Loop through the values and create a new dataframe for each value
for value in values:
    # Filter the original dataframe by the value
    new_df = df[df[column_name] == value]

    # Create a new excel file name based on the value
    # Replace any invalid characters with underscores
    new_file = f"{value}.xlsx".replace("<", "_").replace(">", "_").replace(":", "_")

    # Write the new dataframe to the new excel file
    new_df.to_excel(new_file, index=False)

    # Print a message to indicate the progress
    print(f"Created {new_file} for {value}")