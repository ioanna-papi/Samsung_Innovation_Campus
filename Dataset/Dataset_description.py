''' TEAM 3
    TEAM MEMBERS:
    IOANNA - MARIA PAPIDAKI
    VASILIKI PSOROGIANNI
    IOANNA DEDELOUDI '''

import pandas as pd

# DATASET DESCRIPTION

# 1st question
df = pd.read_csv('C:/Users/User/Documents/data.csv' ,sep  = ',', header= 'infer')

# 2nd question
print(df.tail(5))

# 3rd question
columns_list = df.columns
print("Number of columns: ", len(columns_list))
print("Columns names: ", columns_list)

# 4th question

