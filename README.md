# GestureOS

GestureOS is a computer interaction system that allows users to control their computer using **hand gestures detected through a camera**. The project uses computer vision and machine learning techniques to recognize specific hand poses and translate them into system actions.

The goal of GestureOS is to create a more **intuitive, touch-free interface** that allows users to perform common computer tasks without using a keyboard or mouse.

---

## Features

- Hand gesture recognition using a webcam  
- Gesture-based system activation and control  
- Custom gesture detection with configurable delays  
- Visual feedback through a camera interface  
- Real-time gesture processing  
- Lightweight and easily extendable architecture  

---

## How It Works

GestureOS uses computer vision to track **hand landmarks** from the webcam feed. Specific combinations of finger positions are interpreted as gestures, which trigger predefined computer actions.

The system continuously analyzes the camera input and determines whether a gesture has been held long enough to activate a command, helping prevent accidental activations.

---

## Technologies Used

- **Python**
- **OpenCV**
- **MediaPipe**
- **PyAutoGUI**
- Computer Vision techniques

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/GestureOS.git
```

Enter the project folder:

```bash
cd GestureOS
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the main script:

```bash
python main.py
```

Make sure your webcam is connected and accessible before running the program.

---

## Project Status

🚧 GestureOS is currently **under development**.  
New gestures, system integrations, and interface improvements are planned for future updates.

---

## Future Improvements

- Additional gesture commands
- Custom gesture configuration
- Graphical settings interface
- Multi-gesture combinations
- Performance optimization
- Cross-platform improvements

---

## Author

**Fernando Santillán Rodríguez**
