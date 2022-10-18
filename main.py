import mysql.connector
from mysql.connector import Error
import streamlit as st
import time
connection = mysql.connector.connect(host='localhost',port=3308,database='DoctorPres',user='ala',password='ala')
print("Connected to Server - DoctorPres")
mycursor = connection.cursor()
mycursor.execute("SELECT * FROM `Medicine`;")
myresult = mycursor.fetchall()
st.dataframe(myresult)
