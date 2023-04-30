import numpy as np
import streamlit as st
import pandas as pd

options = st.sidebar.radio('Sections',
                           options=('Summary Of all pots', 'Create Trend Base on PotID', 'Best Performance'))


def divider(dataframe, div):
    rep = []
    for data in dataframe[div]:
        if data in rep:
            continue
        else:
            rep.append(data)
    return rep


def SummaryReportDataframeForEC(dataframe, div, rep):
    st.header("Summary Form All Pots")
    for sub in rep:
        subdataframe = dataframe.query(f'PotID == {sub}')
        headers = subdataframe.columns
        st.text(f"Pot ID : {sub}")
        st.text("EC")
        print(headers)
        col1, col2, col3 = st.columns(3)
        col1.line_chart(subdataframe, x='Timestamp', y='Initial EC')
        col2.line_chart(subdataframe, x='Timestamp', y='Final EC')
        col3.line_chart(subdataframe, x='Timestamp', y='EC Setting')


def SummaryReportDataframeForPH(dataframe, div, rep):
    st.header("Summary Form All Pots")
    for sub in rep:
        subdataframe = dataframe.query(f'PotID == {sub}')
        headers = subdataframe.columns
        st.text(f"Pot ID : {sub}")
        st.text("PH")
        print(headers)
        col1, col2 = st.columns(2)
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
        col1.line_chart(subdataframe, x='Timestamp', y='Temperature')


def SummaryBestPots(dataframe, div, rep):
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
        st.line_chart(bestFrame, x='Time Stamp', y=head)


def printTitle():
    return """
    <div class="jumbotron">
    <h1>Make your Report</h1>
    <p>In this section you can upload your file here and get a summary of your greenhouse</p>
    </div>
    <div class="container">
    </div>
    """

def costumPrintTitle(title):
    return f"""
    <div class="jumbotron">
    <h4>{title}</h4>
    </div>
    <div class="container">
    </div>
    """


def printCostumTitle(title, context):
    return f"""
        <div class="jumbotron">
        <h3>{title}</h3>
        <p>{context}</p>
        </div>
        <div class="container">
        </div>
        """


def printCostumTitleH2(title, context):
    return f"""
        <div class="jumbotron">
        <h1>{title}</h1>
        <p>{context}</p>
        </div>
        <div class="container">
        </div>
        """


def printText(input):
    return f"""
        <div class="jumbotron">
        <p>{input}</p>
        </div>
        <div class="container">
        </div>
        """


def uploadFile():
    return """
    <label class="form-label" for="customFile">Default file input example</label>
    <input type="file" class="form-control" id="customFile" />
    """


def tableGenerator3(data):

    effectiveMetrics = ['Final EC' , 'Final pH' , 'MoistContent' , 'Temperature'  , 'WaterSaturation']


    table = """"""
    print("moasdjasd")
    for metric in effectiveMetrics:
        print(metric)
        state = ''
        if True :
            state = 'Excellent'

        else :
            state = 'good'
        databody = f"""<tr>
                <td>{metric}</td>
                <td>{data[metric][0]}</td>
                <td>{data[metric][1]}</td>
                <td>{state}</td>
            </tr>"""
        table = table + databody

    print(table)

    return f"""
        <div class="container">
      <h2>Analyze</h2>
      <p>In the table below, the pots with the best apparent growth metrics such as height, number of leaves, etc. are shown.</p>            
      <table class="table table-hover">
        <thead>
          <tr>
            <th>Effective Metric</th>
            <th>Ideal</th>
            <th>Pot</th>
            <th>The state of the pot</th>
          </tr>
        </thead>
        <tbody>
          {table}
        </tbody>
      </table>
    </div>"""

