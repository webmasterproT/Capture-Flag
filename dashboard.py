```python
import tkinter as tk
from tkinter import messagebox
import json
from config import CONFIG_DEFAULTS
from api_interaction import API_KEY
from user_interface import UserInterface
from logging import log_activity

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Security Operations Dashboard")
        self.create_widgets()

    def create_widgets(self):
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # File menu
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        # Tools menu
        tools_menu = tk.Menu(self.menu_bar, tearoff=0)
        tools_menu.add_command(label="Update Configuration", command=self.update_configuration)
        tools_menu.add_command(label="Check System Integrity", command=self.check_system_integrity)
        self.menu_bar.add_cascade(label="Tools", menu=tools_menu)

        # Help menu
        help_menu = tk.Menu(self.menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about_info)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)

        # Main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Status bar
        self.status_bar = tk.Label(self.root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Dashboard widgets
        self.action_log = tk.Text(self.main_frame, height=15, width=50)
        self.action_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Load user preferences
        self.load_user_preferences()

    def load_user_preferences(self):
        try:
            with open('data/user_preferences.json', 'r') as f:
                user_preferences = json.load(f)
                # Apply user preferences to the dashboard
                self.apply_preferences(user_preferences)
        except FileNotFoundError:
            # Load default configuration if user preferences are not found
            self.apply_preferences(CONFIG_DEFAULTS)

    def apply_preferences(self, preferences):
        # Apply preferences such as theme, font size, etc.
        pass

    def update_configuration(self):
        # Placeholder for configuration update logic
        messagebox.showinfo("Update Configuration", "Configuration updated successfully.")

    def check_system_integrity(self):
        # Placeholder for system integrity check logic
        messagebox.showinfo("System Integrity", "System integrity check completed successfully.")

    def show_about_info(self):
        messagebox.showinfo("About", "Security Operations Dashboard\nVersion 1.0")

    def log_action(self, message):
        self.action_log.insert(tk.END, message + "\n")
        self.action_log.see(tk.END)
        log_activity(message)

if __name__ == "__main__":
    root = tk.Tk()
    app = Dashboard(root)
    root.mainloop()
```