# Handy_shortcuts 🖐️


https://github.com/user-attachments/assets/d340eb60-6723-4613-afb4-446b5702fd85


Welcome to the **Handy_shortcuts**! This project allows you to control your computer using hand gestures, making it easier to launch applications, execute commands, and perform tasks without touching your keyboard or mouse. 
I wanted it to be customable so feel free to custom it for own use cases!

---

## Features

- **Hand Gesture Detection**: Detect various hand gestures like thumbs-up, fist, peace sign (V), and more.
- **Customizable Shortcuts**: Map gestures to system shortcuts (e.g., open apps, execute commands).
- **Real-Time Feedback**: Visual feedback on the webcam feed when gestures are detected.
- **Cool-down System**: Prevent accidental repeated triggers with a configurable cool-down timer.
- **Cross-Platform**: Works on Linux, Windows, and macOS (with appropriate shortcut configurations).

---

## Supported Gestures 🖐️

Here are the gestures currently supported by the system:

| Gesture       | Description                             | Example Shortcut                 |
|---------------|-----------------------------------------|----------------------------------|
| **Fist**      | All fingers closed                      | Open Terminal (`Ctrl + Alt + T`) |
| **Peace Sign**| Index and middle fingers extended       | Open VS Code (`Win + 2`)         |
| **One**       | Index finger extended                   | Open Filesystem (`Win + 4`)      |
| **Two**       | Index and middle fingers extended       | Open Spotify (`Win + 3`)         |
| **Three**     | Index, middle, and ring fingers extended| Open Calculator (`Win + 5`)      |
| **Four**      | All fingers extended                    | Change the Desktop (`Win + F1`)  |
| **Like**      | Thumb extended, other fingers closed    | Screen Shot (`alt` + printsc)    |
---

## Installation 🚀

Clone the repository:
   ```bash
   git clone https://github.com/your-username/gesture-shortcut-system.git
   cd gesture-shortcut-system
   ```
   ```bash
   pip install -r requirements.txt
   ```
   ```bash
   python3 app.py
   ```

## Configuration ⚙️
You can customize the gestures and shortcuts by editing the configs/shortcuts.py file:

```python
Copy
shortcuts = [
 {
    # Mapped to gesture 4
    'hotkey': ('Win', '4'),
    'message': 'Filesystem Launched'
 },
 {
    # Mapped to gesture Like!     
    'hotkey': ('ctrl', 'alt', 't'),
    'message': 'New Terminal'
 },
 {
    # Mapped to gesture V! -> used for VS code!
    'hotkey': ('Win', '2'),
    'message': 'VS Code Launched'
 },
]
```

## Use Cases 📋
Detect Hand Gestures: The system detects hand gestures using a webcam and MediaPipe.

Map Gestures to Shortcuts: Gestures are mapped to predefined shortcuts.

Trigger Shortcut Actions: The system executes shortcuts using PyAutoGUI.

Handle Cooldown: A cooldown timer prevents repeated triggers.

Display Feedback: Visual feedback is shown on the webcam feed.

## Contributing 🤝
If youre intreted to add new gestures, improve the code, or fix bugs, please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeature).

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature/YourFeature).

Open a pull request.

## Architecture 🏗️
if you like to read more about the architecture of this project you can read more on the doc.md file. [View Documentation](doc.md)
