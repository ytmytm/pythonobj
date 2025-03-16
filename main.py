import pandas as pd

def extract(path):
  return pd.read_csv(path)

def transform(df):
  return df[["Imię"]].drop_duplicates()

def load(df, path):
  return df.to_json(path, orient="records", index=False, lines=True)


def job(input_path, output_path):
  source_data = extract(input_path)
  transformed_data = transform(source_data)
  load(transformed_data, output_path)