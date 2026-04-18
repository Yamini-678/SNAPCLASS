import streamlit as st

def footer_home():
    
    logo_url = 'https://i.ibb.co/4r5X1FY/apnacollege.png'
    st.markdown(
        f"""
        <div style="margin-top:2rem;
            display:flex;
            gap:6px;
            justify-content:center;
            items-align:center"
        >
        <p style='font-weight:bold; color:white;'>Created With ❤️ by</p>
        <p style='max-height:25px;font-weight:bold; color:white'>Yamini</p>
        </div>
               
                """ , unsafe_allow_html=True
    )