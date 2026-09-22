import streamlit as st
import pandas as pd

# Step 1: Load QA results
data = pd.read_csv("qa_results.csv")

# Step 2: Title
st.title("QA Agent Dashboard")

# Step 3: Show raw data
st.write("### Test Results Overview")
st.dataframe(data)

# Step 4: Summary stats
st.write("### Summary")
st.write("Total Tests Run:", len(data))
st.write("Tests Passed:", (data['Result'] == 'Pass').sum())
st.write("Tests Failed:", (data['Result'] == 'Fail').sum())

# Step 5: Pass/Fail chart
st.write("### Pass vs Fail")
status_counts = data['Result'].value_counts()
st.bar_chart(status_counts)

# Step 6: Trend over time
st.write("### Test Results Over Time")
data['Timestamp'] = pd.to_datetime(data['Timestamp'])
trend = data.groupby([data['Timestamp'].dt.date, 'Result']).size().unstack(fill_value=0)
st.line_chart(trend)

csv = filtered_data.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='filtered_results.csv',
    mime='text/csv',
)
