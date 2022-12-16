import pandas as pd
import pickle
from sklearn.model_selection import train_test_split

def get_voted_label(csv):
    df = pd.read_csv(csv, index_col=0)
    annotations = df.iloc[:,4:].mode(axis = 1)[0]
    annotations = annotations.apply(lambda x : x.lower())
    df['label'] = annotations
    df.index.name = 'id'
    df = df[['sentence', 'subject', 'object', 'label']]
    return df

def train_dev_test_split(df):
    original = pd.read_csv(df)
    train, test = train_test_split(original, test_size=.3, random_state=42,
                stratify=original['label'])
    dev, test= train_test_split(test, test_size = .5, random_state=42,
                stratify=test['label'])
    return train, dev, test

def voted_to_csv(csv):
    df = pd.read_csv(csv, index_col=0)
    df = get_voted_label(df)
    df.to_csv("output.csv")

def splitted_to_csv(csv):
    df = pd.read_csv(csv, index_col=0)
    train, dev, test = train_dev_test_split(df)
    train.to_csv("train.csv", index="id")
    dev.to_csv("dev.csv", index="id")
    test.to_csv("test.csv", index="id")

def num_to_label(label, pkl = 'dict_num_to_label.pkl'):
  """
    숫자로 되어 있던 class를 원본 문자열 라벨로 변환 합니다.
  """
  origin_label = []
  with open(pkl, 'rb') as f:
    dict_num_to_label = pickle.load(f)
  for v in label:
    origin_label.append(dict_num_to_label[v])
  
  return origin_label
  
def label_to_num(label, pkl = 'dict_label_to_num.pkl'):
  num_label = []
  with open(pkl, 'rb') as f:
    dict_label_to_num = pickle.load(f)
  for v in label:
    num_label.append(dict_label_to_num[v])
  
  return num_label