import cv2
import pytesseract
from text_preprocess import preprocess

def get_URL(sec,video_path):
    global prep
    vidcap = cv2.VideoCapture(video_path) 
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000) 
    hasFrames,image = vidcap.read() 
    if hasFrames: 
        raw_Text = pytesseract.image_to_string(image)
        if(raw_Text != ''):
            prep = preprocess(raw_Text)
        else:
            print('Unable to extract  text from the video')
    return hasFrames,prep