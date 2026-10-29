@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo.
echo  이규영 포트폴리오 — 로컬 미리보기
echo  http://localhost:8080
echo  (창을 닫으면 서버가 종료됩니다)
echo.
start "" http://localhost:8080/
python -m http.server 8080 --directory .
pause
