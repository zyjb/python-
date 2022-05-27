import pandas as pd
import sqlalchemy as sl
import random
data = pd.read_csv('data/ll.csv')
data.loc[:, ('推荐值')] = [random.randint(0, 5) for _ in range(0, data.shape[0])]
conn = sl.create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/data?charset=utf8')
pd.io.sql.to_sql(data, 'data_', con=conn, schema='data', if_exists='fail')
