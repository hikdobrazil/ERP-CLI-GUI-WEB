// Gerenciamento de Formulários - Sistema ERP Web

// Estilos CSS adicionais para formulários
function addFormStyles() {
    if (!document.querySelector('#form-styles')) {
        const styles = document.createElement('style');
        styles.id = 'form-styles';
        styles.textContent = `
            .form-group {
                margin-bottom: 20px;
            }
            
            .form-group label {
                display: block;
                margin-bottom: 6px;
                font-weight: 500;
                color: var(--text-primary);
            }
            
            .form-group input,
            .form-group select,
            .form-group textarea {
                width: 100%;
                padding: 10px 12px;
                border: 1px solid var(--border-color);
                border-radius: 6px;
                font-size: 14px;
                font-family: inherit;
                transition: border-color 0.2s ease;
            }
            
            .form-group input:focus,
            .form-group select:focus,
            .form-group textarea:focus {
                outline: none;
                border-color: var(--primary-color);
                box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
            }
            
            .form-group textarea {
                resize: vertical;
                min-height: 80px;
            }
            
            .form-actions {
                display: flex;
                gap: 12px;
                justify-content: flex-end;
                margin-top: 24px;
                padding-top: 20px;
                border-top: 1px solid var(--border-color);
            }
            
            .form-row {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 16px;
            }
            
            .form-row-3 {
                display: grid;
                grid-template-columns: 1fr 1fr 1fr;
                gap: 16px;
            }
            
            .employee-details {
                display: grid;
                gap: 16px;
            }
            
            .detail-item {
                padding: 12px;
                background: #f8fafc;
                border-radius: 6px;
                border-left: 3px solid var(--primary-color);
            }
            
            .detail-item strong {
                color: var(--text-primary);
                margin-right: 8px;
            }
            
            .profile-info {
                display: flex;
                align-items: center;
                gap: 20px;
                margin-bottom: 20px;
                padding: 20px;
                background: #f8fafc;
                border-radius: 8px;
            }
            
            .profile-avatar {
                font-size: 4rem;
                color: var(--primary-color);
            }
            
            .profile-details h3 {
                margin-bottom: 8px;
                color: var(--text-primary);
            }
            
            .profile-details p {
                margin-bottom: 4px;
                color: var(--text-secondary);
            }
            
            .required {
                color: var(--error-color);
            }
            
            .form-help {
                font-size: 12px;
                color: var(--text-secondary);
                margin-top: 4px;
            }
            
            .form-error {
                color: var(--error-color);
                font-size: 12px;
                margin-top: 4px;
                display: none;
            }
            
            .form-group.error input,
            .form-group.error select,
            .form-group.error textarea {
                border-color: var(--error-color);
            }
            
            .form-group.error .form-error {
                display: block;
            }
            
            @media (max-width: 768px) {
                .form-row,
                .form-row-3 {
                    grid-template-columns: 1fr;
                }
                
                .form-actions {
                    flex-direction: column;
                }
                
                .profile-info {
                    flex-direction: column;
                    text-align: center;
                }
            }
        `;
        document.head.appendChild(styles);
    }
}

// Inicializar estilos ao carregar
document.addEventListener('DOMContentLoaded', addFormStyles);

// Validação de formulários
function validateForm(formId) {
    const form = document.getElementById(formId);
    if (!form) return false;
    
    let isValid = true;
    const requiredFields = form.querySelectorAll('[required]');
    
    requiredFields.forEach(field => {
        const formGroup = field.closest('.form-group');
        const errorElement = formGroup.querySelector('.form-error');
        
        if (!field.value.trim()) {
            formGroup.classList.add('error');
            if (errorElement) {
                errorElement.textContent = 'Este campo é obrigatório';
            }
            isValid = false;
        } else {
            formGroup.classList.remove('error');
        }
    });
    
    return isValid;
}

// Limpar erros de validação
function clearValidationErrors(formId) {
    const form = document.getElementById(formId);
    if (!form) return;
    
    form.querySelectorAll('.form-group.error').forEach(group => {
        group.classList.remove('error');
    });
}

