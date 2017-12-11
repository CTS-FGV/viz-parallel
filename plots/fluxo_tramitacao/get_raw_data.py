import pandas as pd

"""
Get the data and pass it to output as the value of 'raw_data'. It does not matter where
the data is comming from, just that in the end it has to be a Pandas DataFrame.
"""

# From CSV
raw_data = pd.read_csv('plots/fluxo_tramitacao/fluxo_tramitacoes.csv')

# From SQL
# import sqlalchemy
# con = sqlalchemy ...
# raw_data = pd.read_sql_query('SELECT * FROM somewhere', con)

# Your way to get data!

output = {'raw_data': raw_data}
