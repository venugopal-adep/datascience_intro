import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide", page_title="What and Why of Data Preprocessing?")

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
    st.title("What and Why of Data Preprocessing?")
    st.write('**Developed by : Venugopal Adep**')

    tabs = st.tabs([
        "Image Information",
        "What is Data Preprocessing?", 
        "Why Preprocess Data?", 
        "Data Preprocessing Techniques",
        "EDA and Preprocessing",
        "Quiz"
    ])

    with tabs[0]:
        image_information_tab()

    with tabs[1]:
        what_is_preprocessing_tab()

    with tabs[2]:
        why_preprocess_tab()

    with tabs[3]:
        preprocessing_techniques_tab()

    with tabs[4]:
        eda_and_preprocessing_tab()

    with tabs[5]:
        quiz_tab()

def explain(text):
    st.markdown(f"""
    <div style='background-color: white; padding: 15px; border-radius: 5px; border-left: 5px solid {colors['accent']}; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
        <p style='color: {colors['text']}; margin: 0;'>{text}</p>
    </div>
    """, unsafe_allow_html=True)

def image_information_tab():
    st.header("What and Why of Data Preprocessing?")

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("""
        Data preprocessing refers to the process of preparing the raw data into a structured format before building a machine learning model.

        - Raw data is often incomplete, inconsistent and has many other fallacies
        - This makes it inapt for any statistical analysis
            - It might lead to wrong insights
            - Decisions taken from this data can be counter productive for the organization
        - So you can't directly go from data to insights

        In the real world, the journey looks more like this:
        1. Raw Data
        2. Structure Data
        3. Exploratory Data Analysis and Data Preprocessing (iterative process)
        4. Insights, Visualizations
        """)

    with col2:
        fig, ax = plt.subplots(figsize=(8, 6))
        steps = ['Raw Data', 'Structure\nData', 'EDA &\nPreprocessing', 'Insights,\nVisualizations']
        x = np.arange(len(steps))
        ax.plot(x, [0, 0, 0, 0], 'o-', color=colors['primary'])
        ax.set_xticks(x)
        ax.set_xticklabels(steps)
        ax.set_yticks([])
        ax.spines['left'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.title("Data Processing Journey")
        st.pyplot(fig)

def what_is_preprocessing_tab():
    st.header("What is Data Preprocessing?")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.code("""
        import pandas as pd
        import numpy as np

        # Generate sample data
        data = pd.DataFrame({
            'Age': np.random.randint(18, 80, 1000),
            'Income': np.random.normal(50000, 15000, 1000),
            'Education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD', None], 1000),
            'Customer_Score': np.random.uniform(0, 100, 1000)
        })

        # Add some issues
        data.loc[np.random.choice(data.index, 50), 'Income'] = np.nan
        data.loc[np.random.choice(data.index, 10), 'Age'] = 0

        # Preprocessing steps
        data_cleaned = data.dropna()
        data_cleaned = data_cleaned[data_cleaned['Age'] > 0]
        data_encoded = pd.get_dummies(data_cleaned, columns=['Education'])

        print(data_encoded.head())
        """, language="python")

    with col2:
        st.markdown("""
        Data preprocessing involves:
        
        - Cleaning and handling missing data
        - Transforming data into a suitable format
        - Reducing noise and correcting inconsistencies
        - Normalizing or scaling features
        - Encoding categorical variables
        
        The code example demonstrates:
        1. Generating sample data
        2. Introducing common data issues
        3. Handling missing values
        4. Removing erroneous entries
        5. Encoding categorical variables
        """)

def why_preprocess_tab():
    st.header("Why Preprocess Data?")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.code("""
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt

        # Generate sample data with outliers
        np.random.seed(0)
        data = pd.DataFrame({
            'Value': np.random.normal(100, 20, 1000)
        })
        data.loc[np.random.choice(data.index, 10), 'Value'] = 1000

        # Plot before preprocessing
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.hist(data['Value'], bins=50)
        plt.title("Before Preprocessing")

        # Preprocess: Remove outliers
        data_cleaned = data[data['Value'] < 500]

        # Plot after preprocessing
        plt.subplot(1, 2, 2)
        plt.hist(data_cleaned['Value'], bins=50)
        plt.title("After Preprocessing")

        plt.tight_layout()
        plt.show()
        """, language="python")

    with col2:
        explain("""
        Preprocessing is crucial because:
        - Raw data often contains inconsistencies and errors
        - It makes data suitable for analysis and modeling
        - It helps avoid wrong insights and decisions
        - It's a necessary step before deriving meaningful insights

        The code example shows how preprocessing (removing outliers) 
        can dramatically change the distribution of data, leading to 
        more accurate analysis and insights.
        """)

def preprocessing_techniques_tab():
    st.header("Data Preprocessing Techniques")
    
    techniques = [
        "Handling missing data",
        "Outlier detection and treatment",
        "Feature scaling",
        "Encoding categorical variables",
        "Feature selection and dimensionality reduction"
    ]
    
    for technique in techniques:
        st.markdown(f"- {technique}")
    
    explain("Different preprocessing techniques are applied based on the nature of the data and the requirements of the subsequent analysis or modeling.")

def eda_and_preprocessing_tab():
    st.header("EDA and Preprocessing")
    
    st.markdown("""
    The real-world journey from raw data to insights involves:
    1. Raw Data
    2. Structure Data
    3. Exploratory Data Analysis (EDA) and Data Preprocessing (iterative process)
    4. Insights, Visualizations
    """)
    
    explain("EDA and preprocessing work hand in hand in an iterative process to prepare data for analysis and modeling.")

def quiz_tab():
    st.header("Data Preprocessing Quiz")
    
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
            "question": "Why is raw data often unsuitable for direct analysis?",
            "options": [
                "It's too colorful",
                "It's always perfectly structured",
                "It's often incomplete, inconsistent, and has many fallacies",
                "Raw data is always suitable for analysis"
            ],
            "correct": 2
        },
        {
            "question": "What is the relationship between EDA and Data Preprocessing?",
            "options": [
                "They are completely unrelated",
                "EDA comes after all preprocessing is complete",
                "Preprocessing comes after all EDA is complete",
                "They work together in an iterative cycle"
            ],
            "correct": 3
        }
    ]
    
    for i, q in enumerate(questions):
        st.subheader(f"Question {i+1}")
        st.write(q["question"])
        answer = st.radio(f"Select your answer for question {i+1}:", q["options"], key=f"q{i}")
        if st.button(f"Submit Answer {i+1}"):
            if q["options"].index(answer) == q["correct"]:
                st.success("Correct!")
            else:
                st.error(f"Incorrect. The correct answer is: {q['options'][q['correct']]}")

if __name__ == "__main__":
    main()
