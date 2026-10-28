import streamlit as st
import pandas as pd
import numpy as np

st.title("hello, streamlit")
st.write(":streamlit: This is your first streamlit app")
st.text("lets get started")

#condition logic with widgets

name= st.text_input("enter your name ")
if st.button("greet"):
    st.success(f"hello,{name}!")


    #dispalying data and charts 
    df = pd.DataFrame(np.random.randn(10,2),columns=['A' , 'B'])
    st.line_chart(df)
    st.bar_chart(df)

    #file uploading and catch topics 
    upload_file = st.file_uploader("Upload a document",type=["pdf", "txt", "docx"])


    uploading_file = st.file_uploader("uplaod a csv",type='csv')
    if upload_file:
        df = pd.read_csv(upload_file)
        st.dataframe(df)

st.title("text and markdown demo")
st.header("this is a header")
st.subheader("this is a subheader")
st.markdown("**bold**,*Ttalic*,'code',[link](https://streamlit.io)")
st.code("for i in ramge(5): print(i)",language="python")

st.text_input("what's your name?")
st.text_area("Write something....")
st.number_input("pick a number",min_value=0, max_value=100)
st.slider("choose a range",0,100)
st.selectbox("select a fruit",["apple","banana","mango"])
st.multiselect("choose toppings",["cheese","tamato","olive"])
st.radio("pick one",["option A","option B"])
st.checkbox("I agree to the terms")

if st.checkbox("Show Details"):
    st.info("Here are the more details...")


option = st.radio("choose view",["show chart","show table"])
if option =="show chart":
    st.write("Chart would appear here")
else:
    st.write("table would appear here")

with st.form("login_form"):
    username=st.text_input("username")
    password=st.text_input("password",type="password")
    submitted=st.form_submit_button("login")

    if submitted:
        st.success(f"welcome,{username}!")

st.image("https://via.placeholder.com/300", caption = "simple image", use_column_width=True)
st.video("https://youtu.be/aSugSGCC12I?si=Pthjn5j9KdFLnF6I")
