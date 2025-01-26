def get_extended_fingers(fingers):
    return {
        'thumb': fingers['thumb']['thumb_tip'].y < fingers['thumb']['thumb_ip'].y,
        'index': fingers['index']['index_tip'].y < fingers['index']['index_pip'].y,
        'middle': fingers['middle']['middle_tip'].y < fingers['middle']['middle_pip'].y,
        'ring': fingers['ring']['ring_tip'].y < fingers['ring']['ring_pip'].y,
        'pinky': fingers['pinky']['pinky_tip'].y < fingers['pinky']['pinky_pip'].y
    }
