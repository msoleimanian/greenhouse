import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px



st.title("Green House Demo")
st.text("This is a Demo for Greenhouse")

st.sidebar.title("Navigation")
Options = st.sidebar.radio('Sections' , options=('Home', 'Upload' , 'pak choy greenhouse'))