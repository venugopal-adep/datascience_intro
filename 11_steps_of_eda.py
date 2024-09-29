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
    st.title("Steps of EDA")
    st.write('**Developed by : Venugopal Adep**')
    
    tabs = st.tabs([
        "Steps of EDA",
        "Overview of Data",
        "Summary Statistics",
        "Univariate Analysis",
        "Bivariate Analysis",
        "Multivariate Analysis",
        "Key fixes and summarize",
        "Quiz"
    ])

    with tabs[0]:
        steps_of_eda_tab()

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

def steps_of_eda_tab():
    st.header("Steps of EDA")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Overview of Data")
        st.write("Gain basic understanding of the data - shape, data types, etc.")
        
        st.subheader("Summary Statistics")
        st.write("Check descriptive statistics about the data - mean, std, median, etc.")
        
        st.subheader("Univariate Analysis")
        st.write("Check distribution of variables in the data, missing values, outliers")
        
        st.subheader("Bivariate Analysis")
        st.write("Find the patterns or relationships between different variables")
        
        st.subheader("Multivariate Analysis")
        st.write("Explore more combination of variables to unearth deeper insights")
        
        st.subheader("Key fixes and summarize")
        st.write("Identify and do the key fixes in the data. Finally, summarize the key findings from EDA")
    
    with col2:
        st.image("https://raw.githubusercontent.com/your_username/your_repo/main/steps_of_eda.png", use_column_width=True)

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
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.write("Gain basic understanding of the data - shape, data types, etc.")
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
    
    with col2:
        st.write(data.head())

def summary_statistics_tab():
    st.header("Summary Statistics")
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.write("Check descriptive statistics about the data - mean, std, median, etc.")
        st.code("""
        # Display summary statistics
        print(data.describe())
        """)
    
    with col2:
        st.write(data.describe())

def univariate_analysis_tab():
    st.header("Univariate Analysis")
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.write("Check distribution of variables in the data, missing values, outliers")
        col = st.selectbox("Select a column for univariate analysis", data.columns)
        
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
    
    with col2:
        if data[col].dtype == 'object':
            fig = px.bar(data[col].value_counts().reset_index(), x='index', y='count', labels={'index': col, 'count': 'Count'})
        else:
            fig = px.histogram(data, x=col)
        
        st.plotly_chart(fig, use_container_width=True)

def bivariate_analysis_tab():
    st.header("Bivariate Analysis")
    left_col, right_col = st.columns([1, 1])
    
    with left_col:
        st.write("Find the patterns or relationships between different variables")
        var1 = st.selectbox("Select first variable", data.columns, key="var1")
        var2 = st.selectbox("Select second variable", data.columns, key="var2")
        
        st.code(f"""
        import plotly.express as px

        # If either variable is categorical
        if data['{var1}'].dtype == 'object' or data['{var2}'].dtype == 'object':
            fig = px.box(data, x='{var1}', y='{var2}')
        # If both variables are numerical
        else:
            fig = px.scatter(data, x='{var1}', y='{var2}')
        
        fig.show()
        """)
    
    with right_col:
        if data[var1].dtype == 'object' or data[var2].dtype == 'object':
            fig = px.box(data, x=var1, y=var2)
        else:
            fig = px.scatter(data, x=var1, y=var2)
        
        st.plotly_chart(fig, use_container_width=True)

def multivariate_analysis_tab():
    st.header("Multivariate Analysis")
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.write("Explore more combination of variables to unearth deeper insights")
        st.code("""
        import plotly.express as px

        # Create a scatter matrix plot
        fig = px.scatter_matrix(data)
        fig.show()
        """)
    
    with col2:
        fig = px.scatter_matrix(data)
        st.plotly_chart(fig, use_container_width=True)

def key_fixes_and_summarize_tab():
    st.header("Key fixes and summarize")
    col1, col2 = st.columns([1, 1])
    
    with col1:
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
    
    with col2:
        # Example plot for key fixes
        fig = px.box(data, x='Education', y='Income', title='Income Distribution by Education Level')
        st.plotly_chart(fig, use_container_width=True)

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
