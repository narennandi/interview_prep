import pandas as pd

from table_data import data, columns

df = pd.DataFrame(data = data).T



df.to_csv("data.csv")

df = pd.read_csv("data.csv", index_col = 0, parse_dates = ['INDDAY'])
print(df)

# We generally use class method to create factory methods. Factory methods return class object ( similar to a constructor ) for different use cases.
# We generally use static methods to create utility functions.