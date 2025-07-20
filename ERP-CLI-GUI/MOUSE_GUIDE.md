# 🖱️ Suporte ao Mouse - Sistema ERP

O Sistema ERP agora possui suporte avançado ao "mouse" através de simulação inteligente via teclado, permitindo uma navegação ainda mais intuitiva e moderna.

## 🎯 **Como Funciona o "Mouse" no Terminal**

### 🔧 **Simulação de Mouse**
Como terminais tradicionais não suportam mouse diretamente, criamos um sistema inovador que simula cliques através de teclas específicas:

- **Cada opção** recebe uma **letra identificadora**
- **Teclar a letra** = "clicar" na opção
- **Navegação visual** mostra as letras disponíveis
- **Compatível** com todos os terminais

## ⌨️ **Controles de Navegação Avançada**

### **🖱️ Simulação de Mouse:**
- **A-M**: Acesso rápido às opções 1-13 do menu principal
- **X**: Sair/Voltar (equivale a clicar em "Sair")
- **Letras**: Cada submenu mostra suas próprias letras

### **🔄 Navegação Tradicional:**
- **↑↓**: Setas para navegar
- **ENTER**: Selecionar opção
- **ESC**: Alternar modo digitação
- **0-9**: Digitação direta de números

## 📋 **Mapeamento das "Áreas Clicáveis"**

### **Menu Principal:**
```
A = 1. Funcionários          H = 8. Orc.em aberto
B = 2. Equipamentos          I = 9. Consultas  
C = 3. Ordem de Serv.        J = 10. Reg.Material
D = 4. O.S.concluídas        K = 11. Reg.pendentes
E = 5. O.S.em aberto         L = 12. Movimento
F = 6. Orc.aprovados         M = 13. Administração
G = 7. Orc.excluídos         X = 0. Sair do Sistema
```

### **Submenus:**
Cada submenu gera automaticamente suas próprias letras:
```
A = Primeira opção
B = Segunda opção  
C = Terceira opção
...
X = Voltar/Sair
```

## 🎪 **Recursos Especiais**

### **🔍 Indicadores Visuais:**
- **Destaque com fundo branco** para item selecionado
- **Letras entre parênteses** mostram tecla de acesso rápido
- **Lista de áreas clicáveis** exibida automaticamente
- **Instruções contextuais** sempre visíveis

### **🔄 Modos de Operação:**

#### **1. Modo Mouse Avançado (Padrão)**
```
• Use setas ↑↓ para navegar
• Pressione ENTER para selecionar  
• Tecle A-M para acesso rápido às opções
• Tecle X para sair
• ESC para modo digitação
```

#### **2. Modo Navegação por Setas**
```
• ↑↓ para navegar
• ENTER para selecionar
• ESC para digitar
```

#### **3. Modo Digitação Tradicional**
```
• Digite número da opção
• ENTER para confirmar
```

## 🎨 **Interface Visual Aprimorada**

### **Exemplo de Exibição:**
```
1. Funcionários (A)          ← Tecle 'A' para acesso direto
2. Equipamentos (B)          ← Tecle 'B' para acesso direto
3. Ordem de Serv. (C)        ← Tecle 'C' para acesso direto
...

🖱️  Áreas Clicáveis Disponíveis:
   Tecle 'A' para: Selecionar 'Funcionários'
   Tecle 'B' para: Selecionar 'Equipamentos'
   Tecle 'X' para: Sair/Voltar
```

## 🔧 **Configurações Técnicas**

### **Detecção Automática:**
- **Sistema detecta** capacidades do terminal
- **Fallback automático** para modo tradicional se necessário
- **Compatibilidade total** com Windows e Linux

### **Arquivo de Configuração:**
```json
{
  "display_config": {
    "mouse_simulation": true,
    "arrow_navigation": true,
    "highlight_color": "cyan"
  }
}
```

## 📖 **Como Usar - Exemplos Práticos**

### **Exemplo 1: Acesso Rápido a Funcionários**
```
1. Faça login no sistema
2. Tecle 'A' (sem navegar)
3. Sistema vai direto para Gestão de Funcionários
```

### **Exemplo 2: Navegação Híbrida**
```
1. Use ↑↓ para ver opções
2. Quando encontrar a desejada, tecle sua letra
3. Ou pressione ENTER na seleção atual
```

### **Exemplo 3: Acesso à Administração**
```
1. Tecle 'M' de qualquer lugar do menu
2. Sistema vai direto para Administração
3. Ou navegue até opção 13 e pressione ENTER
```

## 🛠️ **Funcionalidades em Submenus**

### **Gestão de Funcionários:**
```
A = Cadastrar Funcionário
B = Consultar Funcionário  
C = Alterar Dados
D = Relatórios
X = Voltar ao Menu Principal
```

### **Menu Administrativo:**
```
A = Alterar Minha Senha
B = Gerenciar Usuários
C = Informações do Sistema
D = Backup de Dados
E = Configurações
X = Voltar ao Menu Principal
```

## 🔍 **Troubleshooting**

### **"Mouse" não funciona?**
- ✅ Verifique se está usando Windows
- ✅ Terminal deve suportar entrada de teclado
- ✅ Use modo setas como alternativa

### **Letras não aparecem?**
- ✅ Sistema pode estar em modo digitação
- ✅ Pressione ESC para voltar ao modo navegação
- ✅ Reinicie o sistema se necessário

### **Navegação travada?**
- ✅ Pressione ESC para resetar modo
- ✅ Use CTRL+C para sair completamente
- ✅ Digite números diretamente como alternativa

## 📊 **Vantagens do Sistema**

### **✅ Velocidade:**
- Acesso direto às opções sem navegar
- Reduz tempo de operação
- Interface mais responsiva

### **✅ Intuitividade:**
- Simulação de cliques familiar
- Indicadores visuais claros
- Múltiplas formas de navegação

### **✅ Compatibilidade:**
- Funciona em qualquer terminal
- Não requer drivers ou software adicional
- Fallback automático para modo tradicional

### **✅ Flexibilidade:**
- Combine mouse, setas e digitação
- Personalize conforme preferência
- Modo híbrido para máxima eficiência

---

**💡 Dica Avançada**: Memorize as letras das opções mais usadas (A=Funcionários, C=Ordens de Serviço, M=Administração) para navegação ultra-rápida pelo sistema!
