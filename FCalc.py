#!/usr/bin/env python
# coding: utf-8

# In[2]:


# file: app_streamlit.py
# Run with:  streamlit run app_streamlit.py

import streamlit as st

def calculate_final_amount(
    principal: float, 
    rate: float, 
    years: int, 
    compounding: str, 
    yearly_contribution: float
) -> float:
    """
    Compound interest calculator with yearly contributions.
    """
    comp_map = {"Yearly": 1, "Quarterly": 4, "Monthly": 12}
    n = comp_map.get(compounding, 1)
    r = rate / 100.0

    balance = principal
    for year in range(1, years + 1):
        # compound existing balance for one year
        balance = balance * (1 + r / n) ** n
        # add yearly contribution at the end of the year
        balance += yearly_contribution
    return round(balance, 2)

# ------------------ Streamlit UI ------------------
st.set_page_config(page_title="Investment Calculator", layout="centered")
st.title("🐦‍🔥 Investment Calculator")

principal = st.number_input(
    "Initial Investment Amount", min_value=0.0, value=1000.0, step=100.0, format="%.2f"
)
rate = st.number_input(
    "Annual Interest Rate (%)", min_value=0.0, value=5.0, step=0.1, format="%.2f"
)
years = st.number_input("Number of Years", min_value=1, value=10, step=1)
compounding = st.selectbox("Compounding Frequency", ["Yearly", "Quarterly", "Monthly"])
yearly_contribution = st.number_input(
    "Yearly Contribution", min_value=0.0, value=0.0, step=100.0, format="%.2f"
)

if st.button("Calculate"):
    final_amount = calculate_final_amount(
        principal, rate, int(years), compounding, yearly_contribution
    )
    st.success(f"Your investment will be worth: ${final_amount:,.2f}")



# In[ ]:





