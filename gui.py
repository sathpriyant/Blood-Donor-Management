import streamlit as st
from bd_views import BloodDonorManager
donor=BloodDonorManager()

tab1,tab2= st.tabs(["ADD","VIEW"])
with tab1:
    st.title("add new donor")
    name=st.text_input("name")
    blood_group=st.selectbox("select blood group",options=["A+","B+","O+","AB+","A-","B-","O-","AB-"])
    phone=st.text_input("phone")
    city=st.text_input("city")
    last_donation=st.date_input("last donation")
    if st.button("ADD"):
        donor.post(name=name,blood_group=blood_group,phone=phone,city=city,last_donation=last_donation)
        st.success("added successfully")
with tab2:
    st.title("view donors")
    records=donor.get()
    if records:
        st.table(records)
    else:
        st.warning("No data")