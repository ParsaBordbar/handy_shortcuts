from hand_landmarks import get_finger_data

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
    