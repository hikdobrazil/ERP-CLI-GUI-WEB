// Sistema ERP - Web Edition
// JavaScript Principal

// Estado global da aplicação
const AppState = {
    currentUser: null,
    currentPage: 'dashboard',
    sidebarCollapsed: false,
    employees: [],
    equipment: [],
    serviceOrders: []
};

// Inicialização da aplicação
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
    updateDateTime();
    setInterval(updateDateTime, 1000);
});

function initializeApp() {
    // Event listeners
    document.getElementById('loginForm').addEventListener('submit', handleLogin);
    
    // Inicializar dados demo
    initializeDemoData();
    
    // Verificar se há sessão ativa
    const savedUser = localStorage.getItem('erpUser');
    if (savedUser) {
        AppState.currentUser = JSON.parse(savedUser);
        showApp();
    }
}

// Gerenciamento de Login
function handleLogin(e) {
    e.preventDefault();
    
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();
    
    // Validação básica
    if (!username || !password) {
        showAlert('Por favor, preencha todos os campos!', 'error');
        return;
    }
    
    // Verificar credenciais (simulado)
    if (username === 'admin' && password === 'mudar@123') {
        AppState.currentUser = {
            username: username,
            role: 'Admin',
            loginTime: new Date().toISOString()
        };
        
        // Salvar sessão
        localStorage.setItem('erpUser', JSON.stringify(AppState.currentUser));
        
        // Mostrar feedback de sucesso
        showAlert('Login realizado com sucesso!', 'success');
        
        // Aguardar um pouco e mostrar a aplicação
        setTimeout(() => {
            showApp();
        }, 1000);
        
    } else {
        showAlert('Usuário ou senha inválidos!\\n\\nCredenciais corretas:\\nUsuário: admin\\nSenha: mudar@123', 'error');
        document.getElementById('password').value = '';
        document.getElementById('password').focus();
    }
}

function togglePassword() {
    const passwordField = document.getElementById('password');
    const toggleBtn = document.querySelector('.password-toggle i');
    
    if (passwordField.type === 'password') {
        passwordField.type = 'text';
        toggleBtn.className = 'fas fa-eye-slash';
    } else {
        passwordField.type = 'password';
        toggleBtn.className = 'fas fa-eye';
    }
}

function showApp() {
    document.getElementById('loginScreen').style.display = 'none';
    document.getElementById('appContainer').style.display = 'grid';
    
    // Atualizar informações do usuário
    document.getElementById('currentUser').textContent = AppState.currentUser.username;
    
    // Mostrar dashboard
    showDashboard();
    
    // Carregar dados iniciais
    loadEmployees();
}

function logout() {
    if (confirm('Deseja realmente sair do sistema?')) {
        localStorage.removeItem('erpUser');
        AppState.currentUser = null;
        
        document.getElementById('appContainer').style.display = 'none';
        document.getElementById('loginScreen').style.display = 'flex';
        
        // Limpar formulário
        document.getElementById('loginForm').reset();
        document.getElementById('username').value = 'admin';
    }
}

// Gerenciamento de Navegação
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const appContainer = document.getElementById('appContainer');
    
    AppState.sidebarCollapsed = !AppState.sidebarCollapsed;
    
    if (AppState.sidebarCollapsed) {
        sidebar.classList.add('collapsed');
        appContainer.classList.add('collapsed');
    } else {
        sidebar.classList.remove('collapsed');
        appContainer.classList.remove('collapsed');
    }
}

