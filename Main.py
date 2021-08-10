from Automate import web_Automate
from http_add import add_http
from URL import get_URL
import cv2
from globals import *

def main():
    print('Enter the video path')
    video_path = input()
    sec = 0 
    frameRate = 0.5
    success = get_URL(sec,video_path) 
    while success: 
        sec = sec + frameRate 
        sec = round(sec, 2) 
        success,output = get_URL(sec,video_path)
    output = list(set(output))
    if(output != []):
        urls = add_http(output)
        print('Extracted URLs are ')
        print(urls)
        web_Automate(urls)
    else:
        print('Unable to extract urls from the text')


if __name__=="__main__":
    main()
