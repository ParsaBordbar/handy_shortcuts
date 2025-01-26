import cv2
import mediapipe as mp
import pyautogui
from utils.gestures import *
from configs.shortcuts import shortcuts

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)
mp_drawing = mp.solutions.drawing_utils


def main():
    # Webcam
    try:
        video_cap = cv2.VideoCapture(0)
        if not video_cap.isOpened():
            raise RuntimeError("Could not open webcam.")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

    gesture_to_shortcut = {
        is_one: shortcuts[0],
        is_two: shortcuts[1],
        is_three: shortcuts[2],
        is_four: shortcuts[3],
        is_fist: shortcuts[4],
        is_V: shortcuts[5],
    }

    while video_cap.isOpened():
        success, frame = video_cap.read()
        if not success:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                # Dynamic gesture handling
                for gesture_func, shortcut in gesture_to_shortcut.items():
                    if handle_gesture_action(
                        gesture_func(hand_landmarks),
                        lambda: pyautogui.hotkey(*shortcut['hotkey']),
                        cool_down=True
                    ):
                        cv2.putText(frame, shortcut['message'], (50, 50), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        break

        cv2.imshow("Hand Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()