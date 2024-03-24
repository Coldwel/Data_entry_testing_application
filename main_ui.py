# main_ui.py
from tkinter import ttk
import tkinter as tk
from second_window_ui import SecondWindow
import json
from controller import Controller

with open('config.json') as f:
    data = json.load(f)

# Google color theme
BACKGROUND = data['background']
PRIMARY_COLOR = data['primary_color']
SECONDARY = data['secondary']
THIRD = data['third']
FOURTH = data['fourth']
SOFTWARE_VERSION = data['software_version']


class MainUserInterface:

    def __init__(self):
        self.entry_data = {}
        self.window = tk.Tk()
        self.window.title("Employee Interface")

    def set_controller(self, controller):
        self.controller = controller

    def shift_listbox(self, frame):
        listbox = ttk.Combobox(frame, state="readonly",
                               values=["1st Shift", "2nd Shift", "3rd shift"])
        self.entry_data["shift"] = listbox
        return listbox

    def main_window(self):
        frame = tk.Frame(self.window)
        frame.configure(background=BACKGROUND)
        frame.grid()

        name_label = tk.Label(frame, text="Last and first name:")
        name_label.configure(background=BACKGROUND, fg=PRIMARY_COLOR, font=("Arial", 14, "bold"))
        name_label.grid(row=0, column=0, padx=15, pady=15)

        date_label = tk.Label(frame, text="Date:")
        date_label.configure(background=BACKGROUND, fg=SECONDARY, font=("Arial", 14, "bold"))
        date_label.grid(row=1, column=0, padx=15, pady=15)

        shift_label = tk.Label(frame, text="Shift:")
        shift_label.configure(background=BACKGROUND, fg=FOURTH, font=("Arial", 14, "bold"))
        shift_label.grid(row=2, column=0, padx=15, pady=15)

        employee_id_label = tk.Label(frame, text="Employee ID:")
        employee_id_label.configure(background=BACKGROUND, fg=THIRD, font=("Arial", 14, "bold"))
        employee_id_label.grid(row=3, column=0, padx=15, pady=15)

        location_label = tk.Label(frame, text="Location:")
        location_label.configure(background=BACKGROUND, fg=PRIMARY_COLOR, font=("Arial", 14, "bold"))
        location_label.grid(row=4, column=0, padx=15, pady=15)

        testing_label = tk.Label(frame, text="Testing version:")
        testing_label.configure(background=BACKGROUND, fg=SECONDARY, font=("Arial", 14, "bold"))
        testing_label.grid(row=5, column=0, padx=15, pady=15)

        version_label = tk.Label(frame, text=f"{SOFTWARE_VERSION}")
        version_label.configure(background=BACKGROUND, fg=THIRD, font=("Arial", 12))
        version_label.grid(row=9, column=2, padx=15, pady=15)

        last_name = tk.Entry(frame)
        last_name.grid(row=0, column=1, padx=15, pady=15)
        self.entry_data["last_name"] = last_name

        last_name.focus_set()

        first_name = tk.Entry(frame)
        first_name.grid(row=0, column=2, padx=15, pady=15)
        self.entry_data["first_name"] = first_name

        date_entry = tk.Entry(frame)
        date_entry.grid(row=1, column=1, padx=15, pady=15)
        self.entry_data["date_entry"] = date_entry

        self.shift_listbox = self.shift_listbox(frame)
        self.shift_listbox.grid(row=2, column=1, padx=15, pady=15)
        self.shift_listbox.bind("<<ComboboxSelected>>", self.update_shift)

        employee_id_entry = tk.Entry(frame)
        employee_id_entry.grid(row=3, column=1, padx=15, pady=15)
        self.entry_data["employee_id"] = employee_id_entry

        location_entry = tk.Entry(frame)
        location_entry.grid(row=4, column=1, padx=15, pady=15)
        self.entry_data["location"] = location_entry

        testing_version_entry = tk.Entry(frame)
        testing_version_entry.grid(row=5, column=1, padx=15, pady=15)
        self.entry_data["testing_version"] = testing_version_entry

        button_next = tk.Button(frame, text="Next", height=3, width=10, background=THIRD, fg=BACKGROUND,
                                font=("Arial", 12, "bold"), command=self.show_second_window)
        button_next.grid(row=8, column=1, padx=15, pady=15)

    def get_main_window_data(self):
        for key, value in self.entry_data.items():
            if not isinstance(value, str):
                self.entry_data[key] = value.get()
        return self.entry_data

    def update_shift(self, event):
        selected_shift = self.shift_listbox.get()
        self.entry_data["shift"] = selected_shift

    def show_second_window(self):
        self.get_main_window_data()
        second_window = SecondWindow(main_ui=self, controller=self.controller)
        second_window.second_window()
