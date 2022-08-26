# ...............Import Libraries..................
import streamlit as st  # for User Interface (UI) design

st.set_page_config(
    page_title="Sedex English Academy",
    page_icon="🕉️",
    layout="wide"
)

st.markdown(
    "<div style='text-align:center;margin-bottom:20px'>"
    "<h1>Social Media Analytics Dashboard</h1>"
    "<h2>Sedex English Academy</h2>"
    "<img src='https://scontent.fcmb3-2.fna.fbcdn.net/v/t1.6435-9/76198290_1353971444763492_5186922095166095360_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=BuSMbfA48kcAX8vKKMo&_nc_ht=scontent.fcmb3-2.fna&oh=00_AT9Tf7Xi2oNUBlJYUAXCB0ylNPVobLfjkP3og8bOvjprQA&oe=632E445B' style='width:300px; margin-top:5px;'>"
    "</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div style='text-align:center; margin-top:80px;'>"
    "<h3>Designed By : Gehan Pasindhu(20235926)</h3>"
    "</div>", unsafe_allow_html=True
)

st.markdown(
 "<div style='text-align:right; margin-top:20px;'>"
    "<p style='font-style:italic'>Note *<br>Social Media Analytics Dashboard for Sedex English Academys Application is designed only for educational purpose.<br> And any of the data used here will not be used for any other purposes.</p>"
    "</div>", unsafe_allow_html=True
)

hide_stremlit_style = """
<style>
#MainMenu{visibility:hidden}
footer{visibility:hidden}
</style>

"""
st.markdown(hide_stremlit_style, unsafe_allow_html=True)