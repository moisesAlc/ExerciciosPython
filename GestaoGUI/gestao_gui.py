import tkinter as tk
import tkinter.ttk as ttk


def darkstyle(root):
    """ Return a dark style to the window"""

    style = ttk.Style(root)
    #root.tk.call('source', 'azure dark/azure dark.tcl')
    root.tk.call('source', 'scidthemes.0.9.3\scidthemes.tcl')
    style.theme_use('scidgrey')
    #style.configure("Accentbutton", selectbackground='white')
    return style


def main_window():
    """ The window with the darkstyle """
    root = tk.Tk()
    root.title("Login")
    root.resizable(True, True)
    root.geometry("600x350")
    root.iconbitmap("img/icone.ico")

    img = tk.PhotoImage(file="img/logo20dpi.png")

    style = darkstyle(root)
    PADY = 15

    frame_logo_welcome = ttk.Frame(root)
    logo = ttk.Label(
        frame_logo_welcome,
        anchor="w",
        image=img)

    welcome = ttk.Label(
        frame_logo_welcome,
        text="Gestão de Automóveis",
        #compound="center",
        font="arial 30",
        anchor="e")

    logo.pack(side="left")
    welcome.pack(side="right", padx=15)

    frame_logo_welcome.pack(pady=PADY+10)

    #-------------------------------------------------

    frame_authorization = ttk.Frame(root)

    login_label = ttk.Label(
        frame_authorization,
        text="Login",
        font="arial 12"
    )

    login_entry = ttk.Entry(
        frame_authorization,
        foreground='#666699',
        justify="center",
        )
    login_entry.insert(0, 'E-mail/Username')    

    password_label = ttk.Label(
        frame_authorization,
        text="Senha",
        font="arial 12"
    )

    password_entry = ttk.Entry(
        frame_authorization, 
        show="●", 
        width=20,
        foreground='#666699',
        justify="center",
        )
    password_entry.insert(0, 'Min 6 characters')    

    login_label.grid(row=0, column=0, padx=10, pady=PADY)
    login_entry.grid(row=0, column=1, padx=10, pady=PADY)
    password_label.grid(row=1, column=0, padx=10, pady=PADY)
    password_entry.grid(row=1, column=1, padx=10, pady=PADY)

    frame_authorization.pack()

    button = ttk.Button(
        root,
        text="Login",
        width=20,
        #style="Accentbutton"
    )

    button.pack(pady=PADY)

    root.mainloop()


main_window()
