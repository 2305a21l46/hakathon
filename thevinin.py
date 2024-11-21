import streamlit as st

def calcu_thevenin(vth,rth,rl):
    il=vth/(rth+rl)
    pl=il**2*rl
    return il,pl
st.title("thevenin's theorem")

tab1,tab2=st.tabs(["compute","explanation"])
with tab1:
    col1,col2=st.columns(2)
    with col1:
        st.container(border=True)
        vth=st.number_input("Vth(v)",value=1)
        rth=st.number_input("Rth(r)",value=1)
        rl=st.number_input("r(l)",value=1)
        
        compute=st.button('compute')
    with col2:
        if compute:
            il,pl=calcu_thevenin(vth,rth,rl)
            st.write(f'Il={il:.2f}A')
            st.write(f'Pl={pl:.2f}W')
with tab2:
    st.latex(r"V_{th}=V_{oc}")
    