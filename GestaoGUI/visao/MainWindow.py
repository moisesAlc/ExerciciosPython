import tkinter as tk
from GestaoGUI.visao.Detail import Detail


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the main window
        self.title('Gestão de Automóveis')

        # configure the details frame
        self.detail_frame = Detail(self).pack(ipadx=20, ipady=20)