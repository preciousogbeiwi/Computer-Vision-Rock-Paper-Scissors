import cv2
from keras.models import load_model
import numpy as np
import random
import time

cam = cv2.VideoCapture(0)
model = load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 32:
        # SPACE pressed
        def countdown(t):
            while t: # while t > 0 for clarity 
                mins = t // 60
                secs = t % 60
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end="\r") # overwrite previous line 
                time.sleep(1)
                t -= 1
        t = input("Enter the time in seconds: ") 
        countdown(int(t))
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        
        def get_user_choice():
            user_input = input("Enter your input: ")
            return(user_input)
        user_choice = get_user_choice()
        
        def get_computer_choice():
            pred_list = ['Rock', 'Scissors', 'Paper']
            return(random.choice(pred_list))
        computer_choice = get_computer_choice()
        
        def pred_results():
            if prediction[0][0] > 0.5: #Rock
                return "Rock"
            elif prediction[0][1] > 0.5: #Paper
                return "Paper"
            elif prediction[0][2] > 0.5: #Scissors
                return "Scissors"
            else: #Nothing
                return "Nothing"
        real_pred = pred_results()

        def get_winner():
            if (user_choice == real_pred) & (computer_choice != real_pred): #User Won
                return "User Won"
            elif (computer_choice == real_pred) & (user_choice != real_pred): # Computer Won
                return "Computer Won"
            elif (computer_choice == real_pred) & (user_choice == real_pred): # Computer and User Won
                return "Draw"
            else: # Neither Won
                return "No Winner yet! Try Again"
        result = get_winner()
        print(result)

    elif k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break   
cam.release()
cv2.destroyAllWindows() 