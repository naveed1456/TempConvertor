import streamlit as st

# Title
st.title("Temperature Converter")

# Radio buttons for unit selection
unit = st.radio("Select Unit:", ("Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"))

# Input for temperature
temp = st.number_input("Enter Temperature:", value=0.0, format="%.2f")

# Convert button
if st.button("Convert"):
    # Conversion logic
    if unit == "Celsius (°C)":
        f = (temp * 9/5) + 32
        k = temp + 273.15
        st.write(f"**{temp:.2f} °C = {f:.2f} °F**")
        st.write(f"**{temp:.2f} °C = {k:.2f} K**")

    elif unit == "Fahrenheit (°F)":
        c = (temp - 32) * 5/9
        k = c + 273.15
        st.write(f"**{temp:.2f} °F = {c:.2f} °C**")
        st.write(f"**{temp:.2f} °F = {k:.2f} K**")

    elif unit == "Kelvin (K)":
        c = temp - 273.15
        f = (c * 9/5) + 32
        st.write(f"**{temp:.2f} K = {c:.2f} °C**")
        st.write(f"**{temp:.2f} K = {f:.2f} °F**")
