import streamlit as st
user_name = st.text_input("Enter your name:")

# Dropdown Selection
choice = st.selectbox("Choose an option:", ["Option A", "Option B", "Option C"])

# Slider
age = st.slider("Select your age:", min_value=0, max_value=100, value=25)

# Checkbox
agree = st.checkbox("I agree to the terms")

# Button (returns True when clicked)
if st.button("Submit"):
    st.write(f"Hello {user_name}, you selected {choice} and are {age} years old.")