// Formulário de Funcionários
function showEmployeeForm(employeeId = null) {
    const isEdit = employeeId !== null;
    const employee = isEdit ? AppState.employees.find(emp => emp.id === employeeId) : null;
    
    const formContent = `
        <form id="employeeForm" onsubmit="saveEmployee(event)">
            ${isEdit ? `<input type="hidden" id="empId" value="${employee.id}">` : ''}
            
            <div class="form-row">
                <div class="form-group">
                    <label for="empName">Nome Completo <span class="required">*</span></label>
                    <input type="text" id="empName" required value="${employee ? employee.name : ''}">
                    <div class="form-error"></div>
                </div>
                
                <div class="form-group">
                    <label for="empPosition">Cargo <span class="required">*</span></label>
                    <input type="text" id="empPosition" required value="${employee ? employee.position : ''}">
                    <div class="form-error"></div>
                </div>
            </div>
            
            <div class="form-row">
                <div class="form-group">
                    <label for="empDepartment">Departamento <span class="required">*</span></label>
                    <select id="empDepartment" required>
                        <option value="">Selecione...</option>
                        <option value="TI" ${employee && employee.department === 'TI' ? 'selected' : ''}>TI</option>
                        <option value="RH" ${employee && employee.department === 'RH' ? 'selected' : ''}>RH</option>
                        <option value="Financeiro" ${employee && employee.department === 'Financeiro' ? 'selected' : ''}>Financeiro</option>
                        <option value="Operações" ${employee && employee.department === 'Operações' ? 'selected' : ''}>Operações</option>
                        <option value="Vendas" ${employee && employee.department === 'Vendas' ? 'selected' : ''}>Vendas</option>
                        <option value="Marketing" ${employee && employee.department === 'Marketing' ? 'selected' : ''}>Marketing</option>
                    </select>
                    <div class="form-error"></div>
                </div>
                
                <div class="form-group">
                    <label for="empHireDate">Data de Admissão <span class="required">*</span></label>
                    <input type="date" id="empHireDate" required value="${employee ? employee.hireDate : ''}">
                    <div class="form-error"></div>
                </div>
            </div>
            
            <div class="form-row">
                <div class="form-group">
                    <label for="empSalary">Salário (R$) <span class="required">*</span></label>
                    <input type="number" id="empSalary" step="0.01" min="0" required value="${employee ? employee.salary : ''}">
                    <div class="form-help">Digite apenas números, sem pontos ou vírgulas</div>
                    <div class="form-error"></div>
                </div>
                
                <div class="form-group">
                    <label for="empStatus">Status</label>
                    <select id="empStatus">
                        <option value="true" ${!employee || employee.active ? 'selected' : ''}>Ativo</option>
                        <option value="false" ${employee && !employee.active ? 'selected' : ''}>Inativo</option>
                    </select>
                </div>
            </div>
            
            <div class="form-actions">
                <button type="submit" class="btn btn-primary">
                    <i class="fas fa-save"></i> ${isEdit ? 'Atualizar' : 'Salvar'}
                </button>
                <button type="button" class="btn btn-secondary" onclick="closeModal()">
                    <i class="fas fa-times"></i> Cancelar
                </button>
            </div>
        </form>
    `;
    
    showModal(isEdit ? 'Editar Funcionário' : 'Cadastrar Funcionário', formContent);
    
    // Focar no primeiro campo
    setTimeout(() => {
        document.getElementById('empName').focus();
    }, 100);
}

