# 🚀 Deploy Completo - GitHub Pages

## ✅ **Passo a Passo - Repositório Completo**

### **1. Criar Repositório no GitHub**
1. Acesse [github.com](https://github.com)
2. Clique em **"New repository"**
3. Nome sugerido: `sistema-erp-completo`
4. Marque **"Public"** 
5. Clique **"Create repository"**

### **2. Upload da Pasta Completa**
Faça upload de **TODA a pasta "CLI ERP"** para o repositório:

```
📁 Estrutura completa a enviar:
├── README.md              # Documentação principal
├── DEPLOY.md              # Este guia
├── main.py                # Versão CLI
├── gui_main.py            # Versão GUI
├── .gitignore             # Arquivos ignorados
├── .github/workflows/     # GitHub Actions
│   └── deploy.yml         # Deploy automático
└── web/                   # 🌐 Versão Web
    ├── index.html
    ├── css/styles.css
    └── js/*.js
```

**💡 Vantagem**: Visitantes verão todas as 3 versões e a evolução do projeto!

### **3. Ativar GitHub Pages**
1. No seu repositório, vá em **Settings**
2. Role até **"Pages"** no menu lateral
3. Em **"Source"**, selecione **"Deploy from a branch"**
4. Escolha **"main"** e **"/ (root)"**
5. Clique **"Save"**

**🤖 GitHub Actions**: O arquivo `.github/workflows/deploy.yml` automaticamente fará deploy da pasta `/web/` para GitHub Pages!

### **4. Acessar o Sistema**
- ⏱️ Aguarde **2-3 minutos** para o deploy
- 🌐 URL: `https://SEUUSUARIO.github.io/sistema-erp-completo`
- 👤 Login: **admin** / **mudar@123**

### **5. Verificar Deploy**
- ✅ **Repositório**: Mostra todas as 3 versões
- ✅ **GitHub Pages**: Serve apenas a versão web
- ✅ **README**: Documentação completa do projeto

---

## 🎯 **Teste Local Primeiro**

Antes do deploy, teste localmente:

```powershell
# Navegue até a pasta web
cd "c:\Users\hikdo\Desktop\CLI ERP\web"

# Inicie o servidor
python -m http.server 8000

# Acesse: http://localhost:8000
```

---

## 🔧 **Solução de Problemas**

### **❌ Página em branco**
- Verifique se os arquivos estão na **raiz** do repositório
- Certifique-se que o arquivo se chama **index.html** (não Index.html)

### **❌ CSS não carrega**
- Verifique se a pasta **css/** está no repositório
- Confirme que o arquivo é **styles.css**

### **❌ JavaScript não funciona**
- Verifique se a pasta **js/** está completa
- Confirme se todos os 3 arquivos JS estão presentes

### **❌ 404 Error**
- GitHub Pages pode demorar até 10 minutos
- Tente acessar com **https://** (não http://)
- Verifique se o repositório é **público**

---

## 📱 **Features da Versão Web**

### ✨ **O que funciona agora:**
- ✅ Login seguro (admin/mudar@123)
- ✅ Dashboard com estatísticas
- ✅ CRUD completo de Funcionários
- ✅ Design responsivo (mobile/desktop)
- ✅ Persistência local (LocalStorage)
- ✅ Formulários com validação
- ✅ Filtros e busca em tempo real

### 🔄 **Em desenvolvimento:**
- CRUD de Equipamentos (interface criada)
- CRUD de Ordens de Serviço (interface criada)
- Relatórios avançados
- Gráficos dinâmicos

---

## 🎨 **Personalização Rápida**

### **Alterar Nome/Logo**
Edite o arquivo `index.html`, linha ~25:
```html
<div class="logo">
    <i class="fas fa-building"></i>
    <h1>MEU SISTEMA ERP</h1>
    <p>Minha Empresa</p>
</div>
```

### **Alterar Cores**
Edite o arquivo `css/styles.css`, início do arquivo:
```css
:root {
  --primary-color: #3b82f6;    /* Sua cor principal */
  --secondary-color: #6b7280;  /* Cor secundária */
}
```

---

## 🎯 **URL Final**

Substitua `SEUUSUARIO` pelo seu username do GitHub:

🌐 **https://SEUUSUARIO.github.io/sistema-erp-completo**

**Exemplo:**
- Username: `joaosilva`
- URL: `https://joaosilva.github.io/sistema-erp-completo`

### **🎁 Bonus - Repositório Completo**
Os visitantes do seu GitHub verão:
- 📖 **README.md**: Documentação das 3 versões
- 💻 **main.py**: Código da versão CLI
- 🖥️ **gui_main.py**: Código da versão GUI  
- 🌐 **web/**: Código da versão web
- 🚀 **DEPLOY.md**: Este guia de deploy
- ⚙️ **GitHub Actions**: Deploy automático

**Isso mostra sua evolução como desenvolvedor: CLI → GUI → Web!**

---

**🎉 Pronto! Seu Sistema ERP estará online e acessível de qualquer lugar!**
