import streamlit as st

def delta_to_star(r12, r23, r31):
    R1=(r12 * r31)/(r12 + r23 + r31)
    R2=(r12 * r23)/(r12 + r23 + r31)
    R3=(r31 * r23)/(r12 + r23 + r31)
    return R1, R2, R3

st.title("Delta to Star Conversion")

st.write("Calculate the resistance values (R1, R2, R3) of the star connection network for the given delta connection network having resistance R12, R23, R31.")

#tab1=st.tabs(["Conversion"])
#with tab1:
col1, col2 = st.columns(2)
with col1:
        r12 = st.number_input("R12 (Ohms)")
        r23 = st.number_input("R23 (Ohms)")
        r31 = st.number_input("R31 (Ohms)")
        convert = st.button('Compute')
with col2:
    if convert:
            R1,R2,R3 = delta_to_star(r12, r23, r31)
            st.write(f"R1 = {R1:.2f} Ohms")
            st.write(f"R2 = {R2:.2f} Ohms")
            st.write(f"R3 = {R3:.2f} Ohms")