import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide", page_title="Steps of EDA")

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

def main():
    st.title("Data Preprocessing and EDA Demo")
    st.write('**Developed by : Venugopal Adep**')
    
    tabs = st.tabs([
        "Learn",
        "Overview of Data",
        "Summary Statistics",
        "Univariate Analysis",
        "Bivariate Analysis",
        "Multivariate Analysis",
        "Key fixes and summarize",
        "Quiz"
    ])

    with tabs[0]:
        learn_tab()

    with tabs[1]:
        overview_of_data_tab()

    with tabs[2]:
        summary_statistics_tab()

    with tabs[3]:
        univariate_analysis_tab()

    with tabs[4]:
        bivariate_analysis_tab()

    with tabs[5]:
        multivariate_analysis_tab()

    with tabs[6]:
        key_fixes_and_summarize_tab()

    with tabs[7]:
        quiz_tab()

def explain(text):
    st.markdown(f"""
    <div style='background-color: white; padding: 15px; border-radius: 5px; border-left: 5px solid {colors['accent']}; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
        <p style='color: {colors['text']}; margin: 0;'>{text}</p>
    </div>
    """, unsafe_allow_html=True)

def learn_tab():
    st.header("Learn about Data Preprocessing and EDA")
    
    st.subheader("What is Data Preprocessing?")
    st.markdown("""
    Data preprocessing refers to the process of preparing raw data into a structured format before building a machine learning model or performing analysis. It involves:
    
    - Cleaning and handling missing data
    - Transforming data into a suitable format
    - Reducing noise and correcting inconsistencies
    - Normalizing or scaling features
    - Encoding categorical variables
    """)
    explain("Data preprocessing is a crucial step that transforms raw data into a format that's more suitable for analysis and modeling.")

    st.subheader("Why Preprocess Data?")
    st.markdown("""
    Preprocessing data is crucial because:
    - Raw data is often incomplete, inconsistent, and has many fallacies
    - It makes the data suitable for statistical analysis and machine learning
    - It helps avoid wrong insights and counter-productive decisions
    - It's a necessary step before moving from data to insights
    """)
    explain("Preprocessing ensures that your data is in the best possible shape for analysis, reducing errors and improving the quality of insights.")

    st.subheader("Data Preprocessing Techniques")
    st.markdown("""
    Common preprocessing techniques include:
    - Handling missing data (deletion or imputation)
    - Outlier detection and treatment
    - Feature scaling (normalization, standardization)
    - Encoding categorical variables
    - Feature selection and dimensionality reduction
    """)
    explain("Different preprocessing techniques are used depending on the nature of the data and the requirements of the subsequent analysis or modeling.")

    st.subheader("EDA and Preprocessing")
    st.markdown("""
    Exploratory Data Analysis (EDA) and preprocessing are closely related:
    - EDA helps identify preprocessing needs (e.g., missing values, outliers)
    - Preprocessing improves the quality of EDA insights
    - Both are iterative processes that inform each other
    """)
    explain("EDA and preprocessing work hand in hand to prepare data for analysis and modeling, often in an iterative cycle.")

# Generate sample data
np.random.seed(0)
data = pd.DataFrame({
    'Age': np.random.randint(18, 80, 1000),
    'Income': np.random.normal(50000, 15000, 1000),
    'Education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], 1000),
    'Satisfaction': np.random.randint(1, 6, 1000)
})

def overview_of_data_tab():
    st.header("Overview of Data")
    st.write("Gain basic understanding of the data - shape, data types, etc.")
    st.write(data.head())
    st.write(f"Data shape: {data.shape}")
    st.write(data.dtypes)

    st.code("""
    # View the first few rows of the data
    print(data.head())

    # Check the shape of the data
    print(f"Data shape: {data.shape}")

    # Display data types of each column
    print(data.dtypes)
    """)

def summary_statistics_tab():
    st.header("Summary Statistics")
    st.write("Check descriptive statistics about the data - mean, std, median, etc.")
    st.write(data.describe())

    st.code("""
    # Display summary statistics
    print(data.describe())
    """)

def univariate_analysis_tab():
    st.header("Univariate Analysis")
    st.write("Check distribution of variables in the data, missing values, outliers")
    col = st.selectbox("Select a column for univariate analysis", data.columns)
    
    if data[col].dtype == 'object':
        fig = px.bar(data[col].value_counts().reset_index(), x='index', y='count', labels={'index': col, 'count': 'Count'})
    else:
        fig = px.histogram(data, x=col)
    
    st.plotly_chart(fig)

    st.code(f"""
    import plotly.express as px

    # For categorical variables
    if data['{col}'].dtype == 'object':
        fig = px.bar(data['{col}'].value_counts().reset_index(), x='index', y='count', labels={{'index': '{col}', 'count': 'Count'}})
    # For numerical variables
    else:
        fig = px.histogram(data, x='{col}')
    
    fig.show()
    """)

