import streamlit as st
with st.form("my_form",clear_on_submit=True):
    st.title("Patient Details")
    patient_name=st.text_input("Enter Patient Name")
    st.write("You entered:",patient_name)
    patient_age=st.text_input("Enter Patient Age")
    st.write("You entered:",patient_age)
    symptoms=st.text_input("Please enter your symptoms")
    st.write("You entered",symptoms)
    submitted = st.form_submit_button("Submit")
    if submitted:   
        st.write("## Thank you for your response :-) ")
    