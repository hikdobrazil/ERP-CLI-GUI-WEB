@echo off
title Sistema ERP Empresarial - Launcher
chcp 65001 > nul
color 0B

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║                    SISTEMA ERP EMPRESARIAL                     ║
echo ║                        Versão 1.1a                           ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.
echo Escolha uma opção:
echo.
echo [1] Executar Sistema ERP
echo [2] Gerar Dados de Demonstração  
echo [3] Ver Arquivos de Configuração
echo [4] Verificar Requisitos
echo [0] Sair
echo.
set /p choice="Digite sua escolha (0-4): "

if "%choice%"=="1" goto run_erp
if "%choice%"=="2" goto demo_data
if "%choice%"=="3" goto show_config
if "%choice%"=="4" goto check_requirements
if "%choice%"=="0" goto exit
goto invalid

:run_erp
echo.
echo Iniciando Sistema ERP...
python main.py
goto end

:demo_data
echo.
echo Gerando dados de demonstração...
python demo_generator.py
echo.
pause
goto menu

:show_config
echo.
echo Arquivos de configuração:
echo ========================
if exist config.json (
    echo ✓ config.json encontrado
) else (
    echo ✗ config.json não encontrado
)
if exist erp_data.json (
    echo ✓ erp_data.json encontrado
) else (
    echo ✗ erp_data.json não encontrado
)
if exist demo_data.json (
    echo ✓ demo_data.json encontrado
) else (
    echo ✗ demo_data.json não encontrado
)
echo.
pause
goto menu

:check_requirements
echo.
echo Verificando requisitos...
echo =========================
python --version 2>nul
if errorlevel 1 (
    echo ✗ Python não está instalado ou não está no PATH
) else (
    echo ✓ Python está instalado
)
echo.
pause
goto menu

:invalid
echo.
echo ❌ Opção inválida! Tente novamente.
echo.
pause
goto menu

:menu
cls
goto :eof

:exit
echo.
echo Encerrando...
exit /b 0

:end
pause
