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
from view import plot_pres
from bill import bill_pres
from queries_list import query_list
selection = ["Create", "Read", "Update", "Delete", "Query","Bill","List of Queries"]
# config for the database
connection = pymysql.connect(
    host="localhost",
    user="ala",
    password="ala",
    db="DoctorPres",
    cursorclass=pymysql.cursors.DictCursor,
)
connection.autocommit(True)
cursor = connection.cursor()
query = "SELECT `Medicine Name` FROM MedicineDB"
cursor.execute(query)
result = cursor.fetchall()
result = [i["Medicine Name"] for i in result]
# GUI Login Screen
st.header("Doctor Prescription System")
st.sidebar.image("pharmacy.svg")
st.sidebar.header("Doctor Prescription System")
st.sidebar.subheader("Operations")
but2 = st.sidebar.button("About")
option = st.sidebar.selectbox("Operations", selection)


if option == "Update":
    update_pres()
if option == "Create":
    create_pres()
if option == "Delete":
    delete_pres()
if option == "Read":
    view_pres()
    plot_pres()
if option == "Query":
    query_pres()
if option == "Bill":
    bill_pres()
if option == "List of Queries":
    query_list()
if but2:
    st.write("### This is a Doctor Prescription System")
    st.write("### Made with :heart: by Adarsh Liju Abraham")