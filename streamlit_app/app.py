import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    thinking_level="low",
    timeout=60,
    max_retries=1
)

# Page configuration
st.set_page_config(
    page_title="Bloodwork Analysis",
    layout="centered"
)

# App title
st.title("🩸 Bloodwork Analysis & Diet Plan Generator")

st.write(
    "Upload your blood report as a `.txt` file "
    "to get an extracted analysis and a personalized Indian diet plan."
)

# Upload blood report
uploaded_file = st.file_uploader(
    "Upload bloodwork.txt",
    type=["txt"]
)

if uploaded_file is not None:

    # Read uploaded file
    bloodreport = uploaded_file.read().decode("utf-8")

    # Display uploaded report
    st.subheader("📄 Uploaded Blood Report")
    st.text(bloodreport[:200])

    # Run analysis button
    if st.button("Run Analysis"):

        # --------------------------------------------------
        # STAGE 1: Extract blood test values
        # --------------------------------------------------

        with st.spinner("Extracting values from bloodwork..."):

            extraction_prompt = f"""
You are a medical data extraction assistant.

Extract every blood test from the report below.

For each test, return exactly this format:

- Test Name: value | Status: HIGH/LOW/NORMAL | Reference: range

Classify each value as HIGH, LOW, or NORMAL using the reference range
provided in the report.

Do not provide explanations.
Do not provide medical advice.
Do not omit any test.

Blood report:
{bloodreport}
"""

            extraction_response = llm.invoke(extraction_prompt)

            extracted_values = extraction_response.text

            st.subheader("=== Stage 1: Extracted Values ===")
            st.text(extracted_values)

        # --------------------------------------------------
        # STAGE 2: Generate diet plan
        # --------------------------------------------------

        with st.spinner("Generating diet plan..."):

            diet_prompt = f"""
You are a professional nutritional specialist in Indian Diet System.

Based on the blood report analysis below:

- Prepare a brief summary of 4-5 lines.
- Prepare a simple diet plan containing:
  1. Foods to avoid
  2. Foods to consume more

Don't include anything else in the diet plan.
Keep it as simple as possible.

Bloodwork analysis:
{extracted_values}
"""

            diet_response = llm.invoke(diet_prompt)

            st.subheader("==== DIET PLAN ====")
            st.markdown(diet_response.text)

else:

    st.info("Please upload a bloodwork .txt file to begin.")