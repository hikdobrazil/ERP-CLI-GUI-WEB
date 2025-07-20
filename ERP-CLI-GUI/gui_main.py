#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema ERP - Versão GUI
Interface gráfica moderna inspirada em sistemas profissionais
Autor: Sistema ERP
Data: 2025
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os
import hashlib
from datetime import datetime
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Any
import sqlite3

@dataclass
class Employee:
    """Classe para representar um funcionário"""
    id: str
    name: str
    position: str
    department: str
    hire_date: str
    salary: float
    active: bool = True

@dataclass
class Equipment:
    """Classe para representar um equipamento"""
    id: str
    name: str
    type: str
    brand: str
    model: str
    serial_number: str
    purchase_date: str
    status: str = "Ativo"

@dataclass
class ServiceOrder:
    """Classe para representar uma ordem de serviço"""
    id: str
    employee_id: str
    equipment_id: str
    description: str
    priority: str
    status: str
    created_date: str
    due_date: str

class DatabaseManager:
    """Gerenciador de banco de dados SQLite"""
    
    def __init__(self, db_path: str = "erp_database.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Inicializa o banco de dados com as tabelas necessárias"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Tabela de usuários
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                role TEXT NOT NULL,
                created_date TEXT NOT NULL,
                last_login TEXT,
                active BOOLEAN DEFAULT 1
            )
        ''')
        
        # Tabela de funcionários
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                position TEXT NOT NULL,
                department TEXT NOT NULL,
                hire_date TEXT NOT NULL,
                salary REAL NOT NULL,
                active BOOLEAN DEFAULT 1
            )
        ''')
        
        # Tabela de equipamentos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS equipment (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                brand TEXT NOT NULL,
                model TEXT NOT NULL,
                serial_number TEXT NOT NULL,
                purchase_date TEXT NOT NULL,
                status TEXT DEFAULT 'Ativo'
            )
        ''')
        
        # Tabela de ordens de serviço
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS service_orders (
                id TEXT PRIMARY KEY,
                employee_id TEXT NOT NULL,
                equipment_id TEXT NOT NULL,
                description TEXT NOT NULL,
                priority TEXT NOT NULL,
                status TEXT NOT NULL,
                created_date TEXT NOT NULL,
                due_date TEXT NOT NULL,
                FOREIGN KEY (employee_id) REFERENCES employees (id),
                FOREIGN KEY (equipment_id) REFERENCES equipment (id)
            )
        ''')
        
        # Criar usuário admin padrão se não existir
        cursor.execute('SELECT COUNT(*) FROM users WHERE username = ?', ('admin',))
        if cursor.fetchone()[0] == 0:
            password_hash = hashlib.sha256('mudar@123'.encode()).hexdigest()
            cursor.execute('''
                INSERT INTO users (username, password_hash, role, created_date)
                VALUES (?, ?, ?, ?)
            ''', ('admin', password_hash, 'Admin', datetime.now().isoformat()))
        
        conn.commit()
        conn.close()
    
    def execute_query(self, query: str, params: tuple = ()) -> List[tuple]:
        """Executa uma query e retorna os resultados"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        conn.commit()
        conn.close()
        return results
    
    def execute_insert(self, query: str, params: tuple = ()) -> bool:
        """Executa uma query de inserção"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Erro ao executar inserção: {e}")
            return False

