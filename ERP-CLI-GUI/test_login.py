#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste da Tela de Login GUI
Versão simplificada para teste
"""

import tkinter as tk
from tkinter import ttk, messagebox
import hashlib

class LoginTest:
    """Teste da janela de login"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema ERP - Login (Teste)")
        self.root.geometry("450x350")
        self.root.resizable(False, False)
        
        # Centralizar janela
        self.center_window()
        
        self.authenticated_user = None
        self.create_widgets()
    
    def center_window(self):
        """Centraliza a janela na tela"""
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (450 // 2)
        y = (self.root.winfo_screenheight() // 2) - (350 // 2)
        self.root.geometry(f'450x350+{x}+{y}')
    
    def create_widgets(self):
        """Cria os widgets da janela de login"""
        # Configurar estilo
        style = ttk.Style()
        style.theme_use('clam')
        
        # Frame principal com cor de fundo
        main_frame = tk.Frame(self.root, bg='#f0f0f0', padx=30, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_label = tk.Label(main_frame, text="🏢 Sistema ERP", 
                              font=("Arial", 22, "bold"), 
                              bg='#f0f0f0', fg='#2c3e50')
        title_label.pack(pady=(10, 5))
        
        # Subtitle
        subtitle_label = tk.Label(main_frame, text="Enterprise Resource Planning", 
                                 font=("Arial", 11), 
                                 bg='#f0f0f0', fg='#7f8c8d')
        subtitle_label.pack(pady=(0, 30))
        
        # Frame de login com borda
        login_frame = tk.LabelFrame(main_frame, text=" 🔐 Autenticação ", 
                                   font=("Arial", 12, "bold"),
                                   bg='#ffffff', fg='#2c3e50',
                                   relief='raised', bd=2)
        login_frame.pack(fill=tk.X, pady=20, padx=10)
        
        # Padding interno
        inner_frame = tk.Frame(login_frame, bg='#ffffff')
        inner_frame.pack(fill=tk.BOTH, padx=20, pady=15)
        
        # Campo Usuário
        user_label = tk.Label(inner_frame, text="👤 Usuário:", 
                             font=("Arial", 11, "bold"), 
                             bg='#ffffff', fg='#2c3e50')
        user_label.pack(anchor=tk.W, pady=(5, 2))
        
        self.username_var = tk.StringVar(value="admin")
        self.username_entry = tk.Entry(inner_frame, textvariable=self.username_var, 
                                      font=("Arial", 12), width=25,
                                      relief='solid', bd=1)
        self.username_entry.pack(fill=tk.X, pady=(0, 15), ipady=5)
        
        # Campo Senha
        pass_label = tk.Label(inner_frame, text="🔑 Senha:", 
                             font=("Arial", 11, "bold"), 
                             bg='#ffffff', fg='#2c3e50')
        pass_label.pack(anchor=tk.W, pady=(0, 2))
        
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(inner_frame, textvariable=self.password_var, 
                                      show="●", font=("Arial", 12), width=25,
                                      relief='solid', bd=1)
        self.password_entry.pack(fill=tk.X, pady=(0, 20), ipady=5)
        
        # Frame para botões
        button_frame = tk.Frame(inner_frame, bg='#ffffff')
        button_frame.pack(fill=tk.X, pady=10)
        
        # Botão de login
        self.login_btn = tk.Button(button_frame, text="🚀 Entrar no Sistema", 
                                  command=self.login,
                                  font=("Arial", 11, "bold"),
                                  bg='#3498db', fg='white',
                                  relief='raised', bd=2,
                                  cursor='hand2')
        self.login_btn.pack(side=tk.LEFT, padx=(0, 10), pady=5, fill=tk.X, expand=True)
        
        # Botão de sair
        exit_btn = tk.Button(button_frame, text="❌ Sair", 
                            command=self.root.quit,
                            font=("Arial", 11),
                            bg='#e74c3c', fg='white',
                            relief='raised', bd=2,
                            cursor='hand2')
        exit_btn.pack(side=tk.RIGHT, pady=5)
        
        # Eventos de teclado
        self.username_entry.bind('<Return>', lambda e: self.password_entry.focus())
        self.password_entry.bind('<Return>', lambda e: self.login())
        self.root.bind('<Escape>', lambda e: self.root.quit())
        
        # Frame de informações
        info_frame = tk.Frame(main_frame, bg='#ecf0f1', relief='sunken', bd=1)
        info_frame.pack(fill=tk.X, pady=10, padx=10)
        
        info_title = tk.Label(info_frame, text="📋 Informações de Acesso", 
                             font=("Arial", 10, "bold"), 
                             bg='#ecf0f1', fg='#2c3e50')
        info_title.pack(pady=(10, 5))
        
        info_text = tk.Label(info_frame, 
                            text="🔑 Usuário: admin\n🔑 Senha: mudar@123\n\n💡 Pressione Enter para fazer login", 
                            font=("Arial", 9), 
                            bg='#ecf0f1', fg='#34495e',
                            justify=tk.CENTER)
        info_text.pack(pady=(0, 10))
        
        # Foco inicial no campo de senha (usuário já preenchido)
        self.password_entry.focus()
    
    def login(self):
        """Realiza o processo de login"""
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()
        
        # Debug - mostrar o que foi digitado
        print(f"Debug - Usuário: '{username}', Senha: '{password}'")
        
        # Validar campos
        if not username:
            messagebox.showerror("❌ Erro de Login", "Por favor, digite o nome de usuário!")
            self.username_entry.focus()
            return
            
        if not password:
            messagebox.showerror("❌ Erro de Login", "Por favor, digite a senha!")
            self.password_entry.focus()
            return
        
        # Feedback visual
        self.login_btn.configure(text="🔄 Verificando...", state="disabled")
        self.root.update()
        
        # Simular verificação (credenciais fixas para teste)
        if username == "admin" and password == "mudar@123":
            self.authenticated_user = {
                'username': username,
                'role': 'Admin'
            }
            messagebox.showinfo("✅ Login Realizado", f"Bem-vindo(a), {username}!\n\n🚀 Acessando o sistema...")
            self.root.destroy()
        else:
            messagebox.showerror("❌ Erro de Login", 
                               "Usuário ou senha inválidos!\n\n" +
                               "💡 Credenciais corretas:\n" +
                               "• Usuário: admin\n" +
                               "• Senha: mudar@123")
            self.password_var.set("")
            self.password_entry.focus()
        
        # Restaurar botão
        self.login_btn.configure(text="🚀 Entrar no Sistema", state="normal")
    
    def run(self):
        """Executa a janela de login"""
        self.root.mainloop()
        return self.authenticated_user

def main():
    """Teste da tela de login"""
    print("🧪 Iniciando teste da tela de login GUI...")
    
    login = LoginTest()
    user_info = login.run()
    
    if user_info:
        print(f"✅ Login realizado com sucesso!")
        print(f"📋 Usuário: {user_info['username']}")
        print(f"🔐 Role: {user_info['role']}")
        print("\n🎉 Teste da tela de login concluído com sucesso!")
    else:
        print("❌ Login cancelado pelo usuário.")

if __name__ == "__main__":
    main()
