#!/usr/bin/env python3

import os
import sys
import shutil
import argparse
from pathlib import Path

class CursorUninstaller:
    """Class responsible for uninstalling Cursor and removing all associated files"""
    
    def __init__(self, save_cache=False, save_config=False):
        self.home_dir = Path.home()
        self.bin_dir = self.home_dir / '.local' / 'bin'
        self.desktop_dir = self.home_dir / '.local' / 'share' / 'applications'
        self.config_dir = self.home_dir / '.config' / 'Cursor'
        self.cache_dir = self.home_dir / '.cache' / 'Cursor'
        self.save_cache = save_cache
        self.save_config = save_config
        
    def remove_appimage(self) -> None:
        """Remove Cursor AppImage from ~/.local/bin"""
        try:
            cursor_files = list(self.bin_dir.glob('Cursor-*.AppImage'))
            if cursor_files:
                for file in cursor_files:
                    file.unlink()
                print(f"✓ Removed Cursor AppImage from {self.bin_dir}")
            else:
                print("ℹ No Cursor AppImage found in ~/.local/bin")
        except Exception as e:
            print(f"⚠ Error removing AppImage: {e}")

    def remove_desktop_entry(self) -> None:
        """Remove Cursor desktop entry"""
        try:
            desktop_file = self.desktop_dir / 'cursor-editor.desktop'
            if desktop_file.exists():
                desktop_file.unlink()
                print(f"✓ Removed desktop entry from {self.desktop_dir}")
            else:
                print("ℹ No desktop entry found")
        except Exception as e:
            print(f"⚠ Error removing desktop entry: {e}")

    def remove_config(self) -> None:
        """Remove Cursor configuration directory"""
        if self.save_config:
            print("ℹ Preserving configuration directory (--save-config flag used)")
            return
            
        try:
            if self.config_dir.exists():
                shutil.rmtree(self.config_dir)
                print(f"✓ Removed configuration directory: {self.config_dir}")
            else:
                print("ℹ No configuration directory found")
        except Exception as e:
            print(f"⚠ Error removing configuration directory: {e}")

    def remove_cache(self) -> None:
        """Remove Cursor cache directory"""
        if self.save_cache:
            print("ℹ Preserving cache directory (--save-cache flag used)")
            return
            
        try:
            if self.cache_dir.exists():
                shutil.rmtree(self.cache_dir)
                print(f"✓ Removed cache directory: {self.cache_dir}")
            else:
                print("ℹ No cache directory found")
        except Exception as e:
            print(f"⚠ Error removing cache directory: {e}")

    def uninstall(self) -> None:
        """Run full uninstallation process"""
        print("\nStarting Cursor uninstallation...\n")
        
        self.remove_appimage()
        self.remove_desktop_entry()
        self.remove_config()
        self.remove_cache()
        
        print("\nUninstallation completed successfully!")
        print("Cursor has been removed from your system.")

def main():
    parser = argparse.ArgumentParser(description='Uninstall Cursor Editor')
    parser.add_argument('--save-cache', action='store_true', help='Preserve the cache directory during uninstallation')
    parser.add_argument('--save-config', action='store_true', help='Preserve the configuration directory during uninstallation')
    args = parser.parse_args()

    try:
        uninstaller = CursorUninstaller(save_cache=args.save_cache, save_config=args.save_config)
        uninstaller.uninstall()
    except Exception as e:
        print(f"\n⚠ Error during uninstallation: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main() 