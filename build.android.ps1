# powershell ./build.android.ps1
Remove-Item .\dist -Recurse -Force
flet build apk
Remove-Item .\build -Recurse -Force
Remove-Item .\main.spec
