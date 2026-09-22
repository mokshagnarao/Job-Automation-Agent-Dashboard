import streamlit as st
import pandas as pd

# Step 1: Load application history
data = pd.read_csv("applications.csv")

# Step 2: Title
st.title("Job Automation Agent Dashboard")

# Step 3: Show raw data
st.write("### Applications Overview")
st.dataframe(data)

# Step 4: Summary stats
st.write("### Summary")
st.write("Total Applications:", len(data))
st.write("Unique Companies Applied:", data['Company'].nunique())

# Step 5: Applications by Status
st.write("### Applications by Status")
status_counts = data['Status'].value_counts()
st.bar_chart(status_counts)

# Step 6: Applications by Company
st.write("### Applications by Company")
company_counts = data['Company'].value_counts()
st.bar_chart(company_counts)

csv = filtered_data.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='filtered_results.csv',
    mime='text/csv',
)
