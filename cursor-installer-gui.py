#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess
from pathlib import Path

class CursorInstallerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cursor Installer")
        self.root.geometry("400x400")
        
        # Configure style
        self.root.configure(bg='#f0f0f0')
        
        # Create main frame
        main_frame = tk.Frame(root, bg='#f0f0f0', padx=20, pady=20)
        main_frame.pack(expand=True, fill='both')
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="Cursor Editor Installer",
            font=('Helvetica', 16, 'bold'),
            bg='#f0f0f0'
        )
        title_label.pack(pady=(0, 20))
        
        # Check if Cursor is installed
        self.is_installed = self.check_installation()
        
        # Status frame
        status_frame = tk.Frame(main_frame, bg='#f0f0f0')
        status_frame.pack(fill='x', pady=(0, 20))
        
        # Installation status
        self.status_label = tk.Label(
            status_frame,
            text="Status: " + ("Installed" if self.is_installed else "Not installed"),
            font=('Helvetica', 10),
            bg='#f0f0f0',
            fg='#34C759' if self.is_installed else '#FF3B30'
        )
        self.status_label.pack(side='left')
        
        # Uninstall button (only if installed)
        if self.is_installed:
            self.uninstall_button = tk.Button(
                status_frame,
                text="Uninstall",
                command=self.uninstall,
                bg='#FF3B30',
                fg='white',
                font=('Helvetica', 10),
                padx=10,
                pady=5
            )
            self.uninstall_button.pack(side='right')
        
        # Description
        desc_label = tk.Label(
            main_frame,
            text="Select Cursor AppImage file to install",
            font=('Helvetica', 10),
            bg='#f0f0f0'
        )
        desc_label.pack(pady=(0, 20))
        
        # File selection button
        self.file_path = tk.StringVar()
        select_button = tk.Button(
            main_frame,
            text="Select AppImage",
            command=self.select_file,
            bg='#007AFF',
            fg='white',
            font=('Helvetica', 10),
            padx=20,
            pady=10
        )
        select_button.pack(pady=10)
        
        # Selected file label
        self.file_label = tk.Label(
            main_frame,
            text="No file selected",
            font=('Helvetica', 9),
            bg='#f0f0f0',
            wraplength=350
        )
        self.file_label.pack(pady=10)
        
        # Icon selection button
        self.icon_path = tk.StringVar()
        icon_button = tk.Button(
            main_frame,
            text="Select Custom Icon",
            command=self.select_icon,
            bg='#5856D6',
            fg='white',
            font=('Helvetica', 10),
            padx=20,
            pady=10
        )
        icon_button.pack(pady=10)
        
        # Selected icon label
        self.icon_label = tk.Label(
            main_frame,
            text="No icon selected",
            font=('Helvetica', 9),
            bg='#f0f0f0',
            wraplength=350
        )
        self.icon_label.pack(pady=10)
        
        # Install button
        self.install_button = tk.Button(
            main_frame,
            text="Install",
            command=self.install,
            bg='#34C759',
            fg='white',
            font=('Helvetica', 10),
            padx=20,
            pady=10,
            state='disabled'
        )
        self.install_button.pack(pady=10)
        
        # Message label
        self.message_label = tk.Label(
            main_frame,
            text="",
            font=('Helvetica', 9),
            bg='#f0f0f0',
            wraplength=350
        )
        self.message_label.pack(pady=10)
        
        # Download link
        link_label = tk.Label(
            main_frame,
            text="Download Cursor AppImage from cursor.com",
            font=('Helvetica', 9),
            bg='#f0f0f0',
            fg='blue',
            cursor='hand2'
        )
        link_label.pack(pady=10)
        link_label.bind('<Button-1>', lambda e: self.open_url('https://www.cursor.com/'))
    
    def check_installation(self):
        """Check if Cursor is installed"""
        try:
            # Check for Cursor*.AppImage in .local/bin/
            local_bin = os.path.expanduser('~/.local/bin')
            if os.path.exists(local_bin):
                for file in os.listdir(local_bin):
                    if file.startswith('Cursor') and file.endswith('.AppImage'):
                        return True
            
            return False
        except Exception as e:
            print(f"Error checking installation: {str(e)}")
            return False
    
    def select_file(self):
        file_path = filedialog.askopenfilename(
            title="Select Cursor AppImage",
            filetypes=[("AppImage files", "*.AppImage"), ("All files", "*.*")]
        )
        if file_path:
            self.file_path.set(file_path)
            self.file_label.config(text=os.path.basename(file_path))
            self.install_button.config(state='normal')
            self.message_label.config(text="")
    
    def select_icon(self):
        file_path = filedialog.askopenfilename(
            title="Select Icon File",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.ico"), ("All files", "*.*")]
        )
        if file_path:
            self.icon_path.set(file_path)
            self.icon_label.config(text=os.path.basename(file_path))
    
    def install(self):
        if not self.file_path.get():
            messagebox.showerror("Error", "Please select an AppImage file first")
            return
            
        try:
            # Get the absolute path of the installer script
            script_dir = os.path.dirname(os.path.abspath(__file__))
            installer_script = os.path.join(script_dir, 'install.py')
            
            # Check if installer script exists and is executable
            if not os.path.exists(installer_script):
                raise FileNotFoundError(f"Installer script not found at {installer_script}")
            if not os.access(installer_script, os.X_OK):
                os.chmod(installer_script, 0o755)
            
            # Prepare command with full path
            cmd = [installer_script, self.file_path.get()]
            if self.icon_path.get():
                cmd.extend(['--icon', self.icon_path.get()])
            
            print(f"Running command: {' '.join(cmd)}")  # Debug output
            
            # Run the installer script
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            print(f"Return code: {result.returncode}")  # Debug output
            print(f"stdout: {result.stdout}")  # Debug output
            print(f"stderr: {result.stderr}")  # Debug output
            
            if result.returncode == 0:
                self.message_label.config(
                    text="Installation successful!",
                    fg='#34C759'
                )
                messagebox.showinfo(
                    "Success",
                    "Cursor has been installed successfully!"
                )
                self.root.after(2000, self.root.destroy)
            else:
                error_msg = f"Installation failed:\n{result.stderr}"
                if result.stdout:
                    error_msg += f"\nOutput: {result.stdout}"
                self.message_label.config(
                    text=error_msg,
                    fg='#FF3B30'
                )
                messagebox.showerror(
                    "Error",
                    error_msg
                )
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            print(f"Exception details: {error_msg}")  # Debug output
            self.message_label.config(
                text=error_msg,
                fg='#FF3B30'
            )
            messagebox.showerror("Error", error_msg)
    
    def uninstall(self):
        if messagebox.askyesno("Confirm Uninstall", "Are you sure you want to uninstall Cursor?"):
            try:
                # Get the absolute path of the uninstaller script
                script_dir = os.path.dirname(os.path.abspath(__file__))
                uninstaller_script = os.path.join(script_dir, 'uninstall.py')
                
                # Check if uninstaller script exists and is executable
                if not os.path.exists(uninstaller_script):
                    raise FileNotFoundError(f"Uninstaller script not found at {uninstaller_script}")
                if not os.access(uninstaller_script, os.X_OK):
                    os.chmod(uninstaller_script, 0o755)
                
                print(f"Running command: {uninstaller_script}")  # Debug output
                
                # Run the uninstaller script
                result = subprocess.run([uninstaller_script], capture_output=True, text=True)
                
                print(f"Return code: {result.returncode}")  # Debug output
                print(f"stdout: {result.stdout}")  # Debug output
                print(f"stderr: {result.stderr}")  # Debug output
                
                if result.returncode == 0:
                    self.message_label.config(
                        text="Uninstallation successful!",
                        fg='#34C759'
                    )
                    messagebox.showinfo(
                        "Success",
                        "Cursor has been uninstalled successfully!"
                    )
                    self.root.after(2000, self.root.destroy)
                else:
                    error_msg = f"Uninstallation failed:\n{result.stderr}"
                    if result.stdout:
                        error_msg += f"\nOutput: {result.stdout}"
                    self.message_label.config(
                        text=error_msg,
                        fg='#FF3B30'
                    )
                    messagebox.showerror(
                        "Error",
                        error_msg
                    )
            except Exception as e:
                error_msg = f"Error: {str(e)}"
                print(f"Exception details: {error_msg}")  # Debug output
                self.message_label.config(
                    text=error_msg,
                    fg='#FF3B30'
                )
                messagebox.showerror("Error", error_msg)
    
    def open_url(self, url):
        import webbrowser
        webbrowser.open(url)

def main():
    root = tk.Tk()
    app = CursorInstallerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 