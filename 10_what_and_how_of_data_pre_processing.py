import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

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

    # Interactive visualization
    st.subheader("Interactive Data Journey Visualization")
    selected_step = st.selectbox("Select a step in the data journey:", steps)
    st.write(f"You selected: {selected_step}")
    if selected_step == 'Raw Data':
        st.write("Raw data is the starting point of your data journey. It's often messy and unstructured.")
    elif selected_step == 'Structure\nData':
        st.write("Structuring data involves organizing it into a format that's easier to work with, like tables or matrices.")
    elif selected_step == 'EDA &\nPreprocessing':
        st.write("This is where you explore your data and apply various preprocessing techniques to clean and prepare it for analysis.")
    else:
        st.write("The final step where you derive meaningful insights and create visualizations to communicate your findings.")

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

    # Interactive visualization
    st.subheader("Interactive Data Preprocessing Demonstration")
    
    # Generate sample data
    np.random.seed(0)
    data = pd.DataFrame({
        'Age': np.random.randint(18, 80, 1000),
        'Income': np.random.normal(50000, 15000, 1000),
        'Education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD', None], 1000),
        'Customer_Score': np.random.uniform(0, 100, 1000)
    })
    data.loc[np.random.choice(data.index, 50), 'Income'] = np.nan
    data.loc[np.random.choice(data.index, 10), 'Age'] = 0

    preprocessing_step = st.selectbox("Choose a preprocessing step:", 
                                      ["Raw Data", "Handle Missing Values", "Remove Errors", "Encode Categories"])

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

    # Interactive visualization
    st.subheader("Interactive Outlier Removal Demonstration")
    
    np.random.seed(0)
    data = pd.DataFrame({
        'Value': np.random.normal(100, 20, 1000)
    })
    data.loc[np.random.choice(data.index, 10), 'Value'] = 1000

    outlier_threshold = st.slider("Select outlier threshold:", 
                                  min_value=int(data['Value'].min()), 
                                  max_value=int(data['Value'].max()), 
                                  value=500)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    ax1.hist(data['Value'], bins=50)
    ax1.set_title("Before Preprocessing")
    ax1.set_xlabel("Value")
    ax1.set_ylabel("Frequency")

    data_cleaned = data[data['Value'] < outlier_threshold]
    
    ax2.hist(data_cleaned['Value'], bins=50)
    ax2.set_title("After Preprocessing")
    ax2.set_xlabel("Value")
    ax2.set_ylabel("Frequency")

    plt.tight_layout()
    st.pyplot(fig)

    st.write(f"Number of data points removed: {len(data) - len(data_cleaned)}")

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

    # Interactive visualization
    st.subheader("Interactive Preprocessing Technique Demonstration")
    
    technique = st.selectbox("Choose a preprocessing technique to visualize:", 
                             ["Feature Scaling", "Encoding Categorical Variables", "Dimensionality Reduction"])

    if technique == "Feature Scaling":
        feature_scaling_demo()
    elif technique == "Encoding Categorical Variables":
        encoding_demo()
    else:
        dimensionality_reduction_demo()

def feature_scaling_demo():
    np.random.seed(0)
    data = pd.DataFrame({
        'Feature1': np.random.normal(0, 1, 1000),
        'Feature2': np.random.normal(0, 10, 1000),
        'Feature3': np.random.normal(0, 100, 1000)
    })

    scaler = StandardScaler()
    data_scaled = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    data.boxplot(ax=ax1)
    ax1.set_title("Before Scaling")
    ax1.set_ylabel("Value")

    data_scaled.boxplot(ax=ax2)
    ax2.set_title("After Scaling")
    ax2.set_ylabel("Scaled Value")

    plt.tight_layout()
    st.pyplot(fig)

def encoding_demo():
    np.random.seed(0)
    data = pd.DataFrame({
        'Category': np.random.choice(['A', 'B', 'C'], 1000)
    })

    data_encoded = pd.get_dummies(data, columns=['Category'])

    st.write("Original data:")
    st.write(data.head())
    st.write("\nEncoded data:")
    st.write(data_encoded.head())

