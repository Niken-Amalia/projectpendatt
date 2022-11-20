import streamlit as st
import re
import pandas as pd 
import numpy as np

st.title("""
form input data, by Niken Amalia
""")

#Fractional Knapsack Problem
#Getting input from user
JenisKelamin=int(st.text_input("Masukkan Gender: ",0))
Umur=int(st.number_input("Masukkan Umur : ",0))
Rokok=int(st.number_input("Status Merokok  : ",0))
JariKuning=int(st.number_input("Apakah Jari Menguning ? : ",0))
Kecemasan=int(st.number_input("Apakah Mengalami Anxiety ?  : ",0))
Peerpressure=int(st.number_input("Apakah Pernah Merasakan perrpressure ?  : ",0))
Riwayat Penyakit=int(st.number_input("Riwayat Penyakit   : ",0))
Fatigue=int(st.number_input("Apakah Merasa Kelelahan?  : ",0))
Alergi=int(st.number_input("Apakah Memiliki Alergi?  : ",0))
Wheezing=int(st.number_input("Apakah Merasa Sesak Nafas?  : ",0))


submit = st.button("submit")


if submit:
    st.info("Jadi,dinyakataan . ")


