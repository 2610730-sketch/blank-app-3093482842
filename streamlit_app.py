import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
height=int(input('키:'))
if height < 100:
    print('탐승불가')
elif 100<=height<130:
    print('보호자 동행시 탑승 가능')
elif 130<=height<195:
    print('탐승 가능')
else :
    print('탑승 불가')