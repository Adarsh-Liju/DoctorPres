import streamlit as st


def query_list():
    st.header("Queries")
    st.write("## Join Queries")
    f = open("join_queries.sql", "r")
    st.code(f.read(), language="sql")
    st.write("## Aggregate Queries")
    f = open("aggregate_queries.sql", "r")
    st.code(f.read(), language="sql")
    st.write("## Trigger Queries")
    f = open("trigger_queries.sql", "r")
    st.code(f.read(), language="sql")
    f= open("proc_queries.sql","r")
    st.code(f.read(),language="sql")
    
