# Import pandas library to work with excel files
import pandas as pd

# Read the original excel file into a dataframe
df = pd.read_excel("plagiarism_results.xlsx")

# Define the names of the columns to match
column_name_1 = "Level"
column_name_2 = "Layer"

# Get the unique values in the first column
values_1 = df[column_name_1].unique()

# Loop through the values in the first column and create a new dataframe for each value
for value_1 in values_1:
    # Filter the original dataframe by the value in the first column
    new_df = df[df[column_name_1] == value_1]

    # Get the unique values in the second column
    values_2 = new_df[column_name_2].unique()

    # Loop through the values in the second column and create a new dataframe for each value
    for value_2 in values_2:
        # Filter the new dataframe by the value in the second column
        new_df_2 = new_df[new_df[column_name_2] == value_2]

        # Create a new excel file name based on the values in both columns
        # Replace any invalid characters with underscores
        new_file = f"{value_1}_{value_2}.xlsx".replace("<", "_").replace(">", "_").replace(":", "_")

        # Write the new dataframe to the new excel file
        new_df_2.to_excel(new_file, index=False)

        # Print a message to indicate the progress
        print(f"Created {new_file} for {value_1} and {value_2}")