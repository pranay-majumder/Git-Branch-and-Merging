## Create Virtual Enviorment
## python -m venv env
## venv/Scripts/Activate
## streamlit run app.py


import streamlit as st ## type:ignore

st.title('CampusX Online Platform')

col1,col2=st.columns(2)

with col1:
    st.image('image.jpeg')

with col2:
    st.header('Campusx is an Online Platform')

st.header('Courses')
st.subheader('DSA')
st.subheader('ML')
st.subheader('DL')

st.sidebar.title("Menu")

st.sidebar.markdown("""
- Home
- About
- Contact           
- Career                  
- Login                  
""")

## Add Selection Box on Side Bar
st.sidebar.selectbox('Select One',['teacher','student'])
st.sidebar.button('Select')