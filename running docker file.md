## 1. Prerequisites (Windows 10/11 with WSL2)
1. turn on WSL2 + restartēt
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
wsl --install -d Ubuntu

2. Docker Desktop installation

On first launch: Settings → General → Enable “Use the WSL 2 based engine.”

Settings → Resources → WSL integration → Enable integration with Ubuntu.

(Optional) File Sharing: add D:\ — sometimes works, but the WSL home-folder path is more reliable.
