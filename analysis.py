import pandas as pd

df=pd.read_csv("customer_shopping_behavior.csv")

df.head()

df.info()

df.describe(include='all')

df.isnull().sum()

df['Review Rating']=df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
df.isnull().sum()

df.columns=df.columns.str.lower()

df.columns=df.columns.str.replace(' ','_')

df=df.rename(columns={"purchase_amount_(usd)":'purchase_amount'})

df.columns

# create a column age_group
labels=['Young Adult','Adult','Middle-aged','Senior']
df['age_group']=pd.qcut(df['age'],q=4, labels = labels)
df[['age','age_group']].head(10)

# create column purchase_frequency_days.
frequency_mapping={
'Fortnightly':14,
    'Weekly':7,
    'Monthly':30,
    'Quarterly':90,
    'Bi-weekly':14,
    'Annualy':365,
    'every 3 Months':90
    
}
df['purchase_frequency_days']=df['frequency_of_purchases'].map(frequency_mapping)
df[['purchase_frequency_days','frequency_of_purchases']].head(10)
df[['discount_applied','promo_code_used']].head(10)
(df['discount_applied'] == df['promo_code_used']).all()
df=df.drop('promo_code_used',axis=1)
df.columns

# pip install pymysql sqlalchemy
from sqlalchemy import create_engine
import urllib.parse

#mysql connection
username= "root"
password=urllib.parse.quote_plus("f5f4n3n1@12345#")
host= "localhost"
port= 3306
database="customer_behavior"

engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')
connection=engine.connect()
print("connected successfully!")

# load dataframe to mysql.
table_name="mytable"

# create any table name.
df.to_sql(table_name, engine, if_exists='replace',index=False)

# read back sample..
pd.read_sql("select * from mytable LIMIT 5",engine)
from sqlalchemy import create_engine,text
import pandas as pd
import urllib.parse

password = urllib.parse.quote_plus("f5f4n3n1@12345#")

engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost:3306/customer_behavior"
)
with engine.connect() as connection:result=connection.execute(text("SELECT 1"))
print("Connection object created successfully")
engine.connect()
print("connected successfully")
df=pd.read_sql("SHOW DATABASES;",engine)
print(df)
