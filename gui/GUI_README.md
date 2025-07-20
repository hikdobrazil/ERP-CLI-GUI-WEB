# 🖥️ Sistema ERP - Versão GUI

Interface gráfica moderna e profissional para o Sistema ERP, desenvolvida com Python tkinter.

## 🎯 **Características da Versão GUI**

### 🖼️ **Interface Moderna**
- **Design profissional** similar a sistemas corporativos
- **Formulários intuitivos** com campos organizados
- **Tabelas dinâmicas** para visualização de dados
- **Barra de menu** completa com todas as funcionalidades
- **Toolbar** com ações rápidas
- **Barra de status** com informações do usuário

### 🗃️ **Banco de Dados SQLite**
- **Persistência robusta** com SQLite
- **Estrutura normalizada** com relacionamentos
- **Backup automático** dos dados
- **Performance otimizada** para consultas

### 🔐 **Sistema de Autenticação**
- **Login gráfico** elegante e seguro
- **Controle de sessão** por usuário
- **Diferentes níveis** de acesso
- **Criptografia** de senhas

## 🚀 **Como Executar**

### **Método 1: Arquivo Batch (Windows)**
```cmd
run_gui.bat
```

### **Método 2: PowerShell**
```powershell
.\run_gui.ps1
```

### **Método 3: Python Direto**
```bash
python gui_main.py
```

## 📋 **Funcionalidades Principais**

### 🏠 **Dashboard**
- **Visão geral** do sistema
- **Estatísticas em tempo real**
- **Ações rápidas** para funções principais
- **Cards informativos** com dados importantes

### 👥 **Gestão de Funcionários**
- ✅ **Cadastro completo** com validação
- ✅ **Consulta em tabela** dinâmica
- 🔄 **Edição de dados** (em desenvolvimento)
- 🔄 **Relatórios** (em desenvolvimento)

### 🔧 **Gestão de Equipamentos**
- 🔄 **Cadastro de equipamentos** (em desenvolvimento)
- 🔄 **Controle de manutenção** (em desenvolvimento)
- 🔄 **Histórico completo** (em desenvolvimento)

### 📋 **Ordens de Serviço**
- 🔄 **Criação de O.S.** (em desenvolvimento)
- 🔄 **Acompanhamento** (em desenvolvimento)
- 🔄 **Relatórios de produtividade** (em desenvolvimento)

## 🎨 **Interface Visual**

### **Tela de Login**
```
┌─────────────────────────────────┐
│         Sistema ERP             │
│   Enterprise Resource Planning │
│                                 │
│  ┌─── Autenticação ──────────┐  │
│  │ Usuário: [admin      ]   │  │
│  │ Senha:   [**********]   │  │
│  │        [  Entrar  ]      │  │
│  └─────────────────────────────┘  │
│                                 │
│    Senha inicial: mudar@123     │
└─────────────────────────────────┘
```

### **Janela Principal**
```
┌─ Sistema ERP - admin (Admin) ────────────────────────────────┐
│ Arquivo  Funcionários  Equipamentos  O.S.  Administração  │
├──────────────────────────────────────────────────────────────┤
│ [📊 Dashboard] [👥 Funcionários] [🔧 Equipamentos] [📋 O.S.] │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  Dashboard - Sistema ERP                                     │
│                                                              │
│  ┌─👥 Funcionários─┐ ┌─🔧 Equipamentos─┐ ┌─📋 O.S. Abertas─┐│
│  │       15        │ │        8         │ │        3        ││
│  └─────────────────┘ └──────────────────┘ └─────────────────┘│
│                                                              │
│  ┌─── Ações Rápidas ──────────────────────────────────────┐ │
│  │ [Cadastrar Funcionário] [Nova O.S.] [Consultar Equip.] │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│ Usuário: admin | 20/07/2025 14:30                           │
└──────────────────────────────────────────────────────────────┘
```

## 🔧 **Requisitos Técnicos**

### **Dependências**
- **Python 3.6+**
- **tkinter** (incluído no Python)
- **sqlite3** (incluído no Python)

### **Compatibilidade**
- ✅ **Windows 10/11**
- ✅ **Linux** (com GUI)
- ✅ **macOS**

## 📊 **Estrutura do Banco de Dados**

### **Tabelas Principais**
```sql
-- Usuários do sistema
users (id, username, password_hash, role, created_date, last_login, active)

-- Funcionários
employees (id, name, position, department, hire_date, salary, active)

-- Equipamentos  
equipment (id, name, type, brand, model, serial_number, purchase_date, status)

-- Ordens de Serviço
service_orders (id, employee_id, equipment_id, description, priority, status, created_date, due_date)
```

## 🎮 **Como Usar**

### **1. Primeiro Acesso**
1. Execute `run_gui.bat`
2. Use **usuário**: `admin`
3. Use **senha**: `mudar@123`
4. Sistema abrirá na tela principal

### **2. Cadastrar Funcionário**
1. Clique em **"👥 Funcionários"** no menu ou toolbar
2. Clique em **"+ Novo Funcionário"**
3. Preencha o formulário
4. Clique em **"Salvar"**

### **3. Navegar pelo Sistema**
- Use o **menu superior** para acesso completo
- Use a **toolbar** para ações rápidas
- **Dashboard** mostra visão geral
- **Double-click** em tabelas para detalhes

## 🔒 **Segurança**

### **Autenticação**
- **Senhas criptografadas** com SHA-256
- **Controle de sessão** ativo
- **Logout automático** por inatividade
- **Níveis de permissão** por role

### **Dados**
- **Banco SQLite** com transações
- **Backup automático** diário
- **Integridade referencial** garantida
- **Validação** de entrada de dados

## 🚧 **Desenvolvimento Futuro**

### **Funcionalidades Planejadas**
- 🔄 **CRUD completo** para todas as entidades
- 🔄 **Relatórios avançados** com gráficos
- 🔄 **Importação/Exportação** Excel/CSV
- 🔄 **Notificações** do sistema
- 🔄 **Multi-idioma** (PT/EN/ES)
- 🔄 **Temas** customizáveis
- 🔄 **Integração** com APIs externas

### **Melhorias de Interface**
- 🔄 **Ícones** modernos
- 🔄 **Drag & Drop** para uploads
- 🔄 **Auto-complete** em campos
- 🔄 **Filtros avançados** em tabelas
- 🔄 **Paginação** para grandes datasets

## 📞 **Suporte**

### **Arquivos de Log**
- `erp_database.db` - Banco de dados principal
- `erp_gui.log` - Logs do sistema (futuro)

### **Troubleshooting**
- **Erro de banco**: Arquivo será recriado automaticamente
- **Tela branca**: Verifique resolução e drivers gráficos
- **Login falha**: Use credenciais padrão `admin`/`mudar@123`

---

**🎯 A versão GUI oferece uma experiência moderna e profissional, mantendo toda a robustez do sistema CLI original!**
