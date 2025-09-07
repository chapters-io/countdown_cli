@echo off

REM call :doit num tag
call :doit 1 0

echo "delete emails 5"
pause

:doit
call python countdown.py %~1 %~2
call cat todo.txt -l
