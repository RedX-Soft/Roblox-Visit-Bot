# Roblox Visit Bot README


**Note:** This script is for educational purposes only. Using bots to manipulate Roblox game visits may violate Roblox’s Terms of Service. Use responsibly and ethically.

---

## **Features**
- Automates clicking the "Play" button to start a Roblox game.
- Waits for the game to load and then clicks the "Exit" button to close it.
- Tracks the total number of visits in the console.
- Displays progress dynamically in the console title.
- Includes error handling and retry mechanisms to ensure smooth operation.

---

## **Requirements**
### **Software Requirements**
1. **Python 3.6 or later**
2. Required Python libraries:
   - `pyautogui`
   - `time`

---

## **Setup and Installation**

### 1. Install Python Dependencies
Ensure you have Python installed. Install the required library by running:
```bash
pip install pyautogui
```

### 2. Prepare Button Images
Take screenshots of the "Play" and "Exit" buttons on the Roblox interface and save them as:
- `play.PNG`
- `exit.PNG`

Place these image files in the same directory as the script. Ensure the images are cropped and clear for accurate recognition.

### 3. Configure Script Parameters
Modify the following variables in the script as needed:
- `TIME_TO_LOAD_GAME`: Average time (in seconds) it takes to load a Roblox game.
- `TIME_BETWEEN_SESSIONS`: Time delay (in seconds) between botting sessions.
- `PLAY_BUTTON_IMAGE` and `EXIT_BUTTON_IMAGE`: File paths for the button images.

---

## **How to Run the Script**
1. Open a terminal or command prompt in the script’s directory.
2. Run the script using Python:
```bash
python main.py
```
3. The script will:
   - Locate the "Play" button and click it.
   - Wait for the game to load.
   - Locate the "Exit" button and click it.
   - Update the console with the total number of visits.

---

## **How the Script Works**
1. **Startup:**
   - The script sets the console title to display the bot’s status.

2. **Play Button Click:**
   - Locates the "Play" button using the `play.PNG` image.
   - Moves the cursor to the button and clicks it.

3. **Game Loading:**
   - Waits for the game to load (configurable using `TIME_TO_LOAD_GAME`).

4. **Exit Button Click:**
   - Locates the "Exit" button using the `exit.PNG` image.
   - Moves the cursor to the button and clicks it to close the game.

5. **Repeat:**
   - The process repeats after a short delay (configurable using `TIME_BETWEEN_SESSIONS`).

6. **Progress Tracking:**
   - Updates the console title and logs actions to track the number of visits.

---

## **Troubleshooting**
1. **Play or Exit Button Not Found:**
   - Ensure the `play.PNG` and `exit.PNG` images are accurate and cropped properly.
   - Adjust screen resolution and scaling if necessary.

2. **Script Exits Unexpectedly:**
   - Check for error messages in the console.
   - Ensure you have the required Python libraries installed.

3. **Slow Performance:**
   - Increase the delays (`TIME_TO_LOAD_GAME` and `TIME_BETWEEN_SESSIONS`) if your PC is slow or lagging.

---

## **Disclaimer**
This script is for educational purposes only. Using automation tools on Roblox could result in account bans or other consequences. Always adhere to Roblox's Terms of Service and use this script responsibly.
