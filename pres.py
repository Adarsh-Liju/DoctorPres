# Importing all Libraries
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
query = "SELECT * FROM PatientPres"
cursor.execute(query)
result = cursor.fetchall()
pat_id = [i['Pat_ID'] for i in result]
# GUI Login Screen
st.header("Doctor Prescription System")
st.write("## Enter Patient ID")
search=st.selectbox(" ",pat_id)
generate_pres=st.button("Generate Prescription")
if generate_pres:
    query2 = 'SELECT * FROM PatientPres WHERE Pat_ID=%s' % (search)
    cursor.execute(query2)
    result2 = cursor.fetchall()
    st.write("# Patient Details")
    st.write("Patient ID: ", result2[0]['Pat_ID'])
    st.write("## Patient Name: ",result2[0]['Pat_Name'])
    st.write("## Patient Age: ",result2[0]['Pat_Age'])
    st.write("## Medicines: ",result2[0]['Medicine_1'],",",result2[0]['Medicine_2'],",",result2[0]['Medicine_3'])
    