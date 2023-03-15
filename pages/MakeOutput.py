import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px



st.title("Create Out put")
st.text("This is a section that you can upload your CSV file here ")

uploadFile = st.file_uploader("Upload your file here")
if uploadFile:
    st.text("The file successfully is uploaded")
    dataframe = pd.read_csv(uploadFile)
#   SHOW DATA
    st.header('Data Statistics')
    st.write(dataframe)
#   Select and filter data
    inputs = []
    for c in dataframe.columns:
        inputs.append(st.text_input('Input your range:'))

#   CREATE PLOT
    x_axis_val = st.selectbox('Select X-Axis Value', options=dataframe.columns)
    y_axis_val = st.selectbox('Select Y-Axis Value', options=dataframe.columns)
    plot = px.scatter(dataframe, x=x_axis_val, y=y_axis_val)
    st.plotly_chart(plot)