class LoginWindow:
    """Janela de login do sistema"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema ERP - Login")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Centralizar janela
        self.center_window()
        
        self.db = DatabaseManager()
        self.authenticated_user = None
        
        self.create_widgets()
    
    def center_window(self):
        """Centraliza a janela na tela"""
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.root.winfo_screenheight() // 2) - (300 // 2)
        self.root.geometry(f'400x300+{x}+{y}')
    
    def create_widgets(self):
        """Cria os widgets da janela de login"""
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_label = ttk.Label(main_frame, text="Sistema ERP", font=("Arial", 20, "bold"))
        title_label.pack(pady=(0, 20))
        
        # Subtitle
        subtitle_label = ttk.Label(main_frame, text="Enterprise Resource Planning", font=("Arial", 10))
        subtitle_label.pack(pady=(0, 30))
        
        # Frame de login
        login_frame = ttk.LabelFrame(main_frame, text="Autenticação", padding="20")
        login_frame.pack(fill=tk.X, pady=10)
        
        # Grid para organizar campos
        login_frame.grid_columnconfigure(1, weight=1)
        
        # Usuário
        ttk.Label(login_frame, text="Usuário:", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w", pady=5)
        self.username_var = tk.StringVar(value="admin")
        self.username_entry = ttk.Entry(login_frame, textvariable=self.username_var, width=25, font=("Arial", 10))
        self.username_entry.grid(row=0, column=1, sticky="ew", padx=(10, 0), pady=5)
        
        # Senha
        ttk.Label(login_frame, text="Senha:", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w", pady=5)
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(login_frame, textvariable=self.password_var, show="*", width=25, font=("Arial", 10))
        self.password_entry.grid(row=1, column=1, sticky="ew", padx=(10, 0), pady=5)
        
        # Frame para botões
        button_frame = ttk.Frame(login_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=20)
        
        # Botão de login
        login_btn = ttk.Button(button_frame, text="🔐 Entrar", command=self.login)
        login_btn.pack(side=tk.LEFT, padx=10)
        
        # Botão de sair
        exit_btn = ttk.Button(button_frame, text="❌ Sair", command=self.root.quit)
        exit_btn.pack(side=tk.LEFT, padx=10)
        
        # Bind Enter key nos campos
        self.username_entry.bind('<Return>', lambda e: self.password_entry.focus())
        self.password_entry.bind('<Return>', lambda e: self.login())
        
        # Bind Escape para sair
        self.root.bind('<Escape>', lambda e: self.root.quit())
        
        # Foco inicial no campo de senha (usuário já preenchido)
        self.password_entry.focus()
        
        # Separador
        separator = ttk.Separator(main_frame, orient='horizontal')
        separator.pack(fill=tk.X, pady=10)
        
        # Informação inicial
        info_frame = ttk.Frame(main_frame)
        info_frame.pack(pady=10)
        
        info_label = ttk.Label(info_frame, text="🔑 Senha inicial: mudar@123", 
                              font=("Arial", 10, "bold"), foreground="blue")
        info_label.pack()
        
        help_label = ttk.Label(info_frame, text="💡 Pressione Enter para fazer login", 
                              font=("Arial", 8), foreground="gray")
        help_label.pack(pady=5)
    
    def login(self):
        """Realiza o processo de login"""
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()
        
        # Validar campos
        if not username:
            messagebox.showerror("Erro de Login", "Por favor, digite o nome de usuário!")
            self.username_entry.focus()
            return
            
        if not password:
            messagebox.showerror("Erro de Login", "Por favor, digite a senha!")
            self.password_entry.focus()
            return
        
        # Desabilitar botão durante login
        login_btn = None
        for widget in self.root.winfo_children():
            if hasattr(widget, 'winfo_children'):
                for child in widget.winfo_children():
                    if isinstance(child, ttk.LabelFrame):
                        for btn in child.winfo_children():
                            if isinstance(btn, ttk.Frame):
                                for button in btn.winfo_children():
                                    if isinstance(button, ttk.Button) and "Entrar" in button['text']:
                                        login_btn = button
                                        break
        
        if login_btn:
            login_btn.configure(text="🔄 Conectando...", state="disabled")
            self.root.update()
        
        try:
            # Verificar credenciais
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            result = self.db.execute_query(
                'SELECT id, username, role FROM users WHERE username = ? AND password_hash = ? AND active = 1',
                (username, password_hash)
            )
            
            if result:
                user_id, username, role = result[0]
                self.authenticated_user = {
                    'id': user_id,
                    'username': username,
                    'role': role
                }
                
                # Atualizar último login
                self.db.execute_insert(
                    'UPDATE users SET last_login = ? WHERE id = ?',
                    (datetime.now().isoformat(), user_id)
                )
                
                # Sucesso - mostrar mensagem e fechar
                messagebox.showinfo("Login", f"Bem-vindo(a), {username}!\n\nAcessando o sistema...")
                self.root.destroy()
                
            else:
                # Falha no login
                messagebox.showerror("Erro de Login", 
                                   "❌ Usuário ou senha inválidos!\n\n" +
                                   "💡 Verifique:\n" +
                                   "• Usuário: admin\n" +
                                   "• Senha: mudar@123")
                self.password_var.set("")
                self.password_entry.focus()
                
        except Exception as e:
            messagebox.showerror("Erro do Sistema", f"Erro ao conectar com o banco de dados:\n{str(e)}")
            
        finally:
            # Reabilitar botão
            if login_btn:
                login_btn.configure(text="🔐 Entrar", state="normal")
    
    def run(self):
        """Executa a janela de login"""
        self.root.mainloop()
        return self.authenticated_user

class MainWindow:
    """Janela principal do sistema ERP"""
    
    def __init__(self, user_info):
        self.user_info = user_info
        self.db = DatabaseManager()
        
        self.root = tk.Tk()
        self.root.title(f"Sistema ERP - {user_info['username']} ({user_info['role']})")
        self.root.geometry("1200x800")
        self.root.state('zoomed')  # Maximizar no Windows
        
        self.create_menu()
        self.create_widgets()
        self.create_status_bar()
        
        # Mostrar dashboard inicial
        self.show_dashboard()
    
    def create_menu(self):
        """Cria a barra de menu"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Menu Arquivo
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Arquivo", menu=file_menu)
        file_menu.add_command(label="Dashboard", command=self.show_dashboard)
        file_menu.add_separator()
        file_menu.add_command(label="Sair", command=self.root.quit)
        
        # Menu Funcionários
        emp_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Funcionários", menu=emp_menu)
        emp_menu.add_command(label="Cadastrar", command=self.show_employee_form)
        emp_menu.add_command(label="Consultar", command=self.show_employees)
        
        # Menu Equipamentos
        eq_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Equipamentos", menu=eq_menu)
        eq_menu.add_command(label="Cadastrar", command=self.show_equipment_form)
        eq_menu.add_command(label="Consultar", command=self.show_equipment)
        
        # Menu Ordens de Serviço
        os_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ordens de Serviço", menu=os_menu)
        os_menu.add_command(label="Nova O.S.", command=self.show_service_order_form)
        os_menu.add_command(label="Consultar", command=self.show_service_orders)
        
        # Menu Administração
        if self.user_info['role'] == 'Admin':
            admin_menu = tk.Menu(menubar, tearoff=0)
            menubar.add_cascade(label="Administração", menu=admin_menu)
            admin_menu.add_command(label="Gerenciar Usuários", command=self.show_user_management)
            admin_menu.add_command(label="Backup", command=self.backup_database)
        
        # Menu Ajuda
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ajuda", menu=help_menu)
        help_menu.add_command(label="Sobre", command=self.show_about)
    
    def create_widgets(self):
        """Cria os widgets principais"""
        # Frame principal
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Toolbar
        toolbar = ttk.Frame(self.main_frame)
        toolbar.pack(fill=tk.X, pady=(0, 10))
        
        # Botões da toolbar
        ttk.Button(toolbar, text="📊 Dashboard", command=self.show_dashboard).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="👥 Funcionários", command=self.show_employees).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="🔧 Equipamentos", command=self.show_equipment).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="📋 Ordens de Serviço", command=self.show_service_orders).pack(side=tk.LEFT, padx=2)
        
        # Frame de conteúdo
        self.content_frame = ttk.Frame(self.main_frame)
        self.content_frame.pack(fill=tk.BOTH, expand=True)
    
    def create_status_bar(self):
        """Cria a barra de status"""
        status_frame = ttk.Frame(self.root)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        self.status_var = tk.StringVar()
        self.status_var.set(f"Usuário: {self.user_info['username']} | {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        
        status_label = ttk.Label(status_frame, textvariable=self.status_var)
        status_label.pack(side=tk.LEFT, padx=10, pady=5)
        
        # Atualizar hora a cada minuto
        self.update_status()
    
    def update_status(self):
        """Atualiza a barra de status"""
        self.status_var.set(f"Usuário: {self.user_info['username']} | {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        self.root.after(60000, self.update_status)  # Atualizar a cada minuto
    
    def clear_content(self):
        """Limpa o frame de conteúdo"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def show_dashboard(self):
        """Mostra o dashboard principal"""
        self.clear_content()
        
        # Título
        title = ttk.Label(self.content_frame, text="Dashboard - Sistema ERP", 
                         font=("Arial", 16, "bold"))
        title.pack(pady=20)
        
        # Frame de estatísticas
        stats_frame = ttk.Frame(self.content_frame)
        stats_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Obter estatísticas
        emp_count = len(self.db.execute_query('SELECT id FROM employees WHERE active = 1'))
        eq_count = len(self.db.execute_query('SELECT id FROM equipment'))
        os_open = len(self.db.execute_query("SELECT id FROM service_orders WHERE status != 'Concluída'"))
        
        # Cards de estatísticas
        self.create_stat_card(stats_frame, "👥 Funcionários", str(emp_count), 0, 0)
        self.create_stat_card(stats_frame, "🔧 Equipamentos", str(eq_count), 0, 1)
        self.create_stat_card(stats_frame, "📋 O.S. Abertas", str(os_open), 0, 2)
        
        # Frame de ações rápidas
        actions_frame = ttk.LabelFrame(self.content_frame, text="Ações Rápidas", padding="20")
        actions_frame.pack(fill=tk.X, padx=20, pady=20)
        
        ttk.Button(actions_frame, text="Cadastrar Funcionário", 
                  command=self.show_employee_form).pack(side=tk.LEFT, padx=10)
        ttk.Button(actions_frame, text="Nova Ordem de Serviço", 
                  command=self.show_service_order_form).pack(side=tk.LEFT, padx=10)
        ttk.Button(actions_frame, text="Consultar Equipamentos", 
                  command=self.show_equipment).pack(side=tk.LEFT, padx=10)
    
    def create_stat_card(self, parent, title, value, row, col):
        """Cria um card de estatística"""
        card = ttk.LabelFrame(parent, text=title, padding="20")
        card.grid(row=row, column=col, padx=10, pady=10, sticky="ew")
        
        value_label = ttk.Label(card, text=value, font=("Arial", 24, "bold"))
        value_label.pack()
        
        # Configurar grid weights
        parent.grid_columnconfigure(col, weight=1)
    
    def show_employees(self):
        """Mostra a lista de funcionários"""
        self.clear_content()
        
        # Título e botão de novo
        header_frame = ttk.Frame(self.content_frame)
        header_frame.pack(fill=tk.X, padx=20, pady=10)
        
        ttk.Label(header_frame, text="Gestão de Funcionários", 
                 font=("Arial", 14, "bold")).pack(side=tk.LEFT)
        ttk.Button(header_frame, text="+ Novo Funcionário", 
                  command=self.show_employee_form).pack(side=tk.RIGHT)
        
        # Treeview para funcionários
        columns = ('ID', 'Nome', 'Cargo', 'Departamento', 'Data Admissão', 'Salário')
        tree = ttk.Treeview(self.content_frame, columns=columns, show='headings', height=15)
        
        # Configurar colunas
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.content_frame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        # Pack treeview e scrollbar
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Carregar dados
        employees = self.db.execute_query('SELECT * FROM employees WHERE active = 1')
        for emp in employees:
            tree.insert('', tk.END, values=emp)
    
    def show_employee_form(self):
        """Mostra o formulário de cadastro de funcionário"""
        form_window = tk.Toplevel(self.root)
        form_window.title("Cadastro de Funcionário")
        form_window.geometry("500x600")
        form_window.resizable(False, False)
        
        # Centralizar janela
        form_window.transient(self.root)
        form_window.grab_set()
        
        # Frame principal
        main_frame = ttk.Frame(form_window, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        ttk.Label(main_frame, text="Cadastro de Funcionário", 
                 font=("Arial", 14, "bold")).pack(pady=(0, 20))
        
        # Campos do formulário
        fields = [
            ("ID:", "id"),
            ("Nome:", "name"),
            ("Cargo:", "position"),
            ("Departamento:", "department"),
            ("Data de Admissão:", "hire_date"),
            ("Salário:", "salary")
        ]
        
        entries = {}
        for label, field in fields:
            frame = ttk.Frame(main_frame)
            frame.pack(fill=tk.X, pady=5)
            
            ttk.Label(frame, text=label, width=15).pack(side=tk.LEFT)
            entry = ttk.Entry(frame, width=30)
            entry.pack(side=tk.LEFT, padx=(10, 0), fill=tk.X, expand=True)
            entries[field] = entry
        
        # Gerar ID automático
        emp_count = len(self.db.execute_query('SELECT id FROM employees'))
        entries['id'].insert(0, f"EMP{emp_count + 1:04d}")
        entries['hire_date'].insert(0, datetime.now().strftime('%Y-%m-%d'))
        
        # Botões
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=20)
        
        def save_employee():
            data = {field: entry.get().strip() for field, entry in entries.items()}
            
            if not all(data.values()):
                messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
                return
            
            try:
                salary = float(data['salary'])
                success = self.db.execute_insert('''
                    INSERT INTO employees (id, name, position, department, hire_date, salary, active)
                    VALUES (?, ?, ?, ?, ?, ?, 1)
                ''', (data['id'], data['name'], data['position'], data['department'], 
                     data['hire_date'], salary))
                
                if success:
                    messagebox.showinfo("Sucesso", "Funcionário cadastrado com sucesso!")
                    form_window.destroy()
                    self.show_employees()
                else:
                    messagebox.showerror("Erro", "Erro ao cadastrar funcionário!")
            except ValueError:
                messagebox.showerror("Erro", "Salário deve ser um número válido!")
        
        ttk.Button(button_frame, text="Salvar", command=save_employee).pack(side=tk.LEFT, padx=10)
        ttk.Button(button_frame, text="Cancelar", command=form_window.destroy).pack(side=tk.LEFT)
    
    def show_equipment(self):
        """Mostra a lista de equipamentos"""
        self.clear_content()
        
        # Implementação similar aos funcionários
        ttk.Label(self.content_frame, text="Gestão de Equipamentos", 
                 font=("Arial", 14, "bold")).pack(pady=20)
        
        # Botão temporário
        ttk.Button(self.content_frame, text="Em desenvolvimento...", 
                  state=tk.DISABLED).pack()
    
    def show_equipment_form(self):
        """Mostra o formulário de cadastro de equipamento"""
        messagebox.showinfo("Em desenvolvimento", "Funcionalidade em desenvolvimento!")
    
    def show_service_orders(self):
        """Mostra a lista de ordens de serviço"""
        self.clear_content()
        
        ttk.Label(self.content_frame, text="Ordens de Serviço", 
                 font=("Arial", 14, "bold")).pack(pady=20)
        
        ttk.Button(self.content_frame, text="Em desenvolvimento...", 
                  state=tk.DISABLED).pack()
    
    def show_service_order_form(self):
        """Mostra o formulário de nova ordem de serviço"""
        messagebox.showinfo("Em desenvolvimento", "Funcionalidade em desenvolvimento!")
    
    def show_user_management(self):
        """Mostra o gerenciamento de usuários"""
        messagebox.showinfo("Administração", "Gerenciamento de usuários em desenvolvimento!")
    
    def backup_database(self):
        """Realiza backup do banco de dados"""
        messagebox.showinfo("Backup", "Funcionalidade de backup em desenvolvimento!")
    
    def show_about(self):
        """Mostra informações sobre o sistema"""
        about_text = """Sistema ERP - Versão GUI 1.0

Enterprise Resource Planning
Interface gráfica moderna e intuitiva

Desenvolvido em Python com tkinter
Base de dados SQLite

© 2025 - Sistema ERP"""
        
        messagebox.showinfo("Sobre o Sistema", about_text)
    
    def run(self):
        """Executa a janela principal"""
        self.root.mainloop()

def main():
    """Função principal da aplicação"""
    # Tela de login
    login = LoginWindow()
    user_info = login.run()
    
    if user_info:
        # Se login foi bem-sucedido, abrir janela principal
        main_app = MainWindow(user_info)
        main_app.run()

if __name__ == "__main__":
    main()
