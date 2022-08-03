import time
import cv2
from keras.models import load_model
import numpy as np

cam = cv2.VideoCapture(0)
model = load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def pred_results():
        if prediction[0][0] > 0.5: #Rock
            return "Rock"
        elif prediction[0][1] > 0.5: #Paper
            return "Paper"
        elif prediction[0][2] > 0.5: #Scissors
            return "Scissors"
        else: #Nothing
            return "Nothing"

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    
    if k%256 == 27:
        # Press ESC to exit
        print("Escape hit, closing...")
        break
    elif k%256 == 32: # Press SPACE to start
        def countdown(t):
            while t: # while t > 0 for clarity 
                mins = t // 60
                secs = t % 60
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end="\r") # overwrite previous line 
                time.sleep(1)
                t -= 1
        print('Showing Results!!!')
        t = input("Enter the time in seconds: ") 
        countdown(int(t))
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        # cv2.imshow('frame', frame)
        # Press q to close the window
        results = pred_results()   
        print(results)
       
cam.release() 
cv2.destroyAllWindows()