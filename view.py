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


def view_pres():
    query = "SELECT `Pat_ID`,`Pat_Name`,`Pat_Age`,`Medicine_1`,`Medicine_2`,`Medicine_3`,Date(`Date`) FROM `PatientPres`;"
    cursor.execute(query)
    result = cursor.fetchall()
    st.table(result)