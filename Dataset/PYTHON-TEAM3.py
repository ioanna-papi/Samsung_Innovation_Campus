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
''' Παρατηρούμε ότι στις στήλες Description και CustomerID, υπάρχουν 540.455 και 406.829 μη κενά σημεία.
    Αυτό σημαίνει ότι κάποια κελιά είναι κενά, αφού στο σύνολο είναι 541.909.
    Άρα υπάρχουν στήλες με τιμές που λείπουν, η Description και η CustomerID. '''

# 6th question
''' Το dataset έχει μέγεθος 541.909 '''
print("Total number of records: ", len(df))
    
# DATASET CLEARING

# 1st question
''' Συνολικά αφαιρέθηκαν 135.080 εγγραφές. Άρα το dataset έχει μέγεθος 406.829 '''
df = df.dropna(axis=0, how = 'any', subset=['Description', 'CustomerID'])

# 2nd question
''' Συνολικά αφαιρέθηκαν 1.677 εγγραφές. Άρα το dataset έχει μέγεθος 405.152 '''
options = ['AMAZON FEE', 'SAMPLES', 'Manual', 'POSTAGE', 'PACKING CHARGE']
rslt_df = df[df['Description'].isin(options)]
for x in df.index:
    if (x in rslt_df.index ):
        df.drop(x, inplace = True) 
        
# 3rd question
''' Συνολικά αφαιρέθηκαν 8.631 εγγραφές. Άρα το dataset έχει μέγεθος 396.521 '''
for x in df.index :
    if df.loc[x,'Quantity'] < 0:
        df.drop(x, inplace = True)
     
# 4th question
df['ItemTotal'] = df['Quantity'] * df['UnitPrice']

# DATASET QUERIES

# 1st question
customers_by_id = df.groupby('CustomerID')
print("Total number of different customers is: ", len(customers_by_id.size()))

# 2nd question
by_country = df.groupby('Country')
print('Countries that have transactions with the company: \n')
for index_country, value in by_country.size().items():
    print(index_country)

# 3rd question
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
print('The time period related to the data is: ', df['InvoiceDate'].min(), ' to ',  df['InvoiceDate'].max())
print('In total: ', df['InvoiceDate'].max() -  df['InvoiceDate'].min(), 'hours')

# 4th question
''' Συνολικά ένας πελάτης που επιθυμεί να διαθέσει 100-150 ευρώ μπορεί να αγοράσει 6 διαφορετικούς τύπους προϊόντων '''
lst = []
for x in df.index :
    if df.loc[x,'UnitPrice'] >= 100 and df.loc[x,'UnitPrice'] <= 150:
        lst.append(df.loc[x, 'Description'])  
products = pd.DataFrame(data=lst, columns = ["name"])
by_name = products.groupby('name')
print("The products that a customer can buy with 100-150 euros are:")
print(by_name.size())
print("In total they are:",len(products), "products belonging in", len(by_name),"different categories" )

# 5th question
''' Αν κάνουμε αναζήτηση με τον όρο 'HANDBAG', θα λάβουμε συνολικά 13 διαφορετικούς τύπους προϊόντων '''
contains_handbag = df.loc[df['Description'].str.contains("HANDBAG",case = False)]
print("The products that include the word HANDBAG are: ")
print(contains_handbag['Description'].unique())
print("In total they are:",len(contains_handbag), "products belonging in", len(contains_handbag['Description'].unique()),"different categories")


