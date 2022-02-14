import pandas as pd
#Windows=========================================================================================================
df = pd.read_csv ('./static/assets/windows.csv', on_bad_lines='skip')
allColumns = df.columns.values
allUniqEventIDs = sorted(df['EventID'].unique().tolist())
allUniqEventIDsFreq = df['EventID'].value_counts().to_dict()
#print(allUniqEventIDs)
#print(allUniqEventIDsFreq)