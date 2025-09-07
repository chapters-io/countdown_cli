@echo off
call py countdown.py %1 T
cls
call cat todo.txt -l
