@echo off
echo ====================================
echo   Grae-X AlgoScope v2.1
echo   SEO Command Center
echo ====================================
echo.

set PYTHONWARNINGS=ignore
set STREAMLIT_LOGGING_LEVEL=error
python -m streamlit run web_app.py --server.port=8501 --logger.level=error

pause