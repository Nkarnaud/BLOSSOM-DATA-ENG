# Importing pandas as pd
import pandas as pd
import os
import pandavro as pdx


# Reading CSV file with pandas to a dataframe
df = pd.read_csv("free-7-million-company-dataset.zip", compression='zip', engine='python')
# Droping out the companies with no domain
df.dropna(subset=['domain'], inplace=True)
# writing the output in avro
# pdx.to_avro("project1/free-7-million-company-dataset.avro".format, df)
# writing the output in a parquet format
df.to_parquet("free-7-million-company-dataset.parquet", engine='fastparquet', compression='gzip')
# writing the out put in json and compress format.
df.to_json("free-7-million-company-dataset.json.zip", compression='zip')
