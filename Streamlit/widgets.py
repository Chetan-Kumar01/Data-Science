import streamlit as st
import pandas as pd

# Step 1: Create a sample DataFrame
data = {
    "Name": ["John", "Emma", "Alex", "Sophia"],
    "Age": [25, 30, 28, 22],
    "City": ["Delhi", "Mumbai", "Pune", "Chennai"]
}
df = pd.DataFrame(data)

# Step 2: Save the DataFrame as a CSV file
df.to_csv("sampledata.csv", index=False)   # <-- yahi line hum explain kar rahe the

st.write("✅ Here is a sample dataframe:")
st.write(df)

# Step 3: Let user upload any file
uploaded_file = st.file_uploader("📁 Upload a file", type=["csv", "txt", "xlsx", "mp4","mov","avi","mkv"])

# Step 4: If a file is uploaded
if uploaded_file is not None:
    file_name = uploaded_file.name

    if file_name.endswith(".csv") or file_name.endswith(".txt"):
        uploaded_df = pd.read_csv(uploaded_file)
        st.write("📊 Uploaded CSV/Text file:")
        st.write(uploaded_df)

    elif file_name.endswith(".xlsx"):
        uploaded_df = pd.read_excel(uploaded_file)
        st.write("📊 Uploaded Excel file:")
        st.write(uploaded_df)

    elif file_name.endswith((".mp4", ".mov", ".avi", ".mkv")):
        st.video(uploaded_file)

    else:
        st.warning("⚠️ File format not supported.")
