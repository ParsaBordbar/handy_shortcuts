from hand_landmarks import get_finger_data, get_extended_fingers

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
