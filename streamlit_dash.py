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

# Initialize connection.
conn = st.experimental_connection("postgresql", type="sql")

# Perform query.
df = conn.query('SELECT * FROM rna LIMIT 10;', ttl="10m")

# Print results.
st.table(df)
