import streamlit as st

st.title("🧮 Simple Calculator")

num1 = st.number_input("Enter first number", format="%f")
num2 = st.number_input("Enter second number", format="%f")
operation = st.selectbox("Choose operation", ["+", "-", "*", "/"])

if st.button("Calculate"):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "❌ Cannot divide by zero"

    # Format result
    if isinstance(result, float):
        result = int(result) if result.is_integer() else round(result, 2)

    st.success(f"Result: {result}")
