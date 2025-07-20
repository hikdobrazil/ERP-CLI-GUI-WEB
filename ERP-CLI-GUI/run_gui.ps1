# Sistema ERP - Launcher GUI PowerShell
Write-Host "===========================================" -ForegroundColor Cyan
Write-Host "      SISTEMA ERP - VERSAO GUI" -ForegroundColor Yellow  
Write-Host "===========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Iniciando interface grafica..." -ForegroundColor Green
Write-Host ""

try {
    python gui_main.py
} catch {
    Write-Host "Erro ao executar o sistema: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "Verifique se o Python está instalado e no PATH." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Sistema encerrado." -ForegroundColor Blue
Read-Host "Pressione Enter para continuar..."
