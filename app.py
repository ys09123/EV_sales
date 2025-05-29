import streamlit as st

st.title('EV Infrastructure Recommendations')
st.map(df_cluster[['lat', 'lon']])
st.dataframe(df_cluster[['region', 'value', 'num_chargers', 'charger_density', 'cluster']])
