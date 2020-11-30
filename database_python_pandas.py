import pandas as pd

from sqlalchemy import create_engine
engine = create_engine('sqlite:///data.db', echo = False)

from table_data import data, columns

dtypes = {	
			'POP': 'float64', 
			'AREA': 'float64', 
			'GDP': 'float64', 
			'INDDAY': 'datetime64'
		}

df = pd.DataFrame(data = data).T.astype(dtype=dtypes)
# print(df)

# df.to_sql('data.db', con = engine, index_label = 'ID')


df = pd.read_sql('data.db', con=engine, index_col='ID')
# print(df)

# print(df.groupby('CONT').count())
# print(df.CONT.value_counts())
# print()
#select statement
# print(df[['AREA', 'CONT', 'COUNTRY']])

# print(df.loc[:, ['AREA', 'CONT', 'COUNTRY']])


#get distinct rows
# print(df.loc[:,['CONT']].drop_duplicates())

#limit statement
# print(df.loc[:,:].head(5))

#Min statement
print(df.loc[:, ['GDP']].min())

#Max statement
print(df.loc[:,['GDP']].max())

#Count statement
print(df.loc[:,['GDP']].count())

#average statement
print(df.loc[:,['GDP']].mean())

#sum statement
print(df.loc[:,['GDP']].sum())

#group by
print(df.loc[:, ['CONT','GDP'] ].groupby(['CONT']).sum())