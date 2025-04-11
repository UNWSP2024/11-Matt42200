import tkinter as tk


root = tk.Tk()
root.title("Favorite Saying")
root.geometry("400x200")
root.configure(bg="#1e1e1e")  # Dark background


label = tk.Label(
    root,
    text='"When it rains, it pours."',
    fg="white",
    bg="#1e1e1e",
    font=("Helvetica", 14, "italic"),
    wraplength=380,
    justify="center"
)
label.pack(expand=True)


root.mainloop()