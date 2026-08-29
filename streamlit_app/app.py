import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

st.title("RAG App Test")
st.write("Streamlit UI loaded successfully")

load_dotenv()

llm= ChatGoogleGenerativeAI(model="gemini-3.6-flash")

st.set_page_config(page_title="Bloodwork Analysis", layout="centered")
st.title("🩸 Bloodwork Analysis & Diet Plan Generator")

st.write("Upload your blood report as a `.txt` file to get an extracted analysis and a personalized Indian diet plan.")

uploaded_file = st.file_uploader("Upload bloodwork.txt", type=["txt"])

if uploaded_file is not None:
    bloodreport = uploaded_file.read().decode("utf-8")

    st.subheader("📄 Uploaded Blood Report")
    st.text(bloodreport[:200])

    if st.button("Run Analysis"):
        with st.spinner("Extracting values from bloodwork..."):
            extraction_prompt=f"""
You are medical data extraction assistant
From the blood reports below, extract all TEST values, and classify each one as HIGH, LOW, OR NORMAL
Use the format below for reference to show the results
- Test Name: value| Status: HIGH/LOW/NORMAL| Reference: range

Blood report:
{bloodreport}"""
            extraction_response=llm.invoke(extraction_prompt)
            extracted_values=extraction_response.text
            st.subheader("=== Stage 1: Extracted Values ===")
            st.text(extracted_values)

        with st.spinner("Generating diet plan..."):
            Diet_prompt=f"""
You are professional nutrional specialist in Indian Diet System.
Based on the blood reports extracted
- Prepare a brief summary of 4-5 lines.
- Prepare a proper diet plan with having (1) foods to avoid (2) foods to consume more accordingly.
Don't include any other thing in diet plan, and keep it simple as possible

Bloodwork analysis:
{extracted_values}"""
            Diet_response=llm.invoke(Diet_prompt)
            st.subheader(" ==== DIET PLAN  ==== ")
            st.markdown(Diet_response.text)
else:
    st.info("Please upload a bloodwork .txt file to begin.")