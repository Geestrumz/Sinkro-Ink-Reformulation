import tkinter as tk
from tkinter import ttk, messagebox
import data_manager

class TargetFormulationsTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label = ttk.Label(self, text="Target Formulation Library")
        self.label.pack(pady=10, padx=10)

        # Treeview for targets
        tree_frame = ttk.Frame(self)
        tree_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        scrollbar = ttk.Scrollbar(tree_frame)
        scrollbar.pack(side="right", fill="y")
        
        self.tree = ttk.Treeview(tree_frame, columns=("Name", "Substrate", "L", "a", "b", "Weight"), show="headings", yscrollcommand=scrollbar.set)
        self.tree.heading("Name", text="Target Name/Code")
        self.tree.heading("Substrate", text="Substrate")
        self.tree.heading("L", text="Target L*")
        self.tree.heading("a", text="Target a*")
        self.tree.heading("b", text="Target b*")
        self.tree.heading("Weight", text="Desired Weight")
        self.tree.pack(fill="both", expand=True)

        scrollbar.config(command=self.tree.yview)

        # Buttons
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10, padx=10, fill="x")

        add_button = ttk.Button(button_frame, text="Add Target", command=self.add_target)
        add_button.pack(side="left", padx=5)

        edit_button = ttk.Button(button_frame, text="Edit Selected", command=self.edit_target)
        edit_button.pack(side="left", padx=5)

        delete_button = ttk.Button(button_frame, text="Delete Selected", command=self.delete_target)
        delete_button.pack(side="left", padx=5)

        self.load_targets()

    def load_targets(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        targets = data_manager.load_data(data_manager.TARGETS_FILE)
        for t in targets:
            self.tree.insert("", "end", values=(
                t.get('name', ''),
                t.get('substrate', ''),
                t.get('lab', [0,0,0])[0],
                t.get('lab', [0,0,0])[1],
                t.get('lab', [0,0,0])[2],
                t.get('weight', 0)
            ))

    def add_target(self):
        messagebox.showinfo("Not Implemented", "This will open a dialog to add a new target formulation.")

    def edit_target(self):
        if not self.tree.selection():
            messagebox.showwarning("No Selection", "Please select a target to edit.")
            return
        messagebox.showinfo("Not Implemented", "This will open a dialog to edit the selected target.")

    def delete_target(self):
        if not self.tree.selection():
            messagebox.showwarning("No Selection", "Please select a target to delete.")
            return
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete the selected target?"):
            print("Deleting target...")