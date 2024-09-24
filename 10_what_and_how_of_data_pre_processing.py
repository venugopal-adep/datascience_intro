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
    st.title("Data Preprocessing and EDA Demo")
    st.write('**Developed by : Venugopal Adep**')

    st.markdown(f"""
    <p style='font-size: 1.2em; color: {colors['text']}; background-color: white; padding: 15px; border-radius: 5px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
    Welcome to the Data Preprocessing and Exploratory Data Analysis (EDA) demo! This app will help you understand 
    the importance of data preprocessing and how it relates to EDA in the data analysis process.
    </p>
    """, unsafe_allow_html=True)

    tabs = st.tabs([
        "What is Data Preprocessing?", 
        "Why Preprocess Data?", 
        "Data Preprocessing Techniques",
        "EDA and Preprocessing",
        "Quiz"  # New tab
    ])

    with tabs[0]:
        what_is_preprocessing_tab()

    with tabs[1]:
        why_preprocess_tab()

    with tabs[2]:
        preprocessing_techniques_tab()

    with tabs[3]:
        eda_and_preprocessing_tab()

    with tabs[4]:
        quiz_tab()

def explain(text):
    st.markdown(f"""
    <div style='background-color: white; padding: 15px; border-radius: 5px; border-left: 5px solid {colors['accent']}; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
        <p style='color: {colors['text']}; margin: 0;'>{text}</p>
    </div>
    """, unsafe_allow_html=True)

def what_is_preprocessing_tab():
    st.header("What is Data Preprocessing?")
    
    st.markdown("""
    Data preprocessing refers to the process of preparing raw data into a structured format before building a machine learning model or performing analysis. It involves:
    
    - Cleaning and handling missing data
    - Transforming data into a suitable format
    - Reducing noise and correcting inconsistencies
    - Normalizing or scaling features
    - Encoding categorical variables
    """)
    
    explain("Data preprocessing is a crucial step that transforms raw data into a format that's more suitable for analysis and modeling.")
    
    # Interactive example
    st.subheader("Interactive Preprocessing Example")
    
    # Generate sample data with issues
    np.random.seed(0)
    data = pd.DataFrame({
        'Age': np.random.randint(18, 80, 1000),
        'Income': np.random.normal(50000, 15000, 1000),
        'Education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD', None], 1000),
        'Customer_Score': np.random.uniform(0, 100, 1000)
    })
    data.loc[np.random.choice(data.index, 50), 'Income'] = np.nan  # Add some missing values
    data.loc[np.random.choice(data.index, 10), 'Age'] = 0  # Add some errors
    
    preprocessing_step = st.selectbox("Choose a preprocessing step", ["Raw Data", "Handle Missing Values", "Remove Errors", "Encode Categories"])
    
    if preprocessing_step == "Raw Data":
        st.write(data.head())
        st.write(f"Data shape: {data.shape}")
    elif preprocessing_step == "Handle Missing Values":
        data_cleaned = data.dropna()
        st.write(data_cleaned.head())
        st.write(f"Data shape after handling missing values: {data_cleaned.shape}")
    elif preprocessing_step == "Remove Errors":
        data_cleaned = data[data['Age'] > 0]
        st.write(data_cleaned.head())
        st.write(f"Data shape after removing errors: {data_cleaned.shape}")
    else:  # Encode Categories
        data_encoded = pd.get_dummies(data, columns=['Education'])
        st.write(data_encoded.head())
        st.write(f"Data shape after encoding categories: {data_encoded.shape}")
    
    st.code(f"""
    import pandas as pd
    import numpy as np

    # Generate and preprocess data
    data = pd.DataFrame({{
        'Age': np.random.randint(18, 80, 1000),
        'Income': np.random.normal(50000, 15000, 1000),
        'Education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD', None], 1000),
        'Customer_Score': np.random.uniform(0, 100, 1000)
    }})
    data.loc[np.random.choice(data.index, 50), 'Income'] = np.nan
    data.loc[np.random.choice(data.index, 10), 'Age'] = 0

    # Code for {preprocessing_step.lower()}
    {"# No preprocessing" if preprocessing_step == "Raw Data" else 
     "data_cleaned = data.dropna()" if preprocessing_step == "Handle Missing Values" else 
     "data_cleaned = data[data['Age'] > 0]" if preprocessing_step == "Remove Errors" else 
     "data_encoded = pd.get_dummies(data, columns=['Education'])"}
    """, language="python")

