from screens.newOrder import newOrder
from screens.reportEmployees import reportEmployees
from screens.reportOrders import reportOrders
import tkinter as tk

class home:
    def __init__(self):
        # Configuração da janela principal
        self.window = tk.Tk()
        self.window.resizable(False, False)
        self.window.geometry('300x200')
        self.window.title('Home')
        # Adiciona padding na janela
        self.window.configure(padx=20, pady=20)

        # Frame principal para os botões
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill='both')

        # Fonte padrão para botões
        btn_font = ("Helvetica", 12)

        # Botão Novo Pedido
        btNewOrder = tk.Button(
            frame,
            text="Novo Pedido",
            font=btn_font,
            width=20,
            pady=5,
            command=self.newOrderClick
        )
        btNewOrder.pack(fill='x', pady=5)

        # Botão Relatório Pedidos
        btOrders = tk.Button(
            frame,
            text="Relatório Pedidos",
            font=btn_font,
            width=20,
            pady=5,
            command=self.reportOrdersClick
        )
        btOrders.pack(fill='x', pady=5)

        # Botão Relatório Funcionários
        btEmployees = tk.Button(
            frame,
            text="Relatório Funcionários",
            font=btn_font,
            width=20,
            pady=5,
            command=self.reportEmployeesClick
        )
        btEmployees.pack(fill='x', pady=5)

    def newOrderClick(self):
        # Destrói a janela atual e abre o módulo de Novo Pedido
        self.window.destroy()
        app = newOrder()
        app.run()

    def reportEmployeesClick(self):
        # Destrói a janela atual e abre o relatório de Funcionários
        self.window.destroy()
        app = reportEmployees()
        app.run()

    def reportOrdersClick(self):
        # Destrói a janela atual e abre o relatório de Pedidos
        self.window.destroy()
        app = reportOrders()
        app.run()

    def run(self):
        # Executa o loop principal da interface
        self.window.mainloop()