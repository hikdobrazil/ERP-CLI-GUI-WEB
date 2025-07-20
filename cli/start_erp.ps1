# Sistema ERP - Launcher Unificado PowerShell
Clear-Host

Write-Host ""
Write-Host "╔══════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║                      SISTEMA ERP v2.0                       ║" -ForegroundColor Yellow
Write-Host "║                 Enterprise Resource Planning                 ║" -ForegroundColor White
Write-Host "╠══════════════════════════════════════════════════════════════╣" -ForegroundColor Cyan
Write-Host "║                                                              ║"
Write-Host "║  Escolha a versão do sistema que deseja executar:           ║" -ForegroundColor Green
Write-Host "║                                                              ║"
Write-Host "║  [1] 📱 Versão CLI (Terminal/Console)                       ║" -ForegroundColor White
Write-Host "║      • Interface clássica baseada em texto                  ║" -ForegroundColor Gray
Write-Host "║      • Navegação por setas e teclas                         ║" -ForegroundColor Gray
Write-Host "║      • Suporte a mouse simulado                             ║" -ForegroundColor Gray
Write-Host "║      • Compatível com qualquer terminal                     ║" -ForegroundColor Gray
Write-Host "║                                                              ║"
Write-Host "║  [2] 🖥️  Versão GUI (Interface Gráfica)                     ║" -ForegroundColor White
Write-Host "║      • Interface moderna e profissional                     ║" -ForegroundColor Gray
Write-Host "║      • Formulários intuitivos                               ║" -ForegroundColor Gray
Write-Host "║      • Tabelas dinâmicas                                    ║" -ForegroundColor Gray
Write-Host "║      • Base de dados SQLite                                 ║" -ForegroundColor Gray
Write-Host "║                                                              ║"
Write-Host "║  [0] ❌ Sair                                                 ║" -ForegroundColor Red
Write-Host "║                                                              ║"
Write-Host "╚══════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

do {
    $choice = Read-Host "Digite sua opção (1, 2 ou 0)"
    
    switch ($choice) {
        "1" {
            Write-Host ""
            Write-Host "==========================================" -ForegroundColor Green
            Write-Host "      INICIANDO VERSÃO CLI" -ForegroundColor Yellow
            Write-Host "==========================================" -ForegroundColor Green
            Write-Host ""
            
            try {
                python main.py
            } catch {
                Write-Host "Erro ao executar versão CLI: $($_.Exception.Message)" -ForegroundColor Red
            }
            break
        }
        "2" {
            Write-Host ""
            Write-Host "==========================================" -ForegroundColor Green
            Write-Host "      INICIANDO VERSÃO GUI" -ForegroundColor Yellow
            Write-Host "==========================================" -ForegroundColor Green
            Write-Host ""
            
            try {
                python gui_main.py
            } catch {
                Write-Host "Erro ao executar versão GUI: $($_.Exception.Message)" -ForegroundColor Red
            }
            break
        }
        "0" {
            Write-Host ""
            Write-Host "Saindo do sistema..." -ForegroundColor Blue
            break
        }
        default {
            Write-Host "Opção inválida! Tente novamente." -ForegroundColor Red
        }
    }
} while ($choice -notin @("1", "2", "0"))

Write-Host ""
Write-Host "Sistema encerrado." -ForegroundColor Blue
Read-Host "Pressione Enter para continuar..."
