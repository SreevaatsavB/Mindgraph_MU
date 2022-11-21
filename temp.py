import pandas as pd
import numpy as np
from PIL import Image
import os
import pandas as pd
import streamlit as st
import enum
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px



org_pro_df = pd.read_csv('/Users/sreevaatsav/Desktop/mu_h1/org_pro_df.csv')
clubs_pro_df = pd.read_csv('/Users/sreevaatsav/Desktop/mu_h1/clubs_pro_df.csv')
part_pro_df = pd.read_csv('/Users/sreevaatsav/Desktop/mu_h1/part_pro_df.csv')

metadata_df = pd.read_csv('/Users/sreevaatsav/Desktop/mu_h1/Metadata.csv')







batch_17, batch_18 = 0,0


for i in range(len(clubs_pro_df)):
    temp_arr = str(clubs_pro_df["RollNumber"][i]).split("X")
    if temp_arr[0] == "17":
        batch_17 += 1
    elif temp_arr[0] == "18":
        batch_18 += 1
batch_dist = [batch_17, batch_18]



unique_ID = list(metadata_df["ID"]) 
cevents_participated = {}
for uid in unique_ID:
    cevents_participated[uid] = None


for i in range(len(unique_ID)):
    ID = unique_ID[i]
    temp = []
    for j in range(len(clubs_pro_df)):
        if clubs_pro_df["RollNumber"][j] == ID:
            temp.append(clubs_pro_df["Event"][j])
    cevents_participated[ID] = list(set(temp))
    
    
cevents_participated_count = {}
for k in cevents_participated:
    cevents_participated_count[k] = len(cevents_participated[k])
    
inv_cevents_participated_count = {}
for k in cevents_participated_count:
    if cevents_participated_count[k] not in inv_cevents_participated_count:
        inv_cevents_participated_count[cevents_participated_count[k]] = 1
        
    else:
        inv_cevents_participated_count[cevents_participated_count[k]] += 1

inv_ccount_keys = list(inv_cevents_participated_count.keys())
inv_ccount_values = list(inv_cevents_participated_count.values())

inv_ccountdf = pd.DataFrame([inv_ccount_keys, inv_ccount_values]).T
inv_ccountdf.columns = ["num_cevents", "count"]

# Page setting
st.set_page_config(layout="wide")

st.header('Clubs and Fest data analysis')

# with open('style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# Row A
# a1, a2 = st.columns(2)
# a1.metric("Wind", "9 mph", "-8%")
# a2.metric("Humidity", "86%", "4%")

# # Row B
# b1, b2, b3, b4 = st.columns(4)
# b1.metric("Temperature", "70 °F", "1.2 °F")
# b2.metric("Wind", "9 mph", "-8%")
# b3.metric("Humidity", "86%", "4%")
# b4.metric("Humidity", "86%", "4%")

# # Row C
c1, c2 = st.columns((5,5))

with c1: 
    st.markdown('### Clubs')
    
    fig = px.pie(clubs_pro_df, 'Club_Name')
    
    st.plotly_chart(fig)

    
with c2:
    
    st.markdown('### Fests')
    
    fig = px.pie(part_pro_df, 'Fest_Name')
    
    st.plotly_chart(fig)
    
    

c1, c2 = st.columns((4,4))

with c1: 
    st.markdown('### No.of organizers in clubs')
    
    fig = px.pie(clubs_pro_df, "Role")
    
    st.plotly_chart(fig)

    
with c2:
    
    st.markdown('### Clubs and events')
    
    fig = px.pie(clubs_pro_df, 'Event')
    
    st.plotly_chart(fig)
    
    # st.write('''
    # Streamlit: A web application framework for Python.
# ''')

c1, c2 = st.columns((4,4))


with c1:
    
    st.markdown('### Batches of students participated in club events')
    
    fig = plt.figure(figsize=(4,4))
    
    plt.pie(batch_dist, labels = ["Batch of 17", "Batch of 18"], autopct = "%1.1f", textprops = {'fontsize': 10})
    
    st.pyplot(fig)
    
    
with c2:
    
    st.markdown('### Clubs and events')
    
    fig = plt.figure(figsize=(8,8))
    sns.barplot(y = inv_ccountdf["count"], x = inv_ccountdf["num_cevents"])
    plt.xlabel("No.of events attended by a student (club data)")
    
    st.plotly_chart(fig)
    



    
    # 
    # plost.donut_chart(
    #     data=stocks,
    #     theta='q2',
    #     color='company')