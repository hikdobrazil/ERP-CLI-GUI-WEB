// Dados de demonstração para o Sistema ERP

function initializeDemoData() {
    // Verificar se há dados salvos no localStorage
    const savedEmployees = localStorage.getItem('erpEmployees');
    const savedEquipment = localStorage.getItem('erpEquipment');
    const savedServiceOrders = localStorage.getItem('erpServiceOrders');
    
    if (savedEmployees) {
        AppState.employees = JSON.parse(savedEmployees);
    } else {
        AppState.employees = generateDemoEmployees();
        localStorage.setItem('erpEmployees', JSON.stringify(AppState.employees));
    }
    
    if (savedEquipment) {
        AppState.equipment = JSON.parse(savedEquipment);
    } else {
        AppState.equipment = generateDemoEquipment();
        localStorage.setItem('erpEquipment', JSON.stringify(AppState.equipment));
    }
    
    if (savedServiceOrders) {
        AppState.serviceOrders = JSON.parse(savedServiceOrders);
    } else {
        AppState.serviceOrders = generateDemoServiceOrders();
        localStorage.setItem('erpServiceOrders', JSON.stringify(AppState.serviceOrders));
    }
}

function generateDemoEmployees() {
    return [
        {
            id: 'EMP0001',
            name: 'João Silva Santos',
            position: 'Desenvolvedor Senior',
            department: 'TI',
            hireDate: '2022-03-15',
            salary: 8500.00,
            active: true
        },
        {
            id: 'EMP0002',
            name: 'Maria Oliveira Costa',
            position: 'Analista de RH',
            department: 'RH',
            hireDate: '2021-07-20',
            salary: 6200.00,
            active: true
        },
        {
            id: 'EMP0003',
            name: 'Pedro Henrique Lima',
            position: 'Técnico de Suporte',
            department: 'TI',
            hireDate: '2023-01-10',
            salary: 4500.00,
            active: true
        },
        {
            id: 'EMP0004',
            name: 'Ana Carolina Ferreira',
            position: 'Coordenadora Financeira',
            department: 'Financeiro',
            hireDate: '2020-11-08',
            salary: 9200.00,
            active: true
        },
        {
            id: 'EMP0005',
            name: 'Carlos Eduardo Souza',
            position: 'Analista de Sistemas',
            department: 'TI',
            hireDate: '2022-09-12',
            salary: 7000.00,
            active: true
        },
        {
            id: 'EMP0006',
            name: 'Fernanda Rodrigues',
            position: 'Assistente Administrativo',
            department: 'Operações',
            hireDate: '2023-05-03',
            salary: 3800.00,
            active: true
        },
        {
            id: 'EMP0007',
            name: 'Ricardo Mendes',
            position: 'Gerente de Operações',
            department: 'Operações',
            hireDate: '2019-02-14',
            salary: 12000.00,
            active: true
        },
        {
            id: 'EMP0008',
            name: 'Juliana Alves',
            position: 'Analista Contábil',
            department: 'Financeiro',
            hireDate: '2021-12-01',
            salary: 5500.00,
            active: true
        },
        {
            id: 'EMP0009',
            name: 'Bruno Carvalho',
            position: 'Desenvolvedor Junior',
            department: 'TI',
            hireDate: '2024-01-15',
            salary: 4200.00,
            active: true
        },
        {
            id: 'EMP0010',
            name: 'Camila Torres',
            position: 'Especialista em RH',
            department: 'RH',
            hireDate: '2020-08-25',
            salary: 7200.00,
            active: true
        },
        {
            id: 'EMP0011',
            name: 'Diego Nascimento',
            position: 'Técnico de Manutenção',
            department: 'Operações',
            hireDate: '2022-06-18',
            salary: 4800.00,
            active: true
        },
        {
            id: 'EMP0012',
            name: 'Larissa Campos',
            position: 'Auxiliar Financeiro',
            department: 'Financeiro',
            hireDate: '2023-09-07',
            salary: 3200.00,
            active: true
        },
        {
            id: 'EMP0013',
            name: 'Rafael Pereira',
            position: 'Coordenador de TI',
            department: 'TI',
            hireDate: '2018-05-30',
            salary: 11500.00,
            active: true
        },
        {
            id: 'EMP0014',
            name: 'Priscila Barbosa',
            position: 'Recepcionista',
            department: 'Operações',
            hireDate: '2023-11-20',
            salary: 2800.00,
            active: true
        },
        {
            id: 'EMP0015',
            name: 'Thiago Martins',
            position: 'Analista de Qualidade',
            department: 'Operações',
            hireDate: '2021-04-12',
            salary: 6800.00,
            active: true
        }
    ];
}

