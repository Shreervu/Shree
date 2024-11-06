﻿#Edit the 8th to 12th line code before upload to gihub
# Import necessary libraries
import streamlit as st
import seaborn as sns
import plotly.express as px
import pandas as pd


# --- Title and Introduction ---
st.title("Interactive Visualizations with Plotly and Streamlit")


# --- Input for Author Information ---
st.sidebar.header("Visualization skill workshop - Plotly")
name = st.sidebar.text_input("Shree S. Yadav")
usn = st.sidebar.text_input("34")
instructor_name = st.sidebar.text_input("Prof. Ashwini Mathur _ SOCSE")


# --- Load Dataset ---
tips = sns.load_dataset('tips')  # Loading the tips dataset


# Display the first few rows of the dataset
st.write("## Dataset Overview")
st.write(tips.head())


# --- Task 1: Interactive Bar Chart ---
st.subheader("Task 2: Bar Chart - Average Tip by Day")
# Bar Chart: Average Tip by Day with color for each day
fig2 = px.bar(
    tips, x='day', y='tip', color='day',
    title='Average Tip by Day',
    labels={'tip': 'Average Tip ($)', 'day': 'Day of the Week'},
    template='plotly_white'
)
st.plotly_chart(fig2)  # Display the chart in Streamlit

# --- Task 2: Interactive Scatter Chart ---
st.subheader("Task 2: Scatter Chart - Total Bill vs Tip (Colored by Gender)")
fig3 = px.scatter(
    tips , x='total_bill', y='tip', color='sex',
    title='Total Bill vs Tip (Colored by Gender)',
    labels = {'total_bill':'Total Bill($)', 'tip': 'Tip($)'},
    template='plotly_dark', 
    size='size'
)
st.plotly_chart(fig3)  