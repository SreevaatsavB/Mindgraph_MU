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


# Change paths in your local machines

org_pro_df = pd.read_csv('/Users/sreevaatsav/Desktop/mu_h1/org_pro_df.csv')
clubs_pro_df = pd.read_csv('/Users/sreevaatsav/Desktop/mu_h1/clubs_pro_df.csv')
part_pro_df = pd.read_csv('/Users/sreevaatsav/Desktop/mu_h1/part_pro_df.csv')

metadata_df = pd.read_csv('/Users/sreevaatsav/Desktop/mu_h1/Metadata.csv')


img1_path = '/Users/sreevaatsav/Desktop/mu_h1/f1_events.png'
img2_path = '/Users/sreevaatsav/Desktop/mu_h1/f2_events.png'
img3_path = '/Users/sreevaatsav/Desktop/mu_h1/num_evs.png'


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

st.title('Deduped data analysis')

st.header('Clubs and Fest data analysis')

# with open('style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# Row A
# a1, a2 = st.columns(2)
# a1.metric("Wind", "9 mph", "-8%")
# a2.metric("Humidity", "86%", "4%")

# Row 
b1, b2, b3 = st.columns(3)

b1.metric(
    label = "Number of students", value = len(metadata_df))
    
b2.metric(
    label = "Number of clubs", value = len(clubs_pro_df["Club_Name"].unique()))
    
b3.metric(
    label = "Number of fests", value = len(part_pro_df["Fest_Name"].unique()))
    

# b1, b2 = st.columns(2)

# b1.metric(
#     label = "Number of students", value = len(metadata_df["RollNumber"]))
    
# b2.metric(
#     label = "Number of clubs", value = len(clubs_pro_df["Club_Name"].unique()))



# # Row C
c1, c2 = st.columns((5,5))

with c1: 
    st.markdown('### No.of participants in each club')
    
    fig = px.pie(clubs_pro_df, 'Club_Name')
    
    st.plotly_chart(fig)

    
with c2:
    
    st.markdown('### No.of participants in each fest')
    
    fig = px.pie(part_pro_df, 'Fest_Name')
    
    st.plotly_chart(fig)
    

c1, c2 = st.columns((5,5))
with c1: 
    st.markdown('### No.of events in fests')
    image3 = Image.open(img3_path)
    image3 = np.array(image3)
    st.image(image3)
    
with c2:
    st.markdown('### No.of organizers in fests')
    fig = px.pie(org_pro_df, 'Fest_Name')
    
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
    
    
st.markdown("Here, the event 3 conducted by each club has lesser no.of participants than the other events of the respective clubs. So, analyazing  event 3 of each club could improve the strength and intrest towards that event, or any other alternative could be preferred")

b1, b2, = st.columns(2)

b1.metric(
    label = "Number of batch 18 students", value = len(metadata_df[metadata_df["ID"].str.startswith("18")]))
    
b2.metric(
    label = "Number of batch 17 students", value = len(metadata_df[metadata_df["ID"].str.startswith("17")]))
    


c1, c2 = st.columns((4,4))

with c1:
    
    st.markdown('### Distribution based on batch in club events')
    
    fig = plt.figure(figsize=(4,4))
    
    plt.pie(batch_dist, labels = ["Batch of 17", "Batch of 18"], autopct = "%1.1f", textprops = {'fontsize': 10})
    
    st.pyplot(fig)
    
    
with c2:
    
    st.markdown('### Students participation in club events')
    
    fig = plt.figure(figsize=(8,8))
    sns.barplot(y = inv_ccountdf["count"], x = inv_ccountdf["num_cevents"])
    plt.xlabel("No.of events attended by a student (club event)")
    
    st.plotly_chart(fig)
    
st.markdown("We can see that almost half of the students aren't participating in any of the events")
st.markdown("Also, most of the students who are participating in the events, participate  mostly in 3 events and then the count decreases.")
    
    
st.header('Students participation in fest events')

c1, c2 = st.columns((5,5))
with c1:
        
    image1 = Image.open(img1_path)
    image1 = np.array(image1)
    st.image(image1, caption='Events in fest1')
    
    

with c2:
    
    image2 = Image.open(img2_path)
    image2 = np.array(image2)
    st.image(image2, caption='Events in fest2')
    
st.markdown("Seems like the first 5 events conducted in both the fests have higher strength than the rest of the events, so maybe we could prefer those event organisers or activities of the 5 events of the respective fests")

    