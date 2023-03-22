import streamlit as st
import pandas as pd
import plotly.express as px
import random
import json


def DataStream():
    return random.rand()


st.title("Manitoring the Greenhouse")
st.text("Maitoring")

st.sidebar.title("Navigation")
options = st.sidebar.radio('Sections' , options=('Growth' , 'Soil Sensors', 'Watching the Greenhouse' , 'Create output'))

if options == 'Growth':
    uploadFile = st.file_uploader("Upload your file here")
    if uploadFile:
        dataframe = pd.read_csv(uploadFile)
        st.write(dataframe)
        # Query for select and filter data
        input = st.text_input('''Write your query. For example : {"Cloumn_Name1 " : "value" , "Cloumn_Name2" : "value"} ''')
        print(input)
        if input:
            inputs = json.loads(input)
            query = f""
            control = 0
            for key in inputs:
                q = f"{key} == {inputs[key]}"
                dataframe = dataframe.query(q)
            st.write(dataframe)

            x_axis_val = st.selectbox('Select X-Axis Value', options=dataframe.columns)
            y_axis_val = st.selectbox('Select Y-Axis Value', options=dataframe.columns)
            st.line_chart(dataframe, x=x_axis_val, y=y_axis_val)



