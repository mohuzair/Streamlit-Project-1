import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
import plotly.express as px

diabetes = load_diabetes()
df = pd.DataFrame(diabetes.data , columns=diabetes.feature_names)

st.title("Basic Visualizations on Diabetes Dataset")
st.header("By Mohammed Uzair")
st.markdown("Data Science Intern at Innomatics Resaerch Labs")
st.header("The Data Frame")
st.dataframe(df)
st.header('This is a line chart by streamlit')
st.line_chart(df)

st.header("Histogram on age")
fig_1 = px.histogram(df['age'], x="age")
st.plotly_chart(fig_1)

st.header("Histogram on bmi")
fig_1 = px.histogram(df['bmi'], x="bmi")
st.plotly_chart(fig_1)

st.header("Histogram on bp")
fig_1 = px.histogram(df['bp'], x="bp")
st.plotly_chart(fig_1)

st.header("Boxplot on BP")
fig_2 = px.box(df['bp'], y="bp")
st.plotly_chart(fig_2)