function saveEmployee(e) {
    e.preventDefault();
    
    // Limpar erros anteriores
    clearValidationErrors('employeeForm');
    
    // Validar formulário
    if (!validateForm('employeeForm')) {
        showAlert('Por favor, corrija os erros no formulário!', 'error');
        return;
    }
    
    const isEdit = document.getElementById('empId') !== null;
    const employeeId = isEdit ? document.getElementById('empId').value : null;
    
    const employeeData = {
        id: employeeId || 'EMP' + String(AppState.employees.length + 1).padStart(4, '0'),
        name: document.getElementById('empName').value.trim(),
        position: document.getElementById('empPosition').value.trim(),
        department: document.getElementById('empDepartment').value,
        hireDate: document.getElementById('empHireDate').value,
        salary: parseFloat(document.getElementById('empSalary').value),
        active: document.getElementById('empStatus').value === 'true'
    };
    
    // Validações adicionais
    if (employeeData.salary <= 0) {
        showAlert('O salário deve ser maior que zero!', 'error');
        return;
    }
    
    if (new Date(employeeData.hireDate) > new Date()) {
        showAlert('A data de admissão não pode ser no futuro!', 'error');
        return;
    }
    
    if (isEdit) {
        // Atualizar funcionário existente
        const index = AppState.employees.findIndex(emp => emp.id === employeeId);
        if (index !== -1) {
            AppState.employees[index] = employeeData;
            showAlert('Funcionário atualizado com sucesso!', 'success');
        }
    } else {
        // Adicionar novo funcionário
        AppState.employees.push(employeeData);
        showAlert('Funcionário cadastrado com sucesso!', 'success');
    }
    
    // Salvar no localStorage
    localStorage.setItem('erpEmployees', JSON.stringify(AppState.employees));
    
    closeModal();
    loadEmployees();
    updateDashboardStats();
}

// Formulário de Equipamentos
function showEquipmentForm(equipmentId = null) {
    const isEdit = equipmentId !== null;
    const equipment = isEdit ? AppState.equipment.find(eq => eq.id === equipmentId) : null;
    
    const formContent = `
        <form id="equipmentForm" onsubmit="saveEquipment(event)">
            ${isEdit ? `<input type="hidden" id="eqId" value="${equipment.id}">` : ''}
            
            <div class="form-row">
                <div class="form-group">
                    <label for="eqName">Nome do Equipamento <span class="required">*</span></label>
                    <input type="text" id="eqName" required value="${equipment ? equipment.name : ''}">
                    <div class="form-error"></div>
                </div>
                
                <div class="form-group">
                    <label for="eqType">Tipo <span class="required">*</span></label>
                    <select id="eqType" required>
                        <option value="">Selecione...</option>
                        <option value="Computador" ${equipment && equipment.type === 'Computador' ? 'selected' : ''}>Computador</option>
                        <option value="Impressora" ${equipment && equipment.type === 'Impressora' ? 'selected' : ''}>Impressora</option>
                        <option value="Monitor" ${equipment && equipment.type === 'Monitor' ? 'selected' : ''}>Monitor</option>
                        <option value="Rede" ${equipment && equipment.type === 'Rede' ? 'selected' : ''}>Equipamento de Rede</option>
                        <option value="Projetor" ${equipment && equipment.type === 'Projetor' ? 'selected' : ''}>Projetor</option>
                        <option value="Telefone" ${equipment && equipment.type === 'Telefone' ? 'selected' : ''}>Telefone</option>
                        <option value="Celular" ${equipment && equipment.type === 'Celular' ? 'selected' : ''}>Celular</option>
                        <option value="Segurança" ${equipment && equipment.type === 'Segurança' ? 'selected' : ''}>Segurança</option>
                        <option value="Energia" ${equipment && equipment.type === 'Energia' ? 'selected' : ''}>Energia</option>
                        <option value="Outros" ${equipment && equipment.type === 'Outros' ? 'selected' : ''}>Outros</option>
                    </select>
                    <div class="form-error"></div>
                </div>
            </div>
            
            <div class="form-row">
                <div class="form-group">
                    <label for="eqBrand">Marca <span class="required">*</span></label>
                    <input type="text" id="eqBrand" required value="${equipment ? equipment.brand : ''}">
                    <div class="form-error"></div>
                </div>
                
                <div class="form-group">
                    <label for="eqModel">Modelo <span class="required">*</span></label>
                    <input type="text" id="eqModel" required value="${equipment ? equipment.model : ''}">
                    <div class="form-error"></div>
                </div>
            </div>
            
            <div class="form-row">
                <div class="form-group">
                    <label for="eqSerial">Número de Série <span class="required">*</span></label>
                    <input type="text" id="eqSerial" required value="${equipment ? equipment.serialNumber : ''}">
                    <div class="form-error"></div>
                </div>
                
                <div class="form-group">
                    <label for="eqPurchaseDate">Data de Aquisição <span class="required">*</span></label>
                    <input type="date" id="eqPurchaseDate" required value="${equipment ? equipment.purchaseDate : ''}">
                    <div class="form-error"></div>
                </div>
            </div>
            
            <div class="form-row">
                <div class="form-group">
                    <label for="eqStatus">Status</label>
                    <select id="eqStatus">
                        <option value="Ativo" ${!equipment || equipment.status === 'Ativo' ? 'selected' : ''}>Ativo</option>
                        <option value="Manutenção" ${equipment && equipment.status === 'Manutenção' ? 'selected' : ''}>Em Manutenção</option>
                        <option value="Inativo" ${equipment && equipment.status === 'Inativo' ? 'selected' : ''}>Inativo</option>
                        <option value="Descartado" ${equipment && equipment.status === 'Descartado' ? 'selected' : ''}>Descartado</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="eqLocation">Localização</label>
                    <input type="text" id="eqLocation" value="${equipment ? equipment.location || '' : ''}" placeholder="Ex: Sala 101, TI">
                </div>
            </div>
            
            <div class="form-group">
                <label for="eqResponsible">Responsável</label>
                <select id="eqResponsible">
                    <option value="">Nenhum</option>
                    ${AppState.employees.filter(emp => emp.active).map(emp => 
                        `<option value="${emp.id}" ${equipment && equipment.responsible === emp.id ? 'selected' : ''}>${emp.name}</option>`
                    ).join('')}
                </select>
            </div>
            
            <div class="form-actions">
                <button type="submit" class="btn btn-primary">
                    <i class="fas fa-save"></i> ${isEdit ? 'Atualizar' : 'Salvar'}
                </button>
                <button type="button" class="btn btn-secondary" onclick="closeModal()">
                    <i class="fas fa-times"></i> Cancelar
                </button>
            </div>
        </form>
    `;
    
    showModal(isEdit ? 'Editar Equipamento' : 'Cadastrar Equipamento', formContent);
    
    setTimeout(() => {
        document.getElementById('eqName').focus();
    }, 100);
}

