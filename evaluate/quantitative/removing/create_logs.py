import pandas as pd
import numpy as np

# Load the CSV file into a DataFrame
file_path = r"C:\Users\beyel\Documents\BPM\2024\Code\bpm\evaluation\artificial\logs\case_24.csv"
df = pd.read_csv(file_path)

# Set a random seed for reproducibility
np.random.seed(42)

# Define the percentage of rows to select for modification (e.g., 20%)
selection_percentage = 0.2

# Calculate number of rows to select based on selection_percentage
num_rows_to_select = int(len(df) * selection_percentage)

# Randomly select rows with replacement
selected_indices = np.random.choice(df.index, size=num_rows_to_select, replace=True)

# Create a set to keep track of indices to drop
indices_to_drop = set()


def modify_selected_row(row):
    enabled_activities = [el.strip() for el in row['enabled_activities'].split(',')]

    if len(enabled_activities) > 0:
        # Randomly choose an activity to remove from enabled activities
        activity_to_remove = np.random.choice(enabled_activities)

        # Check if the removed activity is the same as the one in 'activity' column
        if str(activity_to_remove) == str(row['activity']):
            return True  # Mark for deletion

        # Remove selected activity from enabled_activities list
        remaining_activities = [act for act in enabled_activities if act != activity_to_remove]

        # Update remaining enabled activities back to string format
        row['enabled_activities'] = ','.join(remaining_activities)

    return False  # Row remains valid


# Apply modifications only to selected rows and collect indices for removal
for index in selected_indices:
    if modify_selected_row(df.loc[index]):
        indices_to_drop.add(index)

# Drop marked indices from DataFrame
df_cleaned = df.drop(index=indices_to_drop)

# Save cleaned DataFrame back to a new CSV file (optional)
df_cleaned.to_csv('cleaned_event_log.csv', index=False)

print("Processing complete. Cleaned event log saved.")