def why_preprocess_tab():
    st.header("Why Preprocess Data?")
    
    st.markdown("""
    Preprocessing data is crucial because:
    - Raw data is often incomplete, inconsistent, and has many fallacies
    - It makes the data suitable for statistical analysis and machine learning
    - It helps avoid wrong insights and counter-productive decisions
    - It's a necessary step before moving from data to insights
    """)
    
    explain("Preprocessing ensures that your data is in the best possible shape for analysis, reducing errors and improving the quality of insights.")
    
    # Interactive example
    st.subheader("Impact of Preprocessing")
    
    # Generate sample data with outliers
    np.random.seed(0)
    data = pd.DataFrame({
        'Value': np.random.normal(100, 20, 1000)
    })
    data.loc[np.random.choice(data.index, 10), 'Value'] = 1000  # Add some outliers
    
    preprocess = st.checkbox("Remove Outliers")
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    sns.histplot(data=data, x='Value', kde=True, ax=ax1)
    ax1.set_title("Distribution of Values")
    
    if preprocess:
        data_cleaned = data[data['Value'] < 500]
        sns.histplot(data=data_cleaned, x='Value', kde=True, ax=ax2)
        ax2.set_title("Distribution After Removing Outliers")
    else:
        ax2.set_visible(False)
    
    st.pyplot(fig)
    
    st.code(f"""
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt

    # Generate data with outliers
    data = pd.DataFrame({{
        'Value': np.random.normal(100, 20, 1000)
    }})
    data.loc[np.random.choice(data.index, 10), 'Value'] = 1000

    # Plotting
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    sns.histplot(data=data, x='Value', kde=True, ax=ax1)
    ax1.set_title("Distribution of Values")

    {"# Remove outliers" if preprocess else "# No preprocessing"}
    {"data_cleaned = data[data['Value'] < 500]" if preprocess else ""}
    {"sns.histplot(data=data_cleaned, x='Value', kde=True, ax=ax2)" if preprocess else ""}
    {"ax2.set_title('Distribution After Removing Outliers')" if preprocess else ""}

    plt.show()
    """, language="python")

def preprocessing_techniques_tab():
    st.header("Data Preprocessing Techniques")
    
    st.markdown("""
    Common preprocessing techniques include:
    - Handling missing data (deletion or imputation)
    - Outlier detection and treatment
    - Feature scaling (normalization, standardization)
    - Encoding categorical variables
    - Feature selection and dimensionality reduction
    """)
    
    explain("Different preprocessing techniques are used depending on the nature of the data and the requirements of the subsequent analysis or modeling.")
    
    # Interactive example
    st.subheader("Interactive Preprocessing Technique")
    
    # Generate sample data
    np.random.seed(0)
    data = pd.DataFrame({
        'Numeric': np.random.normal(0, 1, 1000),
        'Categorical': np.random.choice(['A', 'B', 'C', None], 1000),
    })
    
    technique = st.selectbox("Choose a preprocessing technique", ["Handle Missing Values", "Encode Categories", "Scale Features"])
    
    if technique == "Handle Missing Values":
        method = st.radio("Select method", ["Drop", "Fill with mode"])
        if method == "Drop":
            data_processed = data.dropna()
        else:
            data_processed = data.fillna(data['Categorical'].mode()[0])
        st.write(data_processed.head())
        st.write(f"Missing values after processing: {data_processed.isnull().sum()}")
    elif technique == "Encode Categories":
        data_processed = pd.get_dummies(data, columns=['Categorical'])
        st.write(data_processed.head())
    else:  # Scale Features
        from sklearn.preprocessing import StandardScaler
        scaler = StandardScaler()
        data['Numeric_Scaled'] = scaler.fit_transform(data[['Numeric']])
        st.write(data.head())
    
    st.code(f"""
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import StandardScaler

    data = pd.DataFrame({{
        'Numeric': np.random.normal(0, 1, 1000),
        'Categorical': np.random.choice(['A', 'B', 'C', None], 1000),
    }})

    # Code for {technique.lower()}
    {"data_processed = data.dropna()" if technique == "Handle Missing Values" and method == "Drop" else 
     "data_processed = data.fillna(data['Categorical'].mode()[0])" if technique == "Handle Missing Values" else 
     "data_processed = pd.get_dummies(data, columns=['Categorical'])" if technique == "Encode Categories" else 
     "scaler = StandardScaler()\ndata['Numeric_Scaled'] = scaler.fit_transform(data[['Numeric']])"}
    """, language="python")

