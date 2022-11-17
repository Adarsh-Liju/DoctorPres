# Importing some global modules
import pymysql
import streamlit as st
import os
import random
# Importing the local modules
from delete import delete_pres
from update import update_pres
from create import create_pres
from query import query_pres
from view import view_pres
selection = ["Create", "Read", "Update", "Delete", "Query"]
# config for the database
connection = pymysql.connect(host='localhost',
                             user='ala',
                             password='ala',
                             db='DoctorPres',
                             cursorclass=pymysql.cursors.DictCursor)
connection.autocommit(True)
cursor = connection.cursor()
query = "SELECT `Medicine Name` FROM MedicineDB"
cursor.execute(query)
result = cursor.fetchall()
result = [i['Medicine Name'] for i in result]
# GUI Login Screen
st.header("Doctor Prescription System")
st.sidebar.image("pharmacy.svg")
st.sidebar.header("Doctor Prescription System")
st.sidebar.subheader("Operations")
option = st.sidebar.selectbox("Operations", selection)
print(option)
if option == "Update":
    update_pres()
if option == "Create":
    create_pres()
if option == "Delete":
    delete_pres()
if option == "Read":
    view_pres()
if option == "Query":
    query_pres()