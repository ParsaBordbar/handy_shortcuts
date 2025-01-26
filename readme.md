# Handy_shortcuts 🖐️

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

| Gesture       | Description                          | Example Shortcut                 |
|---------------|--------------------------------------|----------------------------------|
| **Fist**      | All fingers closed                   | Open Terminal (`Ctrl + Alt + T`) |
| **Peace Sign**| Index and middle fingers extended    | Open VS Code (`Win + 2`)         |
| **One**       | Index finger extended                | Open Filesystem (`Win + 3`)      |
| **Two**       | Index and middle fingers extended    | Open Spotify (`Win + 4`)         |
| **Three**     | Index, middle, and ring fingers extended | Open Calculator (`Win + 5`)  |
| **Four**      | All fingers extended                 | Open Notepad (`Win + 6`)         |
| **Like**      | Thumb extended, other fingers closed | Like a video (`Ctrl + L`)        |
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

python
Copy
shortcuts = [
    {
        'hotkey': ('win', '1'),
        'message': 'Google Chrome Launched',
        'gesture': 'like'  # Triggered by thumbs-up gesture
    },
    {
        'hotkey': ('win', '2'),
        'message': 'VS Code Launched',
        'gesture': 'peace'  # Triggered by peace sign
    },
    {
        'hotkey': ('ctrl', 'alt', 't'),
        'message': 'Terminal Launched',
        'gesture': 'fist'  # Triggered by fist gesture
    }
]

if you like to read more about the architecture of this project you can read more on the doc.md file.