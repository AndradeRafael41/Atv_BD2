from screens.newOrder import newOrder
from screens.reportEmployees import reportEmployees
from screens.reportOrders import reportOrders
import tkinter as tk

class home:

    def __init__(self):
        self.window = tk.Tk()
        self.window.resizable(0,0)
        self.window.geometry('200x200')
        self.window.title('Home')

        btNewOrder = tk.Button(self.window, text="Novo Pedido", width="16", command=self.newOrderClick)
        btNewOrder.place(relx=0.1, rely=0.1)

        btOrders = tk.Button(self.window, text="Relatório Pedidos", width="16", command=self.reportOrdersClick)
        btOrders.place(relx=0.1, rely=0.4)

        btEmployees = tk.Button(self.window, text="Relatório Funcionários", width="16", command=self.reportEmployeesClick)
        btEmployees.place(relx=0.1, rely=0.7)

        self.window.mainloop()

    def newOrderClick(self):
        self.window.destroy()
        newOrder()

    def reportEmployeesClick(self):
        self.window.destroy()
        reportEmployees()

    def reportOrdersClick(self):
        self.window.destroy()
        reportOrders()
