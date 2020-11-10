import sys
##import re

import numpy as np
import pandas as pd

try:
    df_col_explain = pd.read_csv("HomeCredit_columns_description.csv", encoding= 'unicode_escape')
    df_col_explain = df_col_explain[df_col_explain["Table"] == "application_{train|test}.csv"] \
                        .drop(columns=["Unnamed: 0", "Table"]) \
                        .set_index("Row")
except FileNotFoundError:
    print("ERROR : ", "Couldn't find file :", "HomeCredit_columns_description.csv")
    print("This file should be present in the directory in order to get the wanted columns definitions")
except Exception as e:
    print(e)
    
rows = sys.argv

##reg = []
##
##for r in rows:
##    reg.append('^' + r.replace('*', '.*').replace('?', '.') + '$')
##
##df_col_explain.filter(regex = )

try:
    for row in rows[1:]:
        print("=>", row, ':\n\nDefinition:\n\t', df_col_explain.loc[row][0], '\n\nSpecial:\n\t', df_col_explain.loc[row][1])
        print("\n")
except KeyError:
    print("ERROR : ", row, ": Unknown column")
except Exception as e:
    print(e)
