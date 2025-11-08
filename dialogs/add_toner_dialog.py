import tkinter as tk
from tkinter import ttk, messagebox

class AddTonerDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add New Toner")
        self.geometry("350x250")
        self.transient(parent)
        self.grab_set()

        self.toner_data = None

        # Create a frame for the form
        form_frame = ttk.Frame(self, padding="10")
        form_frame.pack(fill="both", expand=True)

        # Form fields
        fields = ["Name", "L*", "a*", "b*", "Density", "Cost"]
        self.entries = {}

        for i, field in enumerate(fields):
            label = ttk.Label(form_frame, text=f"{field}:")
            label.grid(row=i, column=0, padx=5, pady=5, sticky="w")
            
            entry = ttk.Entry(form_frame)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="ew")
            self.entries[field] = entry
        
        form_frame.columnconfigure(1, weight=1)

        # Buttons
        button_frame = ttk.Frame(self)
        button_frame.pack(fill="x", padx=10, pady=(0, 10))

        save_button = ttk.Button(button_frame, text="Save", command=self.save)
        save_button.pack(side="right", padx=5)

        cancel_button = ttk.Button(button_frame, text="Cancel", command=self.destroy)
        cancel_button.pack(side="right")
        
        self.protocol("WM_DELETE_WINDOW", self.destroy)
        self.wait_window(self)

    def save(self):
        """
        Validates input and prepares the data to be returned.
        """
        try:
            name = self.entries["Name"].get().strip()
            if not name:
                messagebox.showerror("Validation Error", "Toner name cannot be empty.", parent=self)
                return

            lab_l = float(self.entries["L*"].get())
            lab_a = float(self.entries["a*"].get())
            lab_b = float(self.entries["b*"].get())
            density = float(self.entries["Density"].get())
            cost = float(self.entries["Cost"].get())

            self.toner_data = {
                "name": name,
                "lab": [lab_l, lab_a, lab_b],
                "density": density,
                "cost": cost
            }
            self.destroy()

        except ValueError:
            messagebox.showerror("Validation Error", "Please enter valid numbers for LAB, Density, and Cost.", parent=self)
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}", parent=self)

    def show(self):
        """
        Returns the entered data after the window is closed.
        """
        return self.toner_data