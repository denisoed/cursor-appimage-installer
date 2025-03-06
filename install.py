#!/usr/bin/env python3

import os
import sys
import shutil
import argparse
from pathlib import Path
from typing import Optional

class CursorInstaller:
    """Class responsible for installing Cursor AppImage and creating desktop entry"""
    
    def __init__(self, appimage_path: str, icon_path: Optional[str] = None):
        self.appimage_path = os.path.abspath(appimage_path)
        self.icon_path = os.path.abspath(icon_path) if icon_path else None
        self.app_name = os.path.basename(self.appimage_path)
        self.install_dir = os.path.expanduser('~/.local/bin')
        self.desktop_dir = os.path.expanduser('~/.local/share/applications')
        
    def create_directories(self) -> None:
        """Create necessary directories if they don't exist"""
        os.makedirs(self.install_dir, exist_ok=True)
        os.makedirs(self.desktop_dir, exist_ok=True)
        
    def make_executable(self) -> None:
        """Make AppImage file executable"""
        try:
            os.chmod(self.appimage_path, 0o755)
            print(f"Made {self.app_name} executable")
        except Exception as e:
            print(f"Error making file executable: {e}")
            sys.exit(1)
            
    def install_appimage(self) -> str:
        """Install AppImage to ~/.local/bin"""
        try:
            destination = os.path.join(self.install_dir, self.app_name)
            shutil.copy2(self.appimage_path, destination)
            print(f"Installed {self.app_name} to {destination}")
            return destination
        except Exception as e:
            print(f"Error installing AppImage: {e}")
            sys.exit(1)
            
    def create_desktop_entry(self, installed_path: str) -> None:
        """Create .desktop file for the application"""
        desktop_file = os.path.join(self.desktop_dir, 'cursor-editor.desktop')
        
        try:
            with open(desktop_file, 'w') as f:
                f.write(f"""[Desktop Entry]
Name=Cursor Editor
Comment=The IDE that helps you code faster
Exec={installed_path} --no-sandbox
Icon={self.icon_path if self.icon_path else 'cursor-editor'}
Type=Application
Categories=Development;IDE;
Terminal=false
StartupWMClass=Cursor
MimeType=text/plain;inode/directory;
Keywords=cursor;editor;ide;
""")
            
            # Make desktop file executable
            os.chmod(desktop_file, 0o755)
            print(f"Created desktop entry at {desktop_file}")
            
        except Exception as e:
            print(f"Error creating desktop entry: {e}")
            sys.exit(1)
            
    def install(self) -> None:
        """Run full installation process"""
        print("Starting Cursor installation...")
        
        self.create_directories()
        self.make_executable()
        installed_path = self.install_appimage()
        self.create_desktop_entry(installed_path)
        
        print("\nInstallation completed successfully!")
        print("You can now launch Cursor from your applications menu")

def main():
    parser = argparse.ArgumentParser(description='Install Cursor AppImage')
    parser.add_argument('appimage', help='Path to Cursor AppImage file')
    parser.add_argument('--icon', help='Path to icon file (optional)', default=None)
    
    args = parser.parse_args()
    
    if not os.path.exists(args.appimage):
        print(f"Error: AppImage file not found at {args.appimage}")
        sys.exit(1)
        
    if args.icon and not os.path.exists(args.icon):
        print(f"Error: Icon file not found at {args.icon}")
        sys.exit(1)
    
    installer = CursorInstaller(args.appimage, args.icon)
    installer.install()

if __name__ == '__main__':
    main()
