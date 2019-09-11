import pandas as pd
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

data = pd.read_csv("/home/dingjin/DOTA/training608/dota/DOTA/ImageSets/Main/all.txt")
print(data)
data = shuffle(data)

train = data.iloc[6000:]
test = data.iloc[: 6000]

train.to_csv("/home/dingjin/DOTA/training608/dota/DOTA/ImageSets/Main/" + "train" +'.txt', index=False, header=None)
test.to_csv("/home/dingjin/DOTA/training608/dota/DOTA/ImageSets/Main/" + "test" +'.txt', index=False, header=None)

