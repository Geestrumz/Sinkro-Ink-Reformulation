import tkinter as tk
from tkinter import ttk
from tabs.toner_inventory_tab import TonerInventoryTab
from tabs.substrate_library_tab import SubstrateLibraryTab
from tabs.target_formulations_tab import TargetFormulationsTab
from tabs.ink_batch_tab import InkBatchTab

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sinkro - Ink Reformulation")
        self.geometry("1024x768")

        # Create a notebook (tabbed interface)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, padx=10, expand=True, fill="both")

        # Create tabs
        self.toner_tab = TonerInventoryTab(self.notebook)
        self.substrate_tab = SubstrateLibraryTab(self.notebook)
        self.target_tab = TargetFormulationsTab(self.notebook)
        self.batch_tab = InkBatchTab(self.notebook)

        # Add tabs to the notebook
        self.notebook.add(self.toner_tab, text="Toner Inventory")
        self.notebook.add(self.substrate_tab, text="Substrate Library")
        self.notebook.add(self.target_tab, text="Target Formulations")
        self.notebook.add(self.batch_tab, text="Ink Batch & Correction")

if __name__ == "__main__":
    app = Application()
    app.mainloop()