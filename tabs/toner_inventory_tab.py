import tkinter as tk
from tkinter import ttk, messagebox
import data_manager
from dialogs.add_toner_dialog import AddTonerDialog

class TonerInventoryTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Placeholder for the UI elements
        self.label = ttk.Label(self, text="Toner Inventory Management")
        self.label.pack(pady=10, padx=10)

        # Create a frame for the treeview
        tree_frame = ttk.Frame(self)
        tree_frame.pack(pady=10, padx=10, fill="both", expand=True)

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(tree_frame)
        scrollbar.pack(side="right", fill="y")

        # Create the Treeview
        self.tree = ttk.Treeview(tree_frame, columns=("Name", "L", "a", "b", "Density", "Cost"), show="headings", yscrollcommand=scrollbar.set)
        self.tree.heading("Name", text="Toner Name")
        self.tree.heading("L", text="L*")
        self.tree.heading("a", text="a*")
        self.tree.heading("b", text="b*")
        self.tree.heading("Density", text="Density")
        self.tree.heading("Cost", text="Cost/unit")
        self.tree.pack(fill="both", expand=True)
        
        scrollbar.config(command=self.tree.yview)

        # Create a frame for buttons
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10, padx=10, fill="x")

        # Add buttons
        add_button = ttk.Button(button_frame, text="Add Toner", command=self.add_toner)
        add_button.pack(side="left", padx=5)

        edit_button = ttk.Button(button_frame, text="Edit Selected", command=self.edit_toner)
        edit_button.pack(side="left", padx=5)

        delete_button = ttk.Button(button_frame, text="Delete Selected", command=self.delete_toner)
        delete_button.pack(side="left", padx=5)

        self.load_toners()

    def load_toners(self):
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Load from data file
        toners = data_manager.load_data(data_manager.TONERS_FILE)
        for toner in toners:
            self.tree.insert("", "end", values=(
                toner.get('name', ''),
                toner.get('lab', [0,0,0])[0],
                toner.get('lab', [0,0,0])[1],
                toner.get('lab', [0,0,0])[2],
                toner.get('density', 0),
                toner.get('cost', 0)
            ))

    def add_toner(self):
        """
        Opens a dialog to add a new toner and saves it.
        """
        dialog = AddTonerDialog(self)
        new_toner_data = dialog.show()

        if new_toner_data:
            try:
                # Load existing data, append new data, and save
                toners = data_manager.load_data(data_manager.TONERS_FILE)
                toners.append(new_toner_data)
                data_manager.save_data(data_manager.TONERS_FILE, toners)
                
                # Refresh the treeview to show the new toner
                self.load_toners()
                messagebox.showinfo("Success", f"Toner '{new_toner_data['name']}' added successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save toner: {e}")

    def edit_toner(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a toner to edit.")
            return
        messagebox.showinfo("Not Implemented", "This will open a dialog to edit the selected toner.")
        # After editing, save and reload

    def delete_toner(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a toner to delete.")
            return
        
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete the selected toner?"):
            # Placeholder for deletion logic
            print("Deleting toner...")
            # After deleting, save and reload