function generateDemoEquipment() {
    return [
        {
            id: 'EQ0001',
            name: 'Notebook Dell Latitude 5520',
            type: 'Computador',
            brand: 'Dell',
            model: 'Latitude 5520',
            serialNumber: 'DL5520001',
            purchaseDate: '2023-01-15',
            status: 'Ativo',
            location: 'TI - Sala 101',
            responsible: 'EMP0001'
        },
        {
            id: 'EQ0002',
            name: 'Impressora HP LaserJet Pro',
            type: 'Impressora',
            brand: 'HP',
            model: 'LaserJet Pro M404n',
            serialNumber: 'HP404001',
            purchaseDate: '2022-11-08',
            status: 'Ativo',
            location: 'Administrativo',
            responsible: 'EMP0006'
        },
        {
            id: 'EQ0003',
            name: 'Monitor Samsung 24"',
            type: 'Monitor',
            brand: 'Samsung',
            model: 'S24F350FH',
            serialNumber: 'SM24001',
            purchaseDate: '2023-03-20',
            status: 'Ativo',
            location: 'TI - Sala 101',
            responsible: 'EMP0005'
        },
        {
            id: 'EQ0004',
            name: 'Projetor Epson PowerLite',
            type: 'Projetor',
            brand: 'Epson',
            model: 'PowerLite X49',
            serialNumber: 'EP49001',
            purchaseDate: '2022-09-12',
            status: 'Manutenção',
            location: 'Sala de Reuniões',
            responsible: 'EMP0011'
        },
        {
            id: 'EQ0005',
            name: 'Roteador TP-Link AC1750',
            type: 'Rede',
            brand: 'TP-Link',
            model: 'Archer C7',
            serialNumber: 'TP1750001',
            purchaseDate: '2023-05-10',
            status: 'Ativo',
            location: 'TI - Rack Principal',
            responsible: 'EMP0003'
        },
        {
            id: 'EQ0006',
            name: 'Smartphone Samsung Galaxy A54',
            type: 'Celular',
            brand: 'Samsung',
            model: 'Galaxy A54 5G',
            serialNumber: 'SGA54001',
            purchaseDate: '2024-02-01',
            status: 'Ativo',
            location: 'Gerência',
            responsible: 'EMP0007'
        },
        {
            id: 'EQ0007',
            name: 'No-Break APC Smart-UPS',
            type: 'Energia',
            brand: 'APC',
            model: 'Smart-UPS 1500VA',
            serialNumber: 'APC1500001',
            purchaseDate: '2022-12-15',
            status: 'Ativo',
            location: 'TI - Rack Principal',
            responsible: 'EMP0013'
        },
        {
            id: 'EQ0008',
            name: 'Câmera de Segurança Hikvision',
            type: 'Segurança',
            brand: 'Hikvision',
            model: 'DS-2CD2085FWD-I',
            serialNumber: 'HK085001',
            purchaseDate: '2023-08-22',
            status: 'Manutenção',
            location: 'Entrada Principal',
            responsible: 'EMP0011'
        }
    ];
}

