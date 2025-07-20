# Sistema de Segurança - ERP Empresarial

## 🔐 Sistema de Autenticação

O sistema ERP agora possui um robusto sistema de autenticação que protege o acesso aos dados empresariais.

### 🔑 Senha Padrão
- **Senha inicial**: `mudar@123`
- **Política**: Recomenda-se alterar a senha padrão no primeiro acesso

### 🛡️ Funcionalidades de Segurança

#### 1. Tela de Login
- Interface inspirada no sistema original ORDEM DE SERVIÇO versão 1.1a
- ASCII art profissional com informações do sistema
- Exibição de data e hora atual
- Campo de senha oculto (não mostra caracteres digitados)

#### 2. Controle de Tentativas
- Máximo de **3 tentativas** de login
- Sistema bloqueado após tentativas excedidas
- Mensagens claras sobre tentativas restantes
- Encerramento automático por segurança

#### 3. Menu Administrativo
Acessível através da opção **13. Administração** no menu principal:

- **Alterar Senha**: Permite trocar a senha do sistema
- **Informações do Sistema**: Mostra estatísticas e configurações
- **Backup de Dados**: (Em desenvolvimento)
- **Configurações**: (Em desenvolvimento)

#### 4. Alteração de Senha
- Verificação da senha atual
- Senha nova deve ter mínimo 6 caracteres
- Confirmação da nova senha
- Validação de segurança

#### 5. Informações do Sistema
- Dados da sessão atual
- Status da senha (se ainda é a padrão)
- Estatísticas operacionais
- Timestamp de acesso

### 📋 Como Usar

#### Primeiro Acesso:
1. Execute o sistema
2. Digite a senha: `mudar@123`
3. Acesse **13. Administração** → **1. Alterar Senha**
4. Defina uma nova senha segura

#### Login Diário:
1. Execute o sistema
2. Digite sua senha
3. Acesse normalmente o ERP

### 🚨 Medidas de Segurança

- **Senhas ocultas**: Uso do módulo `getpass` para entrada segura
- **Tentativas limitadas**: Proteção contra ataques de força bruta
- **Timeouts**: Pequenos delays para reduzir velocidade de ataques
- **Validação**: Verificação de políticas de senha
- **Feedback claro**: Mensagens específicas sobre erros

### ⚠️ Recomendações de Segurança

1. **Altere a senha padrão** imediatamente após o primeiro acesso
2. Use senhas com pelo menos **8 caracteres** (mínimo 6 requerido)
3. Combine letras, números e símbolos especiais
4. Não compartilhe a senha com outros usuários
5. Altere a senha periodicamente

### 🔧 Configurações Técnicas

- Arquivo de configuração: `config.json`
- Dados persistentes: `erp_data.json`
- Logs de sistema: (Implementação futura)
- Backup automático: (Implementação futura)

### 📝 Códigos de Status

- ✅ **Acesso autorizado**: Login bem-sucedido
- ❌ **Senha incorreta**: Credenciais inválidas
- 🔒 **Sistema bloqueado**: Muitas tentativas falharam
- 🔄 **Senha alterada**: Alteração bem-sucedida

### 🆘 Recuperação de Acesso

Em caso de esquecimento da senha:

#### Método 1 - Via Administrador:
1. Peça para um administrador resetar sua senha
2. Acesse **13. Administração** → **2. Gerenciar Usuários** → **4. Resetar Senha**
3. Digite sua nova senha

#### Método 2 - Recuperação Manual:
1. Edite o arquivo `users_data.json`
2. Localize seu usuário e altere o campo `"password"`
3. Execute o sistema e faça login

#### Método 3 - Usuário Padrão:
1. Use o usuário padrão: `admin` senha: `mudar@123`
2. Crie um novo usuário ou resete senhas conforme necessário

## 👥 Sistema Multi-Usuário

### 🔑 Gerenciamento de Usuários

#### Visualizar Usuários Cadastrados:
- **Menu**: Administração → Gerenciar Usuários → Ver Usuários Cadastrados
- **Informações mostradas**:
  - Nome do usuário
  - Função (Administrador/Operador/Consulta)
  - Status (Ativo/Inativo)
  - Último acesso
  - Destaque do usuário atual

#### Criar Novos Usuários:
- **Menu**: Administração → Gerenciar Usuários → Criar Novo Usuário
- **Funções disponíveis**:
  - **Administrador**: Acesso total ao sistema
  - **Operador**: Acesso às operações principais
  - **Consulta**: Apenas visualização de dados

#### Ver Detalhes e Senhas:
- **Detalhes completos** de qualquer usuário
- **Visualização de senha**: Apenas administrador pode ver sua própria senha
- **Informações de segurança**: Data de criação, último acesso, status

#### Gerenciar Status:
- **Ativar/Desativar** usuários
- **Resetar senhas** de outros usuários
- **Proteção**: Não pode alterar próprio status

### 🛡️ Níveis de Acesso

#### Administrador:
- ✅ Criar/gerenciar usuários
- ✅ Ver senhas (própria apenas)
- ✅ Resetar senhas de outros
- ✅ Alterar status de usuários
- ✅ Acesso total ao sistema

#### Operador:
- ✅ Usar funcionalidades principais
- ✅ Alterar própria senha
- ❌ Gerenciar outros usuários

#### Consulta:
- ✅ Visualizar dados
- ✅ Alterar própria senha
- ❌ Modificar dados
- ❌ Gerenciar usuários

### 📊 Auditoria e Logs

#### Informações Registradas:
- **Data de criação** de cada usuário
- **Último acesso** ao sistema
- **Status atual** (ativo/inativo)
- **Função atribuída** ao usuário

#### Arquivos de Dados:
- **`users_data.json`**: Banco de dados de usuários
- **`erp_data.json`**: Dados operacionais do sistema
- **Backup automático**: (Em desenvolvimento)

---

**Importante**: Este sistema é para fins educacionais. Para uso em produção, implemente criptografia adequada, banco de dados seguro e auditoria completa.
