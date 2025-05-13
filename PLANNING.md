# DarkToLight Windows Tray - Project Planning

## Project Overview
This project implements a Windows 11 Task Bar Tray application that allows users to change from Dark Mode to Light Mode and back.

### MVP
- [ ] Show a tray icon in the task bar
- [ ] Allow users to change from Dark Mode to Light Mode and back

### Future Features
- [ ] Allow users to set a default mode
- [ ] Automatically switch to the opposite mode at sunset and sunrise
- [ ] Allow users to double click the tray icon to switch modes or click and hold to open a menu if windows does not allow double click.
- [ ] show a moon icon when it is light and a sun icon when it is dark

## Tech Stack
- **Backend**: Windows

## Commands
In PowerShell the commands to change the theme are:
- DarkMode: New-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize -Name AppsUseLightTheme -Value 0 -Type Dword -Force
- LightMode: Remove-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize -Name AppsUseLightTheme
