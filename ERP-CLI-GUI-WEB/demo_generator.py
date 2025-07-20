#!/usr/bin/env python3
"""
CLI ERP System - Demo Data Generator
Creates sample data for demonstration purposes
"""

import json
import random
from datetime import datetime, timedelta

def create_demo_data():
    """Create demonstration data for the ERP system"""
    
    # Sample employees
    employees = [
        {
            "id": "001",
            "name": "João Silva",
            "position": "Analista de Sistemas",
            "department": "TI",
            "salary": "R$ 5.500,00",
            "status": "Ativo",
            "hire_date": "2023-01-15"
        },
        {
            "id": "002", 
            "name": "Maria Santos",
            "position": "Técnica em Eletrônica",
            "department": "Manutenção",
            "salary": "R$ 4.200,00",
            "status": "Ativo",
            "hire_date": "2022-08-20"
        },
        {
            "id": "003",
            "name": "Carlos Ferreira",
            "position": "Supervisor de Produção",
            "department": "Produção",
            "salary": "R$ 6.800,00",
            "status": "Ativo",
            "hire_date": "2021-03-10"
        },
        {
            "id": "004",
            "name": "Ana Costa",
            "position": "Auxiliar Administrativo",
            "department": "Administrativo",
            "salary": "R$ 3.800,00",
            "status": "Ativo",
            "hire_date": "2023-06-01"
        }
    ]
    
    # Sample equipment
    equipment = [
        {
            "id": "EQ001",
            "name": "Torno Mecânico CNC",
            "type": "Máquina Industrial",
            "location": "Setor A",
            "status": "Operacional",
            "last_maintenance": "2025-06-15",
            "next_maintenance": "2025-09-15"
        },
        {
            "id": "EQ002",
            "name": "Compressor de Ar",
            "type": "Equipamento Auxiliar",
            "location": "Setor B",
            "status": "Manutenção",
            "last_maintenance": "2025-07-01",
            "next_maintenance": "2025-10-01"
        },
        {
            "id": "EQ003",
            "name": "Fresadora Universal",
            "type": "Máquina Industrial",
            "location": "Setor A",
            "status": "Operacional",
            "last_maintenance": "2025-05-20",
            "next_maintenance": "2025-08-20"
        }
    ]
    
    # Sample service orders
    service_orders = [
        {
            "id": "OS1001",
            "client": "Metalúrgica XYZ Ltda",
            "equipment": "Torno Mecânico CNC",
            "problem": "Ruído excessivo no fuso principal",
            "technician": "Maria Santos",
            "status": "Em Andamento",
            "created_date": "2025-07-18",
            "priority": "Alta"
        },
        {
            "id": "OS1002",
            "client": "Indústria ABC S/A",
            "equipment": "Compressor de Ar",
            "problem": "Perda de pressão",
            "technician": "Carlos Ferreira",
            "status": "Aguardando Peças",
            "created_date": "2025-07-19",
            "priority": "Média"
        },
        {
            "id": "OS1003",
            "client": "Empresa DEF",
            "equipment": "Fresadora Universal",
            "problem": "Calibração dos eixos",
            "technician": "João Silva",
            "status": "Concluída",
            "created_date": "2025-07-15",
            "priority": "Baixa"
        },
        {
            "id": "OS1004",
            "client": "Fábrica GHI",
            "equipment": "Sistema Elétrico",
            "problem": "Falha no quadro principal",
            "technician": "Maria Santos",
            "status": "Em Aberto",
            "created_date": "2025-07-20",
            "priority": "Crítica"
        }
    ]
    
    # Sample budgets
    budgets = [
        {
            "id": "ORC2001",
            "client": "Metalúrgica XYZ Ltda",
            "description": "Manutenção preventiva anual",
            "value": "R$ 15.800,00",
            "status": "Aprovado",
            "created_date": "2025-07-10",
            "valid_until": "2025-08-10"
        },
        {
            "id": "ORC2002",
            "client": "Indústria ABC S/A",
            "description": "Substituição de rolamentos",
            "value": "R$ 8.500,00",
            "status": "Em Análise",
            "created_date": "2025-07-18",
            "valid_until": "2025-08-18"
        }
    ]
    
    # Compile all demo data
    demo_data = {
        "employees": employees,
        "equipment": equipment,
        "service_orders": service_orders,
        "budgets": budgets,
        "system_stats": {
            "total_employees": len(employees),
            "active_equipment": len([eq for eq in equipment if eq["status"] == "Operacional"]),
            "pending_orders": len([so for so in service_orders if so["status"] in ["Em Andamento", "Em Aberto", "Aguardando Peças"]]),
            "open_orders": len([so for so in service_orders if so["status"] == "Em Aberto"]),
            "approved_budgets": len([b for b in budgets if b["status"] == "Aprovado"]),
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    }
    
    return demo_data

def save_demo_data():
    """Save demo data to file"""
    demo_data = create_demo_data()
    
    try:
        with open("demo_data.json", "w", encoding="utf-8") as f:
            json.dump(demo_data, f, indent=2, ensure_ascii=False)
        print("✅ Dados de demonstração criados com sucesso!")
        print(f"📊 Total de funcionários: {demo_data['system_stats']['total_employees']}")
        print(f"🔧 Equipamentos ativos: {demo_data['system_stats']['active_equipment']}")
        print(f"📋 Ordens pendentes: {demo_data['system_stats']['pending_orders']}")
        print(f"💰 Orçamentos aprovados: {demo_data['system_stats']['approved_budgets']}")
        
    except Exception as e:
        print(f"❌ Erro ao criar dados de demonstração: {e}")

if __name__ == "__main__":
    print("🔧 Gerando dados de demonstração para o Sistema ERP...")
    save_demo_data()
    print("\n🚀 Execute 'python main.py' para usar o sistema!")
