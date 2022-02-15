import xxlimited
import cv2, dlib, sys
import numpy as np

# model loading, and video loading.
# capturing faces in the video using facenet detector
# detecting face covering images and drawing rectangles.



facenet = cv2.dnn.readNet('caffemodel') # model loading
model = load_model('mask_detector.model') # model loading

cap = cv2.VideoCapture() # capture video (mp4)
ret, img = cap.read()  # video reading

fourcc = cv2.VideoWriter_fourcc('m','p','4','v') #don't know
out = cv2.VideoWriter('mp4', fourcc, cap.get(cv2.CAP_PROP_FPS), (img.shape[1], img.shape[0]) # don't know

while cap.isOpend(): # open
    ret, img = cap.read() # video reading. avobe?
    if not ret:
        break # out

    h, w = img.shape[:2] # height and width 0 and 1 indexing

    blob = cv2.dnn.blobFormImage(img, scalefactor=1, size=(300,300), mean(104,...) # don't know the nubmer
    facebnet.setInput(blob) # facenet model API, setInput, blob (dnn.bringing images?)
    dets = facenet.forward() #detections. facenet. forward?

    result_img = img.copy() # copying image

    for i in range(dets.shape[2]): # multiple faces possible
        confidence = dets[0,0,i,2] #don't know. 
        if confidence < 0.5: # face detects, if it's <0.5 what?
            continue

        x1 = int(Dets[0,0,i,3] * w)
        y1 = int
        x2 = int
        y2 = int

        face = img[y1:y2, x1:x2]

        face_input = cv2.resize(Face,dsize=224,224) #decreasing image size by 224 224
        face_input = cv2.cvtColor(face_input, cv2.COLOR_BGR2RGB)     # resized input face image changes to RGB colour
        face_input = preprocess_input(face_input) # tensorflow process_input method but don't know inside
        face_input = np.expand_dims(face_input, axis=0) #one dimension expanding axis=0 ->?

        mask, nomask = model.predicT(face_input).squeeze() # binary classification, don't know what suqeeze do

        if mask > nomask:
            color = (0,255,0)
            label = 'Mask %d%%' %(mask*100) # confidence score
        else:
            color = (0,0,255)
            label = 'No mask' * 100

        
        v2.rectangle(result_img, pt1= , pt2= , thickness, color, lineType) # drawing a rectangle for the predicted iamge
        cv2.putText(result_img, text=, org=, fontFace=, )

    out.write(result_img)
    cv2.imshow('result', result_img)
    if cv2.waitKy(1)==ord('q'):
        break

    out.release()
    cap.release() #ending.

