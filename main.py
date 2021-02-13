import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber Pickups in NYC')

DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    df = pd.read_csv(DATA_URL, nrows=nrows)
    lower_text = lambda x: str(x).lower()
    df.rename(lower_text, axis='columns', inplace=True)
    df['date/time'] = pd.to_datetime(df['date/time'])
    return df

loading_data = st.text('Loading data...')
df = load_data(100000)
loading_data.text('Done! Thank you for waiting.')

if st.checkbox('Show raw data'):
    st.subheader('Raw Data')
    st.write(df)

st.subheader('Number for pickups per hour')
hist_values = np.histogram(df['date/time'].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = df[df['date/time'].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)



