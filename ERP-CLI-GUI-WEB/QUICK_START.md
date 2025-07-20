# 🎯 GUIA RÁPIDO - Sistema ERP v2.0

## 🚀 **INÍCIO RÁPIDO**

### **Para começar agora:**
1. Execute: `start_erp.bat` ou `start_erp.ps1`
2. Escolha: **[1]** CLI ou **[2]** GUI  
3. Login: `admin` / `mudar@123`
4. Explore o sistema!

---

## 📱 **VERSÃO CLI** (Terminal)

### **🎮 Como Usar:**
- **Setas ↑↓**: Navegar no menu
- **ENTER**: Selecionar opção
- **A-M**: Acesso rápido (A=Funcionários, C=O.S., M=Admin)
- **X**: Sair/Voltar
- **ESC**: Alternar modos

### **📁 Arquivos:**
- `main.py` - Sistema principal
- `run_erp.bat` - Launcher direto

### **📖 Documentação:**
- `NAVIGATION.md` - Navegação completa
- `MOUSE_GUIDE.md` - Suporte a "mouse"
- `PASSWORD_GUIDE.md` - Gerenciar usuários

---

## 🖥️ **VERSÃO GUI** (Interface Gráfica)

### **🎮 Como Usar:**
- **Interface visual** com formulários
- **Clique** para navegar
- **Tabelas dinâmicas** para dados
- **Menu superior** com todas as opções

### **📁 Arquivos:**
- `gui_main.py` - Sistema principal
- `run_gui.bat` - Launcher direto
- `erp_database.db` - Banco SQLite

### **📖 Documentação:**
- `GUI_README.md` - Documentação completa

---

## 🔧 **FUNCIONALIDADES**

### **✅ Implementado:**
- ✅ **Login seguro** com criptografia
- ✅ **Gestão de funcionários** (completa no GUI)
- ✅ **Dashboard** com estatísticas
- ✅ **Multi-usuário** com diferentes roles
- ✅ **Navegação avançada** (CLI com mouse simulado)

### **🔄 Em Desenvolvimento:**
- 🔄 **Equipamentos** (formulários GUI)
- 🔄 **Ordens de Serviço** (CRUD completo)
- 🔄 **Relatórios** com gráficos
- 🔄 **Backup automático**

---

## 🛠️ **CONFIGURAÇÃO**

### **Requisitos:**
- **Python 3.6+**
- **Windows 10/11** (testado)
- **Terminal** com cores ANSI (CLI)

### **Primeiro Acesso:**
```
Usuário: admin
Senha: mudar@123
```

### **Alterar Senha:**
1. Menu **Administração**
2. **Alterar Minha Senha**
3. Digite nova senha

---

## 🚨 **TROUBLESHOOTING**

### **Problemas Comuns:**

#### **"Python não encontrado"**
```bash
# Verificar instalação:
python --version
```

#### **"Erro de codificação"**
```bash
# No terminal, usar:
chcp 65001
```

#### **"GUI não abre"**
- Verifique drivers gráficos
- Use versão CLI como alternativa

#### **"Login não funciona"**
- Use credenciais padrão: `admin`/`mudar@123`
- Verifique arquivo de usuários

---

## 📞 **SUPORTE RÁPIDO**

### **Comandos Úteis:**

#### **Resetar sistema CLI:**
```bash
# Apagar dados e recriar:
del erp_data.json users_data.json config.json
python main.py
```

#### **Resetar sistema GUI:**
```bash
# Apagar banco e recriar:
del erp_database.db
python gui_main.py
```

#### **Gerar dados demo:**
```bash
python demo_generator.py
```

---

## 🎪 **DIFERENÇAS ENTRE VERSÕES**

| Característica | CLI | GUI |
|---------------|-----|-----|
| **Interface** | Terminal colorido | Janelas gráficas |
| **Navegação** | Setas + mouse simulado | Click + formulários |
| **Banco** | JSON | SQLite |
| **Performance** | Rápida | Média |
| **Funcionalidades** | Completa | Em desenvolvimento |
| **Compatibilidade** | Universal | Requer GUI |

---

## 🎯 **PRÓXIMOS PASSOS**

### **Para Usuários:**
1. **Explore** ambas as versões
2. **Cadastre** funcionários de teste
3. **Configure** o sistema conforme necessário
4. **Reporte** bugs ou sugestões

### **Para Desenvolvedores:**
1. **Leia** toda a documentação
2. **Analise** o código fonte
3. **Contribua** com melhorias
4. **Teste** novas funcionalidades

---

**💡 Dica:** Use o **launcher unificado** (`start_erp.bat`) para escolher facilmente entre as versões e descobrir qual prefere!