function saveEquipment(e) {
    e.preventDefault();
    
    clearValidationErrors('equipmentForm');
    
    if (!validateForm('equipmentForm')) {
        showAlert('Por favor, corrija os erros no formulário!', 'error');
        return;
    }
    
    const isEdit = document.getElementById('eqId') !== null;
    const equipmentId = isEdit ? document.getElementById('eqId').value : null;
    
    const equipmentData = {
        id: equipmentId || 'EQ' + String(AppState.equipment.length + 1).padStart(4, '0'),
        name: document.getElementById('eqName').value.trim(),
        type: document.getElementById('eqType').value,
        brand: document.getElementById('eqBrand').value.trim(),
        model: document.getElementById('eqModel').value.trim(),
        serialNumber: document.getElementById('eqSerial').value.trim(),
        purchaseDate: document.getElementById('eqPurchaseDate').value,
        status: document.getElementById('eqStatus').value,
        location: document.getElementById('eqLocation').value.trim(),
        responsible: document.getElementById('eqResponsible').value
    };
    
    // Validação de data
    if (new Date(equipmentData.purchaseDate) > new Date()) {
        showAlert('A data de aquisição não pode ser no futuro!', 'error');
        return;
    }
    
    if (isEdit) {
        const index = AppState.equipment.findIndex(eq => eq.id === equipmentId);
        if (index !== -1) {
            AppState.equipment[index] = equipmentData;
            showAlert('Equipamento atualizado com sucesso!', 'success');
        }
    } else {
        AppState.equipment.push(equipmentData);
        showAlert('Equipamento cadastrado com sucesso!', 'success');
    }
    
    localStorage.setItem('erpEquipment', JSON.stringify(AppState.equipment));
    
    closeModal();
    updateDashboardStats();
}

