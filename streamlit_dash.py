'''
import streamlit as st
from sqlalchemy import text
import pandas as pd
import sqlalchemy as sqa
import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('postgresql://alex_baker:Tony1181*@localhost/lego_database')

stuff = text("SELECT * FROM colors")

with engine.connect() as con:
    fg = con.execute(stuff).fetchall()

df = pd.DataFrame(fg)
st.table(df)
'''

# streamlit_app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)
# Initialize connection.
conn = st.experimental_connection("postgresql", type="sql")

# Perform query.
df = conn.query('SELECT * FROM rnc_database;', ttl="10m")
st.header('Sample SQL Dash')
df[['avg_length','min_length','max_length']] = df[['avg_length','min_length','max_length']].fillna(0)
metric = st.selectbox('Select metric', options = ['avg_length','min_length','max_length'],index = 0)

c1,c2,c3 = st.columns(3)

with c1:
    df_g = df.groupby('timestamp').sum()[metric].plot(kind = 'bar')
    st.pyplot()
with c2:
    dfr = df.groupby('alive').count()['id'].plot(kind = 'bar')
    st.pyplot()
with c3:
    dfr2 = df[['alive','avg_length','min_length','max_length']].groupby('alive').sum()[metric].plot(kind = 'bar')
    st.pyplot()

selections = list(set(df['descr']))
# Print results.
selected = st.multiselect('Select Value', options = selections)
if selected == []:
    st.header('Please Select a Value')
else:
    select = df[df['descr'].isin(selected)][['id','timestamp','display_name','project_id','alive']]
    st.table(select)