def tableGenerator2(data):

    effectiveMetrics = ['Height', 'Width', 'Leaves Count', 'Longest Leaf', 'Shortest Leaf' ]


    table = """"""
    print("moasdjasd")
    for metric in effectiveMetrics:
        print(metric)
        state = ''
        if data[metric][2] < 0 :
            state = 'Excellent'

        else :
            state = 'good'
        databody = f"""<tr>
                <td>{metric}</td>
                <td>{data[metric][0]}</td>
                <td>{data[metric][1]}</td>
                <td>{state}</td>
            </tr>"""
        table = table + databody

    print(table)

    return f"""
        <div class="container">
      <h2>Analyze</h2>
      <p>In the table below, the pots with the best apparent growth metrics such as height, number of leaves, etc. are shown.</p>            
      <table class="table table-hover">
        <thead>
          <tr>
            <th>Growth Metric</th>
            <th>Ideal</th>
            <th>Pot</th>
            <th>The state of the pot</th>
          </tr>
        </thead>
        <tbody>
          {table}
        </tbody>
      </table>
    </div>"""



def tableGenerator(data):

    growthMetrics = ['Height', 'Width', 'Leaves Count', 'Longest Leaf', 'Shortest Leaf', 'Yield per Plant',
                     'Yield per Land']
    table = """"""
    print("moasdjasd")
    for metric in growthMetrics:
        print(metric)
        databody = f"""<tr>
            <td>{metric}</td>
            <td>{data[metric][0]}</td>
            <td>{data[metric][1]}</td>
            <td>{data[metric][2]}</td>
            <td>{data[metric][3]}</td>
            <td>{data[metric][4]}</td>
        </tr>"""
        table = table + databody

    print(table)

    return f"""
    <div class="container">
  <h2>Performance</h2>
  <p>In the table below, the pots with the best apparent growth metrics such as height, number of leaves, etc. are shown.</p>            
  <table class="table table-hover">
    <thead>
      <tr>
        <th>Growth Metric</th>
        <th>Average in all pots</th>
        <th>Best Value</th>
        <th>Best Pot</th>
        <th>Worst Value</th>
        <th>Worst Pot</th>
      </tr>
    </thead>
    <tbody>
      {table}
    </tbody>
  </table>
</div>"""

def SummaryBestPots(dataframe, div, rep):
    st.markdown(printCostumTitle('Show the Best Pots in Growth Metrics',
                                 'The graphs below show the best pots with the best growth metrics such as height, number of leaves, etc.'),
                unsafe_allow_html=True)
    headers = dataframe.columns
    headers = headers[13:16]
    print(headers)
    for head in headers:
        bestvalue = 0
        bestPot = ''
        bestFrame = ''
        for sub in rep:
            subdataframe = dataframe.query(f'PotID == "{sub}"')
            print(subdataframe)
            print(head)
            print(subdataframe[head])
            for val in subdataframe[head]:
                print("afjlsdashfosiahfasdpasl[dpkasd")
                print(type(val))
                if 'cm' in str(val):
                    print('True')
                    val = val.replace('cm', '')
                print(val)
                if int(val) > int(bestvalue):
                    bestPot = sub
                    bestvalue = val
                    bestFrame = subdataframe
        print("afjlsdashfosiahfasdpasl[dpkasdasdsa")
        print(bestvalue)
        # col4 , col5 = st.columns(2)
        st.markdown(printCostumTitleH2(f'Growth Metric : {head}', f'BestPot : {bestPot}'), unsafe_allow_html=True)
        # col5.markdown(printCostumTitleH2(f'Growth Metric : {head}' , f'BestPot : {bestPot}' ))
        st.line_chart(bestFrame, x='Timestamp', y=head)
        # col5.line_chart(bestFrame , x='Timestamp', y=head)


st.markdown(printTitle(), unsafe_allow_html=True)
uploadFile = st.file_uploader("Upload your file here")


