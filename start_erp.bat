@echo off
chcp 65001 >nul
color 0B
cls

echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                    🏢 SISTEMA ERP v3.0                      ║
echo ║                 Enterprise Resource Planning                 ║
echo ╠══════════════════════════════════════════════════════════════╣
echo ║                                                              ║
echo ║  Escolha a versão do sistema que deseja executar:           ║
echo ║                                                              ║
echo ║  [1] 📱 Versão CLI (Terminal/Console)                       ║
echo ║      • Interface clássica baseada em texto                  ║
echo ║      • Navegação por setas e teclas                         ║
echo ║      • Arquivos JSON para dados                             ║
echo ║      • Funciona em qualquer terminal                       ║
echo ║                                                              ║
echo ║  [2] 🖥️  Versão GUI (Interface Gráfica)                     ║
echo ║      • Interface moderna e profissional                     ║
echo ║      • Formulários intuitivos                               ║
echo ║      • Base de dados SQLite                                 ║
echo ║      • Janelas nativas do sistema                           ║
echo ║                                                              ║
echo ║  [3] 🌐 Versão Web (Navegador)                              ║
echo ║      • Interface responsiva moderna                         ║
echo ║      • Acesso via navegador local                           ║
echo ║      • Demonstração online disponível                       ║
echo ║      • PWA-ready e mobile-first                             ║
echo ║                                                              ║
echo ║  [0] ❌ Sair                                                 ║
echo ║                                                              ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

set /p choice="Digite sua escolha (0-3): "

if "%choice%"=="1" (
    echo.
    echo 🚀 Iniciando Versão CLI...
    echo.
    cd cli
    call run_erp.bat
    cd ..
) else if "%choice%"=="2" (
    echo.
    echo 🚀 Iniciando Versão GUI...
    echo.
    cd gui
    call run_gui.bat
    cd ..
) else if "%choice%"=="3" (
    echo.
    echo 🚀 Iniciando Versão Web...
    echo 🌐 Abrindo servidor local...
    echo.
    echo ├─ Servidor: http://localhost:8000
    echo ├─ Demo Online: https://hikdobrazil.github.io/ERP-CLI-GUI-WEB/
    echo └─ Pressione Ctrl+C para parar o servidor
    echo.
    cd web
    python -m http.server 8000
    cd ..
) else if "%choice%"=="0" (
    echo.
    echo 👋 Obrigado por usar o Sistema ERP!
    echo.
    exit /b 0
) else (
    echo.
    echo ❌ Opção inválida! Tente novamente.
    echo.
    pause
    goto :start
)

echo.
pause