def dimensionality_reduction_demo():
    np.random.seed(0)
    data = pd.DataFrame(np.random.randn(1000, 10), columns=[f'Feature{i}' for i in range(1, 11)])

    pca = PCA()
    data_pca = pca.fit_transform(data)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(range(1, 11), np.cumsum(pca.explained_variance_ratio_))
    ax.set_xlabel("Number of Components")
    ax.set_ylabel("Cumulative Explained Variance Ratio")
    ax.set_title("PCA: Cumulative Explained Variance Ratio")
    st.pyplot(fig)

    n_components = st.slider("Select number of components to keep:", min_value=1, max_value=10, value=3)
    st.write(f"Explained variance with {n_components} components: {np.sum(pca.explained_variance_ratio_[:n_components]):.2f}")

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

    # Interactive visualization
    st.subheader("Interactive EDA and Preprocessing Demonstration")

    np.random.seed(0)
    data = pd.DataFrame({
        'Age': np.random.randint(18, 80, 1000),
        'Income': np.random.normal(50000, 15000, 1000),
        'Education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], 1000),
        'Spending': np.random.normal(1000, 500, 1000)
    })

    # Add some outliers and missing values
    data.loc[np.random.choice(data.index, 20), 'Income'] = np.random.normal(200000, 50000, 20)
    data.loc[np.random.choice(data.index, 50), 'Spending'] = np.nan

    step = st.radio("Select step in the EDA and Preprocessing cycle", 
                    ["Initial EDA", "Handle Missing Values", "Remove Outliers", "Final Analysis"])

    if step == "Initial EDA":
        st.write("Initial data overview:")
        st.write(data.describe())
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        sns.scatterplot(data=data, x='Age', y='Income', hue='Education', ax=ax1)
        ax1.set_title("Age vs Income by Education")
        sns.boxplot(data=data, y='Spending', ax=ax2)
        ax2.set_title("Distribution of Spending")
        st.pyplot(fig)

    elif step == "Handle Missing Values":
        st.write("Handling missing values in 'Spending'")
        data['Spending'].fillna(data['Spending'].median(), inplace=True)
        st.write(data.isnull().sum())

    elif step == "Remove Outliers":
        st.write("Removing outliers from 'Income'")
        Q1 = data['Income'].quantile(0.25)
        Q3 = data['Income'].quantile(0.75)
        IQR = Q3 - Q1
        data_cleaned = data[(data['Income'] >= Q1 - 1.5*IQR) & (data['Income'] <= Q3 + 1.5*IQR)]
        st.write(f"Rows removed: {len(data) - len(data_cleaned)}")

    else:  # Final Analysis
        data['Spending'].fillna(data['Spending'].median(), inplace=True)
        Q1 = data['Income'].quantile(0.25)
        Q3 = data['Income'].quantile(0.75)
        IQR = Q3 - Q1
        data_cleaned = data[(data['Income'] >= Q1 - 1.5*IQR) & (data['Income'] <= Q3 + 1.5*IQR)]

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        sns.scatterplot(data=data_cleaned, x='Age', y='Income', hue='Education', ax=ax1)
        ax1.set_title("Age vs Income by Education (Cleaned)")
        sns.boxplot(data=data_cleaned, y='Spending', ax=ax2)
        ax2.set_title("Distribution of Spending (Cleaned)")
        st.pyplot(fig)

        st.write("Correlation matrix:")
        st.write(data_cleaned.corr())

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
        },
        {
            "question": "Which of the following is NOT a common data preprocessing technique?",
            "options": [
                "Handling missing values",
                "Feature scaling",
                "Encoding categorical variables",
                "Increasing data volume"
            ],
            "correct": 3
        },
        {
            "question": "What is the purpose of feature scaling?",
            "options": [
                "To increase the number of features",
                "To make features comparable by bringing them to a common scale",
                "To remove all numerical features",
                "To add more categorical variables"
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
