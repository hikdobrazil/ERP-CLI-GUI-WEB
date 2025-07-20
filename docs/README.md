# 🏢 Sistema ERP - Evolução Completa

Um **Sistema ERP** completo desenvolvido em **3 versões progressivas**: CLI, GUI e Web. Este repositório mostra a evolução de uma aplicação desde terminal até uma moderna interface web.

## 🌐 **[🔗 Demonstração Online](https://seuusuario.github.io/sistema-erp-completo)**

**Credenciais de Acesso:**
- **Usuário**: admin  
- **Senha**: mudar@123

---

## 🎯 **Versões Disponíveis**

### 1. � **Versão CLI** (Terminal)
- **Arquivo**: `main.py`
- **Tecnologia**: Python puro
- **Interface**: Terminal com navegação por setas
- **Dados**: JSON local
- **Recursos**: ANSI colors, autenticação, CRUD completo

### 2. 🖥️ **Versão GUI** (Desktop)
- **Arquivo**: `gui_main.py`  
- **Tecnologia**: Python + tkinter
- **Interface**: Janelas nativas do sistema
- **Dados**: SQLite database
- **Recursos**: Formulários, tabelas, dialogs

### 3. 🌐 **Versão Web** (Online) ⭐
- **Pasta**: `/web/`
- **Tecnologia**: HTML5 + CSS3 + JavaScript
- **Interface**: Responsiva e moderna
- **Dados**: LocalStorage
- **Recursos**: PWA-ready, mobile-first, GitHub Pages

## Características Gerais

- Interface organizada e intuitiva
- Menu hierárquico completo
- Gestão de funcionários, equipamentos e ordens de serviço
- Painel de status com informações em tempo real
- Sistema de persistência de dados
- Design responsivo e moderno

## Funcionalidades Principais

### � Sistema de Segurança
- Autenticação obrigatória com senha
- Controle de tentativas de acesso (máx. 3)
- Menu administrativo para gerenciar senhas
- Tela de login profissional

### �📊 Dashboard Principal
- Visualização de pendências em tempo real
- Menu lateral com todas as opções
- Barra de status com data, hora e versão

### 👥 Gestão de Funcionários
- Cadastro de novos funcionários
- Consulta por nome ou código
- Alteração de dados
- Relatórios (em desenvolvimento)

### 🔧 Gestão de Equipamentos
- Cadastro de equipamentos
- Controle de manutenção preventiva e corretiva
- Histórico de manutenções

### 📋 Ordens de Serviço
- Criação de novas OS
- Acompanhamento de status
- Relatórios detalhados
- Controle de técnicos responsáveis

### 🛠️ Administração do Sistema
- Alteração de senhas
- Informações do sistema
- Backup de dados (em desenvolvimento)
- Configurações avançadas (em desenvolvimento)

## Como Executar

### ⚠️ **PRIMEIRO ACESSO - IMPORTANTE!**
- **Senha inicial**: `mudar@123`
- **Recomendação**: Altere a senha no primeiro acesso via menu Administração

### � **Launcher Unificado (Recomendado)**

#### Método 1: Arquivo Batch (Windows)
```cmd
start_erp.bat
```

#### Método 2: PowerShell
```powershell
.\start_erp.ps1
```

### �📱 **Versão CLI (Terminal)**

#### Método 1: Arquivo Batch (Windows)
```cmd
run_erp.bat
```

#### Método 2: PowerShell
```powershell
.\run_erp.ps1
```

#### Método 3: Python Direto
```cmd
python main.py
```

### 🖥️ **Versão GUI (Interface Gráfica)**

#### Método 1: Arquivo Batch (Windows)
```cmd
run_gui.bat
```

#### Método 2: PowerShell
```powershell
.\run_gui.ps1
```

#### Método 3: Python Direto
```cmd
python gui_main.py
```

## Requisitos

- Python 3.6+
- Windows (testado no Windows 10/11)
- Terminal com suporte a cores ANSI

## Estrutura de Arquivos

```
CLI ERP/
├── main.py           # Sistema ERP - Versão CLI
├── gui_main.py       # Sistema ERP - Versão GUI
├── start_erp.bat     # 🚀 Launcher Unificado (Batch) - RECOMENDADO
├── start_erp.ps1     # 🚀 Launcher Unificado (PowerShell) - RECOMENDADO
├── run_erp.bat       # Launcher CLI (Batch)
├── run_erp.ps1       # Launcher CLI (PowerShell)
├── run_gui.bat       # Launcher GUI (Batch)
├── run_gui.ps1       # Launcher GUI (PowerShell)
├── launcher.bat      # Launcher avançado com opções (CLI)
├── config.json       # Configurações do sistema CLI
├── erp_data.json     # Dados persistentes CLI (criado automaticamente)
├── erp_database.db   # Banco de dados GUI (SQLite)
├── demo_data.json    # Dados de demonstração
├── demo_generator.py # Gerador de dados de teste
├── users_data.json   # Banco de dados de usuários CLI
├── README.md         # Este arquivo (documentação geral)
├── GUI_README.md     # Documentação específica da versão GUI
├── SECURITY.md       # Documentação de segurança
├── NAVIGATION.md     # Guia de navegação com setas (CLI)
├── MOUSE_GUIDE.md    # Guia completo do suporte ao mouse (CLI)
└── PASSWORD_GUIDE.md # Como ver senhas cadastradas (CLI)
```

## Navegação

### �️ **Simulação de Mouse (NOVO!)**
- **A-M**: Acesso direto às opções do menu (A=Funcionários, M=Administração)
- **X**: Sair/Voltar
- **Clique simulado**: Tecle a letra da opção desejada

### �🔄 **Navegação com Setas**
- **↑↓**: Navegar entre opções do menu
- **ENTER**: Selecionar opção destacada
- **ESC**: Alternar para modo digitação
- **0-9**: Digitação direta de números

### 📝 **Navegação Tradicional**
- Use os números do menu para navegar
- `0` sempre volta ao menu anterior ou sai do sistema
- `Ctrl+C` encerra o sistema a qualquer momento

## Cores e Símbolos

- 🔵 **Azul**: Bordas e estrutura
- 🟡 **Amarelo**: Avisos e prompts
- 🔴 **Vermelho**: Alertas e pendências
- ⚪ **Branco**: Texto principal
- 🟢 **Verde**: Confirmações e sucessos
- 🟦 **Ciano**: Títulos e destaques

## Desenvolvimento

O sistema está estruturado de forma modular, facilitando a adição de novas funcionalidades:

- Cada módulo principal tem sua própria função handler
- Dados são salvos automaticamente em JSON
- Interface responsiva e configurável
- Suporte a temas de cores

## Próximas Funcionalidades

- [ ] Sistema de usuários e permissões
- [ ] Relatórios em PDF
- [ ] Backup automático
- [ ] Interface web opcional
- [ ] Integração com banco de dados
- [ ] Sistema de logs
- [ ] Notificações automáticas

## Problemas Conhecidos

- Cores podem não funcionar em terminais muito antigos
- Requer Python instalado no sistema
- Layout otimizado para resolução mínima 80x24

## Suporte

Para dúvidas ou sugestões, verifique os logs do sistema ou contate o desenvolvedor.

---

**Versão**: 1.1a  
**Compatibilidade**: Windows 10/11  
**Linguagem**: Python 3.6+