function setActivePage(page) {
    // Remover classe active de todos os itens de navegação
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('active');
    });
    
    // Remover classe active de todas as seções de conteúdo
    document.querySelectorAll('.content-section').forEach(section => {
        section.classList.remove('active');
    });
    
    // Ativar página atual
    AppState.currentPage = page;
    
    // Ativar item de navegação
    const navItems = document.querySelectorAll('.nav-item');
    const pageIndex = ['dashboard', 'employees', 'equipment', 'serviceOrders', 'reports', 'inventory', 'financial', 'admin'].indexOf(page);
    if (pageIndex !== -1 && navItems[pageIndex]) {
        navItems[pageIndex].classList.add('active');
    }
    
    // Mostrar seção de conteúdo
    const contentSection = document.getElementById(page + 'Content');
    if (contentSection) {
        contentSection.classList.add('active');
    }
    
    // Atualizar título da página
    updatePageTitle(page);
}

function updatePageTitle(page) {
    const titles = {
        'dashboard': 'Dashboard',
        'employees': 'Funcionários',
        'equipment': 'Equipamentos',
        'serviceOrders': 'Ordens de Serviço',
        'reports': 'Relatórios',
        'inventory': 'Estoque',
        'financial': 'Financeiro',
        'admin': 'Administração'
    };
    
    document.getElementById('pageTitle').textContent = titles[page] || 'Sistema ERP';
}

// Páginas do Sistema
function showDashboard() {
    setActivePage('dashboard');
    updateDashboardStats();
}

function showEmployees() {
    setActivePage('employees');
    loadEmployees();
}

function showEquipment() {
    setActivePage('equipment');
}

function showServiceOrders() {
    setActivePage('serviceOrders');
}

function showReports() {
    setActivePage('reports');
}

function showInventory() {
    setActivePage('inventory');
}

function showFinancial() {
    setActivePage('financial');
}

function showAdmin() {
    setActivePage('admin');
}

// Dashboard
function updateDashboardStats() {
    document.getElementById('totalEmployees').textContent = AppState.employees.length;
    document.getElementById('totalEquipment').textContent = AppState.equipment.length;
    document.getElementById('openOrders').textContent = AppState.serviceOrders.filter(order => order.status !== 'Concluída').length;
    
    // Atualizar gráfico (simulado)
    drawPerformanceChart();
}

function drawPerformanceChart() {
    const canvas = document.getElementById('performanceChart');
    const ctx = canvas.getContext('2d');
    
    // Limpar canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Dados simulados
    const data = [12, 19, 8, 15, 22, 18, 25];
    const labels = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'];
    
    // Configurações do gráfico
    const padding = 40;
    const chartWidth = canvas.width - (padding * 2);
    const chartHeight = canvas.height - (padding * 2);
    const maxValue = Math.max(...data);
    
    // Desenhar eixos
    ctx.strokeStyle = '#e5e7eb';
    ctx.lineWidth = 1;
    
    // Eixo Y
    ctx.beginPath();
    ctx.moveTo(padding, padding);
    ctx.lineTo(padding, canvas.height - padding);
    ctx.stroke();
    
    // Eixo X
    ctx.beginPath();
    ctx.moveTo(padding, canvas.height - padding);
    ctx.lineTo(canvas.width - padding, canvas.height - padding);
    ctx.stroke();
    
    // Desenhar linha do gráfico
    ctx.strokeStyle = '#3b82f6';
    ctx.lineWidth = 3;
    ctx.beginPath();
    
    data.forEach((value, index) => {
        const x = padding + (index * (chartWidth / (data.length - 1)));
        const y = canvas.height - padding - ((value / maxValue) * chartHeight);
        
        if (index === 0) {
            ctx.moveTo(x, y);
        } else {
            ctx.lineTo(x, y);
        }
        
        // Desenhar pontos
        ctx.fillStyle = '#3b82f6';
        ctx.beginPath();
        ctx.arc(x, y, 4, 0, Math.PI * 2);
        ctx.fill();
    });
    
    ctx.stroke();
    
    // Desenhar labels
    ctx.fillStyle = '#6b7280';
    ctx.font = '12px Inter';
    ctx.textAlign = 'center';
    
    labels.forEach((label, index) => {
        const x = padding + (index * (chartWidth / (data.length - 1)));
        ctx.fillText(label, x, canvas.height - 10);
    });
}

