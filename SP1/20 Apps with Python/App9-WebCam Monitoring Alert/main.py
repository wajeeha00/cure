import cv2 
import time
from emailing import send_email
import glob

video = cv2.VideoCapture(0)
time.sleep(1)
status_list = []
first_frame = None
count = 1
while True:
    status = 0
    check, frame = video.read()
    frame = cv2.flip(frame, 1)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame,(21,21), 0)

    if first_frame is None:
        first_frame = gray_frame_gau
    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)
    thres_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thres_frame, None, iterations=2)
    
    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 15000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rect = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
        if rect.any():
            status = 1
            cv2.imwrite(f"images/{count}.png", frame)
            count+=1
            all_images = glob.glob("images/*.png")
            index = int(len(all_images)/2)
            image_with_object = all_images[index]
                    

    status_list.append(status)
    status_list = status_list[-2:]
    
    # if status_list[0] == 1 and status_list[1] == 0:
        # send_email(image_with_object)

    cv2.imshow("My Video", frame)
    key = cv2.waitKey(1)
    if key==ord("q"):
        break
video.release()

