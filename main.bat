@echo off
mode 100, 35
title All WebHook Alerters - ToonMares
chcp 65001 >nul
cd Files
:start
echo.
echo.
echo =============================== ToonMares's Multi-Tool ===============================
echo [91m               ██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗ [0m
echo [91m               ██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝ [0m
echo [95m               ██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝  [0m
echo [35m               ██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗  [0m 
echo [35m               ╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗ [0m
echo =====================================================================================
echo.
echo 1. [Alert with l. s.h.]
echo 2. [Complex Alert]
echo 3. [Simple alert]
echo 4. [Simple Alert (while true)]
echo 5. [Spammer (manual)]
echo 6. [Key-Logger]
echo =====================================================================================
echo.

set /p choice=Enter your choice (1-6): 
if "%choice%"=="1" start main1.py
if "%choice%"=="2" start main2.py
if "%choice%"=="3" start main3.py
if "%choice%"=="4" start main4.py
if "%choice%"=="5" start wrapper.bat
if "%choice%"=="6" start wrapper1.bat
goto :start
