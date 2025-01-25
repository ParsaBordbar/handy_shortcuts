import cv2
import mediapipe as mp
import pyautogui
from hand_landmarks import get_finger_data

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)
mp_drawing = mp.solutions.drawing_utils



def is_peace_sign(hand_landmarks):
    index_tip = hand_landmarks.landmark[8]
    middle_tip = hand_landmarks.landmark[12]
    ring_tip = hand_landmarks.landmark[16]
    pinky_tip = hand_landmarks.landmark[20]
    
    # Check if index and middle are up, others down
    return (index_tip.y < hand_landmarks.landmark[5].y and
            middle_tip.y < hand_landmarks.landmark[9].y and
            ring_tip.y > hand_landmarks.landmark[13].y and
            pinky_tip.y > hand_landmarks.landmark[17].y)

def is_fist_sign(hand_landmarks):
    return (get_finger_data)

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
                pyautogui.hotkey('ctrl', 'alt', 't')  # Open terminal
                cv2.putText(frame, "TERMINAL OPENED", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                break
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Display frame
    cv2.imshow("Hand Detection", frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
video_cap.release()
cv2.destroyAllWindows()