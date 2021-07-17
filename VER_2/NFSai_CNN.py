#train the data
import numpy as np
from alexnet import alexnet

WIDTH = 160
HEIGHT =120
LR =1e-3
EPOCH =15
MODEL_NAME = 'NFSai_ver1'


model = alexnet(WIDTH,HEIGHT,LR)
train_data=np.load('training_data_v2.npy',allow_pickle=True)

train = train_data[:-3000]
test=train_data[-3000:]

x=np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
y=[i[1] for i in train]

test_x=np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
test_y=[i[1] for i in test]

model.fit({'input':x}, {'targets':y} ,n_epoch=EPOCH ,validation_set=( {'input':test_x}, {'targets':test_y}), snapshot_step=500,show_metric=True,run_id=MODEL_NAME)

model.save(MODEL_NAME)