def showDifferentBestWorst(dataframe, potidBest, potidWorst):
    dataframeBest = dataframe.query(f'PotID == "{potidBest}"')
    dataframeWorst = dataframe.query(f'PotID == "{potidWorst}"')
    timstamp = dataframeBest['Timestamp'].values
    print(timstamp)

    # PH
    Bestval = dataframeBest['Final pH'].values
    Worstval = dataframeWorst['Final pH'].values
    # df = pd.DataFrame([timstamp,Bestval,Worstval], columns=['Timestamp', 'PotID7' , 'PotID4'])
    data = {'Timestamp': timstamp,
            'PotID1': Bestval,
            'PotID2': Worstval}
    df = pd.DataFrame(data)
    print(df)
    st.line_chart(df, x='Timestamp')

    # EC
    Bestval = dataframeBest['Final EC'].values
    Worstval = dataframeWorst['Final EC'].values
    # df = pd.DataFrame([timstamp,Bestval,Worstval], columns=['Timestamp', 'PotID7' , 'PotID4'])
    data = {'Timestamp': timstamp,
            'PotID1': Bestval,
            'PotID2': Worstval}
    df = pd.DataFrame(data)
    print(df)
    st.line_chart(df, x='Timestamp')

    # MoistContent
    Bestval = dataframeBest['MoistContent'].values
    Worstval = dataframeWorst['MoistContent'].values
    # df = pd.DataFrame([timstamp,Bestval,Worstval], columns=['Timestamp', 'PotID7' , 'PotID4'])
    data = {'Timestamp': timstamp,
            'PotID1': Bestval,
            'PotID2': Worstval}
    df = pd.DataFrame(data)
    print(df)
    st.line_chart(df, x='Timestamp')

    # Temperature (Day)
    Bestval = dataframeBest['Temperature'].values
    Worstval = dataframeWorst['Temperature'].values
    # df = pd.DataFrame([timstamp,Bestval,Worstval], columns=['Timestamp', 'PotID7' , 'PotID4'])
    data = {'Timestamp': timstamp,
            'PotID1': Bestval,
            'PotID2': Worstval}
    df = pd.DataFrame(data)
    print(df)
    st.line_chart(df, x='Timestamp')

    # Water Saturation
    Bestval = dataframeBest['WaterSaturation'].values
    Worstval = dataframeWorst['WaterSaturation'].values
    # df = pd.DataFrame([timstamp,Bestval,Worstval], columns=['Timestamp', 'PotID7' , 'PotID4'])
    data = {'Timestamp': timstamp,
            'PotID1': Bestval,
            'PotID2': Worstval}
    df = pd.DataFrame(data)
    print(df)
    st.line_chart(df, x='Timestamp')


