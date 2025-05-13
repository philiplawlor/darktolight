import sys
import threading
import time
import os
import subprocess
from pathlib import Path
from typing import Optional
import math

try:
    import pystray
    from PIL import Image, ImageDraw
except ImportError:
    print("pystray and Pillow are required. Please install them in your virtual environment: pip install pystray pillow")
    sys.exit(1)

# Reason: Registry manipulation is required to toggle Windows Dark/Light mode
import winreg

def is_dark_mode() -> bool:
    """
    Check if Windows is currently in Dark Mode.

    Returns:
        bool: True if Dark Mode is enabled, False if Light Mode is enabled.
    """
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize") as key:
            value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
            return value == 0
    except FileNotFoundError:
        # Default to Light Mode if key does not exist
        return False

def set_dark_mode(enable: bool) -> None:
    """
    Set Windows Dark Mode on or off.

    Args:
        enable (bool): True to enable Dark Mode, False for Light Mode.
    """
    key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize"
    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path) as key:
        winreg.SetValueEx(key, "AppsUseLightTheme", 0, winreg.REG_DWORD, 0 if enable else 1)

def create_image(is_dark: bool) -> Image.Image:
    """
    Create a tray icon image (moon for dark, sun for light).

    Args:
        is_dark (bool): Whether to create the dark mode icon.

    Returns:
        Image.Image: The generated icon.
    """
    # 64x64 icon
    img = Image.new('RGBA', (64, 64), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    if is_dark:
        # Moon icon
        draw.ellipse((16, 16, 48, 48), fill=(180, 180, 180, 255))
        draw.ellipse((28, 16, 60, 48), fill=(0, 0, 0, 0))
    else:
        # Sun icon
        draw.ellipse((16, 16, 48, 48), fill=(255, 221, 51, 255))
        for i in range(8):
            angle = i * 45
            x = 32 + 24 * math.cos(math.radians(angle))
            y = 32 + 24 * math.sin(math.radians(angle))
            draw.line((32, 32, x, y), fill=(255, 221, 51, 255), width=4)
    return img

def toggle_mode(icon: pystray.Icon, item=None):
    """
    Toggle between Dark and Light mode and update the tray icon.
    """
    dark = is_dark_mode()
    set_dark_mode(not dark)
    icon.icon = create_image(not dark)
    icon.title = f"{'Dark' if not dark else 'Light'} Mode"

def quit_app(icon: pystray.Icon, item=None):
    icon.stop()

def main():
    """
    Main entry point for the tray application.
    Handles left-click toggling if supported by pystray, otherwise uses menu.
    """
    dark = is_dark_mode()
    icon = pystray.Icon(
        "DarkToLight",
        create_image(dark),
        f"{'Dark' if dark else 'Light'} Mode",
        menu=pystray.Menu(
            pystray.MenuItem('Toggle Dark/Light', lambda icon, item: toggle_mode(icon)),
            pystray.MenuItem('Quit', lambda icon, item: quit_app(icon))
        )
    )
    # Try to use on_click if available (not available in all backends)
    if hasattr(icon, 'on_click'):
        icon.on_click = lambda icon, event: toggle_mode(icon)
    else:
        print("Left-click toggle is not supported in this backend. Use the menu to toggle mode.")
    icon.run()

if __name__ == "__main__":
    main()
