# Projeto Northwind MVC+DAO - ATVBD2

## 📋 Descrição

Esta aplicação em Python exemplifica o uso dos padrões **MVC** (Model-View-Controller) e **DAO** (Data Access Object) para inserção e consulta de pedidos na base de dados *Northwind*. O projeto oferece duas formas de acesso ao banco de dados:

- **ORM (SQLAlchemy)**: abstração completa usando sessões, modelos relacionais e generics DAO.
- **Driver Puro (psycopg2)**: acesso direto via queries SQL, com e sem proteção contra SQL Injection.

## 🏗 Estrutura do Projeto

```
northwind-mvc-dao/
├── Controller/
│   ├── pedido_controller.py       # Lógica de pedidos (ORM)
│   ├── Psycopg_pedido_controller.py # Lógica de pedidos (psycopg2)
│   ├── relatorio_controller.py    # Relatórios (ORM)
│   └── Psycopg_relatorio_controller.py # Relatórios (psycopg2)
├── DB/
│   ├── DaoOrm.py                  # GenericDAO para SQLAlchemy
│   ├── PsycopgConn.py             # Cria conexão psycopg2 via .env
│   └── PsycopgDao.py              # DAO puro com psycopg2
├── Model/                         # Classes geradas por sqlacodegen
│   ├── base.py
│   ├── customers.py
│   ├── employees.py
│   ├── orders.py
│   ├── orderDetails.py
│   ├── products.py
│   ├── shippers.py
   └── ...
├── screens/                       # Interfaces Tkinter / tkcalendar
│   ├── home.py
│   ├── newOrder.py
│   ├── reportEmployees.py
│   └── reportOrders.py
├── .env                           # Configuração de acesso ao DB
├── main.py                        # Ponto de entrada da aplicação
└── README.md                      # Documentação do projeto
```

## ⚙️ Tecnologias

- Python 3.9+
- Tkinter + tkcalendar
- SQLAlchemy 2.x
- psycopg2 2.9.1
- python-dotenv 1.1
- sqlacodegen 3.0.0

## 🚀 Como executar

1. **Clonar o repositório**

   ```bash
   git clone https://github.com/AndradeRafael41/Atv_BD2
   ```

2. **Criar e ativar ambiente virtual**

   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Instalar dependências**

   ```bash
   pip install sqlalchemy psycopg2 python-dotenv tkcalendar tabulate
   ```

4. **Configurar variáveis de ambiente**

   Crie um arquivo `.env` na raiz com as chaves:

   ```dotenv
   DB_USER=seu_usuario
   DB_PASSWORD=sua_senha
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=northwind
   ```

5. **Executar a aplicação**

   ```bash
   python main.py
   ```

## 👓 Uso

- Na **Home**, escolha uma das opções:

  - **Novo Pedido**: preencha o formulário. Selecione **ORM** ou **Driver** no topo.
  - **Relatório Pedidos**: consulte detalhes de um pedido existente.
  - **Relatório Funcionários**: ranking de vendas por período.

- Alternando entre **ORM** e **Driver**:

  - **ORM**: aproveita relacionamentos e `GenericDAO` do SQLAlchemy.
  - **Driver**: executa SQL manualmente.

## 🔧 Modelos e Relacionamentos

- O diretório `Model/` contém classes com colunas e **relationship()** usadas pelo SQLAlchemy.

## 📚 Boas práticas

- Utilize **queries parametrizadas** no DAO psycopg2 para evitar SQL Injection:

  ```python
  cursor.execute(
      "INSERT INTO schema.table (col1, col2) VALUES (%s, %s)",
      (valor1, valor2)
  )
  ```

- Mantenha **rollback** em transações que falharem.

- Separe claramente as camadas **View**, **Controller** e **DAO**.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
