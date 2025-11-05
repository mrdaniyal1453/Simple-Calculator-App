import streamlit as st

# App title
st.set_page_config(page_title="Calculator App", page_icon="🧮", layout="centered")
st.title("🧮 Simple Calculator App")

# Input fields
num1 = st.number_input("Enter first number", value=0.0)
operation = st.selectbox("Select operation", ["Add (+)", "Subtract (-)", "Multiply (×)", "Divide (÷)"])
num2 = st.number_input("Enter second number", value=0.0)

# Perform calculation
if st.button("Calculate"):
    if operation == "Add (+)":
        result = num1 + num2
        st.success(f"The result of addition is: {result}")
    elif operation == "Subtract (-)":
        result = num1 - num2
        st.success(f"The result of subtraction is: {result}")
    elif operation == "Multiply (×)":
        result = num1 * num2
        st.success(f"The result of multiplication is: {result}")
    elif operation == "Divide (÷)":
        if num2 != 0:
            result = num1 / num2
            st.success(f"The result of division is: {result}")
        else:
            st.error("Error: Division by zero is not allowed!")

# Footer
st.markdown("---")
st.caption("Developed with ❤️ using Streamlit")
