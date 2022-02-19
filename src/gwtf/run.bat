@echo off
echo Set-ExecutionPolicy RemoteSigned -Scope CurrentUser | powershell.exe

PowerShell.exe -ExecutionPolicy Unrestricted -command "%cd%\gwtf.ps1" 

REM REMOVE EXECUTION POLICY !!! # ALSO WRITE Set-ExecutionPolicy RemoteSigned -Scope CurrentUser IN POWERSHELL TO GO BACK TO RUNNING PS1 FILES!!
echo Set-ExecutionPolicy -ExecutionPolicy Undefined -Scope CurrentUse | powershell.exe

exit

