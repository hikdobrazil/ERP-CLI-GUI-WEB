#!/usr/bin/env python3
"""
CLI ERP System - Main Application
A command-line Enterprise Resource Planning system with menu-driven interface
"""

import os
import sys
import datetime
import getpass
import time
import json
from dataclasses import dataclass
from typing import List, Dict, Optional

# Import for keyboard and mouse input detection
if os.name == 'nt':  # Windows
    import msvcrt
    # Try to enable mouse support in Windows terminal
    try:
        import ctypes
        from ctypes import wintypes
        MOUSE_SUPPORT = True
    except ImportError:
        MOUSE_SUPPORT = False
else:  # Unix/Linux
    import termios
    import tty
    MOUSE_SUPPORT = False

# Color codes for Windows CMD
class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[97m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    BLACK = '\033[30m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

class KeyboardInput:
    """Class to handle keyboard input including arrow keys"""
    
    @staticmethod
    def get_key():
        """Get a single key press including special keys like arrows"""
        if os.name == 'nt':  # Windows
            while True:
                if msvcrt.kbhit():
                    key = msvcrt.getch()
                    if key == b'\xe0':  # Special key prefix on Windows
                        key = msvcrt.getch()
                        if key == b'H':  # Up arrow
                            return 'UP'
                        elif key == b'P':  # Down arrow
                            return 'DOWN'
                        elif key == b'K':  # Left arrow
                            return 'LEFT'
                        elif key == b'M':  # Right arrow
                            return 'RIGHT'
                    elif key == b'\r':  # Enter
                        return 'ENTER'
                    elif key == b'\x1b':  # Escape
                        return 'ESC'
                    else:
                        return key.decode('utf-8', errors='ignore')
        else:  # Unix/Linux
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                key = sys.stdin.read(1)
                if key == '\x1b':  # Escape sequence
                    key += sys.stdin.read(2)
                    if key == '\x1b[A':  # Up arrow
                        return 'UP'
                    elif key == '\x1b[B':  # Down arrow
                        return 'DOWN'
                    elif key == '\x1b[C':  # Right arrow
                        return 'RIGHT'
                    elif key == '\x1b[D':  # Left arrow
                        return 'LEFT'
                elif key == '\r' or key == '\n':  # Enter
                    return 'ENTER'
                elif key == '\x1b':  # Escape
                    return 'ESC'
                else:
                    return key
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

class MouseSimulator:
    """Simulate mouse interactions using keyboard input"""
    
    def __init__(self):
        self.click_zones = {}  # Store clickable areas
        self.current_zones = []
        
    def add_click_zone(self, zone_id: str, start_line: int, end_line: int, text: str):
        """Add a clickable zone"""
        self.click_zones[zone_id] = {
            'start_line': start_line,
            'end_line': end_line,
            'text': text,
            'active': True
        }
    
    def clear_zones(self):
        """Clear all click zones"""
        self.click_zones.clear()
        self.current_zones.clear()
    
    def show_clickable_areas(self):
        """Display instructions for clickable areas"""
        if self.click_zones:
            print(f"\n{Colors.CYAN}🖱️  Áreas Clicáveis Disponíveis:{Colors.RESET}")
            for zone_id, zone in self.click_zones.items():
                print(f"{Colors.WHITE}   Tecle {Colors.YELLOW}'{zone_id.upper()}'{Colors.WHITE} para: {zone['text']}{Colors.RESET}")
    
    def handle_click_input(self) -> str:
        """Handle simulated mouse clicks via keyboard"""
        print(f"\n{Colors.CYAN}💡 Use setas ↑↓, ENTER, ou tecle a letra da opção:{Colors.RESET}")
        self.show_clickable_areas()
        print(f"{Colors.YELLOW}Aguardando entrada... {Colors.RESET}", end='', flush=True)
        
        if os.name == 'nt':
            while True:
                if msvcrt.kbhit():
                    key = msvcrt.getch()
                    if key == b'\xe0':  # Arrow keys
                        key = msvcrt.getch()
                        if key == b'H':
                            return 'UP'
                        elif key == b'P':
                            return 'DOWN'
                    elif key == b'\r':
                        return 'ENTER'
                    elif key == b'\x1b':
                        return 'ESC'
                    else:
                        char = key.decode('utf-8', errors='ignore').lower()
                        if char in self.click_zones:
                            return f"CLICK_{char.upper()}"
                        elif char.isdigit():
                            return char
        return 'ESC'

class MenuNavigator:
    """Class to handle menu navigation with arrow keys"""
    
    def __init__(self, items: List[str]):
        self.items = items
        self.selected_index = 0
        self.max_index = len(items) - 1
    
    def move_up(self):
        """Move selection up"""
        if self.selected_index > 0:
            self.selected_index -= 1
        else:
            self.selected_index = self.max_index  # Wrap to bottom
    
    def move_down(self):
        """Move selection down"""
        if self.selected_index < self.max_index:
            self.selected_index += 1
        else:
            self.selected_index = 0  # Wrap to top
    
    def get_selected_item(self):
        """Get currently selected item"""
        return self.items[self.selected_index]
    
    def get_selected_index(self):
        """Get currently selected index (1-based for menu options)"""
        return self.selected_index + 1 if self.selected_index < self.max_index else 0

class EnhancedMenuNavigator(MenuNavigator):
    """Enhanced menu navigator with mouse simulation support"""
    
    def __init__(self, items: List[str], enable_mouse: bool = True):
        super().__init__(items)
        self.mouse_sim = MouseSimulator() if enable_mouse else None
        self.enable_mouse = enable_mouse and MOUSE_SUPPORT
    
    def setup_click_zones(self):
        """Setup clickable zones for menu items"""
        if self.mouse_sim:
            self.mouse_sim.clear_zones()
            # Add zones for each menu item
            for i, item in enumerate(self.items):
                zone_id = chr(ord('a') + i)  # a, b, c, d...
                if i < 26:  # Limit to 26 items (a-z)
                    self.mouse_sim.add_click_zone(
                        zone_id, 
                        i + 3,  # Line number (approximate)
                        i + 3, 
                        f"Selecionar '{item}'"
                    )
            
            # Add zone for exit
            self.mouse_sim.add_click_zone('x', len(self.items) + 5, len(self.items) + 5, "Sair/Voltar")
    
    def handle_input_with_mouse(self):
        """Handle input with mouse simulation support"""
        if not self.enable_mouse or not self.mouse_sim:
            return KeyboardInput.get_key()
        
        self.setup_click_zones()
        action = self.mouse_sim.handle_click_input()
        
        if action.startswith('CLICK_'):
            # Convert click to selection
            zone_id = action.split('_')[1].lower()
            if zone_id == 'x':
                return 'EXIT_SELECTED'
            else:
                # Convert letter to number
                index = ord(zone_id) - ord('a')
                if 0 <= index < len(self.items):
                    self.selected_index = index
                    return 'ENTER'
        
        return action

@dataclass
class SystemStatus:
    pending_orders: int = 6
    open_orders: int = 4
    approved_budgets: int = 1
    current_user: str = "Administrator"
    system_version: str = "1.1a"

class ERPSystem:
    def __init__(self):
        self.status = SystemStatus()
        self.current_menu = "main"
        self.running = True
        self.data_file = "erp_data.json"
        self.users_file = "users_data.json"
        self.authenticated = False
        self.current_user = None
        self.users_db = {}
        self.load_data()
        self.load_users()
        
    def load_data(self):
        """Load system data from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.status.pending_orders = data.get('pending_orders', 6)
                    self.status.open_orders = data.get('open_orders', 4)
                    self.status.approved_budgets = data.get('approved_budgets', 1)
            except:
                pass
    
    def save_data(self):
        """Save system data to JSON file"""
        data = {
            'pending_orders': self.status.pending_orders,
            'open_orders': self.status.open_orders,
            'approved_budgets': self.status.approved_budgets
        }
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
        except:
            pass

    def load_users(self):
        """Load users database from JSON file"""
        # Criar usuário administrador padrão se não existir
        default_users = {
            "admin": {
                "password": "mudar@123",
                "role": "Administrador",
                "created_date": "2025-07-20",
                "last_login": None,
                "active": True
            }
        }
        
        if os.path.exists(self.users_file):
            try:
                with open(self.users_file, 'r', encoding='utf-8') as f:
                    self.users_db = json.load(f)
            except:
                self.users_db = default_users
        else:
            self.users_db = default_users
            self.save_users()
    
    def save_users(self):
        """Save users database to JSON file"""
        try:
            with open(self.users_file, 'w', encoding='utf-8') as f:
                json.dump(self.users_db, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Erro ao salvar usuários: {e}")

    def get_user_by_credentials(self, username, password):
        """Check if user credentials are valid"""
        if username in self.users_db:
            user = self.users_db[username]
            if user.get("active", True) and user.get("password") == password:
                return username, user
        return None, None

    def show_login_screen(self):
        """Display login screen with password input"""
        self.clear_screen()
        
        # ASCII art for the header
        print(f"{Colors.BLUE}")
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                                                              ║")
        print("║   ███████ ██████  ██████      ███████ ██ ███████ ████████    ║")
        print("║   ██      ██   ██ ██   ██     ██      ██ ██         ██       ║")
        print("║   █████   ██████  ██████      ███████ ██ ███████    ██       ║")
        print("║   ██      ██   ██ ██               ██ ██      ██    ██       ║")
        print("║   ███████ ██   ██ ██          ███████ ██ ███████    ██       ║")
        print("║                                                              ║")
        print("╠══════════════════════════════════════════════════════════════╣")
        print(f"║{Colors.CYAN}                    ORDEM DE SERVIÇO                         {Colors.BLUE}║")
        print(f"║{Colors.CYAN}                      VERSÃO 1.1a                           {Colors.BLUE}║")
        print(f"║{Colors.CYAN}              Programa Multi-usuário                        {Colors.BLUE}║")
        print(f"║{Colors.WHITE}                                                              {Colors.BLUE}║")
        print(f"║{Colors.WHITE}               (C) 1998-2000 BY THIAGO FRANCA               {Colors.BLUE}║")
        print("╚══════════════════════════════════════════════════════════════╝")
        print(f"{Colors.RESET}")
        
        # Date and time
        current_date = datetime.datetime.now().strftime("%d/%m/%Y")
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{Colors.WHITE}Data de hoje: {current_date}")
        print(f"Horário     : {current_time}{Colors.RESET}")
        print()
        
        # Login box
        print(f"{Colors.CYAN}╔═══════════════════════════╗{Colors.RESET}")
        print(f"{Colors.CYAN}║{Colors.WHITE} DIGITE SENHA DE ACESSO    {Colors.CYAN}║{Colors.RESET}")
        print(f"{Colors.CYAN}╚═══════════════════════════╝{Colors.RESET}")
        print()

    def authenticate(self):
        """Handle user authentication"""
        max_attempts = 3
        attempts = 0
        
        while attempts < max_attempts and not self.authenticated:
            self.show_login_screen()
            
            # Get username
            username = input(f"{Colors.WHITE}Usuário: {Colors.RESET}").strip()
            if not username:
                username = "admin"  # Default user
            
            # Get password input (hidden)
            try:
                password = getpass.getpass(f"{Colors.YELLOW}Senha: {Colors.RESET}")
            except KeyboardInterrupt:
                print(f"\n{Colors.RED}Acesso cancelado pelo usuário.{Colors.RESET}")
                return False
            
            # Check credentials
            user_id, user_data = self.get_user_by_credentials(username, password)
            
            if user_id:
                self.authenticated = True
                self.current_user = user_id
                self.status.current_user = user_data.get("role", "Usuário")
                
                # Update last login
                self.users_db[user_id]["last_login"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_users()
                
                print(f"\n{Colors.GREEN}✓ Acesso autorizado! Bem-vindo, {user_data.get('role', 'Usuário')}.{Colors.RESET}")
                print(f"{Colors.WHITE}Carregando sistema...{Colors.RESET}")
                time.sleep(1.5)
                return True
            else:
                attempts += 1
                remaining = max_attempts - attempts
                if remaining > 0:
                    print(f"\n{Colors.RED}✗ Credenciais incorretas! Tentativas restantes: {remaining}{Colors.RESET}")
                    print(f"{Colors.YELLOW}Pressione Enter para tentar novamente...{Colors.RESET}")
                    input()
                else:
                    print(f"\n{Colors.RED}✗ Acesso negado! Número máximo de tentativas excedido.{Colors.RESET}")
                    print(f"{Colors.YELLOW}Sistema será encerrado por segurança.{Colors.RESET}")
        
        return False

    def change_password(self):
        """Allow user to change the system password"""
        self.clear_screen()
        print(f"{Colors.CYAN}╔{self.draw_border(50, '═')}╗{Colors.RESET}")
        print(f"{Colors.CYAN}║{Colors.WHITE}{self.center_text('ALTERAÇÃO DE SENHA', 50)}{Colors.CYAN}║{Colors.RESET}")
        print(f"{Colors.CYAN}╚{self.draw_border(50, '═')}╝{Colors.RESET}")
        print()
        
        current_password = self.users_db[self.current_user]["password"]
        
        # Verify current password
        input_password = getpass.getpass(f"{Colors.WHITE}Senha atual: {Colors.RESET}")
        if input_password != current_password:
            print(f"{Colors.RED}✗ Senha atual incorreta!{Colors.RESET}")
            input(f"{Colors.YELLOW}Pressione Enter para continuar...{Colors.RESET}")
            return
        
        # Get new password
        new_password = getpass.getpass(f"{Colors.WHITE}Nova senha: {Colors.RESET}")
        if len(new_password) < 6:
            print(f"{Colors.RED}✗ A senha deve ter pelo menos 6 caracteres!{Colors.RESET}")
            input(f"{Colors.YELLOW}Pressione Enter para continuar...{Colors.RESET}")
            return
        
        # Confirm new password
        confirm_password = getpass.getpass(f"{Colors.WHITE}Confirme a nova senha: {Colors.RESET}")
        if new_password != confirm_password:
            print(f"{Colors.RED}✗ As senhas não coincidem!{Colors.RESET}")
            input(f"{Colors.YELLOW}Pressione Enter para continuar...{Colors.RESET}")
            return
        
        # Save new password
        self.users_db[self.current_user]["password"] = new_password
        self.save_users()
        
        print(f"\n{Colors.GREEN}✓ Senha alterada com sucesso!{Colors.RESET}")
        input(f"{Colors.YELLOW}Pressione Enter para continuar...{Colors.RESET}")

    def view_registered_users(self):
        """Display all registered users and their information"""
        self.clear_screen()
        print(f"{Colors.CYAN}╔{self.draw_border(70, '═')}╗{Colors.RESET}")
        print(f"{Colors.CYAN}║{Colors.WHITE}{self.center_text('USUÁRIOS CADASTRADOS', 70)}{Colors.CYAN}║{Colors.RESET}")
        print(f"{Colors.CYAN}╚{self.draw_border(70, '═')}╝{Colors.RESET}")
        print()
        
        if not self.users_db:
            print(f"{Colors.YELLOW}Nenhum usuário cadastrado no sistema.{Colors.RESET}")
        else:
            print(f"{Colors.WHITE}{'Usuário':<15} {'Função':<15} {'Status':<10} {'Último Acesso':<20}{Colors.RESET}")
            print(f"{Colors.BLUE}{'-'*70}{Colors.RESET}")
            
            for username, user_data in self.users_db.items():
                status = "Ativo" if user_data.get("active", True) else "Inativo"
                last_login = user_data.get("last_login", "Nunca")
                role = user_data.get("role", "Usuário")
                
                # Highlight current user
                if username == self.current_user:
                    print(f"{Colors.GREEN}{username:<15} {role:<15} {status:<10} {last_login:<20} (ATUAL){Colors.RESET}")
                else:
                    print(f"{Colors.WHITE}{username:<15} {role:<15} {status:<10} {last_login:<20}{Colors.RESET}")
        
        print()
        choice = input(f"{Colors.YELLOW}Deseja ver detalhes de um usuário específico? (s/N): {Colors.RESET}").lower()
        
        if choice in ['s', 'sim', 'y', 'yes']:
            username = input(f"{Colors.WHITE}Digite o nome do usuário: {Colors.RESET}").strip()
            if username in self.users_db:
                self.show_user_details(username)
            else:
                print(f"{Colors.RED}Usuário '{username}' não encontrado.{Colors.RESET}")
                input(f"{Colors.YELLOW}Pressione Enter para continuar...{Colors.RESET}")

    def show_user_details(self, username):
        """Show detailed information about a specific user"""
        self.clear_screen()
        print(f"{Colors.CYAN}╔{self.draw_border(60, '═')}╗{Colors.RESET}")
        print(f"{Colors.CYAN}║{Colors.WHITE}{self.center_text(f'DETALHES DO USUÁRIO: {username.upper()}', 60)}{Colors.CYAN}║{Colors.RESET}")
        print(f"{Colors.CYAN}╚{self.draw_border(60, '═')}╝{Colors.RESET}")
        print()
        
        user_data = self.users_db[username]
        
        print(f"{Colors.WHITE}Nome de usuário: {Colors.CYAN}{username}{Colors.RESET}")
        print(f"{Colors.WHITE}Função: {Colors.CYAN}{user_data.get('role', 'Usuário')}{Colors.RESET}")
        print(f"{Colors.WHITE}Data de criação: {Colors.CYAN}{user_data.get('created_date', 'Não informado')}{Colors.RESET}")
        print(f"{Colors.WHITE}Último acesso: {Colors.CYAN}{user_data.get('last_login', 'Nunca')}{Colors.RESET}")
        print(f"{Colors.WHITE}Status: {Colors.GREEN if user_data.get('active', True) else Colors.RED}{'Ativo' if user_data.get('active', True) else 'Inativo'}{Colors.RESET}")
        
        # Show password only for admin user viewing their own account
        if username == self.current_user and self.users_db[self.current_user].get("role") == "Administrador":
            show_password = input(f"\n{Colors.YELLOW}Mostrar senha? (s/N): {Colors.RESET}").lower()
            if show_password in ['s', 'sim', 'y', 'yes']:
                print(f"{Colors.WHITE}Senha atual: {Colors.RED}{user_data.get('password', 'N/A')}{Colors.RESET}")
                print(f"{Colors.YELLOW}⚠️  Mantenha esta informação segura!{Colors.RESET}")
        
        print()
        input(f"{Colors.YELLOW}Pressione Enter para continuar...{Colors.RESET}")

    def create_new_user(self):
        """Create a new user account"""
        self.clear_screen()
        print(f"{Colors.CYAN}╔{self.draw_border(50, '═')}╗{Colors.RESET}")
        print(f"{Colors.CYAN}║{Colors.WHITE}{self.center_text('CRIAR NOVO USUÁRIO', 50)}{Colors.CYAN}║{Colors.RESET}")
        print(f"{Colors.CYAN}╚{self.draw_border(50, '═')}╝{Colors.RESET}")
        print()
        
        # Get username
        while True:
            username = input(f"{Colors.WHITE}Nome do usuário: {Colors.RESET}").strip().lower()
            if not username:
                print(f"{Colors.RED}Nome de usuário não pode estar vazio!{Colors.RESET}")
                continue
            if username in self.users_db:
                print(f"{Colors.RED}Usuário '{username}' já existe!{Colors.RESET}")
                continue
            break
        
        # Get role
        print(f"\n{Colors.CYAN}Funções disponíveis:{Colors.RESET}")
        print(f"{Colors.WHITE}1. Administrador")
        print(f"2. Operador")
        print(f"3. Consulta{Colors.RESET}")
        
        role_choice = input(f"{Colors.YELLOW}Escolha a função (1-3): {Colors.RESET}")
        roles = {"1": "Administrador", "2": "Operador", "3": "Consulta"}
        role = roles.get(role_choice, "Operador")
        
        # Get password
        while True:
            password = getpass.getpass(f"{Colors.WHITE}Senha: {Colors.RESET}")
            if len(password) < 6:
                print(f"{Colors.RED}A senha deve ter pelo menos 6 caracteres!{Colors.RESET}")
                continue
            
            confirm_password = getpass.getpass(f"{Colors.WHITE}Confirme a senha: {Colors.RESET}")
            if password != confirm_password:
                print(f"{Colors.RED}As senhas não coincidem!{Colors.RESET}")
                continue
            break
        
        # Create user
        self.users_db[username] = {
            "password": password,
            "role": role,
            "created_date": datetime.datetime.now().strftime("%Y-%m-%d"),
            "last_login": None,
            "active": True
        }
        
        self.save_users()
        
        print(f"\n{Colors.GREEN}✓ Usuário '{username}' criado com sucesso!{Colors.RESET}")
        print(f"{Colors.WHITE}Função: {role}{Colors.RESET}")
        input(f"{Colors.YELLOW}Pressione Enter para continuar...{Colors.RESET}")

    def manage_users_menu(self):
        """User management submenu"""
        options = [
            "Ver Usuários Cadastrados",
            "Criar Novo Usuário",
            "Alterar Status de Usuário",
            "Resetar Senha de Usuário"
        ]
        
        choice = self.show_submenu_with_navigation("GERENCIAMENTO DE USUÁRIOS", options)
        
        if choice == "1":
            self.view_registered_users()
        elif choice == "2":
            self.create_new_user()
        elif choice == "3":
            self.toggle_user_status()
        elif choice == "4":
            self.reset_user_password()
        elif choice != "0":
            print(f"{Colors.RED}Opção inválida!{Colors.RESET}")
            input("Pressione Enter para continuar...")

    def toggle_user_status(self):
        """Toggle user active/inactive status"""
        self.clear_screen()
        print(f"{Colors.CYAN}╔{self.draw_border(50, '═')}╗{Colors.RESET}")
        print(f"{Colors.CYAN}║{Colors.WHITE}{self.center_text('ALTERAR STATUS', 50)}{Colors.CYAN}║{Colors.RESET}")
        print(f"{Colors.CYAN}╚{self.draw_border(50, '═')}╝{Colors.RESET}")
        print()
        
        username = input(f"{Colors.WHITE}Nome do usuário: {Colors.RESET}").strip().lower()
        
        if username not in self.users_db:
            print(f"{Colors.RED}Usuário '{username}' não encontrado!{Colors.RESET}")
        elif username == self.current_user:
            print(f"{Colors.RED}Você não pode alterar seu próprio status!{Colors.RESET}")
        else:
            current_status = self.users_db[username].get("active", True)
            new_status = not current_status
            self.users_db[username]["active"] = new_status
            self.save_users()
            
            status_text = "ativado" if new_status else "desativado"
            print(f"{Colors.GREEN}✓ Usuário '{username}' foi {status_text}!{Colors.RESET}")
        
        input(f"{Colors.YELLOW}Pressione Enter para continuar...{Colors.RESET}")

    def reset_user_password(self):
        """Reset password for a user"""
        self.clear_screen()
        print(f"{Colors.CYAN}╔{self.draw_border(50, '═')}╗{Colors.RESET}")
        print(f"{Colors.CYAN}║{Colors.WHITE}{self.center_text('RESETAR SENHA', 50)}{Colors.CYAN}║{Colors.RESET}")
        print(f"{Colors.CYAN}╚{self.draw_border(50, '═')}╝{Colors.RESET}")
        print()
        
        username = input(f"{Colors.WHITE}Nome do usuário: {Colors.RESET}").strip().lower()
        
        if username not in self.users_db:
            print(f"{Colors.RED}Usuário '{username}' não encontrado!{Colors.RESET}")
        else:
            new_password = getpass.getpass(f"{Colors.WHITE}Nova senha: {Colors.RESET}")
            if len(new_password) < 6:
                print(f"{Colors.RED}A senha deve ter pelo menos 6 caracteres!{Colors.RESET}")
            else:
                self.users_db[username]["password"] = new_password
                self.save_users()
                print(f"{Colors.GREEN}✓ Senha do usuário '{username}' foi resetada!{Colors.RESET}")
        
        input(f"{Colors.YELLOW}Pressione Enter para continuar...{Colors.RESET}")

    def show_system_info(self):
        """Display system information"""
        self.clear_screen()
        print(f"{Colors.CYAN}╔{self.draw_border(60, '═')}╗{Colors.RESET}")
        print(f"{Colors.CYAN}║{Colors.WHITE}{self.center_text('INFORMAÇÕES DO SISTEMA', 60)}{Colors.CYAN}║{Colors.RESET}")
        print(f"{Colors.CYAN}╚{self.draw_border(60, '═')}╝{Colors.RESET}")
        print()
        print(f"{Colors.WHITE}Sistema: ERP Empresarial")
        print(f"Versão: {self.status.system_version}")
        print(f"Usuário atual: {self.current_user}")
        print(f"Função: {self.status.current_user}")
        print(f"Data de acesso: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Total de usuários: {len(self.users_db)}")
        print()
        print(f"{Colors.YELLOW}Estatísticas:")
        print(f"{Colors.WHITE}• OS Pendentes: {self.status.pending_orders}")
        print(f"• OM em Aberto: {self.status.open_orders}")
        print(f"• Orçamentos Aprovados: {self.status.approved_budgets}{Colors.RESET}")
        print()
        input(f"{Colors.YELLOW}Pressione Enter para continuar...{Colors.RESET}")

    def admin_menu(self):
        """Display administrative menu"""
        options = [
            "Alterar Minha Senha",
            "Gerenciar Usuários",
            "Informações do Sistema",
            "Backup de Dados",
            "Configurações"
        ]
        
        choice = self.show_submenu_with_navigation("MENU ADMINISTRATIVO", options)
        
        if choice == "1":
            self.change_password()
        elif choice == "2":
            self.manage_users_menu()
        elif choice == "3":
            self.show_system_info()
        elif choice == "4":
            print(f"{Colors.GREEN}Backup de dados em desenvolvimento...{Colors.RESET}")
            input("Pressione Enter para continuar...")
        elif choice == "5":
            print(f"{Colors.GREEN}Configurações em desenvolvimento...{Colors.RESET}")
            input("Pressione Enter para continuar...")
        elif choice != "0":
            print(f"{Colors.RED}Opção inválida!{Colors.RESET}")
            input("Pressione Enter para continuar...")

    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw_border(self, width=80, char='═'):
        """Draw a horizontal border"""
        return char * width

    def center_text(self, text, width=80):
        """Center text within given width"""
        return text.center(width)

    def draw_header(self):
        """Draw the main header with menu options"""
        header = f"""
{Colors.BLUE}╔{self.draw_border(78, '═')}╗{Colors.RESET}
{Colors.BLUE}║{Colors.WHITE}{self.center_text('SISTEMA ERP EMPRESARIAL', 78)}{Colors.BLUE}║{Colors.RESET}
{Colors.BLUE}╠{self.draw_border(78, '═')}╣{Colors.RESET}
{Colors.BLUE}║ {Colors.CYAN}Cadastro    {Colors.WHITE}Principal    {Colors.CYAN}Consulta    {Colors.WHITE}Processos    {Colors.CYAN}Utilitários{Colors.BLUE}     ║{Colors.RESET}
{Colors.BLUE}╚{self.draw_border(78, '═')}╝{Colors.RESET}
"""
        print(header)

    def draw_status_panel(self):
        """Draw the status panel showing pending items"""
        status_text = f"""
{Colors.RED}╔{self.draw_border(38, '═')}╗{Colors.RESET}
{Colors.RED}║{Colors.YELLOW}{self.center_text('Atenção! Existem pendências', 38)}{Colors.RED}║{Colors.RESET}
{Colors.RED}║{Colors.WHITE}                                      {Colors.RED}║{Colors.RESET}
{Colors.RED}║{Colors.WHITE} Existem {self.status.pending_orders} OS em aberto                {Colors.RED}║{Colors.RESET}
{Colors.RED}║{Colors.WHITE} Existem {self.status.open_orders} OM em aberto                {Colors.RED}║{Colors.RESET}
{Colors.RED}║{Colors.WHITE}                                      {Colors.RED}║{Colors.RESET}
{Colors.RED}║{Colors.WHITE} Existem {self.status.approved_budgets} orçamentos aprovados          {Colors.RED}║{Colors.RESET}
{Colors.RED}╚{self.draw_border(38, '═')}╝{Colors.RESET}
"""
        return status_text

    def draw_menu_panel(self, selected_index=None):
        """Draw the right-side menu panel with optional highlighting"""
        menu_items = [
            "Funcionários",
            "Equipamentos", 
            "Ordem de Serv.",
            "O.S.concluídas",
            "O.S.em aberto",
            "Orc.aprovados",
            "Orc.excluídos",
            "Orc.em aberto",
            "Consultas",
            "Reg.Material",
            "Reg.pendentes",
            "Movimento",
            "Administração"
        ]
        
        menu_text = f"{Colors.BLUE}╔{self.draw_border(38, '═')}╗{Colors.RESET}\n"
        menu_text += f"{Colors.BLUE}║{Colors.CYAN}{self.center_text('MENU PRINCIPAL', 38)}{Colors.BLUE}║{Colors.RESET}\n"
        menu_text += f"{Colors.BLUE}╠{self.draw_border(38, '═')}╣{Colors.RESET}\n"
        
        for i, item in enumerate(menu_items, 1):
            if selected_index is not None and i == selected_index:
                # Highlight selected item
                menu_text += f"{Colors.BLUE}║{Colors.BLACK}\033[47m {i:2d}. {item:<30} {Colors.RESET}{Colors.BLUE}║{Colors.RESET}\n"
            else:
                menu_text += f"{Colors.BLUE}║ {Colors.WHITE}{i:2d}. {item:<30} {Colors.BLUE}║{Colors.RESET}\n"
        
        menu_text += f"{Colors.BLUE}║{Colors.WHITE}                                      {Colors.BLUE}║{Colors.RESET}\n"
        
        # Highlight exit option if selected
        if selected_index is not None and selected_index == 0:
            menu_text += f"{Colors.BLUE}║{Colors.BLACK}\033[47m 0.  Sair do Sistema               {Colors.RESET}{Colors.BLUE}║{Colors.RESET}\n"
        else:
            menu_text += f"{Colors.BLUE}║ {Colors.YELLOW}0.  Sair do Sistema               {Colors.BLUE}║{Colors.RESET}\n"
        
        menu_text += f"{Colors.BLUE}╚{self.draw_border(38, '═')}╝{Colors.RESET}"
        
        return menu_text

    def draw_footer(self):
        """Draw the bottom status bar"""
        current_date = datetime.datetime.now().strftime("%d/%m/%Y")
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        
        footer = f"""
{Colors.BLUE}╔{self.draw_border(78, '═')}╗{Colors.RESET}
{Colors.BLUE}║ {Colors.WHITE}{current_date}        SISTEMA ERP VERSÃO {self.status.system_version}                    {current_time} {Colors.BLUE}║{Colors.RESET}
{Colors.BLUE}╚{self.draw_border(78, '═')}╝{Colors.RESET}
"""
        return footer

    def display_main_screen(self, selected_index=None):
        """Display the main ERP screen with optional menu highlighting"""
        self.clear_screen()
        self.draw_header()
        
        # Display side by side: status panel and menu panel
        status_lines = self.draw_status_panel().strip().split('\n')
        menu_lines = self.draw_menu_panel(selected_index).strip().split('\n')
        
        # Ensure both panels have the same number of lines
        max_lines = max(len(status_lines), len(menu_lines))
        while len(status_lines) < max_lines:
            status_lines.append(' ' * 40)
        while len(menu_lines) < max_lines:
            menu_lines.append(' ' * 40)
        
        print()
        for status_line, menu_line in zip(status_lines, menu_lines):
            print(f"{status_line}  {menu_line}")
        
        print(self.draw_footer())
        
        # Show navigation instructions
        if selected_index is not None:
            print(f"\n{Colors.CYAN}💡 Use ↑↓ para navegar, ENTER para selecionar, ESC para digitar número{Colors.RESET}")
        else:
            print(f"\n{Colors.CYAN}💡 Digite o número da opção ou use ↑↓ + ENTER para navegar{Colors.RESET}")

    def get_menu_choice(self):
        """Get menu choice with arrow key navigation and mouse simulation support"""
        menu_items = [
            "Funcionários", "Equipamentos", "Ordem de Serv.", "O.S.concluídas",
            "O.S.em aberto", "Orc.aprovados", "Orc.excluídos", "Orc.em aberto",
            "Consultas", "Reg.Material", "Reg.pendentes", "Movimento", "Administração"
        ]
        
        # Add exit option
        all_items = menu_items + ["Sair do Sistema"]
        navigator = EnhancedMenuNavigator(all_items, enable_mouse=MOUSE_SUPPORT)
        
        # Start with enhanced navigation mode
        navigation_mode = True
        
        while True:
            if navigation_mode:
                self.display_main_screen(navigator.get_selected_index())
                
                if navigator.enable_mouse:
                    print(f"\n{Colors.CYAN}🖱️  Navegação Avançada Ativada!{Colors.RESET}")
                    print(f"{Colors.WHITE}• Use ↑↓ para navegar")
                    print(f"• Pressione ENTER para selecionar")
                    print(f"• Tecle A-M para acesso rápido às opções")
                    print(f"• Tecle X para sair")
                    print(f"• ESC para modo digitação{Colors.RESET}")
                
                # Get enhanced input
                try:
                    if navigator.enable_mouse:
                        action = navigator.handle_input_with_mouse()
                    else:
                        # Fallback to regular keyboard navigation
                        if os.name == 'nt':
                            while True:
                                if msvcrt.kbhit():
                                    key = msvcrt.getch()
                                    if key == b'\xe0':
                                        key = msvcrt.getch()
                                        if key == b'H':
                                            action = 'UP'
                                            break
                                        elif key == b'P':
                                            action = 'DOWN'
                                            break
                                    elif key == b'\r':
                                        action = 'ENTER'
                                        break
                                    elif key == b'\x1b':
                                        action = 'ESC'
                                        break
                                    elif key.isdigit():
                                        navigation_mode = False
                                        self.display_main_screen()
                                        return key.decode('utf-8')
                        else:
                            action = KeyboardInput.get_key()
                    
                    if action == 'UP':
                        navigator.move_up()
                    elif action == 'DOWN':
                        navigator.move_down()
                    elif action == 'ENTER':
                        return str(navigator.get_selected_index())
                    elif action == 'EXIT_SELECTED':
                        return "0"
                    elif action == 'ESC':
                        navigation_mode = False
                    elif action.isdigit():
                        navigation_mode = False
                        self.display_main_screen()
                        return action
                        
                except KeyboardInterrupt:
                    return "0"
            else:
                # Traditional number input mode
                self.display_main_screen()
                try:
                    choice = input(f"\n{Colors.YELLOW}Digite o número da opção desejada: {Colors.RESET}")
                    return choice
                except KeyboardInterrupt:
                    return "0"

    def show_submenu_with_navigation(self, title: str, options: List[str]) -> str:
        """Display a submenu with arrow key navigation and mouse simulation"""
        navigator = EnhancedMenuNavigator(options + ["Voltar ao Menu Principal"], enable_mouse=MOUSE_SUPPORT)
        navigation_mode = True
        
        while True:
            self.clear_screen()
            width = max(60, len(title) + 10)
            
            print(f"{Colors.CYAN}╔{self.draw_border(width, '═')}╗{Colors.RESET}")
            print(f"{Colors.CYAN}║{Colors.WHITE}{self.center_text(title, width)}{Colors.CYAN}║{Colors.RESET}")
            print(f"{Colors.CYAN}╚{self.draw_border(width, '═')}╝{Colors.RESET}")
            print()
            
            # Display options with highlighting
            for i, option in enumerate(options, 1):
                letter = chr(ord('a') + i - 1) if i <= 26 else str(i)
                if navigation_mode and i == navigator.get_selected_index():
                    print(f"{Colors.BLACK}\033[47m{i}. {option} ({letter.upper()}){Colors.RESET}")
                else:
                    print(f"{Colors.WHITE}{i}. {option} {Colors.CYAN}({letter.upper()}){Colors.RESET}")
            
            # Show exit option
            if navigation_mode and navigator.get_selected_index() == 0:
                print(f"{Colors.BLACK}\033[47m0. Voltar ao Menu Principal (X){Colors.RESET}")
            else:
                print(f"{Colors.WHITE}0. Voltar ao Menu Principal {Colors.CYAN}(X){Colors.RESET}")
            
            if navigation_mode:
                if navigator.enable_mouse:
                    print(f"\n{Colors.CYAN}�️  Navegação: ↑↓ setas, ENTER, ou tecle a letra da opção{Colors.RESET}")
                else:
                    print(f"\n{Colors.CYAN}�💡 Use ↑↓ para navegar, ENTER para selecionar, ESC para digitar{Colors.RESET}")
                
                try:
                    if navigator.enable_mouse:
                        action = navigator.handle_input_with_mouse()
                    else:
                        # Fallback to regular navigation
                        if os.name == 'nt':
                            while True:
                                if msvcrt.kbhit():
                                    key = msvcrt.getch()
                                    if key == b'\xe0':
                                        key = msvcrt.getch()
                                        if key == b'H':
                                            action = 'UP'
                                            break
                                        elif key == b'P':
                                            action = 'DOWN'
                                            break
                                    elif key == b'\r':
                                        action = 'ENTER'
                                        break
                                    elif key == b'\x1b':
                                        action = 'ESC'
                                        break
                                    elif key.isdigit():
                                        return key.decode('utf-8')
                        else:
                            action = 'ESC'  # Simplified for non-Windows
                    
                    if action == 'UP':
                        navigator.move_up()
                    elif action == 'DOWN':
                        navigator.move_down()
                    elif action == 'ENTER':
                        return str(navigator.get_selected_index())
                    elif action == 'EXIT_SELECTED':
                        return "0"
                    elif action == 'ESC':
                        navigation_mode = False
                    elif action.isdigit():
                        return action
                        
                except KeyboardInterrupt:
                    return "0"
            else:
                choice = input(f"\n{Colors.YELLOW}Escolha uma opção: {Colors.RESET}")
                return choice

    def handle_funcionarios(self):
        """Handle employee management"""
        options = [
            "Cadastrar Funcionário",
            "Consultar Funcionário", 
            "Alterar Dados",
            "Relatórios"
        ]
        
        choice = self.show_submenu_with_navigation("GESTÃO DE FUNCIONÁRIOS", options)
        
        if choice == "1":
            self.cadastrar_funcionario()
        elif choice == "2":
            self.consultar_funcionario()
        elif choice == "3":
            print(f"{Colors.GREEN}Função de alteração em desenvolvimento...{Colors.RESET}")
            input("Pressione Enter para continuar...")
        elif choice == "4":
            print(f"{Colors.GREEN}Relatórios em desenvolvimento...{Colors.RESET}")
            input("Pressione Enter para continuar...")

    def cadastrar_funcionario(self):
        """Register new employee"""
        self.clear_screen()
        print(f"{Colors.CYAN}╔{self.draw_border(50, '═')}╗{Colors.RESET}")
        print(f"{Colors.CYAN}║{Colors.WHITE}{self.center_text('CADASTRO DE FUNCIONÁRIO', 50)}{Colors.CYAN}║{Colors.RESET}")
        print(f"{Colors.CYAN}╚{self.draw_border(50, '═')}╝{Colors.RESET}")
        print()
        
        nome = input(f"{Colors.WHITE}Nome: {Colors.RESET}")
        cargo = input(f"{Colors.WHITE}Cargo: {Colors.RESET}")
        departamento = input(f"{Colors.WHITE}Departamento: {Colors.RESET}")
        salario = input(f"{Colors.WHITE}Salário: {Colors.RESET}")
        
        print(f"\n{Colors.GREEN}Funcionário cadastrado com sucesso!{Colors.RESET}")
        print(f"{Colors.WHITE}Nome: {nome}")
        print(f"Cargo: {cargo}")
        print(f"Departamento: {departamento}")
        print(f"Salário: {salario}{Colors.RESET}")
        
        input(f"\n{Colors.YELLOW}Pressione Enter para continuar...{Colors.RESET}")

    def consultar_funcionario(self):
        """Query employee information"""
        self.clear_screen()
        print(f"{Colors.CYAN}╔{self.draw_border(50, '═')}╗{Colors.RESET}")
        print(f"{Colors.CYAN}║{Colors.WHITE}{self.center_text('CONSULTA DE FUNCIONÁRIO', 50)}{Colors.CYAN}║{Colors.RESET}")
        print(f"{Colors.CYAN}╚{self.draw_border(50, '═')}╝{Colors.RESET}")
        print()
        
        criterio = input(f"{Colors.WHITE}Digite o nome ou código do funcionário: {Colors.RESET}")
        
        print(f"\n{Colors.GREEN}Resultado da consulta para: {criterio}{Colors.RESET}")
        print(f"{Colors.WHITE}Nome: João Silva")
        print(f"Código: 001")
        print(f"Cargo: Analista de Sistemas")
        print(f"Departamento: TI")
        print(f"Status: Ativo{Colors.RESET}")
        
        input(f"\n{Colors.YELLOW}Pressione Enter para continuar...{Colors.RESET}")

    def handle_equipamentos(self):
        """Handle equipment management"""
        options = [
            "Cadastrar Equipamento",
            "Consultar Equipamento",
            "Manutenção Preventiva",
            "Manutenção Corretiva"
        ]
        
        choice = self.show_submenu_with_navigation("GESTÃO DE EQUIPAMENTOS", options)
        
        if choice == "1":
            print(f"{Colors.GREEN}Cadastro de equipamento em desenvolvimento...{Colors.RESET}")
        elif choice == "2":
            print(f"{Colors.GREEN}Consulta de equipamento em desenvolvimento...{Colors.RESET}")
        else:
            print(f"{Colors.GREEN}Opção em desenvolvimento...{Colors.RESET}")
        
        if choice != "0":
            input("Pressione Enter para continuar...")

    def handle_ordem_servico(self):
        """Handle service orders"""
        options = [
            "Nova Ordem de Serviço",
            "Consultar OS",
            "Atualizar Status", 
            "Relatório de OS"
        ]
        
        choice = self.show_submenu_with_navigation("ORDENS DE SERVIÇO", options)
        
        if choice == "1":
            self.criar_ordem_servico()
        else:
            print(f"{Colors.GREEN}Opção em desenvolvimento...{Colors.RESET}")
            if choice != "0":
                input("Pressione Enter para continuar...")

    def criar_ordem_servico(self):
        """Create new service order"""
        self.clear_screen()
        print(f"{Colors.CYAN}╔{self.draw_border(50, '═')}╗{Colors.RESET}")
        print(f"{Colors.CYAN}║{Colors.WHITE}{self.center_text('NOVA ORDEM DE SERVIÇO', 50)}{Colors.CYAN}║{Colors.RESET}")
        print(f"{Colors.CYAN}╚{self.draw_border(50, '═')}╝{Colors.RESET}")
        print()
        
        cliente = input(f"{Colors.WHITE}Cliente: {Colors.RESET}")
        equipamento = input(f"{Colors.WHITE}Equipamento: {Colors.RESET}")
        problema = input(f"{Colors.WHITE}Problema relatado: {Colors.RESET}")
        tecnico = input(f"{Colors.WHITE}Técnico responsável: {Colors.RESET}")
        
        # Increment pending orders
        self.status.pending_orders += 1
        self.save_data()
        
        print(f"\n{Colors.GREEN}Ordem de Serviço criada com sucesso!{Colors.RESET}")
        print(f"{Colors.WHITE}Número da OS: {self.status.pending_orders + 1000}")
        print(f"Cliente: {cliente}")
        print(f"Equipamento: {equipamento}")
        print(f"Problema: {problema}")
        print(f"Técnico: {tecnico}{Colors.RESET}")
        
        input(f"\n{Colors.YELLOW}Pressione Enter para continuar...{Colors.RESET}")

    def run_menu_option(self, choice):
        """Execute the selected menu option"""
        if choice == "1":
            self.handle_funcionarios()
        elif choice == "2":
            self.handle_equipamentos()
        elif choice == "3":
            self.handle_ordem_servico()
        elif choice == "4":
            print(f"{Colors.GREEN}O.S. Concluídas - Em desenvolvimento...{Colors.RESET}")
            input("Pressione Enter para continuar...")
        elif choice == "5":
            print(f"{Colors.GREEN}O.S. em Aberto - Em desenvolvimento...{Colors.RESET}")
            input("Pressione Enter para continuar...")
        elif choice == "6":
            print(f"{Colors.GREEN}Orçamentos Aprovados - Em desenvolvimento...{Colors.RESET}")
            input("Pressione Enter para continuar...")
        elif choice == "7":
            print(f"{Colors.GREEN}Orçamentos Excluídos - Em desenvolvimento...{Colors.RESET}")
            input("Pressione Enter para continuar...")
        elif choice == "8":
            print(f"{Colors.GREEN}Orçamentos em Aberto - Em desenvolvimento...{Colors.RESET}")
            input("Pressione Enter para continuar...")
        elif choice == "9":
            print(f"{Colors.GREEN}Consultas - Em desenvolvimento...{Colors.RESET}")
            input("Pressione Enter para continuar...")
        elif choice == "10":
            print(f"{Colors.GREEN}Registro de Material - Em desenvolvimento...{Colors.RESET}")
            input("Pressione Enter para continuar...")
        elif choice == "11":
            print(f"{Colors.GREEN}Registros Pendentes - Em desenvolvimento...{Colors.RESET}")
            input("Pressione Enter para continuar...")
        elif choice == "12":
            print(f"{Colors.GREEN}Movimento - Em desenvolvimento...{Colors.RESET}")
            input("Pressione Enter para continuar...")
        elif choice == "13":
            self.admin_menu()
        elif choice == "0":
            self.running = False
            print(f"{Colors.YELLOW}Encerrando o sistema...{Colors.RESET}")
        else:
            print(f"{Colors.RED}Opção inválida! Tente novamente.{Colors.RESET}")
            input("Pressione Enter para continuar...")

    def run(self):
        """Main application loop"""
        # Authenticate user first
        if not self.authenticate():
            return
            
        while self.running:
            choice = self.get_menu_choice()
            self.run_menu_option(choice)

def main():
    """Main function"""
    # Enable color support on Windows
    if os.name == 'nt':
        os.system('color')
    
    erp = ERPSystem()
    
    try:
        erp.run()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Sistema encerrado pelo usuário.{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}Erro no sistema: {e}{Colors.RESET}")
    finally:
        erp.save_data()

if __name__ == "__main__":
    main()
