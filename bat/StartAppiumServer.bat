
@echo off  

ping -n 2 127.0>nul
echo StartAppiumServer01...
cd %~dp0
start "" "StartAppiumServer01.bat"

ping -n 2 127.0>nul
echo StartAppiumServer02...
cd %~dp0
start "" "StartAppiumServer02.bat"

ping -n 2 127.0>nul    
echo AppiumServerÆô¶¯Íê±Ï...

ping -n 2 127.0>nul 
exit