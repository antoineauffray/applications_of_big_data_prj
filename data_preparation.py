from random import choices
import numpy as np
import pandas as pd

from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

while True:
    try:
        file_name = input("What file should be processed ? (type q or quit to exit)\n")
        
        if file_name == 'q' or file_name == "quit":
            print("\033[A                             \033[A")
            exit(0)
            
        df_train = pd.read_csv(file_name)
        
        break
    except FileNotFoundError:
        print("Error: The file :", file_name, "doesn't exist!", '\n')
    except Exception as e:
        print("Error: %s" % e)
        
print("\033[A                             \033[A")

print(file_name.split('.')[0])
    
print("Initial CSV read !", '\n')

imp_mean = IterativeImputer(random_state=0)
df = df_train.select_dtypes(exclude='object')

imputed = imp_mean.fit_transform(df)

print("Multivariate imputation done !", '\n')

df_imput = pd.DataFrame(imputed, columns=df.columns)

for c in df_imput.columns:
    df_train[c] = df_imput[c]

for c in df_train.isnull().sum()[df_train.isnull().sum() > 0].index:

    d = df_train[c].value_counts() / df_train[c].value_counts().sum()

    for i in range(len(df_train)):
        if pd.isna(df_train[c][i]):
            df_train.at[i, c] = choices(list(d.index), list(d.values))[0]

print("Custom imputation done !", '\n')

with open(file_name.split('.')[0] + "_imputed_a.csv", 'w', newline='') as file:
    df_train.to_csv(file)

print("Final CSV written !")
