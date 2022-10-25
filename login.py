import streamlit as st
import time
import pymysql
import os

# config for the database
connection = pymysql.connect(host='localhost',
                             user='ala',
                             password='ala',
                             db='DoctorPres',
                             cursorclass=pymysql.cursors.DictCursor)
connection.autocommit(True)
cursor = connection.cursor()

# GUI Login Screen
st.write("# Login")
# st.image("")
with st.form("my_form", clear_on_submit=True):
    user_name = st.text_input("Username")
    user_pwd = st.text_input("Password")
    submitted=st.form_submit_button("Login")
if submitted:
        query = "SELECT user_name,user_pwd from LoginCreds WHERE user_name='%s' AND user_pwd='%s'" % (user_name, user_pwd)
        cursor.execute(query)
        if cursor.rowcount == 0:
            st.error("Invalid Credentials")
        else:
            st.success("Login Successful")
