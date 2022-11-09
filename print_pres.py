import pandas as pd
import pymysql
import streamlit as st

# config for the database
connection = pymysql.connect(host='localhost',
                             user='ala',
                             password='ala',
                             db='DoctorPres',
                             cursorclass=pymysql.cursors.DictCursor)
connection.autocommit(True)
cursor = connection.cursor()
query = "SELECT * FROM `PatientPres`"
cursor.execute(query)
result = cursor.fetchall()
result = pd.DataFrame(result)
st.write(result)
