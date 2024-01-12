import os
import pandas as pd

def excel_sheets_to_csv(excel_file):
    # Extract the base name of the Excel file without extension
    base_name = os.path.splitext(os.path.basename(excel_file))[0]

    # Load the Excel file
    xls = pd.ExcelFile(excel_file)

    # Loop through all the sheets in the file
    for sheet_name in xls.sheet_names:
        # Read each sheet into a pandas DataFrame
        df = xls.parse(sheet_name)

        # Check if the sheet is "Data" and if it's empty, skip it
        if sheet_name == "Data" and df.empty:
            continue

        # Construct the CSV file name
        csv_file = f"{base_name}_{sheet_name}.csv"

        # Export each DataFrame to a CSV file with the constructed name
        df.to_csv(csv_file, index=False)

    print("Exported all sheets to CSV files, except empty 'Data' sheets.")

# Example usage:
# excel_sheets_to_csv('path_to_your_excel_file.xlsx')
