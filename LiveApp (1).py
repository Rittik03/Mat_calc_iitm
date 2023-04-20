import streamlit as st
st.write("""
# Maximum Number Finder App
""")
def user_input_features():
    x = st.number_input("First Number",min_value=-1000,max_value=1000,step=1)
    y = st.number_input("Second Number",min_value=-1000,max_value=1000,step=1)
    z = st.number_input("Third Number",min_value=-1000,max_value=1000,step=1)
    return max(x, y, z)

result = user_input_features()
st.subheader('Maximum Number')
st.write(result)