// Gerenciamento de Funcionários
function loadEmployees() {
    const tableBody = document.getElementById('employeesTableBody');
    if (!tableBody) return;
    
    tableBody.innerHTML = '';
    
    AppState.employees.forEach(employee => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${employee.id}</td>
            <td>${employee.name}</td>
            <td>${employee.position}</td>
            <td>${employee.department}</td>
            <td>${formatDate(employee.hireDate)}</td>
            <td><span class="status-badge status-${employee.active ? 'active' : 'inactive'}">${employee.active ? 'Ativo' : 'Inativo'}</span></td>
            <td>
                <button class="btn btn-primary" onclick="editEmployee('${employee.id}')">
                    <i class="fas fa-edit"></i>
                </button>
                <button class="btn btn-secondary" onclick="viewEmployee('${employee.id}')">
                    <i class="fas fa-eye"></i>
                </button>
            </td>
        `;
        tableBody.appendChild(row);
    });
}

function filterEmployees() {
    const searchTerm = document.getElementById('employeeSearch').value.toLowerCase();
    const departmentFilter = document.getElementById('departmentFilter').value;
    
    const filteredEmployees = AppState.employees.filter(employee => {
        const matchesSearch = employee.name.toLowerCase().includes(searchTerm) ||
                            employee.position.toLowerCase().includes(searchTerm);
        const matchesDepartment = !departmentFilter || employee.department === departmentFilter;
        
        return matchesSearch && matchesDepartment;
    });
    
    // Atualizar tabela com funcionários filtrados
    updateEmployeesTable(filteredEmployees);
}

function updateEmployeesTable(employees) {
    const tableBody = document.getElementById('employeesTableBody');
    if (!tableBody) return;
    
    tableBody.innerHTML = '';
    
    employees.forEach(employee => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${employee.id}</td>
            <td>${employee.name}</td>
            <td>${employee.position}</td>
            <td>${employee.department}</td>
            <td>${formatDate(employee.hireDate)}</td>
            <td><span class="status-badge status-${employee.active ? 'active' : 'inactive'}">${employee.active ? 'Ativo' : 'Inativo'}</span></td>
            <td>
                <button class="btn btn-primary" onclick="editEmployee('${employee.id}')">
                    <i class="fas fa-edit"></i>
                </button>
                <button class="btn btn-secondary" onclick="viewEmployee('${employee.id}')">
                    <i class="fas fa-eye"></i>
                </button>
            </td>
        `;
        tableBody.appendChild(row);
    });
}

// Modal Management
function showModal(title, content) {
    document.getElementById('modalTitle').textContent = title;
    document.getElementById('modalBody').innerHTML = content;
    document.getElementById('modalOverlay').classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    document.getElementById('modalOverlay').classList.remove('active');
    document.body.style.overflow = '';
}

// Formulários
function showEmployeeForm() {
    const formContent = `
        <form id="employeeForm" onsubmit="saveEmployee(event)">
            <div class="form-group">
                <label for="empName">Nome Completo:</label>
                <input type="text" id="empName" required>
            </div>
            <div class="form-group">
                <label for="empPosition">Cargo:</label>
                <input type="text" id="empPosition" required>
            </div>
            <div class="form-group">
                <label for="empDepartment">Departamento:</label>
                <select id="empDepartment" required>
                    <option value="">Selecione...</option>
                    <option value="TI">TI</option>
                    <option value="RH">RH</option>
                    <option value="Financeiro">Financeiro</option>
                    <option value="Operações">Operações</option>
                </select>
            </div>
            <div class="form-group">
                <label for="empHireDate">Data de Admissão:</label>
                <input type="date" id="empHireDate" required>
            </div>
            <div class="form-group">
                <label for="empSalary">Salário:</label>
                <input type="number" id="empSalary" step="0.01" required>
            </div>
            <div class="form-actions">
                <button type="submit" class="btn btn-primary">
                    <i class="fas fa-save"></i> Salvar
                </button>
                <button type="button" class="btn btn-secondary" onclick="closeModal()">
                    <i class="fas fa-times"></i> Cancelar
                </button>
            </div>
        </form>
    `;
    
    showModal('Cadastrar Funcionário', formContent);
}

