#!/bin/bash
# Find the main python file with streamlit
MAIN_FILE=""
for file in $(find . -name "*.py" -type f); do
    if grep -q "streamlit run\|import streamlit as st\|from streamlit import" "$file" 2>/dev/null; then
        if [[ "$file" != "./test_app.py" && "$file" != "./run_streamlit.py" && "$file" != "./run_without_warnings.sh" ]]; then
            MAIN_FILE="$file"
            break
        fi
    fi
done

if [ -z "$MAIN_FILE" ]; then
    echo "Could not find main Streamlit app. Please specify:"
    echo "Enter your app filename (e.g., app.py, main.py): "
    read MAIN_FILE
fi

echo "Running $MAIN_FILE without warnings..."
PYTHONWARNINGS="ignore" streamlit run "$MAIN_FILE" --logger.level=error
