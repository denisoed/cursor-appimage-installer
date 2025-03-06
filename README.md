# Cursor AppImage Installer

A Python script for easily installing the Cursor Editor AppImage on Linux systems. This installer automates the process of making the AppImage executable, placing it in the correct directory, and creating a desktop entry.

## Features

- Automatically installs Cursor AppImage to `~/.local/bin`
- Creates desktop entry for easy access
- Makes AppImage executable
- Supports custom icon path
- Creates all necessary directories
- Integrates with system application menu
- Clean uninstallation script included

## Requirements

- Python 3.6 or higher
- Linux operating system
- Cursor AppImage file

## Installation

1. Clone this repository or download the installer script:
```bash
git clone https://github.com/yourusername/cursorInstaller.git
cd cursorInstaller
```

2. Make the installer script executable:
```bash
chmod +x install.py
chmod +x uninstall.py
```

## Usage

### Basic Installation

Download the latest Cursor AppImage from the official website and place it in the cursorInstaller directory:

```bash
./install.py ./Cursor-x.x.x.AppImage --icon custom.png
```

### Uninstallation

To completely remove Cursor from your system:

```bash
./uninstall.py
```

This will remove:
- Cursor AppImage from `~/.local/bin`
- Desktop entry from `~/.local/share/applications`
- Configuration directory from `~/.config/Cursor`
- Cache directory from `~/.cache/Cursor`

### Command Line Arguments

For install.py:
- `appimage`: Path to the Cursor AppImage file (required)
- `--icon`: Path to a custom icon file (optional)

## What the Installer Does

1. Creates necessary directories:
   - `~/.local/bin` for the AppImage
   - `~/.local/share/applications` for the desktop entry

2. Makes the AppImage executable

3. Copies the AppImage to `~/.local/bin`

4. Creates a desktop entry with:
   - Application name and description
   - Executable path
   - Icon
   - File associations
   - Application categories
   - Search keywords

## Desktop Integration

After installation, Cursor Editor will be available in your system's application menu under the "Development" category. You can:

- Launch it from the application menu
- Search for "Cursor" in your system's application launcher
- Open files directly with Cursor Editor
- Pin it to your dock or favorites

## Troubleshooting

If you encounter any issues:

1. Ensure the AppImage file exists and is accessible
2. Check if you have write permissions in `~/.local/bin` and `~/.local/share/applications`
3. Verify that Python 3.6 or higher is installed
4. Make sure the installer script is executable

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is open source and available under the MIT License. 