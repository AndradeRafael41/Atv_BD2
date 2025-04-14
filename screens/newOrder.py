import tkinter as tk
from tkinter import ttk
from Controller.pedido_controller import PedidoController
from tkinter import messagebox

class newOrder:

    def __init__(self):
        self.controller = PedidoController()
        self.window = tk.Tk()
        self.window.resizable(0,0)
        self.window.geometry("800x400")
        self.window.resizable(0, 0)
        self.window.geometry("400x400")
        self.window.title("Novo Pedido")

        # ---------- CLIENTES ----------
        tk.Label(self.window, text="Nome do Cliente:").place(relx=0.1, rely=0.1)
        self.clients = self.controller.listar_clientes()
        self.client_map = {f"{c.companyname} ({c.customerid})": c.customerid for c in self.clients}
        self.client_combo = ttk.Combobox(self.window, values=list(self.client_map.keys()), state="readonly")
        self.client_combo.place(relx=0.5, rely=0.1)
        self.client_combo.current(0)

        # ---------- FUNCIONÁRIOS ----------
        tk.Label(self.window, text="Nome do Vendedor:").place(relx=0.1, rely=0.2)
        self.employees = self.controller.listar_funcionarios()
        self.employee_map = {f"{e.firstname} {e.lastname} ({e.employeeid})": e.employeeid for e in self.employees}
        self.employee_combo = ttk.Combobox(self.window, values=list(self.employee_map.keys()), state="readonly")
        self.employee_combo.place(relx=0.5, rely=0.2)
        self.employee_combo.current(0)

        # ---------- REMETENTES ----------
        tk.Label(self.window, text="Remetente:").place(relx=0.1, rely=0.3)
        self.shippers = self.controller.listar_entregadores()
        self.shipper_map = {f"{s.companyname} ({s.shipperid})": s.shipperid for s in self.shippers}
        self.shipper_combo = ttk.Combobox(self.window, values=list(self.shipper_map.keys()), state="readonly")
        self.shipper_combo.place(relx=0.5, rely=0.3)
        self.shipper_combo.current(0)

        # ---------- OUTROS CAMPOS ----------
        tk.Label(self.window, text="Código Postal:").place(relx=0.1, rely=0.4)
        self.postalCode = tk.Entry(self.window)
        self.postalCode.place(relx=0.5, rely=0.4)

        tk.Label(self.window, text="Endereço:").place(relx=0.1, rely=0.5)
        self.address = tk.Entry(self.window)
        self.address.place(relx=0.5, rely=0.5)

        tk.Label(self.window, text="Cidade:").place(relx=0.1, rely=0.6)
        self.city = tk.Entry(self.window)
        self.city.place(relx=0.5, rely=0.6)

        tk.Label(self.window, text="Região:").place(relx=0.1, rely=0.7)
        self.region = tk.Entry(self.window)
        self.region.place(relx=0.5, rely=0.7)

        tk.Label(self.window, text="País:").place(relx=0.1, rely=0.8)
        self.country = tk.Entry(self.window)
        self.country.place(relx=0.5, rely=0.8)

        tk.Button(self.window, text="Voltar").place(relx=0.1, rely=0.9)
        tk.Button(self.window, text="Regis").place(relx=0.8, rely=0.9)
        # ---------- BOTÕES ----------
        tk.Button(self.window, text="Voltar", command=self.voltar).place(relx=0.1, rely=0.9)
        tk.Button(self.window, text="Enviar", command=self.enviar_pedido).place(relx=0.8, rely=0.9)

        self.window.mainloop()

    def voltar(self):
        self.window.destroy()

    def enviar_pedido(self):
        try:
            cliente_id = self.client_map[self.client_combo.get()]
            funcionario_id = self.employee_map[self.employee_combo.get()]
            shipper_id = self.shipper_map[self.shipper_combo.get()]

            endereco = self.address.get()
            cidade = self.city.get()
            regiao = self.region.get()
            pais = self.country.get()
            cep = self.postalCode.get()

            self.controller.criar_pedido(
                customerid=cliente_id,
                employeeid=funcionario_id,
                shipperid=shipper_id,
                endereco=endereco,
                cidade=cidade,
                regiao=regiao,
                pais=pais,
                cep=cep
            )

            messagebox.showinfo("Sucesso", "Pedido criado com sucesso!")
            self.window.destroy()

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criar pedido: {str(e)}")

