import streamlit as st
import pandas as pd
import numpy as np
import webbrowser


df = pd.read_csv('India_GDP_Data.csv')
st.title("GDP of India")
st.header('from 1961 to 2021')
df.set_index(df['Year'],inplace=True)
if st.checkbox('Dataset'):
    st.write(df)

val = st.sidebar.radio("Pages",['EDA','Info'],index = 0)
if val == "EDA":
    st.image('photo.webp',use_column_width=1)
    graph_type = st.selectbox("Graph_Type",["Interactive","With data"],index=0)
    if graph_type== "Interactive":
        st.write('Line_Graph')
        inp = st.radio("Y-axis",df.columns[1:])
        first,last = st.columns(2)
        with first:
            st.line_chart(df[inp])
        with last:    
            st.bar_chart(df[inp])

    if graph_type== "With data":
        st.write('Scatter_plot')
        col1,col3 = st.columns([3,1])
        with col1:
            st.bar_chart(df['Per_Capita_in_USD'])
 
        with col3:
            st.write(df['Per_Capita_in_USD'].head(5))      
            
        
if val == 'Info':
    
    if st.button("Click Here to know more"):
        url = 'https://en.wikipedia.org/wiki/Economy_of_India'
        webbrowser.open_new_tab(url)



