import streamlit as st
import pandas as pd

# Sidebar menu
st.title("Automation Project: UA + QA Dashboards")
choice = st.sidebar.selectbox("Choose Dashboard", ["UA Dashboard", "QA Dashboard"])

if choice == "UA Dashboard":
    st.header("UA Dashboard - Job Agent Applications")
    data = pd.read_csv("applications.csv")
    st.dataframe(data)
    st.bar_chart(data['Status'].value_counts())

elif choice == "QA Dashboard":
    st.header("QA Dashboard - Test Results")
    data = pd.read_csv("qa_results.csv")
    st.dataframe(data)
    st.bar_chart(data['Result'].value_counts())
