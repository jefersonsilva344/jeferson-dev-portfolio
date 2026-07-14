import customtkinter as ctk


window = ctk.CTk()

window.title("Expense Manager")

window.geometry("400x300")


title = ctk.CTkLabel(
    window,
    text="Expense Manager"
)

title.pack(pady=20)


window.mainloop()
