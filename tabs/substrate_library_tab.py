import tkinter as tk
from tkinter import ttk, messagebox
import data_manager

class SubstrateLibraryTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label = ttk.Label(self, text="Substrate Library Management")
        self.label.pack(pady=10, padx=10)

        # Treeview for substrates
        tree_frame = ttk.Frame(self)
        tree_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        scrollbar = ttk.Scrollbar(tree_frame)
        scrollbar.pack(side="right", fill="y")
        
        self.tree = ttk.Treeview(tree_frame, columns=("Name", "Material", "L", "a", "b", "Gloss"), show="headings", yscrollcommand=scrollbar.set)
        self.tree.heading("Name", text="Substrate Name")
        self.tree.heading("Material", text="Material Type")
        self.tree.heading("L", text="L*")
        self.tree.heading("a", text="a*")
        self.tree.heading("b", text="b*")
        self.tree.heading("Gloss", text="Gloss Level")
        self.tree.pack(fill="both", expand=True)

        scrollbar.config(command=self.tree.yview)

        # Buttons
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10, padx=10, fill="x")

        add_button = ttk.Button(button_frame, text="Add Substrate", command=self.add_substrate)
        add_button.pack(side="left", padx=5)

        edit_button = ttk.Button(button_frame, text="Edit Selected", command=self.edit_substrate)
        edit_button.pack(side="left", padx=5)

        delete_button = ttk.Button(button_frame, text="Delete Selected", command=self.delete_substrate)
        delete_button.pack(side="left", padx=5)

        self.load_substrates()

    def load_substrates(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        substrates = data_manager.load_data(data_manager.SUBSTRATES_FILE)
        for sub in substrates:
            self.tree.insert("", "end", values=(
                sub.get('name', ''),
                sub.get('material_type', ''),
                sub.get('lab', [0,0,0])[0],
                sub.get('lab', [0,0,0])[1],
                sub.get('lab', [0,0,0])[2],
                sub.get('gloss', 0)
            ))

    def add_substrate(self):
        messagebox.showinfo("Not Implemented", "This will open a dialog to add a new substrate.")

    def edit_substrate(self):
        if not self.tree.selection():
            messagebox.showwarning("No Selection", "Please select a substrate to edit.")
            return
        messagebox.showinfo("Not Implemented", "This will open a dialog to edit the selected substrate.")

    def delete_substrate(self):
        if not self.tree.selection():
            messagebox.showwarning("No Selection", "Please select a substrate to delete.")
            return
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete the selected substrate?"):
            print("Deleting substrate...")