function saveEmployee(e) {
    e.preventDefault();
    
    const employee = {
        id: 'EMP' + String(AppState.employees.length + 1).padStart(4, '0'),
        name: document.getElementById('empName').value,
        position: document.getElementById('empPosition').value,
        department: document.getElementById('empDepartment').value,
        hireDate: document.getElementById('empHireDate').value,
        salary: parseFloat(document.getElementById('empSalary').value),
        active: true
    };
    
    AppState.employees.push(employee);
    
    // Salvar no localStorage
    localStorage.setItem('erpEmployees', JSON.stringify(AppState.employees));
    
    closeModal();
    loadEmployees();
    updateDashboardStats();
    
    showAlert('Funcionário cadastrado com sucesso!', 'success');
}

function editEmployee(id) {
    const employee = AppState.employees.find(emp => emp.id === id);
    if (!employee) return;
    
    showAlert('Funcionalidade de edição em desenvolvimento!', 'info');
}

function viewEmployee(id) {
    const employee = AppState.employees.find(emp => emp.id === id);
    if (!employee) return;
    
    const content = `
        <div class="employee-details">
            <div class="detail-item">
                <strong>ID:</strong> ${employee.id}
            </div>
            <div class="detail-item">
                <strong>Nome:</strong> ${employee.name}
            </div>
            <div class="detail-item">
                <strong>Cargo:</strong> ${employee.position}
            </div>
            <div class="detail-item">
                <strong>Departamento:</strong> ${employee.department}
            </div>
            <div class="detail-item">
                <strong>Data de Admissão:</strong> ${formatDate(employee.hireDate)}
            </div>
            <div class="detail-item">
                <strong>Salário:</strong> R$ ${employee.salary.toLocaleString('pt-BR', {minimumFractionDigits: 2})}
            </div>
            <div class="detail-item">
                <strong>Status:</strong> ${employee.active ? 'Ativo' : 'Inativo'}
            </div>
        </div>
        <div class="form-actions">
            <button class="btn btn-primary" onclick="editEmployee('${employee.id}')">
                <i class="fas fa-edit"></i> Editar
            </button>
            <button class="btn btn-secondary" onclick="closeModal()">
                <i class="fas fa-times"></i> Fechar
            </button>
        </div>
    `;
    
    showModal('Detalhes do Funcionário', content);
}

function showServiceOrderForm() {
    showAlert('Funcionalidade de Ordem de Serviço em desenvolvimento!', 'info');
}

function showEquipmentForm() {
    showAlert('Funcionalidade de Equipamentos em desenvolvimento!', 'info');
}

// Perfil e Configurações
function showProfile() {
    const content = `
        <div class="profile-info">
            <div class="profile-avatar">
                <i class="fas fa-user-circle"></i>
            </div>
            <div class="profile-details">
                <h3>${AppState.currentUser.username}</h3>
                <p>Administrador do Sistema</p>
                <p><strong>Login:</strong> ${formatDateTime(AppState.currentUser.loginTime)}</p>
            </div>
        </div>
        <div class="form-actions">
            <button class="btn btn-primary" onclick="changePassword()">
                <i class="fas fa-key"></i> Alterar Senha
            </button>
            <button class="btn btn-secondary" onclick="closeModal()">
                <i class="fas fa-times"></i> Fechar
            </button>
        </div>
    `;
    
    showModal('Perfil do Usuário', content);
}

function showSettings() {
    showAlert('Configurações do sistema em desenvolvimento!', 'info');
}

