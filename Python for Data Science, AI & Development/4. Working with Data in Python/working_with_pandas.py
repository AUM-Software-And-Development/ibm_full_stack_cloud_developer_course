import pandas as pd

csv_path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)

print(df.head())

print("\nnew data from excel\n")

xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'
df=pd.read_excel(xlsx_path)
print(df.head())

x = df[['Length']]
print(x)

x = df['Length']
print(x)

x = df[['Artist']]
print(type(x))

y = df[['Artist', 'Length', 'Genre']]
print(y)

#data from cell at first row first column
print(df.iloc[0,0])

print(df.iloc[1,0])

print(df.iloc[0,2])

print(df.iloc[1,2])

print("\ngetting cell data via keys\n")

#using column key
print(df.loc[1,'Artist'])
print(df.loc[1,'Artist'])
print(df.loc[0,'Artist'])
print(df.loc[1,'Artist'])

#slice
print(df.loc[0:2, 'Artist':'Released'])