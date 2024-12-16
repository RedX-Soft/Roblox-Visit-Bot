import pyautogui
import time
import os
from ctypes import windll

# Configurable parameters
PLAY_BUTTON_IMAGE = 'play.PNG'
EXIT_BUTTON_IMAGE = 'exit.PNG'
TIME_TO_LOAD_GAME = 25  # Seconds to load a Roblox game
TIME_BETWEEN_SESSIONS = 3  # Seconds to wait before starting the next session
botted = 0

def set_console_title(title):
    """Set the console window title."""
    windll.kernel32.SetConsoleTitleW(title)

def log_action(action):
    """Log actions to the console."""
    print(f"[INFO] {action}")

def locate_and_click(image, description, retry_attempts=3, delay_between_retries=2):
    """
    Locate an image on the screen and click it.
    Retry if not found within the defined attempts.
    """
    for attempt in range(retry_attempts):
        try:
            button_pos = pyautogui.locateOnScreen(image)
            if button_pos:
                pyautogui.moveTo(button_pos)
                pyautogui.click()
                log_action(f"{description} button clicked.")
                return True
            else:
                log_action(f"{description} button not found. Retrying...")
                time.sleep(delay_between_retries)
        except Exception as e:
            log_action(f"Error while locating {description} button: {e}")
    log_action(f"Failed to locate {description} button after {retry_attempts} attempts.")
    return False

def bot():
    """Main botting loop."""
    global botted
    while True:
        time.sleep(TIME_BETWEEN_SESSIONS)  # Allow Roblox to close fully before restarting
        log_action("Starting a new botting session...")

        # Click the play button
        if not locate_and_click(PLAY_BUTTON_IMAGE, "Play"):
            log_action("Exiting bot due to Play button not found.")
            break

        # Wait for the game to load
        log_action(f"Waiting {TIME_TO_LOAD_GAME} seconds for the game to load...")
        time.sleep(TIME_TO_LOAD_GAME)

        # Click the exit button
        if not locate_and_click(EXIT_BUTTON_IMAGE, "Exit"):
            log_action("Exiting bot due to Exit button not found.")
            break

        # Increment and update the botted count
        botted += 1
        log_action(f"Botting session complete. Total botted: {botted}.")
        set_console_title(f"Roblox Visit Bot ^| Botted: {botted}")

# Run the bot
if __name__ == "__main__":
    set_console_title(f"Roblox Visit Bot ^| Botted: {botted}")
    bot()
