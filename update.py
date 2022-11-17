import os
import random
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
cursor = connection.cursor()
query = "SELECT `Medicine Name` FROM MedicineDB"
cursor.execute(query)
result = cursor.fetchall()
result = [i['Medicine Name'] for i in result]
pat_query="SELECT `Pat_ID`,`Pat_Name` FROM PatientPres"
cursor.execute(pat_query)
pat_result=cursor.fetchall()
# Combine the two lists
pat_result=[str(i['Pat_ID'])+" "+i['Pat_Name'] for i in pat_result]
st.write("## Update Prescription")
pat_id = st.selectbox("Patient ID",pat_result)
st.write("## Enter Medicines")
med1 = st.selectbox("Medicine 1", result)
med2 = st.selectbox("Medicine 2", result)
med3 = st.selectbox("Medicine 3", result)
update_pres = st.button("Confirm")
if update_pres:
    query2 = "UPDATE PatientPres SET Medicine_1='%s',Medicine_2='%s',Medicine_3='%s' WHERE Pat_ID='%s'" % (
        med1, med2, med3, pat_id)
    cursor.execute(query2)
    st.success("Prescription Updated")