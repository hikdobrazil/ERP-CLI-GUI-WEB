# 👀 Como Ver Senhas Cadastradas - Sistema ERP

## 🔐 Acesso às Informações de Usuários

O Sistema ERP agora possui um sistema completo de gerenciamento de usuários que permite visualizar e gerenciar todas as contas cadastradas.

## 📋 **Passo a Passo para Ver Senhas**

### **1. Fazer Login como Administrador**
```
Usuário: admin
Senha: mudar@123
```

### **2. Acessar o Menu Administrativo**
```
Menu Principal → 13. Administração
```

### **3. Gerenciar Usuários**
```
Menu Administrativo → 2. Gerenciar Usuários
```

### **4. Ver Usuários Cadastrados**
```
Gerenciamento de Usuários → 1. Ver Usuários Cadastrados
```

### **5. Ver Detalhes de um Usuário**
- Responda **"s"** quando perguntado sobre ver detalhes
- Digite o nome do usuário
- Se for administrador visualizando sua própria conta, responda **"s"** para mostrar senha

## 🎯 **Funcionalidades Disponíveis**

### **📊 Lista de Usuários**
Mostra uma tabela com:
- **Nome do usuário**
- **Função** (Administrador/Operador/Consulta)
- **Status** (Ativo/Inativo)
- **Último acesso**
- **Destaque** para o usuário atual

### **🔍 Detalhes Específicos**
Para cada usuário você pode ver:
- Nome de usuário
- Função atribuída
- Data de criação da conta
- Último acesso ao sistema
- Status atual (ativo/inativo)
- **Senha** (apenas admin para própria conta)

### **🛠️ Ações de Gerenciamento**
- **Criar novos usuários**
- **Alterar status** (ativar/desativar)
- **Resetar senhas** de outros usuários
- **Ver informações detalhadas**

## 🔒 **Regras de Segurança**

### **Visualização de Senhas:**
- ✅ **Administrador** pode ver apenas sua própria senha
- ❌ **Nenhum usuário** pode ver senhas de outros
- ⚠️ **Aviso de segurança** é mostrado ao exibir senha

### **Níveis de Acesso:**
- **Administrador**: Pode gerenciar todos os usuários
- **Operador**: Pode apenas alterar sua própria senha
- **Consulta**: Acesso limitado a visualizações

## 📁 **Arquivos de Dados**

### **Local das Informações:**
- **Arquivo**: `users_data.json`
- **Localização**: Pasta do sistema ERP
- **Formato**: JSON estruturado
- **Backup**: Salvo automaticamente a cada alteração

### **Estrutura dos Dados:**
```json
{
  "admin": {
    "password": "mudar@123",
    "role": "Administrador",
    "created_date": "2025-07-20",
    "last_login": "2025-07-20 16:59:45",
    "active": true
  }
}
```

## 🔧 **Métodos Alternativos**

### **1. Via Arquivo JSON:**
```
1. Abra o arquivo users_data.json
2. Visualize as senhas em texto plano
3. ⚠️ NÃO RECOMENDADO por segurança
```

### **2. Criar Novo Usuário:**
```
Menu Administrativo → Gerenciar Usuários → Criar Novo Usuário
- Defina username, função e senha
- Sistema salva automaticamente
```

### **3. Resetar Senha:**
```
Menu Administrativo → Gerenciar Usuários → Resetar Senha
- Digite o nome do usuário
- Defina nova senha
- Alteração é aplicada imediatamente
```

## 🆘 **Solução de Problemas**

### **Esqueceu a Senha do Admin?**
1. Use o usuário padrão: `admin` / `mudar@123`
2. Se alterado, edite `users_data.json` manualmente
3. Restaure a senha padrão temporariamente

### **Usuário Não Aparece?**
1. Verifique se o usuário está ativo
2. Confirme se foi criado corretamente
3. Veja o arquivo `users_data.json`

### **Não Consegue Ver Senha?**
1. Confirme que é administrador
2. Verifique se está tentando ver sua própria senha
3. Outras senhas são protegidas por segurança

## 📝 **Exemplo Prático**

### **Cenário: Ver senha do usuário admin**
```
1. Login: admin / mudar@123
2. Menu: 13 → 2 → 1
3. Responder: s (para ver detalhes)
4. Digitar: admin
5. Responder: s (para mostrar senha)
6. Resultado: Senha atual: mudar@123
```

---

**💡 Dica**: Para maior segurança, altere a senha padrão do administrador após o primeiro acesso e crie usuários específicos para cada função no sistema!
