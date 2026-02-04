#!/bin/bash
# Suppress specific warnings
export PYTHONWARNINGS="ignore:missing ScriptRunContext"

# Find and run the main streamlit app
MAIN_APP=$(find . -name "*.py" -type f -exec grep -l "streamlit run\|import streamlit as st" {} \; | head -1)

if [ -n "$MAIN_APP" ]; then
    echo "Running: $MAIN_APP"
    streamlit run "$MAIN_APP"
else
    echo "No Streamlit app found. Please specify your app file:"
    echo "streamlit run app.py"
fi
