# DarkToLight Tray Application

**Version:** 0.1.0

A Windows 11 system tray application to toggle between Dark Mode and Light Mode with a simple tray icon, as per the PLANNING.md.

## Features
- Tray icon in the Windows task bar
- Toggle between Dark and Light modes with a click
- Moon icon for dark mode, sun icon for light mode

## Requirements
- Python 3.8+
- Windows 11
- Virtual environment recommended
- Install dependencies:
  ```sh
  pip install -r requirements.txt
  ```

## Usage
1. Activate your Python virtual environment.
2. Install requirements: `pip install -r requirements.txt`
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
