import tkinter as tk
import tkinter.ttk as ttk
from tkinter import END

from GestaoGUI.models.Automovel import Automovel


def set_text(entry_widget, text):
    entry_widget.delete(0, END)
    entry_widget.insert(0, text)


class Detail(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)

        # Configure vehicles list
        self.vehicles_list = [
            Automovel("Ford Mustang GT", "Ford", 2015, "branco"),
            Automovel("Hyundai Tiburon GT V6", "Hyundai", 2016, "cinza"),
            Automovel("Lamborghini Murciélago", "Lamborghini", 2017, "preto"),
            Automovel("Nissan 350Z", "Nissan", 2018, "verde perolado"),
        ]

        # Configure vehicles_listbox
        vehicles_listbox = tk.Listbox(root, width=120, selectmode='single')

        for vehicle in self.vehicles_list:
            vehicles_listbox.insert(self.vehicles_list.index(vehicle) + 1, vehicle.get_nome())

        vehicles_listbox.bind('<<ListboxSelect>>', self.change_data)

        vehicles_listbox.pack(expand=True, padx=20, pady=40)

        # Configure labels & entries

        ttk.Label(self, text="Número").pack()
        self.w_numero = ttk.Entry(self, width=30)
        self.w_numero.pack()

        ttk.Label(self, text="Nome").pack()
        self.w_nome = ttk.Entry(self, width=30)
        self.w_nome.pack()

        ttk.Label(self, text="Marca").pack()
        self.w_marca = ttk.Entry(self, width=30)
        self.w_marca.pack()

        ttk.Label(self, text="Ano").pack()
        self.w_ano = ttk.Entry(self, width=30)
        self.w_ano.pack()

        ttk.Label(self, text="Cor").pack()
        self.w_cor = ttk.Entry(self, width=30)
        self.w_cor.pack()

        ttk.Label(self, text="Alugado").pack()
        self.w_alugado = ttk.Entry(self, width=30)
        self.w_alugado.pack()

    def change_data(self, evt):

        widget_selected = evt.widget
        index = int(widget_selected.curselection()[0])
        # value = widget_selected.get(index)
        automovel = self.vehicles_list[index]

        set_text(self.w_numero, automovel.numero[0])
        set_text(self.w_nome, automovel.nome[0])
        set_text(self.w_marca, automovel.marca[0])
        set_text(self.w_ano, automovel.ano[0])
        set_text(self.w_cor, automovel.cor)
        set_text(self.w_alugado, automovel.get_alugado())
