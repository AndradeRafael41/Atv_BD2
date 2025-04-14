import tkinter as tk
from tkinter import ttk

class newOrder:

    def __init__(self):
        self.window = tk.Tk()
        self.window.resizable(0,0)
        self.window.geometry("400x400")
        self.window.title("Novo Pedido")

        tk.Label(self.window, text="Nome do Cliente:").place(relx=0.1, rely=0.1)
        clientName = ttk.Combobox(self.window, values=["", "", ""])
        clientName.place(relx=0.5, rely=0.1)
        clientName.current(0)

        tk.Label(self.window, text="Nome do Vendedor:").place(relx=0.1, rely=0.2)
        employeeName = ttk.Combobox(self.window, values=["", "", ""])
        employeeName.place(relx=0.5, rely=0.2)
        employeeName.current(0)

        tk.Label(self.window, text="Remetente:").place(relx=0.1, rely=0.3)
        shipperName = ttk.Combobox(self.window, values=["", "", ""])
        shipperName.place(relx=0.5, rely=0.3)
        shipperName.current(0)
        
        tk.Label(self.window, text="Código Postal:").place(relx=0.1, rely=0.4)
        postalCode = tk.Entry(self.window)
        postalCode.place(relx=0.5, rely=0.4)

        tk.Label(self.window, text="Endereço:").place(relx=0.1, rely=0.5)
        address = tk.Entry(self.window)
        address.place(relx=0.5, rely=0.5)

        tk.Label(self.window, text="Cidade:").place(relx=0.1, rely=0.6)
        city = tk.Entry(self.window)
        city.place(relx=0.5, rely=0.6)

        tk.Label(self.window, text="Região:").place(relx=0.1, rely=0.7)
        region = tk.Entry(self.window)
        region.place(relx=0.5, rely=0.7)

        tk.Label(self.window, text="País:").place(relx=0.1, rely=0.8)
        country = tk.Entry(self.window)
        country.place(relx=0.5, rely=0.8)

        tk.Button(self.window, text="Voltar").place(relx=0.1, rely=0.9)
        tk.Button(self.window, text="Enviar").place(relx=0.8, rely=0.9)

        self.window.mainloop()