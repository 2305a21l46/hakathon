import streamlit as st 
st.title('nortons theorem')

def calculate_norton(in_,rn,rl):
    vn=in_*rn
    il=in_-vn/rn
    pl=il**2*rl
    return il,pl

tab1,tab2=st.columns(2)

with tab1:
    col1,col2=st.columns(2)
     
    with col1: 
    
        with st.container(border=True):
            in_=st.number_input("In (A)", value=1)
            rn=st.number_input("Rn (o)", value=1)
            rl=st.number_input("rl (o)", value=1)
            compute=st.button("compute")
    with col2:
        if compute:
            il,pl=calculate_norton(in_,rn,rl)
            st.write(f"Il={il}A")
            st.write(f"Pl={pl}w")
with tab2:
    st.write("norton defination")
