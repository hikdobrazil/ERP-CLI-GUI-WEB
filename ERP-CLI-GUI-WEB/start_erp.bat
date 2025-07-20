@echo off
chcp 65001 >nul
color 0B
cls

echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                      SISTEMA ERP v2.0                       ║
echo ║                 Enterprise Resource Planning                 ║
echo ╠══════════════════════════════════════════════════════════════╣
echo ║                                                              ║
echo ║  Escolha a versão do sistema que deseja executar:           ║
echo ║                                                              ║
echo ║  [1] 📱 Versão CLI (Terminal/Console)                       ║
echo ║      • Interface clássica baseada em texto                  ║
echo ║      • Navegação por setas e teclas                         ║
echo ║      • Suporte a mouse simulado                             ║
echo ║      • Compatível com qualquer terminal                     ║
echo ║                                                              ║
echo ║  [2] 🖥️  Versão GUI (Interface Gráfica)                     ║
echo ║      • Interface moderna e profissional                     ║
echo ║      • Formulários intuitivos                               ║
echo ║      • Tabelas dinâmicas                                    ║
echo ║      • Base de dados SQLite                                 ║
echo ║                                                              ║
echo ║  [0] ❌ Sair                                                 ║
echo ║                                                              ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

:menu
set /p choice="Digite sua opcao (1, 2 ou 0): "

if "%choice%"=="1" goto cli
if "%choice%"=="2" goto gui
if "%choice%"=="0" goto exit
echo Opcao invalida! Tente novamente.
goto menu

:cli
echo.
echo ==========================================
echo      INICIANDO VERSAO CLI
echo ==========================================
echo.
python main.py
goto end

:gui
echo.
echo ==========================================
echo      INICIANDO VERSAO GUI
echo ==========================================
echo.
python gui_main.py
goto end

:exit
echo.
echo Saindo do sistema...
goto end

:end
echo.
echo Sistema encerrado.
pause
