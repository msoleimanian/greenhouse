import streamlit as st
import pandas as pd
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

    #   Filter the Data
 #   dataframe = dataframe.applymap(str)
    st.header('Filtering Data')
    st.text("Select the column you want to define for this constraint")
    #   select option
    option = st.selectbox('Select the column', options=dataframe.columns)
    print(option)

#   cloumn name form text input
    input = st.text_input(option)
    if input:
        newdf = dataframe.query(f"{option} == {input} ")
#    newdf = dataframe[(dataframe[option] == tempin)]
        st.write(newdf)

#   CREATE PLOT
    x_axis_val = st.selectbox('Select X-Axis Value', options=dataframe.columns)
    y_axis_val = st.selectbox('Select Y-Axis Value', options=dataframe.columns)
    plot = px.scatter(dataframe, x=x_axis_val, y=y_axis_val)
    st.line_chart(newdf , x=x_axis_val, y=y_axis_val)
    st.plotly_chart(plot)

