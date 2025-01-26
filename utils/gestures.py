from fingers_data import get_finger_data
import time
from utils.extended_fingers import get_extended_fingers

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

# Gesture detection functions
def is_V(hand_landmarks):
    fingers = get_finger_data(hand_landmarks)
    return (
        fingers['index']['index_tip'].y < fingers['index']['index_mcp'].y and
        fingers['middle']['middle_tip'].y < fingers['middle']['middle_mcp'].y and
        fingers['ring']['ring_tip'].y > fingers['ring']['ring_mcp'].y and
        fingers['pinky']['pinky_tip'].y > fingers['pinky']['pinky_mcp'].y
    )

def is_fist(hand_landmarks):
    fingers = get_finger_data(hand_landmarks)
    return (
        fingers['thumb']['thumb_tip'].x > fingers['thumb']['thumb_mcp'].x and
        fingers['index']['index_tip'].y > fingers['index']['index_mcp'].y and
        fingers['middle']['middle_tip'].y > fingers['middle']['middle_mcp'].y and
        fingers['ring']['ring_tip'].y > fingers['ring']['ring_mcp'].y and
        fingers['pinky']['pinky_tip'].y > fingers['pinky']['pinky_mcp'].y
    )


def is_one(hand_landmarks):
    fingers = get_finger_data(hand_landmarks)
    extended = get_extended_fingers(fingers)
    return (
        extended['index'] and 
        not any([extended['middle'], extended['ring'], extended['pinky']])
    )

def is_two(hand_landmarks):
    fingers = get_finger_data(hand_landmarks)
    extended = get_extended_fingers(fingers)
    return (
        extended['index'] and 
        extended['middle'] and 
        not any([extended['ring'], extended['pinky']])
    )

def is_three(hand_landmarks):
    fingers = get_finger_data(hand_landmarks)
    extended = get_extended_fingers(fingers)
    return (
        extended['index'] and 
        extended['middle'] and 
        extended['ring'] and 
        not extended['pinky']
    )

def is_four(hand_landmarks):
    fingers = get_finger_data(hand_landmarks)
    extended = get_extended_fingers(fingers)
    return (
        extended['index'] and 
        extended['middle'] and 
        extended['ring'] and 
        extended['pinky']
    )

def is_like(hand_landmarks):
    fingers = get_finger_data(hand_landmarks)
    extended = get_extended_fingers(fingers)
    return (
        extended['thumb'] and 
        not extended['index'] and 
        not extended['middle'] and
        not extended['ring'] and 
        not extended['pinky']
    )

def is_fu(hand_landmarks):
    fingers = get_finger_data(hand_landmarks)
    extended = get_extended_fingers(fingers)
    return (
        not extended['thumb'] and 
        not extended['index'] and 
        extended['middle'] and
        not extended['ring'] and 
        not extended['pinky']
    )
