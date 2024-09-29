import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

st.set_page_config(layout="wide", page_title="Data Preprocessing Guide")

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
        padding-top: 1rem;
        padding-bottom: 1rem;
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
    .stRadio > div {{
        flex-direction: row;
    }}
</style>
""", unsafe_allow_html=True)

def main():
    st.title("Data Preprocessing Guide")
    st.write('**Developed by: Venugopal Adep**')

    tabs = st.tabs([
        "Overview",
        "What is Preprocessing?", 
        "Why Preprocess?", 
        "Techniques",
        "EDA & Preprocessing",
        "Quiz"
    ])

    with tabs[0]:
        overview_tab()
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
    <div style='background-color: white; padding: 10px; border-radius: 5px; border-left: 5px solid {colors['accent']}; margin-bottom: 10px;'>
        <p style='color: {colors['text']}; margin: 0;'>{text}</p>
    </div>
    """, unsafe_allow_html=True)

def overview_tab():
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("What and Why of Data Preprocessing?")
        st.write("""
        Data preprocessing prepares raw data for analysis:
        - Cleans incomplete or inconsistent data
        - Structures data for analysis
        - Prevents wrong insights and decisions
        - Essential step before deriving insights
        """)
        
        st.subheader("Data Processing Journey")
        step = st.radio("Select a step:", ['Raw Data', 'Structure Data', 'EDA & Preprocessing', 'Insights'])
        if step == 'Raw Data':
            st.write("Starting point: messy, unstructured data.")
        elif step == 'Structure Data':
            st.write("Organize data into a workable format.")
        elif step == 'EDA & Preprocessing':
            st.write("Explore, clean, and prepare data for analysis.")
        else:
            st.write("Derive meaningful insights and visualize findings.")

    with col2:
        fig, ax = plt.subplots(figsize=(8, 6))
        steps = ['Raw Data', 'Structure\nData', 'EDA &\nPreprocessing', 'Insights']
        x = np.arange(len(steps))
        ax.plot(x, [0, 0, 0, 0], 'o-', color=colors['primary'], linewidth=2, markersize=10)
        ax.set_xticks(x)
        ax.set_xticklabels(steps)
        ax.set_yticks([])
        ax.spines['left'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        for i, s in enumerate(steps):
            ax.annotate(s, (i, 0.1), ha='center', fontsize=12, fontweight='bold')
        plt.title("Data Processing Journey", fontsize=16, fontweight='bold')
        st.pyplot(fig)

def what_is_preprocessing_tab():
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("What is Data Preprocessing?")
        explain("""
        Data preprocessing involves:
        - Cleaning and handling missing data
        - Transforming data format
        - Reducing noise and inconsistencies
        - Normalizing or scaling features
        - Encoding categorical variables
        """)
        
        preprocessing_step = st.selectbox("Choose a preprocessing step:", 
                                          ["Raw Data", "Handle Missing Values", "Remove Errors", "Encode Categories"])
        
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

        if preprocessing_step == "Raw Data":
            st.write(data.head())
            st.write(f"Data shape: {data.shape}")
        elif preprocessing_step == "Handle Missing Values":
            data_cleaned = data.dropna()
            st.write(data_cleaned.head())
            st.write(f"Shape after handling missing values: {data_cleaned.shape}")
        elif preprocessing_step == "Remove Errors":
            data_cleaned = data[data['Age'] > 0]
            st.write(data_cleaned.head())
            st.write(f"Shape after removing errors: {data_cleaned.shape}")
        else:  # Encode Categories
            data_encoded = pd.get_dummies(data, columns=['Education'])
            st.write(data_encoded.head())
            st.write(f"Shape after encoding categories: {data_encoded.shape}")

    with col2:
        st.header("Visualization")
        if preprocessing_step == "Raw Data":
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.scatterplot(data=data, x='Age', y='Income', hue='Education', ax=ax)
            ax.set_title("Age vs Income by Education (Raw Data)")
            st.pyplot(fig)
        elif preprocessing_step == "Handle Missing Values":
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
            data['Income'].hist(ax=ax1, bins=30)
            ax1.set_title("Income Distribution (Before)")
            data_cleaned['Income'].hist(ax=ax2, bins=30)
            ax2.set_title("Income Distribution (After)")
            st.pyplot(fig)
        elif preprocessing_step == "Remove Errors":
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
            sns.boxplot(data=data, y='Age', ax=ax1)
            ax1.set_title("Age Distribution (Before)")
            sns.boxplot(data=data_cleaned, y='Age', ax=ax2)
            ax2.set_title("Age Distribution (After)")
            st.pyplot(fig)
        else:  # Encode Categories
            fig, ax = plt.subplots(figsize=(10, 6))
            data_encoded.iloc[:, -4:].sum().plot(kind='bar', ax=ax)
            ax.set_title("Distribution of Encoded Education Categories")
            ax.set_ylabel("Count")
            st.pyplot(fig)

def why_preprocess_tab():
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("Why Preprocess Data?")
        explain("""
        Preprocessing is crucial because:
        - Raw data often contains inconsistencies and errors
        - It makes data suitable for analysis and modeling
        - It helps avoid wrong insights and decisions
        - It's necessary before deriving meaningful insights
        """)
        
        np.random.seed(0)
        data = pd.DataFrame({'Value': np.random.normal(100, 20, 1000)})
        data.loc[np.random.choice(data.index, 10), 'Value'] = 1000

        outlier_threshold = st.slider("Select outlier threshold:", 
                                      min_value=int(data['Value'].min()), 
                                      max_value=int(1500), 
                                      value=500)
        
        data_cleaned = data[data['Value'] < outlier_threshold]
        st.write(f"Number of data points removed: {len(data) - len(data_cleaned)}")

    with col2:
        st.header("Visualization")
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
        
        ax1.hist(data['Value'], bins=50)
        ax1.set_title("Before Preprocessing")
        ax1.set_xlabel("Value")
        ax1.set_ylabel("Frequency")

        ax2.hist(data_cleaned['Value'], bins=50)
        ax2.set_title("After Preprocessing")
        ax2.set_xlabel("Value")
        ax2.set_ylabel("Frequency")

        plt.tight_layout()
        st.pyplot(fig)

def preprocessing_techniques_tab():
    col1, col2 = st.columns([1, 1])
    
    with col1:
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
        
        explain("Techniques are applied based on data nature and analysis requirements.")
        
        technique = st.selectbox("Choose a technique to visualize:", 
                                 ["Feature Scaling", "Encoding Categorical Variables", "Dimensionality Reduction"])

    with col2:
        st.header("Visualization")
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

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
    
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

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
    
    data['Category'].value_counts().plot(kind='bar', ax=ax1)
    ax1.set_title("Original Categories")
    ax1.set_ylabel("Count")

    data_encoded.sum().plot(kind='bar', ax=ax2)
    ax2.set_title("Encoded Categories")
    ax2.set_ylabel("Count")

    plt.tight_layout()
    st.pyplot(fig)

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

def eda_and_preprocessing_tab():
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("EDA and Preprocessing")
        st.write("""
        Real-world data journey:
        1. Raw Data
        2. Structure Data
        3. EDA and Preprocessing (iterative)
        4. Insights, Visualizations
        """)
        
        explain("EDA and preprocessing work together iteratively.")
        
        np.random.seed(0)
        data = pd.DataFrame({
            'Age': np.random.randint(18, 80, 1000),
            'Income': np.random.normal(50000, 15000, 1000),
            'Education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], 1000),
            'Spending': np.random.normal(1000, 500, 1000)
        })
        data.loc[np.random.choice(data.index, 20), 'Income'] = np.random.normal(200000, 50000, 20)
        data.loc[np.random.choice(data.index, 50), 'Spending'] = np.nan

        step = st.radio("Select step in the cycle", 
                        ["Initial EDA", "Handle Missing Values", "Remove Outliers", "Final Analysis"])

        if step == "Initial EDA":
            st.write("Initial data overview:")
            st.write(data.describe())
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
            st.write("Correlation matrix:")
            st.write(data_cleaned.corr())

    with col2:
        st.header("Visualization")
        if step == "Initial EDA":
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
            sns.scatterplot(data=data, x='Age', y='Income', hue='Education', ax=ax1)
            ax1.set_title("Age vs Income by Education")
            sns.boxplot(data=data, y='Spending', ax=ax2)
            ax2.set_title("Distribution of Spending")
            st.pyplot(fig)
        elif step == "Handle Missing Values":
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
            sns.boxplot(data=data, y='Spending', ax=ax1)
            ax1.set_title("Spending Distribution (Before)")
            data['Spending'].fillna(data['Spending'].median(), inplace=True)
            sns.boxplot(data=data, y='Spending', ax=ax2)
            ax2.set_title("Spending Distribution (After)")
            st.pyplot(fig)
        elif step == "Remove Outliers":
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
            sns.boxplot(data=data, y='Income', ax=ax1)
            ax1.set_title("Income Distribution (Before)")
            Q1 = data['Income'].quantile(0.25)
            Q3 = data['Income'].quantile(0.75)
            IQR = Q3 - Q1
            data_cleaned = data[(data['Income'] >= Q1 - 1.5*IQR) & (data['Income'] <= Q3 + 1.5*IQR)]
            sns.boxplot(data=data_cleaned, y='Income', ax=ax2)
            ax2.set_title("Income Distribution (After)")
            st.pyplot(fig)
        else:  # Final Analysis
            data['Spending'].fillna(data['Spending'].median(), inplace=True)
            Q1 = data['Income'].quantile(0.25)
            Q3 = data['Income'].quantile(0.75)
            IQR = Q3 - Q1
            data_cleaned = data[(data['Income'] >= Q1 - 1.5*IQR) & (data['Income'] <= Q3 + 1.5*IQR)]
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
            sns.scatterplot(data=data_cleaned, x='Age', y='Income', hue='Education', ax=ax1)
            ax1.set_title("Age vs Income by Education (Cleaned)")
            sns.boxplot(data=data_cleaned, y='Spending', ax=ax2)
            ax2.set_title("Distribution of Spending (Cleaned)")
            st.pyplot(fig)

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
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        score = 0
        for i, q in enumerate(questions):
            st.subheader(f"Question {i+1}")
            st.write(q["question"])
            answer = st.radio(f"Select your answer:", q["options"], key=f"q{i}")
            if st.button(f"Submit Answer {i+1}"):
                if q["options"].index(answer) == q["correct"]:
                    st.success("Correct!")
                    score += 1
                else:
                    st.error(f"Incorrect. The correct answer is: {q['options'][q['correct']]}")
    
    with col2:
        if st.button("Show Results"):
            st.write(f"Your score: {score}/{len(questions)}")
            if score == len(questions):
                st.balloons()
                st.success("Perfect score! You're a data preprocessing expert!")
            elif score >= len(questions) / 2:
                st.success("Good job! You have a solid understanding of data preprocessing.")
            else:
                st.info("Keep learning! Review the other tabs to improve your understanding of data preprocessing.")

            fig, ax = plt.subplots(figsize=(8, 6))
            ax.bar(['Correct', 'Incorrect'], [score, len(questions) - score])
            ax.set_ylabel('Number of Questions')
            ax.set_title('Quiz Results')
            st.pyplot(fig)

if __name__ == "__main__":
    main()
