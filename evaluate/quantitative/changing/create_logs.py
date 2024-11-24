import pandas as pd
import numpy as np

# Load the CSV file into a DataFrame
file_path = r"C:\Users\beyel\Documents\BPM\2024\Code\bpm\evaluation\artificial\logs\case_24.csv"
df = pd.read_csv(file_path)

# Set a random seed for reproducibility
np.random.seed(42)  # You can change this seed if needed

# Define the percentage of rows to select for modification (e.g., 20%)
selection_percentage = 0.2

# Calculate number of rows to select based on selection_percentage
num_rows_to_select = int(len(df) * selection_percentage)

# Randomly select rows with replacement
selected_indices = np.random.choice(df.index, size=num_rows_to_select, replace=True)

# Get all unique activities from the event log for replacement
all_activities = set(df['activity'].unique())


def modify_selected_row(row):
    enabled_activities = [el.strip() for el in row['enabled_activities'].split(',')]

    # Convert to set to remove duplicates and then back to list for processing
    unique_enabled_activities = list(set(enabled_activities))

    if len(unique_enabled_activities) > 0:
        # Randomly choose an enabled activity to replace
        activity_to_replace = str(np.random.choice(unique_enabled_activities))

        # Randomly choose a new activity from all available activities (excluding the original one)
        new_activity = str(np.random.choice(list(all_activities - {activity_to_replace})))

        # Update enabled activities by replacing the chosen one with the new one
        remaining_activities_set = set(unique_enabled_activities)  # Use set for uniqueness

        remaining_activities_set.remove(activity_to_replace)  # Remove old activity

        remaining_activities_set.add(new_activity)  # Add new activity

        # Check if we need to update the executed activity as well
        if str(row['activity']) == str(activity_to_replace):
            row['activity'] = new_activity

        # Update remaining enabled activities back to string format without duplicates
        row['enabled_activities'] = ','.join(remaining_activities_set)

    return row


# Apply modifications only to selected rows
for index in selected_indices:
    df.loc[index] = modify_selected_row(df.loc[index])

# Save modified DataFrame back to a new CSV file (optional)
df.to_csv('modified_event_log.csv', index=False)

print("Processing complete. Modified event log saved.")