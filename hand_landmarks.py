def get_finger_data(hand_landmarks):
    return {
        "thumb": {
            "thumb_cmc": hand_landmarks.landmark[1],
            "thumb_mcp": hand_landmarks.landmark[2],
            "thumb_ip": hand_landmarks.landmark[3],
            "thumb_tip": hand_landmarks.landmark[4],
        },
        "index": {
            "index_mcp": hand_landmarks.landmark[5],
            "index_pip": hand_landmarks.landmark[6],
            "index_dip": hand_landmarks.landmark[7],
            "index_tip": hand_landmarks.landmark[8],
        },
        "middle": {
            "middle_mcp": hand_landmarks.landmark[9],
            "middle_pip": hand_landmarks.landmark[10],
            "middle_dip": hand_landmarks.landmark[11],
            "middle_tip": hand_landmarks.landmark[12],
        },
        "ring": {
            "ring_mcp": hand_landmarks.landmark[13],
            "ring_pip": hand_landmarks.landmark[14],
            "ring_dip": hand_landmarks.landmark[15],
            "ring_tip": hand_landmarks.landmark[16],
        },
        "pinky": {
            "pinky_mcp": hand_landmarks.landmark[17],
            "pinky_pip": hand_landmarks.landmark[18],
            "pinky_dip": hand_landmarks.landmark[19],
            "pinky_tip": hand_landmarks.landmark[20],
        }
    }

def get_extended_fingers(fingers):
    return {
        'thumb': fingers['thumb']['thumb_tip'].y < fingers['thumb']['thumb_ip'].y,
        'index': fingers['index']['index_tip'].y < fingers['index']['index_pip'].y,
        'middle': fingers['middle']['middle_tip'].y < fingers['middle']['middle_pip'].y,
        'ring': fingers['ring']['ring_tip'].y < fingers['ring']['ring_pip'].y,
        'pinky': fingers['pinky']['pinky_tip'].y < fingers['pinky']['pinky_pip'].y
    }