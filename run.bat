@echo off
cd /d "D:\PythonSelenium\PythonSeleniumFramework"

pytest -s -v -m  "sanity" --html=./Reports/report.html testcases/ --browser chrome
REM pytest -s -v -m "sanity or regression" --html=./Reports/report.html testcases/ --browser chrome

REM pytest -s -v -m "sanity and regression" --html=./Reports/report.html testcases/ --browser chrome

REM pytest -s -v -m  "regression" --html=./Reports/report.html testcases/ --browser chrome

