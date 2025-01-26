import cv2
import mediapipe as mp
import pyautogui
from utils.gestures import *
from shortcuts import *

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)
mp_drawing = mp.solutions.drawing_utils

last_action_time = 0

def main():
    # Webcam
    video_cap = cv2.VideoCapture(0)

    while video_cap.isOpened():
        success, frame = video_cap.read()
        if not success:
            break
        # use rgb for webcam frames
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        # flag to use for coll-down time of a gesture
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
