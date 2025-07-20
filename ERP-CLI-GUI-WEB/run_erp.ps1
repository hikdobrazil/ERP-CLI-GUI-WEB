# ERP System PowerShell Launcher
$Host.UI.RawUI.WindowTitle = "Sistema ERP Empresarial"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

try {
    python main.py
} catch {
    Write-Host "Erro ao executar o sistema: $_" -ForegroundColor Red
}

Write-Host "Pressione qualquer tecla para continuar..." -ForegroundColor Yellow
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
