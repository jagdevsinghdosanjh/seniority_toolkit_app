import streamlit as st
import pandas as pd

def display_results(results):
    df = pd.DataFrame(results)
    st.subheader("🔍 Comparison Results")
    st.dataframe(df.style.applymap(highlight_match, subset=["matched"]))

def highlight_match(val):
    if val is True:
        return "background-color: #d4edda"
    elif val is False:
        return "background-color: #f8d7da"
    return ""
