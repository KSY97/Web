import numpy as np
from numpy import dot
from numpy.linalg import norm
import pickle
from time import sleep
from collections import deque
import pymysql

def cos_sim(A, B):
    return dot(A, B)/(norm(A)*norm(B))

def return_similar_answer(input):
    embedding = model.encode(input)
    train_data['score'] = train_data.apply(lambda x: cos_sim(x['embedding'], embedding), axis=1)
    return train_data.loc[train_data['score'].idxmax()]['A']

with open('data.pkl','rb') as f:
    df = pickle.load(f)

with open('model.pkl','rb') as f:
    model = pickle.load(f)

train_data = df.copy()

# model = SentenceTransformer('sentence-transformers/xlm-r-100langs-bert-base-nli-stsb-mean-tokens')


# db = pymysql.connect(host='localhost', port=3306, user='root', passwd='6245', db='app', charset='utf8')
# cursor = db.cursor()

# sql = "SELECT id, user_id, contents, create_date FROM question;"
# cursor.execute(sql)
# result = cursor.fetchall()

# check_list = []

# for record in result:
#     if record[0] not in check_list:
#         check_list.append(record[0])
#         print(return_similar_answer(record[2]))

# db.close()
# predict()