def findBestPot(dataframe):
    growthMetrics = ['Height', 'Width', 'Leaves Count', 'Longest Leaf', 'Shortest Leaf', 'Yield per Plant',
                     'Yield per Land']
    data = {}
    for metric in growthMetrics:
        print(metric)
        bestVal = 0
        bestPot = 0

        worstVal = 1000
        worstPot = 0

        if dataframe[metric].iloc[-1] > bestVal:
            bestVal = dataframe[metric].iloc[-1]
            bestPot = 10
        if dataframe[metric].iloc[-11] > bestVal:
            bestVal = dataframe[metric].iloc[-11]
            bestPot = 9
        if dataframe[metric].iloc[-21] > bestVal:
            bestVal = dataframe[metric].iloc[-21]
            bestPot = 8
        if dataframe[metric].iloc[-31] > bestVal:
            bestVal = dataframe[metric].iloc[-31]
            bestPot = 7
        if dataframe[metric].iloc[-41] > bestVal:
            bestVal = dataframe[metric].iloc[-41]
            bestPot = 6
        if dataframe[metric].iloc[-51] > bestVal:
            bestVal = dataframe[metric].iloc[-51]
            bestPot = 5
        if dataframe[metric].iloc[-61] > bestVal:
            bestVal = dataframe[metric].iloc[-61]
            bestPot = 4
        if dataframe[metric].iloc[-71] > bestVal:
            bestVal = dataframe[metric].iloc[-71]
            bestPot = 3
        if dataframe[metric].iloc[-81] > bestVal:
            bestVal = dataframe[metric].iloc[-81]
            bestPot = 2
        if dataframe[metric].iloc[-91] > bestVal:
            bestVal = dataframe[metric].iloc[-91]
            bestPot = 1

        if dataframe[metric].iloc[-1] < worstVal:
            worstVal = dataframe[metric].iloc[-1]
            worstPot = 10
        if dataframe[metric].iloc[-11] < worstVal:
            worstVal = dataframe[metric].iloc[-11]
            worstPot = 9
        if dataframe[metric].iloc[-21] < worstVal:
            worstVal = dataframe[metric].iloc[-21]
            worstPot = 8
        if dataframe[metric].iloc[-31] < worstVal:
            worstVal = dataframe[metric].iloc[-31]
            worstPot = 7
        if dataframe[metric].iloc[-41] < worstVal:
            worstVal = dataframe[metric].iloc[-41]
            worstPot = 6
        if dataframe[metric].iloc[-51] < worstVal:
            worstVal = dataframe[metric].iloc[-51]
            worstPot = 5
        if dataframe[metric].iloc[-61] < worstVal:
            worstVal = dataframe[metric].iloc[-61]
            worstPot = 4
        if dataframe[metric].iloc[-71] < worstVal:
            worstVal = dataframe[metric].iloc[-71]
            worstPot = 3
        if dataframe[metric].iloc[-81] < worstVal:
            worstVal = dataframe[metric].iloc[-81]
            worstPot = 2
        if dataframe[metric].iloc[-91] < worstVal:
            worstVal = dataframe[metric].iloc[-91]
            worstPot = 1

        arr = []
        arr.append(dataframe[metric].iloc[-41])
        arr.append(bestVal)
        arr.append(bestPot)
        arr.append(worstVal)
        arr.append(worstPot)
        data[metric] = arr

        print(dataframe[metric].iloc[-1])
        print(dataframe[metric].iloc[-11])
        print(dataframe[metric].iloc[-21])
        print(dataframe[metric].iloc[-31])
        print(dataframe[metric].iloc[-41])
        print(dataframe[metric].iloc[-51])
        print(dataframe[metric].iloc[-61])
        print(dataframe[metric].iloc[-71])
        print(dataframe[metric].iloc[-81])
        print(dataframe[metric].iloc[-91])

    return data


