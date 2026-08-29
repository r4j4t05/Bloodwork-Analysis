# Bloodwork Analysis & Diet Plan Generator

An AI-powered health analysis application that extracts information from bloodwork reports, identifies abnormal test results, and generates a personalized Indian diet plan based on the detected health indicators.

The application provides a simple interface where users can upload their blood report as a `.txt` file and receive an easy-to-understand analysis along with dietary recommendations.
---

# Features

# Blood Report Upload
- Upload bloodwork reports in `.txt` format.
- Automatically extracts relevant laboratory values from the uploaded report.
- Displays the uploaded report for transparency.

# Bloodwork Extraction
The application extracts and evaluates common blood parameters such as:

- Hemoglobin
- Hematocrit
- WBC
- Platelets
- Total Cholesterol
- LDL Cholesterol
- HDL Cholesterol
- Triglycerides
- Fasting Glucose
- HbA1c
- Creatinine
- eGFR
- ALT
- AST
- Total Bilirubin

Each parameter is evaluated against its corresponding reference range.

# Health Analysis
The extracted results are categorized into statuses such as:
- `NORMAL`
- `HIGH`
- `LOW`

The application then summarizes the overall bloodwork and highlights areas that may require dietary attention.

# Personalized Indian Diet Plan

Based on the detected abnormalities, the application generates dietary recommendations tailored toward Indian food habits.
The generated plan can include:

# Foods to Avoid
Examples include:

- Deep-fried foods
- Samosas
- Pakoras
- Puris
- Bhujia
- Excessive ghee and butter
- Vanaspati/dalda
- High-fat dairy
- Refined flour products
- Excessively rich meat dishes

# Foods to Consume More
Examples include:

- Oats
- Barley (Jau)
- Ragi
- Jowar
- Bajra
- Brown/unpolished rice
- Dal and legumes
- Rajma
- Chickpeas
- Walnuts
- Flaxseeds
- Chia seeds
- Vegetables
- Seasonal fruits
- Low-fat dairy
- Buttermilk

---

# Application Workflow

```text
                    ┌─────────────────────┐
                    │ Upload Blood Report │
                    │      (.txt)         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Extract Bloodwork   │
                    │      Values         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Compare With        │
                    │ Reference Ranges    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Identify Abnormal   │
                    │     Parameters      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Generate Health     │
                    │     Summary         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Generate Indian     │
                    │    Diet Plan        │
                    └─────────────────────┘
