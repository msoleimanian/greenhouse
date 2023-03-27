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
        time = st.selectbox('Select the type of the time stamp', options=dataframe.columns)
        metric = st.selectbox('Growth metric', options=dataframe.columns)
        baseCloumn = st.selectbox('Base', options=dataframe.columns)

        newdataframe = dataframe[[time,baseCloumn,metric]]
#        st.line_chart(newdataframe , x=newdataframe[time], y=newdataframe[metric])
        dictData = newdataframe.to_dict()
        print("MOhsbaESSAojaSJojasd")
#        print(dictData)
        print("#############################################################")
        dictm = []
        tempvlaue = []
        for key in dictData[baseCloumn]:
            print('KEY')
            print(key)
            if dictData[baseCloumn][key] in tempvlaue:
                print('dictData[baseCloumn][key]')
                print(dictData[baseCloumn][key])
                for data in dictm:
                    print('DATA')
                    print(data)
                    for im , value in data.items():
                        print(im)
                        print(dictData[baseCloumn][key])
                        if im == dictData[baseCloumn][key]:
                            print('MOASHSAR')
                            data[dictData[baseCloumn][key]].append(dictData[metric][key])
                continue
            tempvlaue.append(dictData[baseCloumn][key])
            temparry = []
            temparry.append(dictData[metric][key])
            print(dictData[metric][key])
            temp1 = {dictData[baseCloumn][key] : []}
            temp1[dictData[baseCloumn][key]].append(dictData[metric][key])
            dictm.append(temp1)
        print(dictm)

        finalDataframe = pd.DataFrame()
        for data in dictm:
            for key , val in data.items():
                print(val)
                finalDataframe.insert(0, key , val)
        print(finalDataframe)

        #timestamp
        tempdf = dataframe[time]
        timedict = tempdf.to_dict()
        print(timedict)
        timear = []
        for key , val in timedict.items():
            if val in timear:
                continue
            timear.append(val)
        finalDataframe.insert(0, time, timear)
        print(finalDataframe)
        st.write(finalDataframe)
        st.line_chart(finalDataframe , x='timestamp')



        dictDataplus = pd.DataFrame()
        for data in dictData:
#            print(data)
            temp = []
            for row in dictData[data]:
 #               print(dictData[data][row])
                if dictData[data][row] == baseCloumn:
                    dictDataplus.insert(0, dictData[data][row] , [])
                    if dictData[data][row] in temp:
                        continue
                if dictData[data][row] in temp:
                    continue
                temp.append(dictData[data][row])
#            dictDataplus.insert(0,data,temp)
#            print(dictDataplus)

if options == 'Create output':
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



