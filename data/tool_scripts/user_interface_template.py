```python
import tkinter as tk
from tkinter import messagebox
import json
import os
from dashboard import Dashboard
from config import CONFIG_DEFAULTS, USER_PREFERENCES
from api_interaction import API_KEY

class UserInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Government Security Operations Interface")
        self.master.geometry("800x600")

        self.load_user_preferences()
        self.create_menu()
        self.dashboard = Dashboard(self.master, self.user_preferences)

    def load_user_preferences(self):
        if os.path.exists(USER_PREFERENCES):
            with open(USER_PREFERENCES, 'r') as f:
                self.user_preferences = json.load(f)
        else:
            self.user_preferences = CONFIG_DEFAULTS

    def create_menu(self):
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.master.quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        tools_menu = tk.Menu(self.menu_bar, tearoff=0)
        tools_menu.add_command(label="Update API Key", command=self.update_api_key)
        self.menu_bar.add_cascade(label="Tools", menu=tools_menu)

        help_menu = tk.Menu(self.menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about_info)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)

    def update_api_key(self):
        new_key = simpledialog.askstring("Update API Key", "Enter the new API Key:")
        if new_key:
            global API_KEY
            API_KEY = new_key
            with open('data/api_keys.json', 'w') as f:
                json.dump({"api_key": API_KEY}, f)
            messagebox.showinfo("API Key", "API Key updated successfully!")

    def show_about_info(self):
        messagebox.showinfo("About", "Government Security Operations Interface\nVersion 1.0")

    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    ui = UserInterface(root)
    ui.run()
```