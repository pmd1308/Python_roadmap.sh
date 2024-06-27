import tkinter as tk
from tkinter import messagebox
import arithmetic

def start_gui():
    # Create the main window
    root = tk.Tk()
    root.title("Python Numbers and Arithmetic")

    # Create frames
    frame_arithmetic = tk.Frame(root, padx=10, pady=10)
    frame_arithmetic.pack(fill="both", expand=True)

    frame_compound = tk.Frame(root, padx=10, pady=10)
    frame_compound.pack(fill="both", expand=True)

    # Arithmetic operations
    tk.Label(frame_arithmetic, text="Arithmetic Operations").grid(row=0, column=0, columnspan=2)
    
    tk.Label(frame_arithmetic, text="Number 1:").grid(row=1, column=0)
    entry_num1 = tk.Entry(frame_arithmetic)
    entry_num1.grid(row=1, column=1)

    tk.Label(frame_arithmetic, text="Number 2:").grid(row=2, column=0)
    entry_num2 = tk.Entry(frame_arithmetic)
    entry_num2.grid(row=2, column=1)

    tk.Label(frame_arithmetic, text="Result").grid(row=3, column=0)
    result = tk.StringVar()
    entry_result_arithmetic = tk.Entry(frame_arithmetic, textvariable=result, state='readonly')
    entry_result_arithmetic.grid(row=3, column=1)

    def perform_operation(operation_func):
        try:
            first_number = float(entry_num1.get())
            second_number = float(entry_num2.get())
            result.set(operation_func(first_number, second_number))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

    tk.Button(frame_arithmetic, text="Add", command=lambda: perform_operation(arithmetic.add)).grid(row=4, column=0)
    tk.Button(frame_arithmetic, text="Subtract", command=lambda: perform_operation(arithmetic.subtract)).grid(row=4, column=1)
    tk.Button(frame_arithmetic, text="Multiply", command=lambda: perform_operation(arithmetic.multiply)).grid(row=5, column=0)
    tk.Button(frame_arithmetic, text="Divide", command=lambda: perform_operation(arithmetic.divide)).grid(row=5, column=1)
    tk.Button(frame_arithmetic, text="Floor Divide", command=lambda: perform_operation(arithmetic.floor_divide)).grid(row=6, column=0)
    tk.Button(frame_arithmetic, text="Modulo", command=lambda: perform_operation(arithmetic.modulo)).grid(row=6, column=1)
    tk.Button(frame_arithmetic, text="Power", command=lambda: perform_operation(arithmetic.power)).grid(row=7, column=0)

    # Compound operation
    tk.Label(frame_compound, text="Compound Interest calculation").grid(row=0, column=0, columnspan=2)
    tk.Label(frame_compound, text="Principal:").grid(row=1, column=0)
    entry_principal = tk.Entry(frame_compound)
    entry_principal.grid(row=1, column=1)

    tk.Label(frame_compound, text="Rate:").grid(row=2, column=0)
    entry_rate = tk.Entry(frame_compound)
    entry_rate.grid(row=2, column=1)

    tk.Label(frame_compound, text="Time:").grid(row=3, column=0)
    entry_time = tk.Entry(frame_compound)
    entry_time.grid(row=3, column=1)

    tk.Label(frame_compound, text="Result").grid(row=4, column=0)
    result_compound = tk.StringVar()
    entry_result_compound = tk.Entry(frame_compound, textvariable=result_compound, state='readonly')
    entry_result_compound.grid(row=4, column=1)

    def perform_compound_operation():
        try:
            principal = float(entry_principal.get())
            rate = float(entry_rate.get())
            time = float(entry_time.get())
            result_compound.set(arithmetic.compound_interest(principal, rate, time))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

    tk.Button(frame_compound, text="Calculate", command=perform_compound_operation).grid(row=5, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    start_gui()
