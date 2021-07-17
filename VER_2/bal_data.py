import numpy as np
import pandas as pd
import cv2
import os
from collections import Counter
from random import shuffle


train_data=np.load('training_data.npy',allow_pickle=True)

print(len(train_data))
df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))

lefts=[]
rights=[]
forwards=[]
back=[]


shuffle(train_data)

for data in train_data:
    img=data[0]
    choice=data[1]
    
    if choice==[1,0,0,0]:
        lefts.append([img,choice])
    
    elif choice==[0,0,1,0]:
        rights.append([img,choice])
        
    elif choice==[0,1,0,0]:
        back.append([img,choice])
    
    elif choice==[0,0,0,1]:
        forwards.append([img,choice])
    else:
        print("something went wrong :(")    
        

forwards=forwards[:len(lefts)][:len(rights)] 
lefts=lefts[:len(forwards)]
rights=rights[:len(forwards)] 

final_data =forwards+lefts+rights+back

shuffle(final_data)
print(len(final_data))
np.save('training_data_v2.npy',final_data)   
    


# for data in train_data:
#     img=data[0]
#     choice=data[1]
#     cv2.imshow('test',img)
#     print(choice)
    
#     if cv2.waitKey(25) & 0xFF == ord('d'):
#         cv2.destroyAllWindows()
#         break