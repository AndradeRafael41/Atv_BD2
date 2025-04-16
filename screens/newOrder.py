import tkinter as tk
from tkinter import ttk
from Model.orderDetails import OrderDetails
from Controller.pedido_controller import PedidoController
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry

class newOrder:

    def __init__(self):
        self.controller = PedidoController()
        self.window = tk.Tk()
        self.window.resizable(0,0)
        self.window.geometry("700x600")
        self.window.title("Novo Pedido")
        self.details = [] 

        # ---------- CLIENTES ----------
        tk.Label(self.window, text="Nome do Cliente:").place(relx=0.05, rely=0.05)
        self.clients = self.controller.listar_clientes()
        self.client_map = {f"{c.companyname}": c.customerid for c in self.clients}
        self.client_combo = ttk.Combobox(self.window, values=list(self.client_map.keys()), state="readonly", width=19)
        self.client_combo.place(relx=0.22, rely=0.05)
        self.client_combo.current(0)

        # ---------- FUNCIONÁRIOS ----------
        tk.Label(self.window, text="Nome do Vendedor:").place(relx=0.5, rely=0.05)
        self.employees = self.controller.listar_funcionarios()
        self.employee_map = {f"{e.firstname} {e.lastname}": e.employeeid for e in self.employees}
        self.employee_combo = ttk.Combobox(self.window, values=list(self.employee_map.keys()), state="readonly", width=19)
        self.employee_combo.place(relx=0.7, rely=0.05)
        self.employee_combo.current(0)

        # ---------- REMETENTES ----------
        tk.Label(self.window, text="Remetente:").place(relx=0.05, rely=0.1)
        self.shippers = self.controller.listar_entregadores()
        self.shipper_map = {f"{s.companyname}": s.shipperid for s in self.shippers}
        self.shipper_combo = ttk.Combobox(self.window, values=list(self.shipper_map.keys()), state="readonly", width=19)
        self.shipper_combo.place(relx=0.22, rely=0.1)
        self.shipper_combo.current(0)

        # ---------- OUTROS CAMPOS ----------
        tk.Label(self.window, text="Nome do Navio:").place(relx=0.5, rely=0.1)
        self.shipName = tk.Entry(self.window)
        self.shipName.place(relx=0.7, rely=0.1)

        tk.Label(self.window, text="Código Postal:").place(relx=0.05, rely=0.15)
        self.postalCode = tk.Entry(self.window)
        self.postalCode.place(relx=0.22, rely=0.15)

        ttk.Label(self.window, text='Data Pretendida:').place(relx=0.5, rely=0.15)
        self.requiredDate = DateEntry(self.window, width=19, background='darkblue', foreground='white', borderwidth=2, year=2025)
        self.requiredDate.place(relx=0.7, rely=0.15)

        tk.Label(self.window, text="Endereço:").place(relx=0.05, rely=0.2)
        self.address = tk.Entry(self.window)
        self.address.place(relx=0.22, rely=0.2)

        ttk.Label(self.window, text='Data de Postagem:').place(relx=0.5, rely=0.2)
        self.shippedDate = DateEntry(self.window, width=19, background='darkblue', foreground='white', borderwidth=2, year=2025)
        self.shippedDate.place(relx=0.7, rely=0.2)

        tk.Label(self.window, text="Cidade:").place(relx=0.05, rely=0.25)
        self.city = tk.Entry(self.window)
        self.city.place(relx=0.22, rely=0.25)

        tk.Label(self.window, text="Região:").place(relx=0.5, rely=0.25)
        self.region = tk.Entry(self.window)
        self.region.place(relx=0.7, rely=0.25)

        tk.Label(self.window, text="País:").place(relx=0.05, rely=0.3)
        self.country = tk.Entry(self.window)
        self.country.place(relx=0.22, rely=0.3)

        tk.Label(self.window, text="Frete:").place(relx=0.5, rely=0.3)
        self.freight = tk.Entry(self.window)
        self.freight.place(relx=0.7, rely=0.3)

        tk.Label(self.window, text="Produto:").place(relx=0.05, rely=0.35)
        self.products = self.controller.listar_produtos()
        self.product_map = {f"{p.productname}": p.productid for p in self.products}
        self.product_combo = ttk.Combobox(self.window, values=list(self.product_map.keys()), state="readonly", width=19)
        self.product_combo.place(relx=0.22, rely=0.35)
        self.product_combo.current(0)

        tk.Label(self.window, text="Quantidade:").place(relx=0.5, rely=0.35)
        self.product_qtd = tk.Entry(self.window)
        self.product_qtd.place(relx=0.7, rely=0.35)

        tk.Label(self.window, text="Preço:").place(relx=0.05, rely=0.4)
        self.product_price = tk.Entry(self.window)
        self.product_price.place(relx=0.22, rely=0.4)

        tk.Label(self.window, text="Desconto:").place(relx=0.5, rely=0.4)
        self.product_discount = tk.Entry(self.window)
        self.product_discount.place(relx=0.7, rely=0.4)

        tk.Button(self.window, text="Adicionar", command=self.adicionar_produto, width=6).place(relx=0.83, rely=0.45)

        self.product_listbox = tk.Listbox(self.window, width=70, height=5)
        self.product_listbox.place(relx=0.1, rely=0.52)


        # ---------- BOTÕES ----------
        tk.Button(self.window, text="Voltar", command=self.voltar).place(relx=0.1, rely=0.75)
        tk.Button(self.window, text="Enviar", command=self.enviar_pedido).place(relx=0.81, rely=0.75)

        self.window.mainloop()

    def voltar(self):
        self.window.destroy()
        from screens.home import home  # ✅ import atrasado, resolve o ciclo
        home()
    
    def adicionar_produto(self):
        try:
            produto_nome = self.product_combo.get()
            quantidade = int(self.product_qtd.get())
            preco = float(self.product_price.get())
            desconto = float(self.product_discount.get())

            detail = OrderDetails(
                productid=self.product_map[produto_nome],
                unitprice=preco,
                quantity=quantidade,
                discount=desconto
            )

            self.details.append(detail)

            # Adiciona ao Listbox uma linha com os dados do produto
            self.product_listbox.insert(tk.END, f"{produto_nome} - Qtd: {quantidade} - Preço: {preco} - Desc: {desconto}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao adicionar produto: {str(e)}")  

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

            requiredDate = self.requiredDate.get()
            shippedDate = self.shippedDate.get()
            freight = self.freight.get()
            shipName = self.shipName.get()
            details = self.details

            self.controller.criar_pedido(
                customerid = cliente_id,
                employeeid = funcionario_id,
                shipperid = shipper_id,
                endereco = endereco,
                cidade = cidade,
                regiao = regiao,
                pais = pais,
                cep = cep,
                requiredDate = requiredDate,
                shippedDate = shippedDate,
                freight = freight,
                shipName = shipName,
                products = details
            )

            messagebox.showinfo("Sucesso", "Pedido criado com sucesso!")
            self.window.destroy()

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criar pedido: {str(e)}")        


