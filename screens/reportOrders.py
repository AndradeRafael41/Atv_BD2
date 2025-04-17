import tkinter as tk
from tkinter import ttk, messagebox
from Controller.relatorio_controller import RelatorioController

class reportOrders:
    
    def __init__(self):
        self.controller = RelatorioController()
        # Configuração da janela principal
        self.root = tk.Tk()
        self.root.title("Pesquisar Pedido")

        # Frame de pesquisa
        frame = tk.Frame(self.root, padx=10, pady=10)
        frame.pack()

        tk.Label(frame, text="Número do Pedido:").grid(row=0, column=0, sticky="w")

        self.orders = self.controller.listar_pedidos()
        self.order_map = {f"{o.orderid}": o.orderid for o in self.orders}
        self.combo_pedidos = ttk.Combobox(frame, values=list(self.order_map.keys()), state="readonly")
        self.combo_pedidos.grid(row=0, column=1, padx=5)
        self.combo_pedidos.current(0)  # Seleciona o primeiro por padrão (opcional)

        btn_pesquisar = tk.Button(frame, text="Pesquisar", command=self.pesquisar_pedido)
        btn_pesquisar.grid(row=0, column=2, padx=5)

        # Treeview para exibição dos pedidos
        self.tree = ttk.Treeview(self.root, columns=("Atributo", "Valor"), show="headings", height=15)
        self.tree.heading("Atributo", text="Atributo")
        self.tree.heading("Valor", text="Valor")
        self.tree.column("Atributo", width=150)
        self.tree.column("Valor", width=400)
        self.tree.pack(padx=10, pady=10)
        
        # Botão de Voltar para Home
        btn_voltar = tk.Button(self.root, text="Voltar", command=self.voltar)
        btn_voltar.pack(pady=(0, 10))

    def pesquisar_pedido(self):
        # Limpa a treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        numero = self.combo_pedidos.get().strip()
        pedido_encontrado = self.controller.listar_relatorio_pedidos(numero)

        if pedido_encontrado:
            self.tree.insert("", "end", values=("Número do Pedido", pedido_encontrado.orderid))
            self.tree.insert("", "end", values=("Data do Pedido", pedido_encontrado.orderdate))
            self.tree.insert("", "end", values=("Nome do Cliente", pedido_encontrado.customers.companyname))
            self.tree.insert("", "end", values=("Nome do Vendedor", f"{pedido_encontrado.employees.firstname} {pedido_encontrado.employees.lastname}"))
            self.tree.insert("", "end", values=("Itens do Pedido", ""))
            for item in pedido_encontrado.order_details:
                desc = f'{item.products.productname} - Quantidade: {item.quantity}, Preço: $ {item.unitprice:.2f}'
                self.tree.insert("", "end", values=("", desc))
        else:
            messagebox.showinfo("Não encontrado", "Pedido não encontrado.")

    def voltar(self):
        self.root.destroy()
        from screens.home import home
        home().run()

    def run(self):
        self.root.mainloop()