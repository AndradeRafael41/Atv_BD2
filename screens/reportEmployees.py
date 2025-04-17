import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # pip install tkcalendar
from Controller.relatorio_controller import RelatorioController

class reportEmployees:

    def __init__(self):
        self.controller = RelatorioController()
        self.root = tk.Tk()
        self.root.title("Ranking de Funcionários por Período")
        self.root.geometry("650x500")

        # Frame de Filtros
        frame_filtros = tk.Frame(self.root, padx=10, pady=10)
        frame_filtros.pack()

        tk.Label(frame_filtros, text="Data Início:").grid(row=0, column=0, sticky="w")
        self.data_inicio = DateEntry(frame_filtros, width=12, background='darkblue',
                                     foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
        self.data_inicio.grid(row=0, column=1, padx=5)

        tk.Label(frame_filtros, text="Data Fim:").grid(row=0, column=2, sticky="w")
        self.data_fim = DateEntry(frame_filtros, width=12, background='darkblue',
                                  foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
        self.data_fim.grid(row=0, column=3, padx=5)

        btn_pesquisar = tk.Button(frame_filtros, text="Pesquisar", command=self.buscar_ranking)
        btn_pesquisar.grid(row=0, column=4, padx=10)

        # Treeview para exibir ranking
        self.tree = ttk.Treeview(self.root, columns=("Nome", "Pedidos", "Total"), show="headings", height=16)
        self.tree.heading("Nome", text="Nome do Funcionário")
        self.tree.heading("Pedidos", text="Total de Pedidos")
        self.tree.heading("Total", text="Valor Total Vendido")

        self.tree.column("Nome", width=250)
        self.tree.column("Pedidos", width=150, anchor="center")
        self.tree.column("Total", width=150, anchor="center")

        self.tree.pack(padx=10, pady=20)

        # Botão de voltar
        btn_voltar = tk.Button(self.root, text="Voltar", command=self.voltar)
        btn_voltar.pack(pady=(0, 10))

    def buscar_ranking(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        inicio = self.data_inicio.get_date()
        fim = self.data_fim.get_date()

        try:
            ranking = self.controller.listar_ranking_funcionarios(inicio, fim)
            if not ranking:
                messagebox.showinfo("Sem dados", "Nenhum registro encontrado para o período selecionado.")
                return

            for row in ranking:
                self.tree.insert("", "end", values=(
                    row.employee_name,
                    row.total_orders,
                    row.total_sales
                ))

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

    def voltar(self):
        self.root.destroy()
        from screens.home import home
        home().run()

    def run(self):
        self.root.mainloop()