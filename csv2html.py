import os
import pandas as pd

# Converts csv files to html formatted table
def csv2html(input_folder):
    output_folder = input_folder + "_html"
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            csv_file = os.path.join(input_folder, filename)
            html_file = os.path.join(output_folder, filename.replace(".csv", ".html"))

            df = pd.read_csv(csv_file, dtype=str)
            df.insert(0, '#', range(1, len(df) + 1))    # Position index in the column '#'
            for ii in range(len(df) - 1):               # fix index increase beased on result column
                if df.iat[ii, 1] == df.iat[ii+1, 1]:
                    df.iat[ii+1, 0] = df.iat[ii, 0]

            html_table = df.to_html(index=False, na_rep='', classes=['centered-table'], justify='left')

            with open(html_file, 'w') as f:
                f.write(html_table)



for ii in ["P", "I"]:
    for jj in ["M", "F"]:
        csv2html("database_ANA/assoluti/database_"+jj+"_"+ii+"_bl012/top_lists")
        csv2html("database_ANA/assoluti/database_"+jj+"_"+ii+"_bl012/lists")