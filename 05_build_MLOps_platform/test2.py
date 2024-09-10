import pandas as pd
from datasets import load_dataset
from sqlalchemy import create_engine

# 加載 HuggingFace IMDB 資料集
dataset = load_dataset("imdb")

# 連接到 PostgreSQL
engine = create_engine("postgresql+psycopg2://mlops:mlops@localhost:5432/imdb_db")


# 將資料集轉換為 DataFrame 並存入 PostgreSQL
def save_to_db(dataset, split, table_name):
    df = pd.DataFrame(dataset[split])
    df.to_sql(table_name, engine, index=False, if_exists="replace")


def fetch_from_db(table_name):
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, engine)
    return df


# 撈取訓練資料和測試資料
train_df = fetch_from_db("imdb_train")
test_df = fetch_from_db("imdb_test")
# save_to_db(dataset, "train", "imdb_train")
# save_to_db(dataset, "test", "imdb_test")
