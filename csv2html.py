import os
import pandas as pd

def csv2html(input_folder):
    output_folder = input_folder + "_html"
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            csv_file = os.path.join(input_folder, filename)
            html_file = os.path.join(output_folder, filename.replace(".csv", ".html"))

            df = pd.read_csv(csv_file)
            html_table = df.to_html(index=False)

            with open(html_file, 'w') as f:
                f.write(html_table)


csv2html("database_ANA/database_F_I_bl012/sorted_data")