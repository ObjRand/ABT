@echo off
for /L %%i in (1,1,50) do ( echo %time% )>nul
start set_bg_gui.py
exit