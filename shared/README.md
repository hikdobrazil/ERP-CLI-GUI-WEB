# 📊 Dados Compartilhados - ERP System

## 🎯 Sobre
Esta pasta contém dados e configurações compartilhadas entre todas as versões do Sistema ERP (CLI, GUI e Web).

## 📁 Arquivos

### `config.json`
Configurações gerais do sistema:
```json
{
  "system_config": {
    "name": "Sistema ERP Empresarial",
    "version": "1.1a",
    "author": "ERP Developer",
    "language": "pt-BR"
  },
  "display_config": {
    "screen_width": 80,
    "use_colors": true,
    "auto_save": true
  }
}
```

### `demo_data.json`
Dados de demonstração padronizados:
- **Funcionários**: 15+ registros com diferentes departamentos
- **Equipamentos**: 8+ itens com status de manutenção
- **Ordens de Serviço**: Exemplos de diferentes prioridades

### `users_data.json`
Base de usuários do sistema:
```json
{
  "admin": {
    "password": "mudar@123",
    "role": "Administrador",
    "active": true
  }
}
```

## 🔄 Sincronização
Estes dados são utilizados como base para:
- **CLI**: Carregamento direto via JSON
- **GUI**: Importação inicial para SQLite
- **Web**: Seed data para LocalStorage

## 🛡️ Segurança
- Senhas são hasheadas nas versões de produção
- Dados demo não contêm informações sensíveis
- Configurações podem ser customizadas por ambiente

## 📈 Versionamento
- Dados mantidos sincronizados entre versões
- Schema compatível com todas as implementações
- Facilita migração entre plataformas

---
📖 **Para mais informações, consulte a documentação em** `/docs/`
