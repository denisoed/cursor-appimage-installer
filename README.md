# Cursor AppImage Installer

A Python script for easily installing the Cursor Editor AppImage on Linux systems. This installer automates the process of making the AppImage executable, placing it in the correct directory, and creating a desktop entry.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
  - [Basic Installation](#basic-installation)
  - [Making Scripts Globally Available](#making-scripts-globally-available)
- [Usage](#usage)
  - [Basic Installation](#basic-installation-1)
  - [Uninstallation](#uninstallation)
  - [Command Line Arguments](#command-line-arguments)
- [What the Installer Does](#what-the-installer-does)
- [Desktop Integration](#desktop-integration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Features

- Automatically installs Cursor AppImage to `~/.local/bin`
- Creates desktop entry for easy access
- Makes AppImage executable
- Supports custom icon path
- Creates all necessary directories
- Integrates with system application menu
- Clean uninstallation script included
- Graphical user interface for easy installation

## Requirements

- Python 3.6 or higher
- Linux operating system
- Cursor AppImage file (download from [cursor.com](https://www.cursor.com/))
- tkinter (Python GUI library)

### Installing Requirements

On Ubuntu/Debian:
```bash
sudo apt-get update
sudo apt-get install python3-tk
```

On Fedora:
```bash
sudo dnf install python3-tkinter
```

On Arch Linux:
```bash
sudo pacman -S tk
```

On openSUSE:
```bash
sudo zypper install python3-tk
```

## Installation

### Basic Installation

1. Download the latest Cursor AppImage from [cursor.com](https://www.cursor.com/)
2. Clone this repository or download the installer script:
```bash
git clone https://github.com/yourusername/cursorInstaller.git
cd cursorInstaller
```

3. Make the installer scripts executable:
```bash
chmod +x install.py
chmod +x uninstall.py
chmod +x cursor-installer-gui.py
```

4. Install the desktop launcher (optional):
```bash
cp cursor-installer-gui.desktop ~/.local/share/applications/
```

### Using the GUI Installer

You can launch the GUI installer in two ways:
1. Double-click the Cursor Installer icon in your applications menu
2. Run from terminal:
```bash
./cursor-installer-gui.py
```

The GUI installer provides:
- Easy file selection through a file dialog
- Visual feedback during installation
- Direct link to download Cursor AppImage
- Error messages in case of installation problems

### Making Scripts Globally Available

To make the installer and uninstaller scripts available globally from anywhere in your terminal:

1. First, remove any existing symbolic links (if they exist):
```bash
rm -f ~/.local/bin/cursor-install
rm -f ~/.local/bin/cursor-uninstall
```

2. Create a symbolic link to the scripts in `~/.local/bin`:

```bash
ln -s "$(pwd)/install.py" ~/.local/bin/cursor-install
ln -s "$(pwd)/uninstall.py" ~/.local/bin/cursor-uninstall
```

After this, you can use the commands from anywhere:
```bash
cursor-install ./Cursor-x.x.x.AppImage
cursor-uninstall
```

## Usage

### Basic Installation

Before installing a new version, it's recommended to uninstall the old one:

```bash
cursor-uninstall
```

Then download the latest Cursor AppImage from the official website and place it in the cursorInstaller directory:

```bash
cursor-install ./Cursor-x.x.x.AppImage --icon custom.png
```

### Uninstallation

To completely remove Cursor from your system:

```bash
cursor-uninstall
```

This will remove:
- Cursor AppImage from `~/.local/bin`
- Desktop entry from `~/.local/share/applications`
- Configuration directory from `~/.config/Cursor`
- Cache directory from `~/.cache/Cursor`

To remove Cursor without cleaning the cache (useful for preserving settings between installations):

```bash
cursor-uninstall --save-cache
```

To remove Cursor while preserving both cache and configuration files:

```bash
cursor-uninstall --save-cache --save-config
```

### Command Line Arguments

- `--icon`: Specify a custom icon for the desktop entry
- `--save-cache`: Preserve the cache directory during uninstallation
- `--save-config`: Preserve the configuration directory during uninstallation

## What the Installer Does

- Makes the AppImage executable
- Places the AppImage in the correct directory
- Creates a desktop entry for easy access
- Supports custom icon path
- Creates all necessary directories
- Integrates with system application menu

## Desktop Integration

- The installer creates a desktop entry in `~/.local/share/applications`
- The desktop entry is integrated with the system application menu

## Troubleshooting

- If the installer fails, check the terminal output for any error messages
- If the desktop entry is not created, check the system's application menu
- If you get "command not found: cursor-install" after making scripts globally available:
  1. Make sure `~/.local/bin` is in your PATH:
     ```bash
     echo $PATH | grep ~/.local/bin
     ```
  2. If not, add it to your shell's configuration file (`~/.bashrc`, `~/.zshrc`, etc.):
     ```bash
     echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
     source ~/.bashrc
     ```
  3. Verify the symbolic links are created correctly:
     ```bash
     ls -l ~/.local/bin/cursor-*
     ```

## Contributing

- Fork the repository
- Create a new branch
- Make your changes
- Commit and push your changes
- Open a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.