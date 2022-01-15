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
print("The last 5 records are: \n")
print(df.tail(5))

# 3rd question
columns_list = df.columns
print("Number of columns: ", len(columns_list))
print("Columns names: ", columns_list)

# 4th question
print("Types of columns: \n")
print(df.dtypes)

# 5th question
df.info()
''' Παρατηρούμε ότι στις στήλες Description και CustomerID, υπάρχουν 540455 και 406829 μη κενά σημεία.
    Αυτό σημαίνει ότι κάποια κελιά είναι κενά, αφού στο σύνολο είναι 541909.
    Άρα υπάρχουν στήλες με τιμές που λείπουν, η Description και η CustomerID. '''

# 6th question
print("Total number of records: ", len(df))
    
# DATASET CLEARING

# 1st question
df = df.dropna(axis=0, how = 'any', subset=['Description', 'CustomerID'])

# 2nd question
for x in df.index :
    if (df.loc[x,'Description']=='AMAZON FEE' or df.loc[x,'Description']=='Manual' or df.loc[x,'Description']=='SAMPLES' or df.loc[x,'Description']=='POSTAGE' or df.loc[x,'Description']=='PACKING CHARGE'):
        df.drop(x, inplace = True)
        
# 3rd question

