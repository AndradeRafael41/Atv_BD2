import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from Model.orderDetails import OrderDetails
from Controller.pedido_controller import PedidoController
from Controller.Psycopg_pedido_controller import PedidoControllerDriver

class newOrder:
    def __init__(self):
        self.controller = PedidoController()
        self.controllerDriver = PedidoControllerDriver()
        self.details = []

        # Configuração da janela
        self.window = tk.Tk()
        self.window.title("Novo Pedido")
        self.window.resizable(False, False)
        self.window.geometry("640x670")
        self.window.configure(padx=20, pady=20)

        self.font = ("Helvetica", 11)
        self.input_width = 18
        
        self.tipo_conexao = tk.StringVar(value="orm")

        # Frame para os radio buttons no topo da janela
        radio_frame = tk.Frame(self.window)
        radio_frame.pack(fill='x', pady=(0, 10))

        tk.Label(radio_frame, text="Tipo de conexão:", font=self.font).pack(side='left', padx=(0, 10))
        tk.Radiobutton(
            radio_frame, text="ORM", variable=self.tipo_conexao,
            value="orm", font=self.font
        ).pack(side='left')
        tk.Radiobutton(
            radio_frame, text="Driver", variable=self.tipo_conexao,
            value="driver", font=self.font
        ).pack(side='left')

        # Frame para dados do pedido
        pedido_frame = tk.LabelFrame(self.window, text="Detalhes do Pedido", font=self.font)
        pedido_frame.pack(fill='x', pady=10)

        pedido_fields = [
            [("Cliente:", ttk.Combobox, self._load_customers), ("Vendedor:", ttk.Combobox, self._load_employees)],
            [("Remetente:", ttk.Combobox, self._load_shippers), ("Navio:", tk.Entry, lambda: None)],
            [("CEP:", tk.Entry, lambda: None), ("Data Pretendida:", DateEntry, lambda: None)],
            [("Endereço:", tk.Entry, lambda: None), ("Data Postagem:", DateEntry, lambda: None)],
            [("Cidade:", tk.Entry, lambda: None), ("Região:", tk.Entry, lambda: None)],
            [("País:", tk.Entry, lambda: None), ("Frete:", tk.Entry, lambda: None)],
        ]

        self.widgets = {}
        for row, field_pair in enumerate(pedido_fields):
            for col, (label_text, widget_type, loader) in enumerate(field_pair):
                label_col = col * 2
                widget_col = col * 2 + 1

                tk.Label(pedido_frame, text=label_text, font=self.font).grid(
                    row=row, column=label_col, sticky='w', padx=(5, 0), pady=3
                )
                if widget_type is ttk.Combobox:
                    widget = widget_type(
                        pedido_frame,
                        state="readonly",
                        width=self.input_width,
                        font=self.font
                    )
                    loader(widget)
                    widget.current(0)
                elif widget_type is DateEntry:
                    widget = widget_type(
                        pedido_frame,
                        width=self.input_width,
                        font=self.font
                    )
                else:
                    widget = widget_type(
                        pedido_frame,
                        width=self.input_width,
                        font=self.font
                    )
                widget.grid(row=row, column=widget_col, sticky='w', padx=(0, 20), pady=3)
                self.widgets[label_text[:-1]] = widget

        # Frame para produtos
        produto_frame = tk.LabelFrame(self.window, text="Itens do Pedido", font=self.font)
        produto_frame.pack(fill='x', pady=10)

        produto_fields = [
            [("Produto:", ttk.Combobox, self._load_products), ("Quantidade:", tk.Entry, lambda: None)],
            [("Preço:", tk.Entry, lambda: None), ("Desconto:", tk.Entry, lambda: None)]
        ]

        for row, field_pair in enumerate(produto_fields):
            for col, (label_text, widget_type, loader) in enumerate(field_pair):
                label_col = col * 2
                widget_col = col * 2 + 1

                tk.Label(produto_frame, text=label_text, font=self.font).grid(
                    row=row, column=label_col, sticky='w', padx=(10, 5), pady=4
                )
                if widget_type is ttk.Combobox:
                    widget = widget_type(
                        produto_frame,
                        state="readonly",
                        width=20,
                        font=self.font
                    )
                    loader(widget)
                    widget.current(0)
                else:
                    widget = widget_type(
                        produto_frame,
                        width=self.input_width,
                        font=self.font
                    )
                widget.grid(row=row, column=widget_col, sticky='w', padx=(0, 15), pady=4)
                self.widgets[label_text[:-1]] = widget

        # Botão Adicionar Item alinhado mais à esquerda
        btn_add = tk.Button(
            produto_frame,
            text="Adicionar Item",
            font=self.font,
            width=15,
            command=self.adicionar_produto
        )
        btn_add.grid(row=2, column=3, sticky='w', padx=(10, 5), pady=(6, 10))

        self.product_listbox = tk.Listbox(
            produto_frame,
            width=70,
            height=10,
            font=self.font
        )
        self.product_listbox.grid(row=3, column=0, columnspan=4, padx=(10, 10), pady=(0, 10))

        # Botões 
        action_frame = tk.Frame(self.window)
        action_frame.pack(fill='x')
        tk.Button(
            action_frame, text="Voltar", font=self.font,
            width=12, command=self.voltar
        ).pack(side='left', padx=5)
        tk.Button(
            action_frame, text="Enviar", font=self.font,
            width=12, command=self.enviar_pedido
        ).pack(side='right', padx=5)

    def _load_customers(self, widget):
        customers = self.controller.listar_clientes()
        self.customer_map = {c.companyname: c.customerid for c in customers}
        widget['values'] = list(self.customer_map.keys())

    def _load_employees(self, widget):
        employees = self.controller.listar_funcionarios()
        self.employee_map = {f"{e.firstname} {e.lastname}": e.employeeid for e in employees}
        widget['values'] = list(self.employee_map.keys())

    def _load_shippers(self, widget):
        shippers = self.controller.listar_entregadores()
        self.shipper_map = {s.companyname: s.shipperid for s in shippers}
        widget['values'] = list(self.shipper_map.keys())

    def _load_products(self, widget):
        products = self.controller.listar_produtos()
        self.product_map = {p.productname: p.productid for p in products}
        widget['values'] = list(self.product_map.keys())

    def voltar(self):
        self.window.destroy()
        from screens.home import home
        home().run()

    def adicionar_produto(self):
        try:
            nome = self.widgets['Produto'].get()
            qtd = int(self.widgets['Quantidade'].get())
            preco = float(self.widgets['Preço'].get())
            desc = float(self.widgets['Desconto'].get())
            detail = OrderDetails(
                productid=self.product_map[nome],
                quantity=qtd,
                unitprice=preco,
                discount=desc
            )
            self.details.append(detail)
            self.product_listbox.insert(
                tk.END,
                f"{nome} - Qtd: {qtd} - Preço: {preco} - Desc: {desc}"
            )
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao adicionar produto: {e}")

    def enviar_pedido(self):
        try:
            data = {
                'customerid': self.customer_map[self.widgets['Cliente'].get()],
                'employeeid': self.employee_map[self.widgets['Vendedor'].get()],
                'shipperid': self.shipper_map[self.widgets['Remetente'].get()],
                'shipName': self.widgets['Navio'].get(),
                'cep': self.widgets['CEP'].get(),
                'requiredDate': self.widgets['Data Pretendida'].get(),
                'endereco': self.widgets['Endereço'].get(),
                'shippedDate': self.widgets['Data Postagem'].get(),
                'cidade': self.widgets['Cidade'].get(),
                'regiao': self.widgets['Região'].get(),
                'pais': self.widgets['País'].get(),
                'freight': self.widgets['Frete'].get(),
                'order_details': self.details
            }
            if(self.tipo_conexao.get()=='orm'):
                self.controller.criar_pedido(**data)
            else:
                self.controllerDriver.criar_pedido(**data)
            messagebox.showinfo("Sucesso", "Pedido criado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criar pedido: {e}")

    def run(self):
        self.window.mainloop()