function generateDemoServiceOrders() {
    return [
        {
            id: 'OS0001',
            title: 'Manutenção Preventiva - Projetor',
            description: 'Realizar limpeza e verificação de componentes do projetor da sala de reuniões',
            equipmentId: 'EQ0004',
            assignedTo: 'EMP0011',
            requestedBy: 'EMP0002',
            priority: 'Média',
            status: 'Em Andamento',
            createdDate: '2025-07-18',
            dueDate: '2025-07-25',
            estimatedHours: 4,
            category: 'Manutenção Preventiva'
        },
        {
            id: 'OS0002',
            title: 'Instalação de Software - Notebook',
            description: 'Instalar e configurar novo software de desenvolvimento no notebook do desenvolvedor',
            equipmentId: 'EQ0001',
            assignedTo: 'EMP0003',
            requestedBy: 'EMP0001',
            priority: 'Alta',
            status: 'Pendente',
            createdDate: '2025-07-19',
            dueDate: '2025-07-22',
            estimatedHours: 2,
            category: 'Instalação'
        },
        {
            id: 'OS0003',
            title: 'Reparo - Câmera de Segurança',
            description: 'Verificar e reparar problema de conexão da câmera de segurança da entrada',
            equipmentId: 'EQ0008',
            assignedTo: 'EMP0011',
            requestedBy: 'EMP0007',
            priority: 'Urgente',
            status: 'Pendente',
            createdDate: '2025-07-20',
            dueDate: '2025-07-21',
            estimatedHours: 6,
            category: 'Reparo'
        },
        {
            id: 'OS0004',
            title: 'Configuração de Rede - Roteador',
            description: 'Atualizar configurações de segurança e QoS do roteador principal',
            equipmentId: 'EQ0005',
            assignedTo: 'EMP0013',
            requestedBy: 'EMP0003',
            priority: 'Média',
            status: 'Concluída',
            createdDate: '2025-07-15',
            dueDate: '2025-07-18',
            estimatedHours: 3,
            category: 'Configuração',
            completedDate: '2025-07-17'
        },
        {
            id: 'OS0005',
            title: 'Troca de Toner - Impressora',
            description: 'Substituir cartucho de toner da impressora do setor administrativo',
            equipmentId: 'EQ0002',
            assignedTo: 'EMP0006',
            requestedBy: 'EMP0014',
            priority: 'Baixa',
            status: 'Concluída',
            createdDate: '2025-07-16',
            dueDate: '2025-07-19',
            estimatedHours: 0.5,
            category: 'Manutenção',
            completedDate: '2025-07-16'
        },
        {
            id: 'OS0006',
            title: 'Atualização de Sistema - Smartphone',
            description: 'Realizar atualização do sistema operacional e aplicativos corporativos',
            equipmentId: 'EQ0006',
            assignedTo: 'EMP0003',
            requestedBy: 'EMP0007',
            priority: 'Média',
            status: 'Em Andamento',
            createdDate: '2025-07-19',
            dueDate: '2025-07-23',
            estimatedHours: 1,
            category: 'Atualização'
        },
        {
            id: 'OS0007',
            title: 'Backup de Dados - Servidor',
            description: 'Realizar backup completo dos dados do servidor principal',
            equipmentId: null,
            assignedTo: 'EMP0013',
            requestedBy: 'EMP0004',
            priority: 'Alta',
            status: 'Agendada',
            createdDate: '2025-07-20',
            dueDate: '2025-07-22',
            estimatedHours: 8,
            category: 'Backup'
        },
        {
            id: 'OS0008',
            title: 'Calibração - Monitor',
            description: 'Calibrar cores e ajustar configurações do monitor para melhor qualidade',
            equipmentId: 'EQ0003',
            assignedTo: 'EMP0005',
            requestedBy: 'EMP0009',
            priority: 'Baixa',
            status: 'Pendente',
            createdDate: '2025-07-18',
            dueDate: '2025-07-26',
            estimatedHours: 1,
            category: 'Calibração'
        },
        {
            id: 'OS0009',
            title: 'Teste de Funcionamento - No-Break',
            description: 'Realizar teste de autonomia e funcionamento do no-break do rack principal',
            equipmentId: 'EQ0007',
            assignedTo: 'EMP0011',
            requestedBy: 'EMP0013',
            priority: 'Média',
            status: 'Concluída',
            createdDate: '2025-07-12',
            dueDate: '2025-07-15',
            estimatedHours: 2,
            category: 'Teste',
            completedDate: '2025-07-14'
        },
        {
            id: 'OS0010',
            title: 'Instalação de Antivírus - Computadores',
            description: 'Instalar e configurar nova versão do antivírus corporativo em todos os computadores',
            equipmentId: null,
            assignedTo: 'EMP0003',
            requestedBy: 'EMP0013',
            priority: 'Alta',
            status: 'Em Andamento',
            createdDate: '2025-07-17',
            dueDate: '2025-07-24',
            estimatedHours: 16,
            category: 'Instalação'
        },
        {
            id: 'OS0011',
            title: 'Limpeza Geral - Equipamentos TI',
            description: 'Realizar limpeza completa de todos os equipamentos de TI',
            equipmentId: null,
            assignedTo: 'EMP0011',
            requestedBy: 'EMP0013',
            priority: 'Baixa',
            status: 'Agendada',
            createdDate: '2025-07-19',
            dueDate: '2025-07-30',
            estimatedHours: 12,
            category: 'Manutenção Preventiva'
        },
        {
            id: 'OS0012',
            title: 'Configuração de Backup Automático',
            description: 'Configurar rotina de backup automático para arquivos críticos',
            equipmentId: 'EQ0001',
            assignedTo: 'EMP0001',
            requestedBy: 'EMP0004',
            priority: 'Média',
            status: 'Pendente',
            createdDate: '2025-07-20',
            dueDate: '2025-07-25',
            estimatedHours: 3,
            category: 'Configuração'
        }
    ];
}

