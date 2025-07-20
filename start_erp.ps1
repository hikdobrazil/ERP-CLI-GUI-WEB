# Sistema ERP v3.0 - Launcher PowerShell
# Enterprise Resource Planning System

Clear-Host
Write-Host ""
Write-Host "╔══════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║                    🏢 SISTEMA ERP v3.0                      ║" -ForegroundColor Cyan
Write-Host "║                 Enterprise Resource Planning                 ║" -ForegroundColor Cyan
Write-Host "╠══════════════════════════════════════════════════════════════╣" -ForegroundColor Cyan
Write-Host "║                                                              ║" -ForegroundColor White
Write-Host "║  Escolha a versão do sistema que deseja executar:           ║" -ForegroundColor White
Write-Host "║                                                              ║" -ForegroundColor White
Write-Host "║  [1] 📱 Versão CLI (Terminal/Console)                       ║" -ForegroundColor Green
Write-Host "║      • Interface clássica baseada em texto                  ║" -ForegroundColor Gray
Write-Host "║      • Navegação por setas e teclas                         ║" -ForegroundColor Gray
Write-Host "║      • Arquivos JSON para dados                             ║" -ForegroundColor Gray
Write-Host "║      • Funciona em qualquer terminal                       ║" -ForegroundColor Gray
Write-Host "║                                                              ║" -ForegroundColor White
Write-Host "║  [2] 🖥️  Versão GUI (Interface Gráfica)                     ║" -ForegroundColor Yellow
Write-Host "║      • Interface moderna e profissional                     ║" -ForegroundColor Gray
Write-Host "║      • Formulários intuitivos                               ║" -ForegroundColor Gray
Write-Host "║      • Base de dados SQLite                                 ║" -ForegroundColor Gray
Write-Host "║      • Janelas nativas do sistema                           ║" -ForegroundColor Gray
Write-Host "║                                                              ║" -ForegroundColor White
Write-Host "║  [3] 🌐 Versão Web (Navegador)                              ║" -ForegroundColor Magenta
Write-Host "║      • Interface responsiva moderna                         ║" -ForegroundColor Gray
Write-Host "║      • Acesso via navegador local                           ║" -ForegroundColor Gray
Write-Host "║      • Demonstração online disponível                       ║" -ForegroundColor Gray
Write-Host "║      • PWA-ready e mobile-first                             ║" -ForegroundColor Gray
Write-Host "║                                                              ║" -ForegroundColor White
Write-Host "║  [0] ❌ Sair                                                 ║" -ForegroundColor Red
Write-Host "║                                                              ║" -ForegroundColor White
Write-Host "╚══════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

$choice = Read-Host "Digite sua escolha (0-3)"

switch ($choice) {
    "1" {
        Write-Host ""
        Write-Host "🚀 Iniciando Versão CLI..." -ForegroundColor Green
        Write-Host ""
        Set-Location "cli"
        & ".\run_erp.ps1"
        Set-Location ".."
    }
    "2" {
        Write-Host ""
        Write-Host "🚀 Iniciando Versão GUI..." -ForegroundColor Yellow
        Write-Host ""
        Set-Location "gui"
        & ".\run_gui.ps1"
        Set-Location ".."
    }
    "3" {
        Write-Host ""
        Write-Host "🚀 Iniciando Versão Web..." -ForegroundColor Magenta
        Write-Host "🌐 Abrindo servidor local..." -ForegroundColor Cyan
        Write-Host ""
        Write-Host "├─ Servidor: http://localhost:8000" -ForegroundColor White
        Write-Host "├─ Demo Online: https://hikdobrazil.github.io/ERP-CLI-GUI-WEB/" -ForegroundColor White
        Write-Host "└─ Pressione Ctrl+C para parar o servidor" -ForegroundColor White
        Write-Host ""
        Set-Location "web"
        python -m http.server 8000
        Set-Location ".."
    }
    "0" {
        Write-Host ""
        Write-Host "👋 Obrigado por usar o Sistema ERP!" -ForegroundColor Green
        Write-Host ""
        exit
    }
    default {
        Write-Host ""
        Write-Host "❌ Opção inválida! Tente novamente." -ForegroundColor Red
        Write-Host ""
        Read-Host "Pressione Enter para continuar"
        & $MyInvocation.MyCommand.Path
    }
}
