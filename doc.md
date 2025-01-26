This project uses the architecture of extensions, meaning we have a core main function/component (main func in app)
and the other modules are extensions of that 

## Architecture 🏗️

The project follows an **extensible architecture** with a **core main function** and **modular extensions**. This design adheres to software engineering principles such as **separation of concerns**, **modularity**, and **extensibility**.

### Core Components
1. **Main Function (`app.py`)**:
   - Initializes the webcam and MediaPipe hand tracking.
   - Processes frames and detects gestures.
   - Coordinates between gesture detection and shortcut execution.

2. **Extensions**:
   - **Gesture Detection (`utils/gestures.py`)**: Contains functions to detect specific gestures (e.g., `is_like`, `is_fist`).
   - **Shortcut Configuration (`configs/shortcuts.py`)**: Stores gesture-to-shortcut mappings.
   - **Finger Data (`utils/finger_data.py`)**: Provides utility functions to extract and process finger landmarks.

### Software Engineering Principles
- **Separation of Concerns**: Each module has a single responsibility (e.g., gesture detection, shortcut management).
- **Modularity**: New gestures and shortcuts can be added without modifying the core logic.
- **Extensibility**: The system is designed to support additional features (e.g., new gestures, platforms) with minimal changes.
- **Reusability**: Utility functions like `get_finger_data` and `get_extended_fingers` are reusable across the project.

## UML Diagrams

### Class Diagram
```plaintext
+-------------------+       +-------------------+       +-------------------+
|   HandDetector    |       |   GestureHandler  |       |   ShortcutManager |
+-------------------+       +-------------------+       +-------------------+
| - video_cap       |       | - gesture_funcs   |       | - shortcuts       |
| - hands           |       | - last_action_time|       +-------------------+
| - mp_drawing      |       | - COOLDOWN        |       | + get_shortcut()  |
+-------------------+       +-------------------+       | + trigger_action()|
| + detect_gesture()|       | + handle_gesture()|       +-------------------+
| + draw_landmarks()|       +-------------------+
+-------------------+
        |                           |
        |                           |
        v                           v
+--------------------+      +-------------------------+
|   FingerData       |      |      GestureUtils       |
+--------------------+      +-------------------------+
| + get_finger_data()|      | + get_extended_fingers()|
+--------------------+      | + is_V()                |
                            | + is_fist()             |
                            | + is_one()              |
                            | + is_two()              |
                            | + is_three()            |
                            | + is_four()             |
                            | + is_like()             |
                            | + is_fu()               |
                            +-------------------------+

```
## Sequence Diagram

User -> HandDetector: Start Webcam 

HandDetector -> MediaPipe: Process Frame

MediaPipe --> HandDetector: Return Hand Landmarks

HandDetector -> FingerData: Get Finger Data

FingerData --> HandDetector: Return Finger Landmarks

HandDetector -> GestureUtils: Detect Gesture

GestureUtils --> HandDetector: Return Gesture Type

HandDetector -> GestureHandler: Handle Gesture

GestureHandler -> ShortcutManager: Get Shortcut

ShortcutManager --> GestureHandler: Return Shortcut

GestureHandler -> PyAutoGUI: Trigger Action

PyAutoGUI --> System: Execute Shortcut

System --> User: Perform Action (e.g., Open App)


## Use Cases

1. #### Detect Hand Gestures
Actor: User

Description: The system detects hand gestures using a webcam and MediaPipe's hand landmark model.

Flow:

User shows hand to the webcam.

System captures the frame and processes it using MediaPipe.

System identifies hand landmarks and maps them to gestures using get_finger_data.


2. #### Map Gestures to Shortcuts
Actor: System

Description: The system maps detected gestures to predefined shortcuts using gesture detection functions.

Flow:

System detects a gesture (e.g., "V sign").

System looks up the gesture in the gesture_to_shortcut mapping.

System retrieves the associated shortcut.


3. #### Trigger Shortcut Actions
Actor: System

Description: The system triggers the mapped shortcut action using PyAutoGUI.

Flow:

System identifies the shortcut for the detected gesture.

System uses PyAutoGUI to simulate the keyboard shortcut.

System displays a confirmation message on the screen.


4. #### Handle Cooldown
Actor: System

Description: The system enforces a cooldown period between gesture actions to prevent spamming.

Flow:

System detects a gesture.

System checks if the cooldown period has passed since the last action.

If cooldown has passed, the system triggers the action and resets the timer.


5. #### Display Feedback
Actor: System

Description: The system provides visual feedback on the webcam feed when a gesture is detected and an action is triggered.

Flow:

System detects a gesture and triggers an action.

System overlays a text message (e.g., "VS Code Launched") on the webcam feed.

User sees the feedback in real-time.


6. #### Check Extended Fingers
Actor: System

Description: The system checks which fingers are extended using get_extended_fingers.

Flow:

System retrieves finger landmarks using get_finger_data.

System checks if each finger is extended using get_extended_fingers.

System returns a dictionary of extended finger states.


7. #### Detect Specific Gestures
Actor: System

Description: The system detects specific gestures (e.g., "V sign", "fist", "like") using gesture detection functions.

Flow:

System retrieves finger landmarks using get_finger_data.

System checks gesture conditions using the appropriate function (e.g., is_V).

System returns True if the gesture is detected, otherwise False.
