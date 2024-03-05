import tkinter as tk

def calculate_bmi():
    height = float(height_entry.get()) / 100  
    weight = float(weight_entry.get())
    bmi = weight / (height ** 2)
    result.config(text="Your BMI: {:.2f}".format(bmi))

root = tk.Tk()
root.configure(bg='Pink')
root.title("BMI Calculator")


root.geometry('300x200')

title_label = tk.Label(root, text="BMI Calculator", font=("Helvetica", 16, "bold"), bg="Pink")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

height_label = tk.Label(root, text="Height (cm):", bg="Pink")
height_label.grid(row=1, column=0, padx=10, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=5)

weight_label = tk.Label(root, text="Weight (kg):", bg="Pink")
weight_label.grid(row=2, column=0, padx=10, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=2, column=1, padx=10, pady=5)


calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi, bg="lightblue", relief=tk.RAISED)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result = tk.Label(root, text="", bg="Pink")
result.grid(row=4, column=0, columnspan=2)

root.mainloop()