if uploadFile:
    dataframe = pd.read_csv(uploadFile)
    if options == 'Summary Of all pots':
        st.markdown(printCostumTitle("PH, EC and Temprature summary Section",
                                     "These are the average pH, EC and total temperature in the entire greenhouse and its changes are determined according to the previous data set"),
                    unsafe_allow_html=True)
        with open('style.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        col1.metric("Temperature", "22 °C", "1.2 °F")
        col2.metric("PH", "6.6", "-8%")
        col3.metric("EC", "1.2", "4%")
        st.markdown(printText(
            "The three graphs below show the average changes in pH, EC and temperature on the days specified in the data set"),
            unsafe_allow_html=True)

        st.header('EC')
        c1, c2 = st.columns(2)
        # st.line_chart(dataframe, x='Timestamp', y='Initial EC')
        st.line_chart(dataframe, x='Timestamp', y='Final EC')

        st.header('PH')
        PHICol, PHFCol = st.columns(2)
        # st.line_chart(dataframe, x='Timestamp', y='Initial pH')
        st.line_chart(dataframe, x='Timestamp', y='Final pH')

        st.header('Temperature')
        st.line_chart(dataframe, x='Timestamp', y='Temperature')

        '''radioOption = st.radio(
            "What trend do you need",
            ('EC', 'PH', 'Temperature', 'leaves count'))
        if radioOption == 'EC':
            SummaryReportDataframeForEC(dataframe, 'PotID', divider(dataframe, 'PotID'))
        if radioOption == 'PH':
            SummaryReportDataframeForPH(dataframe, 'PotID', divider(dataframe, 'PotID'))
        if radioOption == 'Temperature':
            SummaryReportDataframeForTemperature(dataframe, 'PotID', divider(dataframe, 'PotID'))'''

    if options == 'Create Trend Base on PotID':

        print('mohsen')
        st.markdown(printCostumTitle('The situation of the POT' , """In this part, the pot that is selected is compared with the state of the idea in 4 weeks. In this comparison, first, the criteria that are important for plant growth are compared in a graph between the selected pot and the ideal state.
Growth criteria include:
,plant height
,Plant width
,Leaves Count
,Longest Leaf
,Shortest Leaf
,root color
,The color of the plant.
At the end of the diagram, according to the difference that exists, the growth status of the plant is determined and it is analyzed that the difference in what criteria caused this difference.
"""), unsafe_allow_html=True)

        st.markdown(printText("""There are two main parts below for analysis.
The comparison section where the growth rates and effective criteria are compared with the ideal state for each week.
In the analysis part, it is determined how far the selected pot is from the ideal state and which effective criteria should be corrected""") , unsafe_allow_html=True)
        growthMetrics = ['Height' , 'Width' , 'Leaves Count' ,'Longest Leaf' , 'Shortest Leaf']
        effectiveMetrics = ['Final EC' , 'Final pH' , 'MoistContent' , 'Temperature'  , 'WaterSaturation' ]
        PotidCol, CropIdCol = st.columns(2)

        PotID = PotidCol.selectbox('Select Your Pot ID', divider(dataframe, 'PotID'))
        subdataframe = dataframe.query(f'PotID == {PotID} ')
        week = 1

        weeks = [1, 2, 3, 4]
        bestData = pd.read_csv('dataBest.csv')

        st.markdown(costumPrintTitle('Comparison of Growth Metric') , unsafe_allow_html=True)

        table = {}
        # Growth Metrics
        for metric in growthMetrics:
            print(metric)
            week = 1
            heightpot = []
            bestpot = []
            diff = []
            while week <= 4:
                print("#############asdasd#######################asd  ")
                print(week)
                subdataframe1 = subdataframe.query(f'week == {week}')
                subdataframebest1 = bestData.query(f'week == {week}')
                print("asdadasdafasdsadasdasdagasdasdfasdasd")
                temp = subdataframe1[metric].iloc[-1]
                print(temp)
                print(subdataframebest1.iloc[-1])
                heightbestPot = subdataframebest1[metric].iloc[-1]

                heightpot.append(temp)
                bestpot.append(heightbestPot)

                week = week + 1

                diff.append(heightbestPot - temp)

            temp1 = []
            temp1.append(heightbestPot)
            temp1.append(temp)
            temp1.append(heightbestPot - temp)
            table [metric] = temp1
            print(diff)
            print("KENASDKASFKASJASDK:LAS:JLAJD:L sadas asd asd")
            print(len(heightpot))
            print(len(bestpot))
            dataBest = {'week': weeks, 'SelectedPot': heightpot, 'BestPot': bestpot }
            CompairDataSet = pd.DataFrame.from_dict(dataBest)

            st.markdown(printCostumTitle(metric , f"""In this criterion, {metric} is checked. The average number of {metric} in the pots is considered.The amount of difference in the number of petals: \n
            The first week : {diff[0]} 
            second week : {diff[1]} 
            Third week:{diff[2]} 
            forth week : {diff[3]}"""), unsafe_allow_html=True)

            st.line_chart(CompairDataSet, x='week')
            subdataframe = dataframe.query(f'PotID == {PotID}')

        st.markdown(tableGenerator2(table) , unsafe_allow_html=True)

        # effective metrics
        table = {}
        st.markdown(costumPrintTitle('Comparing effective metrics') , unsafe_allow_html=True)

        for metric in effectiveMetrics:
            print(metric)
            week = 1
            heightpot = []
            bestpot = []
            diff = []
            while week <= 4:
                print("####################################")
                print(week)
                subdataframe1 = subdataframe.query(f'week == {week}')
                subdataframebest1 = bestData.query(f'week == {week}')
                print("asdadasdafasdsadasdasdagasdasdfasdsdfsdfasd")
                temp = subdataframe1[metric].iloc[-1]
                print(temp)
                print(subdataframebest1.iloc[-1])
                heightbestPot = subdataframebest1[metric].iloc[-1]

                heightpot.append(temp)
                bestpot.append(heightbestPot)

                week = week + 1

                diff.append(heightbestPot - temp)

            temp1 = []
            temp1.append(heightbestPot)
            temp1.append(temp)
            temp1.append(heightbestPot - temp)
            table[metric] = temp1

            print(diff)
            print("KENASDKASFKASJASDK:LAS:JLAJD:L sadas asd asd")
            print(len(heightpot))
            print(len(bestpot))
            dataBest = {'week': weeks, 'SelectedPot': heightpot, 'BestPot': bestpot }
            CompairDataSet = pd.DataFrame.from_dict(dataBest)

            st.markdown(printCostumTitle(metric , f"""In this criterion, {metric} is checked. The average number of {metric} in the pots is considered.The amount of difference in the number of petals: \n
            The first week : {diff[0]} 
            second week : {diff[1]} 
            Third week:{diff[2]} 
            forth week : {diff[3]}"""), unsafe_allow_html=True)

            st.line_chart(CompairDataSet, x='week')
            subdataframe = dataframe.query(f'PotID == {PotID}')

            print(table)
        st.markdown(tableGenerator3(table), unsafe_allow_html=True)


    if options == 'Best Performance':
        data = findBestPot(dataframe)
        st.markdown(tableGenerator(findBestPot(dataframe)), unsafe_allow_html=True)

        st.markdown(printCostumTitleH2('Details of Best and Worst Pots',
                                       'According to the above table, pot number 1 had the best yield and pot number 2 had the worst yield. To view the measured criteria, you can view the criteria by selecting the criteria.'),
                    unsafe_allow_html=True)
        ColbutBest, ColbutWorst = st.columns(2)
        if ColbutBest.button('Best Pot detail: PotID 1'):
            c1, c2 = st.columns(2)
            bestpotdataframe = dataframe.query('PotID == 1')
            st.line_chart(bestpotdataframe, x='Timestamp', y='Final pH')
            st.line_chart(bestpotdataframe, x='Timestamp', y='Final EC')
        if ColbutWorst.button('Worst Pot detail: PotID2'):
            c1, c2 = st.columns(2)
            worstpotdataframe = dataframe.query('PotID == 2')
            st.line_chart(worstpotdataframe, x='Timestamp', y='Initial EC')
            st.line_chart(worstpotdataframe, x='Timestamp', y='Final EC')
        st.markdown(printCostumTitleH2('Compare & Analyse', 'In this section, the best and worst pots are selected for each growth criterion specified in the table above, and the criteria that are important in plant growth are shown. In the comparison section, the standard for growth is displayed for the best and worst pots, and the changes are displayed. In the analysis section, it specifies the impact of the criterion considered for growth'), unsafe_allow_html=True)
        st.markdown(printCostumTitle('Compare, Metric : PH',
                                     'According to the above table, pot number 7 had the best yield and pot number 2 had the worst yield. To view the measured criteria, you can view the criteria by selecting the criteria. The following graphs are displayed to compare these metrics. In the charts below, the criteria for each pot are drawn.'),
                    unsafe_allow_html=True)
        showDifferentBestWorst(dataframe, 1, 2)
        st.markdown(printCostumTitle('Analyse, Metric : PH',
                                     'As shown in the diagram, since 2023-04-15 17:00:00, the pH level in pot number 4 has decreased, so its efficiency has decreased.'),
                    unsafe_allow_html=True)