def eda_and_preprocessing_tab():
    st.header("EDA and Preprocessing")
    
    st.markdown("""
    Exploratory Data Analysis (EDA) and preprocessing are closely related:
    - EDA helps identify preprocessing needs (e.g., missing values, outliers)
    - Preprocessing improves the quality of EDA insights
    - Both are iterative processes that inform each other
    """)
    
    explain("EDA and preprocessing work hand in hand to prepare data for analysis and modeling, often in an iterative cycle.")
    
    # Interactive example
    st.subheader("EDA and Preprocessing Cycle")
    
    # Generate sample data with issues
    np.random.seed(0)
    data = pd.DataFrame({
        'Value': np.random.normal(100, 20, 1000),
        'Category': np.random.choice(['A', 'B', 'C', None], 1000)
    })
    data.loc[np.random.choice(data.index, 10), 'Value'] = 1000  # Add some outliers
    
    step = st.radio("Select step in the cycle", ["Initial EDA", "Preprocessing", "Post-preprocessing EDA"])
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    if step == "Initial EDA":
        sns.boxplot(data=data, x='Category', y='Value', ax=ax)
        ax.set_title("Initial Distribution of Values by Category")
    elif step == "Preprocessing":
        st.write("Preprocessing steps:")
        st.write("1. Remove outliers (Value > 500)")
        st.write("2. Handle missing categories")
        data_cleaned = data[data['Value'] < 500].fillna({'Category': 'Unknown'})
        st.write(data_cleaned.head())
    else:  # Post-preprocessing EDA
        data_cleaned = data[data['Value'] < 500].fillna({'Category': 'Unknown'})
        sns.boxplot(data=data_cleaned, x='Category', y='Value', ax=ax)
        ax.set_title("Distribution of Values by Category After Preprocessing")
    
    if step != "Preprocessing":
        st.pyplot(fig)
    
    st.code(f"""
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt

    # Generate data with issues
    data = pd.DataFrame({{
        'Value': np.random.normal(100, 20, 1000),
        'Category': np.random.choice(['A', 'B', 'C', None], 1000)
    }})
    data.loc[np.random.choice(data.index, 10), 'Value'] = 1000  # Add outliers

    # Code for {step.lower()}
    {"sns.boxplot(data=data, x='Category', y='Value')" if step == "Initial EDA" else 
     "data_cleaned = data[data['Value'] < 500].fillna({'Category': 'Unknown'})" if step == "Preprocessing" else 
     "data_cleaned = data[data['Value'] < 500].fillna({'Category': 'Unknown'})\nsns.boxplot(data=data_cleaned, x='Category', y='Value')"}
    """, language="python")


def quiz_tab():
    st.header("Data Preprocessing Quiz")
    
    explain("Test your knowledge of data preprocessing concepts!")
    
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
            "question": "What is the relationship between Exploratory Data Analysis (EDA) and Data Preprocessing?",
            "options": [
                "They are completely unrelated",
                "EDA comes after all preprocessing is complete",
                "Preprocessing comes after all EDA is complete",
                "They work together in an iterative cycle"
            ],
            "correct": 3
        },
        {
            "question": "What might happen if you use unpreprocessed data for analysis?",
            "options": [
                "You'll always get perfect insights",
                "It might lead to wrong insights and counter-productive decisions",
                "The data will preprocess itself",
                "Nothing, raw data is always ready for analysis"
            ],
            "correct": 1
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
            st.success("Perfect score! You're a data preprocessing expert!")
        elif score >= len(questions) / 2:
            st.success("Good job! You have a solid understanding of data preprocessing.")
        else:
            st.info("Keep learning! Review the other tabs to improve your understanding of data preprocessing.")

if __name__ == "__main__":
    main()