// Formulário de Ordem de Serviço
function showServiceOrderForm(orderId = null) {
    const isEdit = orderId !== null;
    const order = isEdit ? AppState.serviceOrders.find(os => os.id === orderId) : null;
    
    const formContent = `
        <form id="serviceOrderForm" onsubmit="saveServiceOrder(event)">
            ${isEdit ? `<input type="hidden" id="osId" value="${order.id}">` : ''}
            
            <div class="form-group">
                <label for="osTitle">Título da O.S. <span class="required">*</span></label>
                <input type="text" id="osTitle" required value="${order ? order.title : ''}" placeholder="Ex: Manutenção preventiva - Impressora">
                <div class="form-error"></div>
            </div>
            
            <div class="form-group">
                <label for="osDescription">Descrição <span class="required">*</span></label>
                <textarea id="osDescription" required placeholder="Descreva detalhadamente o serviço a ser realizado...">${order ? order.description : ''}</textarea>
                <div class="form-error"></div>
            </div>
            
            <div class="form-row">
                <div class="form-group">
                    <label for="osEquipment">Equipamento</label>
                    <select id="osEquipment">
                        <option value="">Não se aplica</option>
                        ${AppState.equipment.map(eq => 
                            `<option value="${eq.id}" ${order && order.equipmentId === eq.id ? 'selected' : ''}>${eq.name} (${eq.id})</option>`
                        ).join('')}
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="osCategory">Categoria <span class="required">*</span></label>
                    <select id="osCategory" required>
                        <option value="">Selecione...</option>
                        <option value="Manutenção Preventiva" ${order && order.category === 'Manutenção Preventiva' ? 'selected' : ''}>Manutenção Preventiva</option>
                        <option value="Manutenção Corretiva" ${order && order.category === 'Manutenção Corretiva' ? 'selected' : ''}>Manutenção Corretiva</option>
                        <option value="Instalação" ${order && order.category === 'Instalação' ? 'selected' : ''}>Instalação</option>
                        <option value="Configuração" ${order && order.category === 'Configuração' ? 'selected' : ''}>Configuração</option>
                        <option value="Reparo" ${order && order.category === 'Reparo' ? 'selected' : ''}>Reparo</option>
                        <option value="Atualização" ${order && order.category === 'Atualização' ? 'selected' : ''}>Atualização</option>
                        <option value="Backup" ${order && order.category === 'Backup' ? 'selected' : ''}>Backup</option>
                        <option value="Teste" ${order && order.category === 'Teste' ? 'selected' : ''}>Teste</option>
                        <option value="Outros" ${order && order.category === 'Outros' ? 'selected' : ''}>Outros</option>
                    </select>
                    <div class="form-error"></div>
                </div>
            </div>
            
            <div class="form-row-3">
                <div class="form-group">
                    <label for="osPriority">Prioridade <span class="required">*</span></label>
                    <select id="osPriority" required>
                        <option value="">Selecione...</option>
                        <option value="Baixa" ${order && order.priority === 'Baixa' ? 'selected' : ''}>Baixa</option>
                        <option value="Média" ${order && order.priority === 'Média' ? 'selected' : ''}>Média</option>
                        <option value="Alta" ${order && order.priority === 'Alta' ? 'selected' : ''}>Alta</option>
                        <option value="Urgente" ${order && order.priority === 'Urgente' ? 'selected' : ''}>Urgente</option>
                    </select>
                    <div class="form-error"></div>
                </div>
                
                <div class="form-group">
                    <label for="osStatus">Status</label>
                    <select id="osStatus">
                        <option value="Pendente" ${!order || order.status === 'Pendente' ? 'selected' : ''}>Pendente</option>
                        <option value="Em Andamento" ${order && order.status === 'Em Andamento' ? 'selected' : ''}>Em Andamento</option>
                        <option value="Agendada" ${order && order.status === 'Agendada' ? 'selected' : ''}>Agendada</option>
                        <option value="Concluída" ${order && order.status === 'Concluída' ? 'selected' : ''}>Concluída</option>
                        <option value="Cancelada" ${order && order.status === 'Cancelada' ? 'selected' : ''}>Cancelada</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="osEstimatedHours">Horas Estimadas</label>
                    <input type="number" id="osEstimatedHours" step="0.5" min="0" value="${order ? order.estimatedHours : ''}" placeholder="Ex: 2.5">
                </div>
            </div>
            
            <div class="form-row">
                <div class="form-group">
                    <label for="osAssignedTo">Responsável <span class="required">*</span></label>
                    <select id="osAssignedTo" required>
                        <option value="">Selecione...</option>
                        ${AppState.employees.filter(emp => emp.active).map(emp => 
                            `<option value="${emp.id}" ${order && order.assignedTo === emp.id ? 'selected' : ''}>${emp.name} - ${emp.position}</option>`
                        ).join('')}
                    </select>
                    <div class="form-error"></div>
                </div>
                
                <div class="form-group">
                    <label for="osRequestedBy">Solicitado por</label>
                    <select id="osRequestedBy">
                        <option value="">Selecione...</option>
                        ${AppState.employees.filter(emp => emp.active).map(emp => 
                            `<option value="${emp.id}" ${order && order.requestedBy === emp.id ? 'selected' : ''}>${emp.name}</option>`
                        ).join('')}
                    </select>
                </div>
            </div>
            
            <div class="form-row">
                <div class="form-group">
                    <label for="osCreatedDate">Data de Criação</label>
                    <input type="date" id="osCreatedDate" value="${order ? order.createdDate : new Date().toISOString().split('T')[0]}" readonly>
                </div>
                
                <div class="form-group">
                    <label for="osDueDate">Data de Vencimento</label>
                    <input type="date" id="osDueDate" value="${order ? order.dueDate : ''}">
                </div>
            </div>
            
            <div class="form-actions">
                <button type="submit" class="btn btn-primary">
                    <i class="fas fa-save"></i> ${isEdit ? 'Atualizar' : 'Criar O.S.'}
                </button>
                <button type="button" class="btn btn-secondary" onclick="closeModal()">
                    <i class="fas fa-times"></i> Cancelar
                </button>
            </div>
        </form>
    `;
    
    showModal(isEdit ? 'Editar Ordem de Serviço' : 'Nova Ordem de Serviço', formContent);
    
    setTimeout(() => {
        document.getElementById('osTitle').focus();
    }, 100);
}

