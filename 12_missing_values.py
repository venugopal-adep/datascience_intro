import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide", page_title="Missing Values")

# Custom color palette
colors = {
    "primary": "#0066CC",
    "secondary": "#FF9900", 
    "accent": "#66CC99",
    "background": "#F0F8FF",
    "text": "#333333"
}

# Custom CSS
st.markdown(f"""
<style>
    .reportview-container .main .block-container{{
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }}
    .stApp {{
        background-color: {colors['background']};
    }}
    h1, h2, h3, h4, h5, h6 {{
        color: {colors['primary']};
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }}
    .stButton>button {{
        background-color: {colors['accent']};
        color: {colors['text']};
        font-weight: bold;
        border-radius: 5px;
        border: none;
        padding: 0.5rem 1rem;
        transition: all 0.3s ease;
    }}
    .stButton>button:hover {{
        background-color: {colors['secondary']};
        color: white;
    }}
    .plot-container {{
        display: flex;
        justify-content: center;
        align-items: center;
    }}
</style>
""", unsafe_allow_html=True)

def explain(text):
    st.markdown(f"""
    <div style='background-color: white; padding: 15px; border-radius: 5px; border-left: 5px solid {colors['accent']}; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
        <p style='color: {colors['text']}; margin: 0;'>{text}</p>
    </div>
    """, unsafe_allow_html=True)

def main():
    st.title("Missing Values in Data Preprocessing")
    st.write('**Developed by : Venugopal Adep**')
    
    tabs = st.tabs(["Learn", "Interactive Demo", "Quiz"])
    
    with tabs[0]:
        learn_tab()
    
    with tabs[1]:
        interactive_demo_tab()
    
    with tabs[2]:
        quiz_tab()

def learn_tab():
    st.header("What are missing values?")
    st.write("Missing values occur when no data value is stored for the variable in an observation.")
    st.write("Missing values can have a significant effect on the inferences that are drawn from the data.")
    
    st.header("What are different types of missing values?")
    st.write("1. Values which are not actually missing and represent some information about the data")
    explain("Example: Number of hours an employee works everyday. Missing values can mean that employee was absent or on leave that particular day.")
    
    st.write("2. Values which are actually missing and provide no information about the data")
    explain("Example: A weighing scale that is running out of batteries. Some data will simply be missing randomly.")

def generate_sample_data(n=100):
    np.random.seed(42)
    data = pd.DataFrame({
        'Employee_ID': range(1, n+1),
        'Hours_Worked': np.random.randint(0, 9, n),
        'Weight_Measurement': np.random.normal(70, 10, n)
    })
    
    # Introduce missing values
    data.loc[data['Hours_Worked'] == 0, 'Hours_Worked'] = np.nan
    data.loc[np.random.choice(data.index, 10), 'Weight_Measurement'] = np.nan
    
    return data

def interactive_demo_tab():
    st.header("Interactive Demo: Exploring Missing Values")
    
    data = generate_sample_data()
    
    st.subheader("Sample Data")
    st.write(data.head())
    
    st.subheader("Missing Value Analysis")
    missing_counts = data.isnull().sum()
    fig = px.bar(x=missing_counts.index, y=missing_counts.values, labels={'x': 'Column', 'y': 'Missing Count'})
    fig.update_layout(title="Missing Value Count by Column")
    st.plotly_chart(fig)
    
    st.subheader("Handling Missing Values")
    column = st.selectbox("Select a column to handle missing values", data.columns)
    method = st.radio("Select a method to handle missing values", ["Drop", "Fill with mean", "Fill with median"])
    
    if method == "Drop":
        data_cleaned = data.dropna(subset=[column])
    elif method == "Fill with mean":
        data_cleaned = data.fillna({column: data[column].mean()})
    else:
        data_cleaned = data.fillna({column: data[column].median()})
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("Original Data")
        st.write(data[column].describe())
    with col2:
        st.write("Cleaned Data")
        st.write(data_cleaned[column].describe())
    
    st.code(f"""
    # Handling missing values
    if method == "Drop":
        data_cleaned = data.dropna(subset=['{column}'])
    elif method == "Fill with mean":
        data_cleaned = data.fillna({{'{column}': data['{column}'].mean()}})
    else:
        data_cleaned = data.fillna({{'{column}': data['{column}'].median()}})
    """)

def quiz_tab():
    st.header("Quiz: Missing Values")
    
    questions = [
        {
            "question": "What are missing values in data?",
            "options": [
                "Values that are zero",
                "Values that are not stored for a variable in an observation",
                "Values that are very large",
                "Values that are negative"
            ],
            "correct": 1,
            "explanation": "Missing values occur when no data value is stored for a variable in an observation. This is different from zero values or extreme values, which are actual data points."
        },
        {
            "question": "Which of the following is an example of missing values that represent some information about the data?",
            "options": [
                "A weighing scale running out of batteries",
                "An employee's working hours showing as missing",
                "Random missing values in a dataset",
                "All of the above"
            ],
            "correct": 1,
            "explanation": "An employee's working hours showing as missing can indicate that the employee was absent or on leave that day. This missing value actually provides information about the employee's status, unlike random missing values or technical issues like a scale running out of batteries."
        },
        {
            "question": "How can missing values affect data analysis?",
            "options": [
                "They have no effect on analysis",
                "They always improve the accuracy of analysis",
                "They can significantly affect the inferences drawn from the data",
                "They only affect categorical variables"
            ],
            "correct": 2,
            "explanation": "Missing values can have a significant effect on the inferences drawn from the data. They can introduce bias, reduce the statistical power of analyses, and lead to incorrect conclusions if not handled properly."
        }
    ]
    
    score = 0
    for i, q in enumerate(questions):
        st.subheader(f"Question {i+1}")
        st.write(q["question"])
        answer = st.radio(f"Select your answer for question {i+1}:", q["options"], key=f"q{i}")
        if st.button(f"Submit Answer {i+1}"):
            if q["options"].index(answer) == q["correct"]:
                st.success("Correct!")
                score += 1
            else:
                st.error(f"Incorrect. The correct answer is: {q['options'][q['correct']]}")
            st.info(f"Explanation: {q['explanation']}")
    
    if st.button("Show Results"):
        st.write(f"Your score: {score}/{len(questions)}")
        if score == len(questions):
            st.balloons()
            st.success("Perfect score! You have a great understanding of missing values in data preprocessing!")
        elif score >= len(questions) / 2:
            st.success("Good job! You have a solid grasp of missing values concepts.")
        else:
            st.info("Keep learning! Review the content about missing values to improve your understanding.")

if __name__ == "__main__":
    main()