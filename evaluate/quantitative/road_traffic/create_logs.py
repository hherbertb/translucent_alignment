from evaluate.quantitative.removing.create_logs import manipulate_log as remove_enabled
from evaluate.quantitative.changing.create_logs import manipulate_log as change_enabled
from evaluate.quantitative.adding.add_enabled import manipulate_log as add_enabled_activities_to_events
from evaluate.quantitative.adding.add_events import manipulate_log as add_new_events

import pandas as pd

import warnings
warnings.simplefilter(action="ignore", category=pd.errors.SettingWithCopyWarning)

df = pd.read_csv("original_translucent_event_log_04.csv", sep=",")
# List of percentages
percentages = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for percentage in percentages:
    print(percentage)
    for method_num in range(1, 6):
        if method_num == 1:
            result_df = remove_enabled(df.copy(), percentage/100)
            filename = f"{percentage:03d}_remove.csv"
        elif method_num == 2:
            result_df = change_enabled(df.copy(), percentage/100)
            filename = f"{percentage:03d}_change_enabled.csv"
        elif method_num == 3:
            result_df = add_enabled_activities_to_events(df.copy(), percentage/100)
            filename = f"{percentage:03d}_add_to_enabled.csv"
        elif method_num == 4:
            result_df = add_new_events(df.copy(), percentage/100)
            filename = f"{percentage:03d}_add_events.csv"
        else:
            result_df = remove_enabled(df.copy(), percentage / 100)
            result_df = result_df.reset_index(drop=True)
            result_df = change_enabled(result_df, percentage / 100)
            result_df = result_df.reset_index(drop=True)
            result_df = add_enabled_activities_to_events(result_df, percentage / 100)
            result_df = result_df.reset_index(drop=True)
            result_df = add_new_events(result_df, percentage / 100)
            result_df = result_df.reset_index(drop=True)
            filename = f"{percentage:03d}_all_applied.csv"

        # Save the DataFrame to a CSV file
        result_df.to_csv(filename, index=False, sep=";")
