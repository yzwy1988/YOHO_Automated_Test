
@echo off  

ping -n 2 127.0>nul
echo **********************************
echo 启动AppiumServer...
echo StartAppiumServer 172.16.6.166:4723...
cd %~dp0
start "" "StartAppiumServer01.bat"

ping -n 2 127.0>nul
echo StartAppiumServer 172.16.6.166:4725...
cd %~dp0
start "" "StartAppiumServer02.bat"

ping -n 2 127.0>nul    
echo AppiumServer启动完成...
echo **********************************

ping -n 2 127.0>nul 
exit