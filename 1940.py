import numpy as np
from PIL import ImageGrab
from grabscreen import grab_screen
import cv2

def draw_lines(img,lines):
    for line in lines:
        coords=line[0]
        cv2.line(img, (coords[0],coords[1]) ,(coords[2],coords[3]),(255,255,255),3)

def roi(img,vertices):
    mask=np.zeros_like(img)
    cv2.fillPoly(mask,vertices,255)
    masked=cv2.bitwise_and(img,mask)
    return masked

def process_img(original_img):
    processed_img = cv2.cvtColor(original_img,cv2.COLOR_BGR2GRAY)
    processed_img=cv2.Canny(processed_img,180, 540)
    #processed_img=cv2.GaussianBlur(processed_img,(5,5),0)
    #vertices = np.array([[2,243],[317,167],[495,160],[789,258],[789,491],[646,485],[563,381],[189,392],[7,388]])
    #processed_img=roi(processed_img,[vertices])
    #lines=cv2.HoughLinesP(processed_img,1,np.pi/180,np.array([]) ,180,20,15)
    #draw_lines(processed_img,lines)
    
    return processed_img


def cutimage(original_img):
    pts=np.array([[2,243],[317,167],[495,160],[789,258],[789,491],[646,485],[563,381],[189,392],[7,388]])
    isClosed=True
    color=(0,255,0)
    thickness=8
    highlighted=cv2.polylines(original_img,[pts],isClosed,color,thickness)



def screen_record(): 
    
    while(True):
        #printscreen =  np.array(ImageGrab.grab(bbox=(0,0,1920,1080)))      #(0,40,800,640)
        printscreen = grab_screen(region=(0,0,1920,1080))
        printscreen = cv2.resize(printscreen, (160,120))
        cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('a'):
            cv2.destroyAllWindows()
            break


screen_record()