# import pandas lib as pd
import pandas as pd
# read by default 1st sheet of an excel file
# dataframe1 = pd.read_excel('Pelaajaluettelo.xlsx')
# print(dataframe1)

df = pd.read_excel('instructors.xlsx') # can also index sheet by name or fetch all sheets

print(df.columns.ravel())

ins = df['instructor code'].tolist()
print(df['instructor code'].tolist())
print(df['instructors'].tolist())
print(df['#of hours'].tolist())
