import os

from datasets import load_dataset
from sqlalchemy import Column, Integer, MetaData, Table, Text, create_engine
from sqlalchemy.orm import sessionmaker

# 从环境变量中获取数据库连接信息
db_engine = create_engine("postgresql+psycopg2://mlops:mlops@localhost:2345/imdb_db")

metadata = MetaData(bind=db_engine)

imdb_train = Table("imdb_train", metadata, autoload_with=db_engine)

Session = sessionmaker(bind=db_engine)
session = Session()

dataset = load_dataset("imdb")

# Only insert one data for demo
text = dataset["train"][:1]["text"]
label = dataset["train"][:1]["label"]
ins = imdb_train.insert().values(text=text[0], label=label[0])
session.execute(ins)
session.commit()
session.close()
print("Success!")
