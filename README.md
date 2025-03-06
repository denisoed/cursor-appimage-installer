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

## Requirements

- Python 3.6 or higher
- Linux operating system
- Cursor AppImage file

## Installation

### Basic Installation

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

### Making Scripts Globally Available

To make the installer and uninstaller scripts available globally from anywhere in your terminal:

1. Create a symbolic link to the scripts in `~/.local/bin`:

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

### Command Line Arguments

- `--icon`: Specify a custom icon for the desktop entry

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