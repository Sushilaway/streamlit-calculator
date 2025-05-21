import streamlit as st

st.title("✅ ToDo List App")

# Input box
task = st.text_input("Enter a new task:")

# Button
if st.button("Add Task"):
    st.write("You entered:", task)
