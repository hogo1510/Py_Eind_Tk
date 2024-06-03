import tkinter as tk
from tkinter import messagebox, Menu, Frame, Label, Entry, Button
from math import pi
import random

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Pagina")

        #usrn input
        self.username_label = tk.Label(root, text="Gebruikersnaam:", font=("Helvetica", 14))
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(root, font=("Helvetica", 14))
        self.username_entry.pack(pady=5)

        #passwd input
        self.password_label = tk.Label(root, text="Wachtwoord:", font=("Helvetica", 14))
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(root, font=("Helvetica", 14), show="*")
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(root, text="Login", command=self.validate_login, font=("Helvetica", 14))
        self.login_button.pack(pady=20)

    def validate_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        #usrn en passwd
        valid_username = "root"
        valid_password = "toor"

        if username == valid_username and password == valid_password:
            messagebox.showinfo("Succes", "Login succesvol!")
            self.open_main_app()
        else:
            messagebox.showerror("Fout", "Ongeldige gebruikersnaam of wachtwoord.")

    def open_main_app(self):
        #einde login -> Main
        self.root.destroy()
        main_root = tk.Tk()
        main_app = MainApp(main_root)
        main_root.mainloop()

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu voorbeeld")

        #functies menu
        def show_prog1():
            prog2.pack_forget()
            prog1.pack()

        def show_prog2():
            prog2.pack()
            prog1.pack_forget()

        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        #menu
        mainmenu = Menu(menubar)
        mainmenu.add_command(label="Dobbelsteen", command=show_prog1)
        mainmenu.add_command(label="Cirkel Berekening", command=show_prog2)
        mainmenu.add_separator()
        mainmenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="Tool", menu=mainmenu)

        #dobbelsteen
        prog1 = Frame(self.root, borderwidth=10)
        self.dice_result_label = Label(prog1, text="", font=("Helvetica", 100))
        self.dice_result_label.pack(pady=20)
        self.roll_button = Button(prog1, text="Gooi de dobbelsteen", command=self.roll_dice, font=("Helvetica", 20))
        self.roll_button.pack(pady=20)

        #cirkel
        prog2 = Frame(self.root, borderwidth=10)
        self.diameter_label = Label(prog2, text="Diameter:", font=("Helvetica", 14))
        self.diameter_label.pack(pady=5)
        self.diameter_entry = Entry(prog2, font=("Helvetica", 14))
        self.diameter_entry.pack(pady=5)
        self.calculate_button = Button(prog2, text="Bereken", command=self.calculate_circle, font=("Helvetica", 14))
        self.calculate_button.pack(pady=20)
        self.circumference_label = Label(prog2, text="", font=("Helvetica", 14))
        self.circumference_label.pack(pady=5)
        self.area_label = Label(prog2, text="", font=("Helvetica", 14))
        self.area_label.pack(pady=5)

        #start = frame_1
        prog1.pack()

        self.prog1 = prog1
        self.prog2 = prog2

    def roll_dice(self):
        result = random.randint(1, 6)
        self.dice_result_label.config(text=str(result))

    def calculate_circle(self):
        try:
            diameter = float(self.diameter_entry.get())
            radius = diameter / 2
            circumference = 2 * pi * radius
            area = pi * radius ** 2

            self.circumference_label.config(text=f"Omtrek: {circumference:.2f}")
            self.area_label.config(text=f"Oppervlakte: {area:.2f}")
        except ValueError:
            self.circumference_label.config(text="Ongeldige invoer. Voer een numerieke waarde in.")
            self.area_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()

