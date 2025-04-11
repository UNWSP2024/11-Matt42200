import tkinter as tk


def show_info():
    info_label.config(text="Matt Anderson\n5831 Bayberry Drive")


root = tk.Tk()
root.title("User Info")
root.geometry("300x200")


info_label = tk.Label(root, text="", font=("Helvetica", 12), justify="center")
info_label.pack(pady=20)


show_button = tk.Button(root, text="Show Info", command=show_info)
show_button.pack(pady=5)


quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack(pady=5)


root.mainloop()