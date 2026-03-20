# Key-Logger
This is a Python-based keyboard activity logger developed for cybersecurity learning purposes only.
It demonstrates how keyboard inputs can be captured, logged, and analyzed.
This file can be run directly in windows cmd (win+r -> cmd) and saves the keyboard keys pressed

------------------------------------------

⚙️ Installation

1️⃣ Clone the Repository
git clone https://github.com/your-username/keyboard-keylogger.git
cd keyboard-keylogger
2️⃣ Install Dependencies
pip install pynput pywin32

▶️ Usage Method 1️⃣:
Using this method, the terminal shoud remains open in background and for anonymous purpose use second method:
python keylogger.py

The program will start logging keyboard activity.
Press ESC key to stop logging.

▶️ Usage Method 2️⃣:
If you want to run anonymously without opening the terminal in background:
pythonw keylogger.py
Hint : after running this command you can close the terminal 

The program will start logging keyboard activity.
To close it : Task Manager -> python task -> end task.

------------
Logs will be saved in:
activity_log.txt
-------------------------------------------

🎯 Features

Logs keyboard keystrokes in real-time
Detects and records active window titles
Saves logs with timestamps
Tracks session start and end time

-------------------------------------------

🧰 Technologies Used

Python 3
pynput – for capturing keyboard input
pywin32 – for detecting active window

-------------------------------------------

👨‍💻 Author

Ketan Saini
Cybersecurity Enthusiast | Ethical Hacking Learner

