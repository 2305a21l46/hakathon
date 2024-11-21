import streamlit as st
def another_page():
    st.write('this is another page')

pages = {
    "theorems": [
        st.Page('thevinin.py',title="thevenin's theorem"),
        st.Page('norton.py',title="norton's theorem"),
        ],
    "circuits":[
        st.Page(another_page,title="another page"),
    ]
}

ro=st.navigation(pages)
ro.run() 