def bivariate_analysis_tab():
    st.header("Bivariate Analysis")
    st.write("Find the patterns or relationships between different variables")
    col1 = st.selectbox("Select first variable", data.columns)
    col2 = st.selectbox("Select second variable", data.columns)
    
    if data[col1].dtype == 'object' or data[col2].dtype == 'object':
        fig = px.box(data, x=col1, y=col2)
    else:
        fig = px.scatter(data, x=col1, y=col2)
    
    st.plotly_chart(fig)

    st.code(f"""
    import plotly.express as px

    # If either variable is categorical
    if data['{col1}'].dtype == 'object' or data['{col2}'].dtype == 'object':
        fig = px.box(data, x='{col1}', y='{col2}')
    # If both variables are numerical
    else:
        fig = px.scatter(data, x='{col1}', y='{col2}')
    
    fig.show()
    """)

def multivariate_analysis_tab():
    st.header("Multivariate Analysis")
    st.write("Explore more combination of variables to unearth deeper insights")
    fig = px.scatter_matrix(data)
    st.plotly_chart(fig)

    st.code("""
    import plotly.express as px

    # Create a scatter matrix plot
    fig = px.scatter_matrix(data)
    fig.show()
    """)

def key_fixes_and_summarize_tab():
    st.header("Key fixes and summarize")
    st.write("Identify and do the key fixes in the data. Finally, summarize the key findings from EDA")
    st.write("Based on our EDA, we might want to:")
    st.write("1. Handle any outliers in the Income column")
    st.write("2. Encode the Education column for machine learning models")
    st.write("3. Investigate the relationship between Age, Income, and Satisfaction")
    st.write("4. Consider feature engineering, such as creating age groups")

    st.code("""
    # Example of handling outliers
    Q1 = data['Income'].quantile(0.25)
    Q3 = data['Income'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    data_cleaned = data[(data['Income'] >= lower_bound) & (data['Income'] <= upper_bound)]

    # Example of encoding categorical variables
    data_encoded = pd.get_dummies(data, columns=['Education'])

    # Example of feature engineering
    data['Age_Group'] = pd.cut(data['Age'], bins=[0, 25, 35, 45, 55, 100], labels=['18-25', '26-35', '36-45', '46-55', '55+'])

    # Summarize findings
    print("Key findings from EDA:")
    print("1. Income distribution and potential outliers")
    print("2. Relationship between Education and Income")
    print("3. Correlation between Age, Income, and Satisfaction")
    print("4. Distribution of Age Groups")
    """)

def quiz_tab():
    st.header("Data Preprocessing and EDA Quiz")
    
    explain("Test your knowledge of data preprocessing and EDA concepts!")
    
    questions = [
        {
            "question": "What is the main purpose of data preprocessing?",
            "options": [
                "To make the data look prettier",
                "To prepare raw data into a structured format for analysis or modeling",
                "To delete all the data",
                "To create more data"
            ],
            "correct": 1
        },
        {
            "question": "Which of the following is NOT a common preprocessing technique?",
            "options": [
                "Handling missing data",
                "Feature scaling",
                "Deleting all categorical variables",
                "Encoding categorical variables"
            ],
            "correct": 2
        },
        {
            "question": "What is the purpose of univariate analysis in EDA?",
            "options": [
                "To explore relationships between multiple variables",
                "To check the distribution of a single variable",
                "To create predictive models",
                "To encode categorical variables"
            ],
            "correct": 1
        },
        {
            "question": "Which plot is most suitable for exploring the relationship between two continuous variables?",
            "options": [
                "Bar plot",
                "Pie chart",
                "Scatter plot",
                "Box plot"
            ],
            "correct": 2
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
    
    if st.button("Show Results"):
        st.write(f"Your score: {score}/{len(questions)}")
        if score == len(questions):
            st.balloons()
            st.success("Perfect score! You're a data preprocessing and EDA expert!")
        elif score >= len(questions) / 2:
            st.success("Good job! You have a solid understanding of data preprocessing and EDA.")
        else:
            st.info("Keep learning! Review the other tabs to improve your understanding of data preprocessing and EDA.")

if __name__ == "__main__":
    main()