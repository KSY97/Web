import pickle

path = 'C:/Users/YGL/Desktop/ksy/Web/app/'

with open(path + 'data.pkl','rb') as f:
    df = pickle.load(f)

with open(path + 'model.pkl','rb') as f:
    model = pickle.load(f)

train_data = df.copy()

print('로드 완료')