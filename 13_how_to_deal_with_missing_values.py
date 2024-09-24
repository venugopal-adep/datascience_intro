import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide", page_title="How to deal with missing values?")

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
    st.title("How to Deal with Missing Values")
    st.write('**Developed by : Venugopal Adep**')
    
    tabs = st.tabs(["Learn", "Interactive Demo", "Quiz"])
    
    with tabs[0]:
        learn_tab()
    
    with tabs[1]:
        interactive_demo_tab()
    
    with tabs[2]:
        quiz_tab()

def learn_tab():
    st.header("Dealing with Missing Values")
    
    st.subheader("1. Values Not Actually Missing")
    st.write("If values are not actually missing, we can replace the missing values with the value they actually represent in the data.")
    explain("Example: We can replace all the missing working hours of an employee with 0.")
    
    st.subheader("2. Values Actually Missing")
    st.write("If values are actually missing, we must explore the importance and extent of missing values in the data.")
    
    st.write("a. Large Percentage of Missing Values")
    explain("If the variables have a large percentage of missing values (say more than 70%) and is not significant for our analysis, then we can drop that variable.")
    
    st.write("b. Small Percentage of Missing Values or Significant Variable")
    st.write("If the percentage of missing values is small or the variable is significant for our analysis, we can replace the missing values using:")
    st.write("- Mean or median of that variable if the variable is continuous")
    st.write("- Mode of that variable if the variable is categorical")
    st.write("- Sometimes we use functions like min, max, etc. to replace the missing values depending on the dataset")

def generate_sample_data(n=100):
    np.random.seed(42)
    data = pd.DataFrame({
        'Employee_ID': range(1, n+1),
        'Working_Hours': np.random.randint(0, 9, n),
        'Salary': np.random.normal(50000, 10000, n),
        'Department': np.random.choice(['HR', 'IT', 'Finance', 'Marketing'], n)
    })
    
    # Introduce missing values
    data.loc[np.random.choice(data.index, 10), 'Working_Hours'] = np.nan
    data.loc[np.random.choice(data.index, 5), 'Salary'] = np.nan
    data.loc[np.random.choice(data.index, 3), 'Department'] = np.nan
    
    return data

def interactive_demo_tab():
    st.header("Interactive Demo: Dealing with Missing Values")
    
    data = generate_sample_data()
    
    st.subheader("Sample Data")
    st.write(data.head())
    
    st.subheader("Missing Value Analysis")
    missing_percentages = (data.isnull().sum() / len(data)) * 100
    fig = px.bar(x=missing_percentages.index, y=missing_percentages.values, 
                 labels={'x': 'Column', 'y': 'Missing Percentage'},
                 title="Percentage of Missing Values by Column")
    st.plotly_chart(fig)
    
    st.subheader("Handling Missing Values")
    column = st.selectbox("Select a column to handle missing values", data.columns)
    
    if data[column].dtype == 'object':
        method = st.radio("Select a method to handle missing values", 
                          ["Drop", "Fill with mode", "Fill with a custom value"])
    else:
        method = st.radio("Select a method to handle missing values", 
                          ["Drop", "Fill with mean", "Fill with median", "Fill with a custom value"])
    
    if method == "Drop":
        data_cleaned = data.dropna(subset=[column])
    elif method == "Fill with mean":
        data_cleaned = data.fillna({column: data[column].mean()})
    elif method == "Fill with median":
        data_cleaned = data.fillna({column: data[column].median()})
    elif method == "Fill with mode":
        data_cleaned = data.fillna({column: data[column].mode()[0]})
    else:
        custom_value = st.text_input("Enter a custom value")
        if custom_value:
            data_cleaned = data.fillna({column: custom_value})
        else:
            data_cleaned = data.copy()
    
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
    elif method == "Fill with median":
        data_cleaned = data.fillna({{'{column}': data['{column}'].median()}})
    elif method == "Fill with mode":
        data_cleaned = data.fillna({{'{column}': data['{column}'].mode()[0]}})
    else:
        data_cleaned = data.fillna({{'{column}': custom_value}})
    """)

def quiz_tab():
    st.header("Quiz: Dealing with Missing Values")
    
    questions = [
        {
            "question": "What should we do if the missing values are not actually missing but represent some information?",
            "options": [
                "Always drop the rows with missing values",
                "Replace the missing values with the value they actually represent",
                "Use the mean of the column to fill missing values",
                "Ignore the missing values"
            ],
            "correct": 1,
            "explanation": "If values are not actually missing but represent some information (like 0 hours worked), we should replace the missing values with the value they actually represent in the data."
        },
        {
            "question": "When is it appropriate to drop a variable with missing values?",
            "options": [
                "When the variable has more than 70% missing values and is not significant for the analysis",
                "When the variable has any missing values",
                "When the variable is categorical",
                "When the variable is continuous"
            ],
            "correct": 0,
            "explanation": "If a variable has a large percentage of missing values (e.g., more than 70%) and is not significant for our analysis, we can consider dropping that variable."
        },
        {
            "question": "What method is typically used to fill missing values in a continuous variable?",
            "options": [
                "Mode",
                "Minimum value",
                "Mean or median",
                "Maximum value"
            ],
            "correct": 2,
            "explanation": "For continuous variables, we typically use the mean or median of the variable to fill missing values, especially if the percentage of missing values is small or the variable is significant for our analysis."
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
            st.success("Perfect score! You have a great understanding of how to deal with missing values!")
        elif score >= len(questions) / 2:
            st.success("Good job! You have a solid grasp of dealing with missing values.")
        else:
            st.info("Keep learning! Review the content about dealing with missing values to improve your understanding.")

if __name__ == "__main__":
    main()