function saveServiceOrder(e) {
    e.preventDefault();
    
    clearValidationErrors('serviceOrderForm');
    
    if (!validateForm('serviceOrderForm')) {
        showAlert('Por favor, corrija os erros no formulário!', 'error');
        return;
    }
    
    const isEdit = document.getElementById('osId') !== null;
    const orderId = isEdit ? document.getElementById('osId').value : null;
    
    const orderData = {
        id: orderId || 'OS' + String(AppState.serviceOrders.length + 1).padStart(4, '0'),
        title: document.getElementById('osTitle').value.trim(),
        description: document.getElementById('osDescription').value.trim(),
        equipmentId: document.getElementById('osEquipment').value || null,
        category: document.getElementById('osCategory').value,
        priority: document.getElementById('osPriority').value,
        status: document.getElementById('osStatus').value,
        estimatedHours: parseFloat(document.getElementById('osEstimatedHours').value) || 0,
        assignedTo: document.getElementById('osAssignedTo').value,
        requestedBy: document.getElementById('osRequestedBy').value || null,
        createdDate: document.getElementById('osCreatedDate').value,
        dueDate: document.getElementById('osDueDate').value || null
    };
    
    // Validação de datas
    if (orderData.dueDate && new Date(orderData.dueDate) < new Date(orderData.createdDate)) {
        showAlert('A data de vencimento não pode ser anterior à data de criação!', 'error');
        return;
    }
    
    if (isEdit) {
        const index = AppState.serviceOrders.findIndex(os => os.id === orderId);
        if (index !== -1) {
            // Manter campos que não estão no formulário
            const existingOrder = AppState.serviceOrders[index];
            orderData.completedDate = existingOrder.completedDate;
            
            AppState.serviceOrders[index] = orderData;
            showAlert('Ordem de Serviço atualizada com sucesso!', 'success');
        }
    } else {
        AppState.serviceOrders.push(orderData);
        showAlert('Ordem de Serviço criada com sucesso!', 'success');
    }
    
    localStorage.setItem('erpServiceOrders', JSON.stringify(AppState.serviceOrders));
    
    closeModal();
    updateDashboardStats();
}

// Função para editar funcionário (chamada da tabela)
function editEmployee(id) {
    showEmployeeForm(id);
}

// Função para editar equipamento
function editEquipment(id) {
    showEquipmentForm(id);
}

// Função para editar ordem de serviço
function editServiceOrder(id) {
    showServiceOrderForm(id);
}
