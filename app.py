import cv2
import mediapipe as mp
import pyautogui
import time
from hand_landmarks import get_finger_data

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)
mp_drawing = mp.solutions.drawing_utils


def is_peace_sign(hand_landmarks):
    fingers = get_finger_data(hand_landmarks)

    thumb_tip = fingers['thumb']['thumb_tip']
    thumb_bottom = fingers['thumb']['thumb_mcp']

    index_tip = fingers['index']['index_tip']
    index_bottom = fingers['index']['index_mcp']

    middle_tip = fingers['middle']['middle_tip']
    middle_bottom = fingers['middle']['middle_mcp']

    ring_tip = fingers['ring']['ring_tip']
    ring_bottom = fingers['ring']['ring_mcp']
    
    pinky_tip = fingers['pinky']['pinky_tip']
    pinky_bottom = fingers['pinky']['pinky_mcp']

    return (index_tip.y < index_bottom.y and
            middle_tip.y < middle_bottom.y and
            ring_tip.y > ring_bottom.y and
            pinky_tip.y > pinky_bottom.y and 
            thumb_tip.y < thumb_bottom.y )


def is_fist_sign(hand_landmarks):
    fingers = get_finger_data(hand_landmarks)

    thumb_tip = fingers['thumb']['thumb_tip']
    thumb_bottom = fingers['thumb']['thumb_mcp']

    index_tip = fingers['index']['index_tip']
    index_bottom = fingers['index']['index_mcp']

    middle_tip = fingers['middle']['middle_tip']
    middle_bottom = fingers['middle']['middle_mcp']

    ring_tip = fingers['ring']['ring_tip']
    ring_bottom = fingers['ring']['ring_mcp']
    
    pinky_tip = fingers['pinky']['pinky_tip']
    pinky_bottom = fingers['pinky']['pinky_mcp']

    return (index_tip.y < index_bottom.y and
            middle_tip.y < middle_bottom.y and
            ring_tip.y < ring_bottom.y and
            pinky_tip.y < pinky_bottom.y and 
            thumb_tip.y < thumb_bottom.y )

# webcam
video_cap = cv2.VideoCapture(0)
while video_cap.isOpened():
    success, frame = video_cap.read()
    if not success:
        break
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Detect gestures
            if is_peace_sign(hand_landmarks):
                cv2.putText(frame, "Open Vs code", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                pyautogui.hotkey('win', '2')
                break
            if is_fist_sign(hand_landmarks):
                cv2.putText(frame, "TERMINAL OPENED", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                pyautogui.hotkey('ctrl', 'alt', 't')
                
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Display frame
    cv2.imshow("Hand Detection", frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_cap.release()
cv2.destroyAllWindows()