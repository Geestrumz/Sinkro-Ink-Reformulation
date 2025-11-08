import tkinter as tk
from tkinter import ttk, messagebox
import color_logic

class InkBatchTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Main frame divided into left and right
        main_frame = ttk.Frame(self)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side="left", fill="both", expand=True, padx=(0, 5))
        
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side="right", fill="both", expand=True, padx=(5, 0))

        # --- Left Side: Batch Entry & Measurement ---
        entry_labelframe = ttk.LabelFrame(left_frame, text="Ink Batch Entry")
        entry_labelframe.pack(fill="x", expand=True, pady=(0, 10))

        # Formulation (this would be a more complex widget in a real app)
        ttk.Label(entry_labelframe, text="Current Formulation:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        formulation_text = tk.Text(entry_labelframe, height=5, width=40)
        formulation_text.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        formulation_text.insert("1.0", "Toner A: 50g\nToner B: 30g\nVehicle: 20g")

        # Measured LAB values
        ttk.Label(entry_labelframe, text="Measured L*:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.measured_l = ttk.Entry(entry_labelframe)
        self.measured_l.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(entry_labelframe, text="Measured a*:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.measured_a = ttk.Entry(entry_labelframe)
        self.measured_a.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(entry_labelframe, text="Measured b*:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.measured_b = ttk.Entry(entry_labelframe)
        self.measured_b.grid(row=4, column=1, padx=5, pady=5)

        # --- Right Side: Target & Correction ---
        target_labelframe = ttk.LabelFrame(right_frame, text="Target & Correction")
        target_labelframe.pack(fill="x", expand=True, pady=(0, 10))
        
        # Target Selection
        ttk.Label(target_labelframe, text="Select Target:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.target_combo = ttk.Combobox(target_labelframe, values=["Target 1", "Target 2"])
        self.target_combo.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Target LAB values (would be populated from selection)
        ttk.Label(target_labelframe, text="Target L*:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.target_l = ttk.Entry(target_labelframe, state="readonly")
        self.target_l.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(target_labelframe, text="Target a*:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.target_a = ttk.Entry(target_labelframe, state="readonly")
        self.target_a.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(target_labelframe, text="Target b*:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.target_b = ttk.Entry(target_labelframe, state="readonly")
        self.target_b.grid(row=3, column=1, padx=5, pady=5)
        
        # --- Delta E Display ---
        delta_e_frame = ttk.Frame(right_frame)
        delta_e_frame.pack(fill="x", expand=True, pady=10)
        
        self.delta_e_label = ttk.Label(delta_e_frame, text="ΔE 2000:", font=("Helvetica", 14, "bold"))
        self.delta_e_label.pack(side="left", padx=5)

        self.delta_e_value = ttk.Label(delta_e_frame, text="N/A", font=("Helvetica", 14))
        self.delta_e_value.pack(side="left", padx=5)
        
        # --- Correction Area ---
        correction_labelframe = ttk.LabelFrame(right_frame, text="Correction Suggestion")
        correction_labelframe.pack(fill="both", expand=True)

        suggestion_text = tk.Text(correction_labelframe, height=5, width=40)
        suggestion_text.pack(fill="both", expand=True, padx=5, pady=5)
        suggestion_text.insert("1.0", "Correction suggestions will appear here...")
        suggestion_text.config(state="disabled")

        # --- Main Action Buttons ---
        action_frame = ttk.Frame(self)
        action_frame.pack(fill="x", padx=10, pady=(0, 10))

        calculate_button = ttk.Button(action_frame, text="Calculate DeltaE & Suggest Correction", command=self.run_calculation)
        calculate_button.pack(pady=5)

    def run_calculation(self):
        try:
            # A real implementation would get target LABs from the selected target
            mock_target_lab = (52.0, 21.0, -32.0)
            
            # Update target display
            self.target_l.config(state="normal")
            self.target_l.delete(0, tk.END)
            self.target_l.insert(0, str(mock_target_lab[0]))
            self.target_l.config(state="readonly")
            
            self.target_a.config(state="normal")
            self.target_a.delete(0, tk.END)
            self.target_a.insert(0, str(mock_target_lab[1]))
            self.target_a.config(state="readonly")

            self.target_b.config(state="normal")
            self.target_b.delete(0, tk.END)
            self.target_b.insert(0, str(mock_target_lab[2]))
            self.target_b.config(state="readonly")

            # Get measured values
            measured_lab = (
                float(self.measured_l.get()),
                float(self.measured_a.get()),
                float(self.measured_b.get())
            )

            # Calculate Delta E
            delta_e = color_logic.calculate_delta_e_2000(measured_lab, mock_target_lab)
            if delta_e is not None:
                self.delta_e_value.config(text=f"{delta_e:.2f}")
            else:
                self.delta_e_value.config(text="Error")

        except (ValueError, TypeError) as e:
            messagebox.showerror("Invalid Input", f"Please enter valid numeric LAB values. Error: {e}")