import streamlit as st
from bd_views import BloodDonorManager
donor=BloodDonorManager()

tab1,tab2= st.tabs(["add","view"])
with tab1:
    st.title("add new donor")
    name=st.text_input("enter name")
    blood_group=st.text_input("blood group")
    phone=st.text_input("phone")
    city=st.text_input("city")
    last_donation=st.text_input("last donation")
    if st.button("ADD"):
        donor.post(name=name,blood_group=blood_group,phone=phone,city=city,last_donation=last_donation)
        st.success("added successfully")
with tab2:
    st.title("view donors")