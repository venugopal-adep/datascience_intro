import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide", page_title="Exploratory Data Analysis (EDA) Demo")

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
    .split-container {{
        display: flex;
        justify-content: space-between;
    }}
    .split-column {{
        width: 48%;
    }}
</style>
""", unsafe_allow_html=True)

def main():
    st.title("Exploratory Data Analysis (EDA)")
    st.write('**Developed by : Venugopal Adep**')

    st.markdown(f"""
    <p style='font-size: 1.2em; color: {colors['text']}; background-color: white; padding: 15px; border-radius: 5px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
    Welcome to the Exploratory Data Analysis (EDA) demo! This app will help you understand 
    the concept of EDA, its importance, and common techniques used in EDA.
    </p>
    """, unsafe_allow_html=True)

    tabs = st.tabs([
        "EDA Overview",
        "What is EDA?", 
        "Why EDA?", 
        "EDA Techniques",
        "Quiz"
    ])

    with tabs[0]:
        eda_overview_tab()

    with tabs[1]:
        what_is_eda_tab()

    with tabs[2]:
        why_eda_tab()

    with tabs[3]:
        eda_techniques_tab()

    with tabs[4]:
        quiz_tab()

def explain(text):
    st.markdown(f"""
    <div style='background-color: white; padding: 15px; border-radius: 5px; border-left: 5px solid {colors['accent']}; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
        <p style='color: {colors['text']}; margin: 0;'>{text}</p>
    </div>
    """, unsafe_allow_html=True)

def eda_overview_tab():
    st.header("EDA Overview")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("What is EDA?")
        st.markdown("""
        - Combination of visualization techniques and statistical methods
        - Exploring and summarizing key information within the data
        - Initial examination of data to discover patterns, spot anomalies, test hypotheses, and check assumptions
        """)
    
    with col2:
        st.subheader("Why of EDA?")
        st.markdown("""
        - First step in any analysis
        - Gain good insights into the data
        - Uncover underlying structure of the data
        - Detect and figure out the best strategy to handle unclean data (missing values, outliers etc.)
        - Identify initial set of observations and insights
        """)

def what_is_eda_tab():
    st.header("What is EDA?")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.code("""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.DataFrame({
    'X': np.random.normal(0, 1, 1000),
    'Y': np.random.normal(2, 1, 1000),
})

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(data['X'], data['Y'])
ax.set_title("Scatter Plot of X vs Y")
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.show()
        """, language="python")
    
    with col2:
        # Generate sample data
        np.random.seed(0)
        data = pd.DataFrame({
            'X': np.random.normal(0, 1, 1000),
            'Y': np.random.normal(2, 1, 1000),
        })
        
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.scatter(data['X'], data['Y'])
        ax.set_title("Scatter Plot of X vs Y")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        st.pyplot(fig)
    
    explain("EDA is a critical first step in analyzing datasets to summarize their main characteristics, often with visual methods.")

def why_eda_tab():
    st.header("Why EDA?")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.code("""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(0)
data = pd.DataFrame({
    'A': np.random.normal(0, 1, 1000),
    'B': np.random.normal(2, 1, 1000),
    'C': np.random.normal(-1, 1.5, 1000),
    'D': np.random.normal(5, 2, 1000)
})

# Create correlation heatmap
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', ax=ax)
ax.set_title("Correlation Heatmap")
plt.show()
        """, language="python")
    
    with col2:
        # Generate sample data
        np.random.seed(0)
        data = pd.DataFrame({
            'A': np.random.normal(0, 1, 1000),
            'B': np.random.normal(2, 1, 1000),
            'C': np.random.normal(-1, 1.5, 1000),
            'D': np.random.normal(5, 2, 1000)
        })
        
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(data.corr(), annot=True, cmap='coolwarm', ax=ax)
        ax.set_title("Correlation Heatmap")
        st.pyplot(fig)
    
    explain("EDA helps analysts make sense of data before formal modeling and can lead to new questions and areas of investigation.")

def eda_techniques_tab():
    st.header("EDA Techniques")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.code("""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(0)
data = pd.DataFrame({
    'A': np.random.normal(0, 1, 1000),
    'B': np.random.normal(2, 1, 1000),
})

# Create histogram
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(data=data, x='A', kde=True, ax=ax)
ax.set_title("Histogram of Variable A")
plt.show()
        """, language="python")
    
    with col2:
        # Generate sample data
        np.random.seed(0)
        data = pd.DataFrame({
            'A': np.random.normal(0, 1, 1000),
            'B': np.random.normal(2, 1, 1000),
        })
        
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.histplot(data=data, x='A', kde=True, ax=ax)
        ax.set_title("Histogram of Variable A")
        st.pyplot(fig)
    
    explain("Different EDA techniques help reveal different aspects of the data, from distribution of individual variables to relationships between multiple variables.")

def quiz_tab():
    st.header("EDA Quiz 📊")
    
    st.markdown(f"""
    <p style='font-size: 1.2em; color: {colors['text']}; background-color: white; padding: 15px; border-radius: 5px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
    Test your understanding of Exploratory Data Analysis! Good luck! 🍀
    </p>
    """, unsafe_allow_html=True)

    questions = [
        {
            "question": "What does EDA stand for?",
            "options": ["Extensive Data Analysis", "Exploratory Data Analysis", "Extreme Data Assessment", "External Data Arrangement"],
            "correct": "Exploratory Data Analysis",
            "explanation": "EDA stands for Exploratory Data Analysis, which is an approach to analyzing data sets to summarize their main characteristics."
        },
        {
            "question": "Which of the following is NOT typically a goal of EDA?",
            "options": ["Detect outliers", "Summarize key information", "Fit complex statistical models", "Discover patterns"],
            "correct": "Fit complex statistical models",
            "explanation": "While EDA can inform model selection, fitting complex statistical models is typically a step that comes after EDA, not a primary goal of EDA itself."
        },
        {
            "question": "Which visualization technique is best for showing the distribution of a single continuous variable?",
            "options": ["Scatter plot", "Histogram", "Heat map", "Pair plot"],
            "correct": "Histogram",
            "explanation": "Histograms are excellent for showing the distribution of a single continuous variable, displaying the frequency of data points within bins."
        },
        {
            "question": "What type of plot is most suitable for visualizing the relationship between two continuous variables?",
            "options": ["Bar chart", "Pie chart", "Scatter plot", "Box plot"],
            "correct": "Scatter plot",
            "explanation": "Scatter plots are ideal for visualizing the relationship between two continuous variables, showing how one variable changes with respect to another."
        }
    ]

    for i, q in enumerate(questions, 1):
        st.subheader(f"Question {i}")
        st.markdown(f"<p style='font-size: 1.1em; color: {colors['primary']};'>{q['question']}</p>", unsafe_allow_html=True)
        
        user_answer = st.radio(f"Select your answer for Question {i}", q["options"], key=f"q{i}")
        
        if st.button(f"Check Answer for Question {i}"):
            if user_answer == q["correct"]:
                st.success("Correct! Well done! 🎉")
            else:
                st.error("Oops! That's not quite right. Try again! 🔄")
            
            explain(f"Explanation: {q['explanation']}")
        
        st.markdown("---")

    st.markdown(f"""
    <p style='font-size: 1.2em; color: {colors['text']}; background-color: white; padding: 15px; border-radius: 5px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
    Remember, EDA is a crucial step in any data analysis project. It helps you understand your data better and guides your further analysis. Keep practicing! 📈
    </p>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
