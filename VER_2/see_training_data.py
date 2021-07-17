import numpy as np
import cv2

train_data=np.load('training_data.npy',allow_pickle=True) 

# for data in train_data:
#     img = data[0]
#     choice=data[1]
#     cv2.imshow('test',img)
#     print(choice)
#     if cv2.waitKey(25) & 0xff ==ord('q'):
#         cv2.destroyAllWindows()
#         break

   #output = [0,0,0,0,0,0,0,0]        #[A,S,D,W,WA,WD,SA,SD]  taking S for going
    ######### 0 1 2 3 4 5 6 7           0 1 2 3  4  5  6  7

print(len(train_data))
print(train_data[0][0].shape)
wkey=0
akey=0
skey=0
dkey=0


for data in train_data:
    keyval=data[1]
    if(keyval[0]==1):
        akey=akey+1
    if(keyval[3]==1):
        wkey=wkey+1
    if(keyval[2]==1):
        dkey=dkey+1
    if(keyval[1]==1):
        skey=skey+1
    

print(f"w keys {wkey}\n")
print(f"a keys {akey}\n")
print(f"d keys {dkey}\n")
print(f"s keys {skey}\n")