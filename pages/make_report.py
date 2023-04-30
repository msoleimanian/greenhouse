import streamlit as st
import pandas as pd
import plotly.express as px

options = st.sidebar.radio('Sections' , options=('Summary Of all pots' , 'Create Trend Base on PotID', 'Best Performance' ))


st.title(" IMPORT YOUR DATA ")
st.text("Please enter your dataset.")

def divider(dataframe , div):
    rep = []
    for data in dataframe[div]:
        if data in rep:
            continue
        else:
            rep.append(data)
    return rep

def SummaryReportDataframeForEC(dataframe , div , rep):
    st.header("Summary Form All Pots")
    for sub in rep:
        subdataframe = dataframe.query(f'PotID == {sub}')
        headers = subdataframe.columns
        st.text(f"Pot ID : {sub}")
        st.text("EC")
        print(headers)
        col1 , col2, col3 = st.columns(3)
        col1.line_chart(subdataframe, x='Timestamp', y='Initial EC')
        col2.line_chart(subdataframe, x='Timestamp', y='Final EC')
        col3.line_chart(subdataframe, x='Timestamp', y='EC Setting')

        #for head in headers:
        #    st.line_chart(dataframe, x='Timestamp', y=head)

def SummaryReportDataframeForPH(dataframe , div , rep):
    st.header("Summary Form All Pots")
    for sub in rep:
        subdataframe = dataframe.query(f'PotID == {sub}')
        headers = subdataframe.columns
        st.text(f"Pot ID : {sub}")
        st.text("PH")
        print(headers)
        col1 , col2= st.columns(2)
        col1.line_chart(subdataframe, x='Timestamp', y='Initial pH')
        col2.line_chart(subdataframe, x='Timestamp', y='Initial pH')


def SummaryReportDataframeForTemperature(dataframe, div, rep):
    st.header("Summary Form All Pots")
    for sub in rep:
        subdataframe = dataframe.query(f'PotID == {sub}')
        headers = subdataframe.columns
        st.text(f"Pot ID : {sub}")
        st.text("Temperature")
        print(headers)
        col1, col2 = st.columns(2)
        col1.line_chart(subdataframe, x='Timestamp', y='Temperature (Day)')


def SummaryReportDataframeForLeavesCount(dataframe, div, rep):
    st.header("Summary Form All Pots")
    for sub in rep:
        subdataframe = dataframe.query(f'PotID == {sub}')
        headers = subdataframe.columns
        st.text(f"Pot ID : {sub}")
        st.text("Leaves Count")
        print(headers)
        col1, col2 = st.columns(2)
        col1.line_chart(subdataframe, x='Timestamp', y='Leaves Count')



def SummaryBestPots(dataframe , div ,rep):
    st.header("Summary Of Best Pots")
    headers = dataframe.columns
    headers = headers[5:]
    print(headers)
    for head in headers:
        bestvalue = 0
        bestPot = ''
        bestFrame = ''
        for sub in rep:
            subdataframe = dataframe.query(f'Pot ID == "{sub}"')
            print(subdataframe)
            print(head)
            print(subdataframe[head])
            for val in subdataframe[head]:
                print("afjlsdashfosiahfasdpasl[dpkasd")
                print(type(val))
                if val > bestvalue:
                    bestPot = sub
                    bestvalue = val
                    bestFrame = subdataframe
        print("afjlsdashfosiahfasdpasl[dpkasdasdsa")
        print(bestvalue)
        st.text(f'Growth Metric : {head}')
        st.text(f'BestPot : {bestPot}')
        st.line_chart(bestFrame , x='Time Stamp', y=head)


uploadFile = st.file_uploader("Upload your file here")
if uploadFile:
    st.text("The file successfully is uploaded")
    dataframe = pd.read_csv(uploadFile)

    print(divider(dataframe , 'PotID'))

    if options == 'Summary Of all pots':
        radioOption = st.radio(
            "What trend do you need",
            ('EC', 'PH', 'Temperature' , 'leaves count'))
        if radioOption == 'EC':
            SummaryReportDataframeForEC(dataframe , 'PotID', divider(dataframe , 'PotID'))
        if radioOption == 'PH':
            SummaryReportDataframeForPH(dataframe, 'PotID', divider(dataframe, 'PotID'))
        if radioOption == 'Temperature':
            SummaryReportDataframeForTemperature(dataframe, 'PotID', divider(dataframe, 'PotID'))
        if radioOption == 'leaves count':
            SummaryReportDataframeForLeavesCount(dataframe, 'PotID', divider(dataframe, 'PotID'))

    if options == 'Create Trend Base on PotID':
        PotidCol , CropIdCol = st.columns(2)
        PotID = PotidCol.selectbox('Select Your Pot ID' , divider(dataframe, 'PotID'))
        subdataframe = dataframe.query(f'PotID == {PotID}')
        if PotID:
            CropIdCol.selectbox('Select Your Crop ID' , divider(subdataframe, 'Crop ID'))
            st.header('EC')
            ECSCol, ECICol, ECFCol = st.columns(3)
            ECSCol.line_chart(dataframe, x='Timestamp', y='EC Setting')
            ECICol.line_chart(dataframe, x='Timestamp', y='Initial EC')
            ECFCol.line_chart(dataframe, x='Timestamp', y='Final EC')

            st.header('PH')
            PHICol, PHFCol = st.columns(2)
            PHICol.line_chart(dataframe, x='Timestamp', y='Initial pH')
            PHFCol.line_chart(dataframe, x='Timestamp', y='Final pH')

            st.header('Temperature')
            st.line_chart(dataframe, x='Timestamp', y='Temperature (Day)')

            st.header('Leaves Count')
            st.line_chart(dataframe, x='Timestamp', y='Leaves Count')

    if options == 'Best Performance':
        SummaryBestPots(dataframe , divider(dataframe , 'PotID'))