function changePassword() {
    showAlert('Funcionalidade de alteração de senha em desenvolvimento!', 'info');
}

// Utilitários
function updateDateTime() {
    const now = new Date();
    const datetime = now.toLocaleDateString('pt-BR') + ' ' + now.toLocaleTimeString('pt-BR');
    const datetimeElement = document.getElementById('datetime');
    if (datetimeElement) {
        datetimeElement.textContent = datetime;
    }
}

function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('pt-BR');
}

function formatDateTime(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('pt-BR') + ' ' + date.toLocaleTimeString('pt-BR');
}

function showAlert(message, type = 'info') {
    // Criar elemento de alerta
    const alert = document.createElement('div');
    alert.className = `alert alert-${type}`;
    alert.innerHTML = `
        <div class="alert-content">
            <i class="fas fa-${getAlertIcon(type)}"></i>
            <span>${message}</span>
        </div>
        <button onclick="this.parentElement.remove()" class="alert-close">
            <i class="fas fa-times"></i>
        </button>
    `;
    
    // Adicionar estilos CSS se não existirem
    if (!document.querySelector('#alert-styles')) {
        const styles = document.createElement('style');
        styles.id = 'alert-styles';
        styles.textContent = `
            .alert {
                position: fixed;
                top: 20px;
                right: 20px;
                padding: 16px 20px;
                border-radius: 8px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                z-index: 10001;
                max-width: 400px;
                animation: slideInRight 0.3s ease;
                display: flex;
                justify-content: space-between;
                align-items: center;
                gap: 12px;
            }
            .alert-success { background: #dcfce7; border-left: 4px solid #10b981; color: #166534; }
            .alert-error { background: #fee2e2; border-left: 4px solid #ef4444; color: #991b1b; }
            .alert-warning { background: #fef3c7; border-left: 4px solid #f59e0b; color: #92400e; }
            .alert-info { background: #dbeafe; border-left: 4px solid #3b82f6; color: #1d4ed8; }
            .alert-content { display: flex; align-items: center; gap: 8px; }
            .alert-close { background: none; border: none; cursor: pointer; padding: 4px; }
            @keyframes slideInRight { from { transform: translateX(100%); } to { transform: translateX(0); } }
        `;
        document.head.appendChild(styles);
    }
    
    document.body.appendChild(alert);
    
    // Remover automaticamente após 5 segundos
    setTimeout(() => {
        if (alert.parentElement) {
            alert.remove();
        }
    }, 5000);
}

function getAlertIcon(type) {
    const icons = {
        'success': 'check-circle',
        'error': 'exclamation-circle',
        'warning': 'exclamation-triangle',
        'info': 'info-circle'
    };
    return icons[type] || 'info-circle';
}

// Responsividade móvel
function initializeMobileSupport() {
    // Detectar dispositivos móveis
    const isMobile = window.innerWidth <= 768;
    
    if (isMobile) {
        // Adicionar suporte a gestos de toque
        let startX, startY, dist, threshold = 150;
        
        document.addEventListener('touchstart', function(e) {
            const touch = e.touches[0];
            startX = touch.clientX;
            startY = touch.clientY;
        });
        
        document.addEventListener('touchend', function(e) {
            if (!startX || !startY) return;
            
            const touch = e.changedTouches[0];
            const distX = touch.clientX - startX;
            const distY = touch.clientY - startY;
            
            if (Math.abs(distX) > Math.abs(distY) && Math.abs(distX) > threshold) {
                if (distX > 0) {
                    // Swipe right - abrir sidebar
                    document.getElementById('sidebar').classList.add('active');
                } else {
                    // Swipe left - fechar sidebar
                    document.getElementById('sidebar').classList.remove('active');
                }
            }
            
            startX = startY = null;
        });
    }
}

// Inicializar suporte móvel quando a aplicação carregar
window.addEventListener('load', initializeMobileSupport);
