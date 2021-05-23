'''
facial recognition
'''

import cv2

#load the cascade
face_cascade = cv2.CascadeClassifier("../../data/cascade_xml/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("../../data/cascade_xml/haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("../../data/cascade_xml/haarcascade_smile.xml")

#defining a function todo detections
def detect(gray, frame):
    #get coordinated to rectange to detect face
    #scaledown image to 1.3 times and 5 neighbour zones must be accepted
    #faces are tuples of 4 coordinates, x, y are coordinates, w,h are width and height
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) # 255,0,0, is green color box and thickness is 2
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 62)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)
    return frame

#face recognition with webcam
#0 for internal webcam and 1 for ext
video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    #cvt is used for color to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()


