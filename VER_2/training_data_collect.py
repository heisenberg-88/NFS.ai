import numpy as np
from grabscreen import grab_screen
import cv2
import time

from getkeys import key_check
import os


def keys_to_output(keys):
    
    output = [0,0,0,0]        #[A,S,D,W,WA,WD,SA,SD]  taking S for going
    ######### 0 1 2 3 4 5 6 7           0 1 2 3  4  5  6  7

    if 'A' in keys:
        output[0] = 1
    elif 'S' in keys:
        output[1] = 1    
    elif 'D' in keys:
        output[2] = 1 
    elif 'W' in keys:
        output[3] = 1
    return output


file_name = 'training_data.npy'

if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    training_data = list(np.load(file_name,allow_pickle=True))
else:
    print('File does not exist, starting fresh!')
    training_data = []
    

    
def main():

    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)
        
    while(True):
        print(len(training_data))
        
        screen = grab_screen(region=(0,40,800,640))
        screen=cv2.cvtColor(screen,cv2.COLOR_BGR2GRAY)
        screen = cv2.resize(screen, (160,120))
        # print("loopran")
        
        keys = key_check()
        output = keys_to_output(keys)
        training_data.append([screen,output])
        # print("got the keys")
        
        if len(training_data) % 15000 == 0:
            print(len(training_data))
            np.save(file_name,training_data)
            print("Done Successfully!!!!")
            break    
            
main()