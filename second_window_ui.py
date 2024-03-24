# second_window_ui.py
import tkinter as tk
from tkinter import *
from tkinter import ttk, Text


class SecondWindow:
    def __init__(self, main_ui, controller):
        self.main_ui = main_ui
        self.controller = controller
        try:
            self.main_window_data = self.main_ui.get_main_window_data()
        except AttributeError:
            print("Data not found in main_ui")

        config = self.controller.get_config()
        self.background = config["background"]
        self.primary_color = config["primary_color"]
        self.secondary_color = config["secondary_color"]
        self.third_color = config["third_color"]
        self.fourth_color = config["fourth_color"]
        self.software_version = config["software_version"]

    def set_controller(self, controller):
        self.controller = controller

    def main_tab_window(self, window_frame):
        s = ttk.Style()
        s.configure('Custom.TNotebook.Tab', background=self.background, foreground=self.primary_color,
                    font=("Arial", 10))

        main_tab = ttk.Notebook(window_frame, style='Custom.TNotebook')
        main_tab.configure(style='Custom.TNotebook')

        tab1 = tk.Frame(main_tab)
        self.populate_home_tab(tab1)

        tab2 = tk.Frame(main_tab)
        self.populate_bug_report_tab(tab2)

        main_tab.add(tab1, text="Home")
        main_tab.add(tab2, text="Bug Report")
        main_tab.pack(fill='both', expand=True)

        main_tab.grid_rowconfigure(0, weight=1)
        main_tab.grid_columnconfigure(0, weight=1)

    def populate_bug_report_tab(self, tab):
        bug_report_main_frame = tk.Frame(tab)
        bug_report_main_frame.configure(background=self.background)
        bug_report_main_frame.pack(fill="both", expand=True)
        bug_report_main_frame.grid_columnconfigure(0, weight=1)
        bug_report_main_frame.grid_rowconfigure(0, weight=1)
        bug_report_main_frame.grid_columnconfigure(2, weight=1)
        bug_report_main_frame.grid_rowconfigure(2, weight=1)

        bug_report_frame = tk.Frame(bug_report_main_frame)
        bug_report_frame.configure(background=self.background)
        bug_report_frame.pack(fill="both", expand=True)

        title = tk.Label(bug_report_frame, text="Title:", font=("Arial", 14), bg=self.background, fg=self.third_color)
        title.grid(row=0, column=0, padx=15, pady=15)
        self.title_entry = Text(bug_report_frame, height=2, width=50, font=("Arial", 10))
        self.title_entry.grid(row=0, column=1, padx=15, pady=15)

        preconditions_label = tk.Label(bug_report_frame, text="Preconditions:", font=("Arial", 14, "bold"),
                                       fg=self.fourth_color,
                                       background=self.background)
        preconditions_label.grid(row=1, column=0, padx=15, pady=15)
        self.preconditions_entry = Text(bug_report_frame, height=5, width=50, font=("Arial", 10))
        self.preconditions_entry.grid(row=1, column=1, padx=15, pady=15)

        description_label = tk.Label(bug_report_frame, text="Description:", font=("Arial", 14, "bold"),
                                     fg=self.secondary_color,
                                     background=self.background)
        description_label.grid(row=2, column=0, padx=15, pady=15)
        self.description_entry = Text(bug_report_frame, height=10, width=50, font=("Arial", 10))
        self.description_entry.grid(row=2, column=1, padx=15, pady=15)

        expectation_label = tk.Label(bug_report_frame, text="Expectation:", font=("Arial", 14, "bold"),
                                     fg=self.third_color,
                                     background=self.background)
        expectation_label.grid(row=3, column=0, padx=15, pady=15)
        self.expectation_entry = Text(bug_report_frame, height=2, width=50, font=("Arial", 10))
        self.expectation_entry.grid(row=3, column=1, padx=15, pady=15)

        bug_button = tk.Button(bug_report_frame, text="Save", height=3, width=10, background=self.third_color,
                               fg=self.background,
                               font=("Arial", 12, "bold"), command=self.save_report)
        bug_button.grid(row=8, column=1, padx=15, pady=15)

        reproducible_label = tk.Label(bug_report_frame, background=self.background, text="Reproducible:",
                                      fg=self.fourth_color,
                                      font=("Arial", 13, "bold", 'underline'))
        reproducible_label.grid(row=6, column=1, padx=15, pady=15)

        self.check_button0 = IntVar()
        self.check_button1 = IntVar()
        self.check_button2 = IntVar()

        button0 = Checkbutton(bug_report_frame, text="Once", background=self.background, fg=self.third_color,
                              font=("Arial", 12, "bold"), variable=self.check_button0,
                              onvalue=1, offvalue=0, height=5, width=15)
        button0.grid(row=7, column=0, padx=10)

        button1 = Checkbutton(bug_report_frame, text="Many Times", background=self.background, fg=self.primary_color,
                              font=("Arial", 12, "bold"), variable=self.check_button1,
                              onvalue=1, offvalue=0, height=5, width=15)
        button1.grid(row=7, column=1, padx=10)

        button2 = Checkbutton(bug_report_frame, text="Always", background=self.background, fg=self.secondary_color,
                              font=("Arial", 12, "bold"), variable=self.check_button2,
                              onvalue=1, offvalue=0, height=5, width=15)
        button2.grid(row=7, column=2, padx=10)

        version_label = tk.Label(bug_report_main_frame, text=f"{self.software_version}")
        version_label.configure(background=self.background, fg=self.third_color, font=("Arial", 12))
        version_label.pack()

    def save_report(self):
        title = self.title_entry.get("1.0", "end-1c")
        preconditions = self.preconditions_entry.get("1.0", "end-1c")
        description = self.description_entry.get("1.0", "end-1c")
        expectation = self.expectation_entry.get("1.0", "end-1c")
        reproducible = self.get_reproducible_value()
        employee_id = self.main_window_data["employee_id"]

        bug_report_data = {
            "title": title,
            "preconditions": preconditions,
            "description": description,
            "expectation": expectation,
            "reproducible": reproducible,
            "employee_id": employee_id,
            "last_name": self.main_window_data["last_name"],
            "first_name": self.main_window_data["first_name"],
            "location": self.main_window_data["location"],
            "shift": self.main_window_data["shift"]
        }
        self.controller.control_report(bug_report_data)

        # clear data fields
        self.title_entry.delete("1.0", "end")
        self.preconditions_entry.delete("1.0", "end")
        self.description_entry.delete("1.0", "end")
        self.expectation_entry.delete("1.0", "end")
        self.check_button0.set(0)
        self.check_button1.set(0)
        self.check_button2.set(0)

    def exit_report(self):
        self.main_ui.window.destroy()

    def get_reproducible_value(self):
        if self.check_button0.get() == 1:
            return "Once"
        elif self.check_button1.get() == 1:
            return "Many Times"
        elif self.check_button2.get() == 1:
            return "Always"
        else:
            return ""

    def second_window(self):
        new_window = tk.Toplevel(self.main_ui.window)
        new_window.title("Employee Interface")
        new_window.geometry("800x800")
        new_window.configure(background=self.background)

        self.main_tab_window(new_window)

    def populate_home_tab(self, tab):
        home_tab_frame = tk.Frame(tab)
        home_tab_frame.configure(background=self.background)
        home_tab_frame.pack(fill='both', expand=True)

        home_tab_frame.grid_columnconfigure(0, weight=1)
        home_tab_frame.grid_rowconfigure(0, weight=1)
        home_tab_frame.grid_columnconfigure(2, weight=1)
        home_tab_frame.grid_rowconfigure(2, weight=1)

        new_window_frame = tk.Frame(home_tab_frame)
        new_window_frame.configure(background=self.background)
        new_window_frame.grid(row=0, column=0, sticky='nsew')

        name_label = tk.Label(new_window_frame, text="Last and first name:")
        name_label.configure(background=self.background, fg=self.primary_color, font=("Arial", 14, "bold"))
        name_label.grid(row=1, column=0, padx=15, pady=15)

        date_label = tk.Label(new_window_frame, text="Date:")
        date_label.configure(background=self.background, fg=self.secondary_color, font=("Arial", 14, "bold"))
        date_label.grid(row=2, column=0, padx=15, pady=15)

        shift_label = tk.Label(new_window_frame, text="Shift:")
        shift_label.configure(background=self.background, fg=self.fourth_color, font=("Arial", 14, "bold"))
        shift_label.grid(row=3, column=0, padx=15, pady=15)

        employee_id_label = tk.Label(new_window_frame, text="Employee ID:")
        employee_id_label.configure(background=self.background, fg=self.third_color, font=("Arial", 14, "bold"))
        employee_id_label.grid(row=4, column=0, padx=15, pady=15)

        location_label = tk.Label(new_window_frame, text="Location:")
        location_label.configure(background=self.background, fg=self.primary_color, font=("Arial", 14, "bold"))
        location_label.grid(row=5, column=0, padx=15, pady=15)

        testing_label = tk.Label(new_window_frame, text="Testing version:")
        testing_label.configure(background=self.background, fg=self.secondary_color, font=("Arial", 14, "bold"))
        testing_label.grid(row=6, column=0, padx=15, pady=15)

        version_label = tk.Label(home_tab_frame, text=f"{self.software_version}")
        version_label.configure(background=self.background, fg=self.third_color, font=("Arial", 12))
        version_label.grid(row=9, column=3, sticky='s', padx=15, pady=15)

        last_name = tk.Entry(new_window_frame)
        last_name.insert(0, self.main_window_data["last_name"])
        last_name.grid(row=1, column=1, padx=15, pady=15)

        first_name = tk.Entry(new_window_frame)
        first_name.insert(0, self.main_window_data["first_name"])
        first_name.grid(row=1, column=2, padx=15, pady=15)

        date_entry = tk.Entry(new_window_frame)
        date_entry.insert(0, self.main_window_data["date_entry"])
        date_entry.grid(row=2, column=1, padx=15, pady=15)

        shift_list = ttk.Combobox(new_window_frame, state="readonly",
                                  values=["1st Shift", "2nd Shift", "3rd Shift"])
        shift_list.set(self.main_window_data["shift"])
        shift_list.grid(row=3, column=1, padx=15, pady=15)

        employee_id_entry = tk.Entry(new_window_frame)
        employee_id_entry.insert(0, self.main_window_data["employee_id"])
        employee_id_entry.grid(row=4, column=1, padx=15, pady=15)

        location_entry = tk.Entry(new_window_frame)
        location_entry.insert(0, self.main_window_data["location"])
        location_entry.grid(row=5, column=1, padx=15, pady=15)

        testing_version_entry = tk.Entry(new_window_frame)
        testing_version_entry.insert(0, self.main_window_data["testing_version"])
        testing_version_entry.grid(row=6, column=1, padx=15, pady=15)

        save_exit_button = tk.Button(new_window_frame, text="Exit", background=self.third_color,
                                     fg=self.background,
                                     font=("Arial", 12, "bold"), command=self.exit_report, height=3, width=10)
        save_exit_button.grid(row=7, column=1, padx=15, pady=15)

        new_window_frame.grid_rowconfigure(0, weight=1)
        new_window_frame.grid_columnconfigure(0, weight=1)
