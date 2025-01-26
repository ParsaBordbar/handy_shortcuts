import cv2
import mediapipe as mp
import pyautogui
import time
from gestures import *

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)
mp_drawing = mp.solutions.drawing_utils

COOL_DOWN = 4
last_action_time = 0

def handle_gesture_action(gesture_detected, action, cool_down=True):
    global last_action_time
    current_time = time.time()
    
    if gesture_detected:
        if not cool_down or (current_time - last_action_time) > COOL_DOWN:
            action()
            last_action_time = current_time
            return True
    return False

# Webcam
video_cap = cv2.VideoCapture(0)

while video_cap.isOpened():
    success, frame = video_cap.read()
    if not success:
        break
    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    action_performed = False
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            if handle_gesture_action(
                is_one(hand_landmarks),
                lambda: pyautogui.hotkey('Win', '1'),
                cool_down=True
            ):
                cv2.putText(frame, "VS Code Launched", (50, 50), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                action_performed = True

            if handle_gesture_action(
                is_two(hand_landmarks),
                lambda: pyautogui.hotkey('Win', '2'),
                cool_down=True
            ):
                cv2.putText(frame, "VS Code Launched", (50, 50), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                action_performed = True

            
            if handle_gesture_action(
                is_three(hand_landmarks),
                lambda: pyautogui.hotkey('Win', '3'),
                cool_down=True
            ):
                cv2.putText(frame, "VS Code Launched", (50, 50), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                action_performed = True


            if handle_gesture_action(
                is_four(hand_landmarks),
                lambda: pyautogui.hotkey('Win', '4'),
                cool_down=True
            ):
                cv2.putText(frame, "VS Code Launched", (50, 50), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                action_performed = True

                
            if handle_gesture_action(
                is_V(hand_landmarks),
                lambda: pyautogui.hotkey('Win', '2'),
                cool_down=True
            ):
                cv2.putText(frame, "VS Code Launched", (50, 50), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                action_performed = True
            
            if not action_performed and handle_gesture_action(
                is_fist(hand_landmarks),
                lambda: pyautogui.hotkey('ctrl', 'alt', 't'),
                cool_down=True
            ):
                cv2.putText(frame, "Terminal Opened", (50, 50), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                action_performed = True
    

    cv2.imshow("Hand Detection", frame)    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
video_cap.release()
cv2.destroyAllWindows()