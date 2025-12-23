@echo off
echo WeLearnAuto 依赖验证工具
echo ==========================
echo 此工具将检查打包的应用程序是否包含所有必要的依赖
echo.
echo 按任意键开始验证...
pause > nul

verify_dependencies.exe

echo.
echo 验证完成！
pause