// Funções para obter estatísticas dos dados
function getEmployeeStats() {
    return {
        total: AppState.employees.length,
        active: AppState.employees.filter(emp => emp.active).length,
        byDepartment: getEmployeesByDepartment(),
        newThisMonth: getNewEmployeesThisMonth()
    };
}

function getEmployeesByDepartment() {
    const departments = {};
    AppState.employees.forEach(emp => {
        departments[emp.department] = (departments[emp.department] || 0) + 1;
    });
    return departments;
}

function getNewEmployeesThisMonth() {
    const thisMonth = new Date().getMonth();
    const thisYear = new Date().getFullYear();
    
    return AppState.employees.filter(emp => {
        const hireDate = new Date(emp.hireDate);
        return hireDate.getMonth() === thisMonth && hireDate.getFullYear() === thisYear;
    }).length;
}

function getEquipmentStats() {
    return {
        total: AppState.equipment.length,
        active: AppState.equipment.filter(eq => eq.status === 'Ativo').length,
        maintenance: AppState.equipment.filter(eq => eq.status === 'Manutenção').length,
        byType: getEquipmentByType()
    };
}

function getEquipmentByType() {
    const types = {};
    AppState.equipment.forEach(eq => {
        types[eq.type] = (types[eq.type] || 0) + 1;
    });
    return types;
}

function getServiceOrderStats() {
    return {
        total: AppState.serviceOrders.length,
        open: AppState.serviceOrders.filter(os => os.status !== 'Concluída').length,
        urgent: AppState.serviceOrders.filter(os => os.priority === 'Urgente' && os.status !== 'Concluída').length,
        completed: AppState.serviceOrders.filter(os => os.status === 'Concluída').length,
        byStatus: getServiceOrdersByStatus(),
        byPriority: getServiceOrdersByPriority()
    };
}

function getServiceOrdersByStatus() {
    const statuses = {};
    AppState.serviceOrders.forEach(os => {
        statuses[os.status] = (statuses[os.status] || 0) + 1;
    });
    return statuses;
}

function getServiceOrdersByPriority() {
    const priorities = {};
    AppState.serviceOrders.forEach(os => {
        priorities[os.priority] = (priorities[os.priority] || 0) + 1;
    });
    return priorities;
}

// Função para reset dos dados (para desenvolvimento)
function resetDemoData() {
    if (confirm('Tem certeza que deseja resetar todos os dados? Esta ação não pode ser desfeita.')) {
        localStorage.removeItem('erpEmployees');
        localStorage.removeItem('erpEquipment');
        localStorage.removeItem('erpServiceOrders');
        
        initializeDemoData();
        
        // Atualizar interface se estiver na aplicação
        if (AppState.currentUser) {
            loadEmployees();
            updateDashboardStats();
        }
        
        showAlert('Dados resetados com sucesso!', 'success');
    }
}

// Função para exportar dados (para backup)
function exportData() {
    const data = {
        employees: AppState.employees,
        equipment: AppState.equipment,
        serviceOrders: AppState.serviceOrders,
        exportDate: new Date().toISOString()
    };
    
    const dataStr = JSON.stringify(data, null, 2);
    const dataBlob = new Blob([dataStr], { type: 'application/json' });
    
    const link = document.createElement('a');
    link.href = URL.createObjectURL(dataBlob);
    link.download = `erp-backup-${new Date().toISOString().split('T')[0]}.json`;
    link.click();
    
    showAlert('Dados exportados com sucesso!', 'success');
}

// Função para importar dados
function importData(file) {
    const reader = new FileReader();
    reader.onload = function(e) {
        try {
            const data = JSON.parse(e.target.result);
            
            if (data.employees) AppState.employees = data.employees;
            if (data.equipment) AppState.equipment = data.equipment;
            if (data.serviceOrders) AppState.serviceOrders = data.serviceOrders;
            
            // Salvar no localStorage
            localStorage.setItem('erpEmployees', JSON.stringify(AppState.employees));
            localStorage.setItem('erpEquipment', JSON.stringify(AppState.equipment));
            localStorage.setItem('erpServiceOrders', JSON.stringify(AppState.serviceOrders));
            
            // Atualizar interface
            if (AppState.currentUser) {
                loadEmployees();
                updateDashboardStats();
            }
            
            showAlert('Dados importados com sucesso!', 'success');
        } catch (error) {
            showAlert('Erro ao importar dados. Verifique o formato do arquivo.', 'error');
        }
    };
    reader.readAsText(file);
}
