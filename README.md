# DarkToLight Tray Application

**Version:** 0.01.6

A Windows 11 system tray application to toggle between Dark Mode and Light Mode with a simple tray icon. Designed for convenience, automation, and user customization.

---

## Features
- **Tray Icon:** Sits in the Windows system tray for quick access
- **Dark/Light Toggle:** Instantly switch between Windows 11 Dark and Light modes with a single click
- **Visual Feedback:** Moon icon for dark mode, sun icon for light mode
- **Batch File Launcher:** One-click batch file (`start_darktolight.bat`) to set up and start the app
- **Automatic Dependency Management:** Installs required Python libraries if missing
- **Virtual Environment Support:** Ensures isolated package management
- **Status Persistence:** Remembers your last mode (if implemented in future)
- **Extensible:** Easily add new features, such as auto-switch at sunset/sunrise or user preferences
- **Automatic Theme Switching:** Automatically changes to dark mode at sunset and light mode at sunrise based on your location (uses astral, prompts for city/coordinates on first run)
- **Limitations:** Double-clicking the tray icon is not supported due to Python environment limitations.

---

## Setup

### 1. Clone or Download
Clone this repo or download and extract the ZIP file.

### 2. Create a Virtual Environment (Recommended)
```sh
python -m venv venv
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

---

## Usage

### (A) Quick Start: Batch File
1. Double-click `start_darktolight.bat`.
   - Activates the virtual environment
   - Installs required libraries
   - Launches the tray app

### (B) Manual Start
1. Activate your Python virtual environment:
   ```sh
   venv\Scripts\activate
   ```
2. Install requirements:
   ```sh
   pip install -r requirements.txt
   ```
3. Launch the app:
   ```sh
   python tray_app.py
   ```

---

## Tray Icon & App Behavior
- **Tray Icon:** Appears in the system tray when running
- **Toggle:** Click the icon to switch between Dark and Light modes
- **Icon:** Sun = Light mode, Moon = Dark mode
- **Tooltip:** Shows current mode
- **Exit:** Right-click and select Exit (if menu implemented) or close the process manually

---

## How It Works
- Modifies Windows Registry key `AppsUseLightTheme` to switch modes
- No admin rights required (modifies current user settings)
- Safe to run repeatedly

---

## Environment & Configuration
- No environment variables required for default usage
- All config is local to your user account
- Python virtual environment strongly recommended

---

## Troubleshooting
- **Tray icon not visible:** Ensure the app is running and check the hidden icons area
- **Permissions error:** Run terminal as your user, not as admin
- **Missing dependencies:** Use the batch file or run `pip install -r requirements.txt`
- **Python not found:** Ensure Python 3.8+ is installed and added to PATH

---

## Contributing
- Fork the repo and submit a pull request
- Open issues for bugs or feature requests
- See TODO.md for planned features

---

## License
MIT
3. Run the app:
   ```sh
   python tray_app.py
   ```
4. Use the tray icon to toggle between Dark/Light modes.

## How it works
- Uses Windows Registry to toggle the theme:
    - **Dark Mode:** Sets `AppsUseLightTheme` to `0` in the registry
    - **Light Mode:** Sets `AppsUseLightTheme` to `1` in the registry
- Icon updates to reflect the current mode.

## Version History
- 0.1.0: Initial tray app with dark/light toggle

## Environment Variables
- No environment variables required for basic usage.

## License
MIT
