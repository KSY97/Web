import pickle

path = 'C:/Users/YGL/Desktop/ksy/Web/app/'

with open(path + 'data.pkl','rb') as f:
    df = pickle.load(f)

with open(path + 'model.pkl','rb') as f:
    model = pickle.load(f)

train_data = df.copy()

print('로드 완료')

from numpy import dot
from numpy.linalg import norm
import os

def cos_sim(A, B):
    return dot(A, B)/(norm(A)*norm(B))

def return_similar_answer(input):
    embedding = model.encode(input)
    train_data['score'] = train_data.apply(lambda x: cos_sim(x['embedding'], embedding), axis=1)
    return train_data.loc[train_data['score'].idxmax()]['A']


print(return_similar_answer('질문'))