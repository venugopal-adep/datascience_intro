import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide", page_title="Outliers in Data Analysis")

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
    st.title("Outliers")
    st.write('**Developed by : Venugopal Adep**')
    
    tabs = st.tabs(["Learn", "Interactive Demo", "Quiz"])
    
    with tabs[0]:
        learn_tab()
    
    with tabs[1]:
        interactive_demo_tab()
    
    with tabs[2]:
        quiz_tab()

def learn_tab():
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("What are outliers?")
        st.write("Outliers are the observations which are very different from the other observations. In order to analyze the data, sometimes we have to work with outliers.")
        explain("Detecting and handling outliers is crucial for accurate data analysis and model building.")
    
    with col2:
        st.header("How to detect outliers?")
        st.write("1. Boxplot: We can visualize the outliers by using box plot.")
        st.write("2. Scatter plot: We can check outliers using scatter plot by identifying the data point that lies far from other observations.")

def generate_sample_data(n=100):
    np.random.seed(42)
    x = np.random.normal(10, 2, n)
    y = 2 * x + np.random.normal(0, 5, n)
    
    # Add some outliers
    x = np.append(x, [20, 22, 25])
    y = np.append(y, [80, 90, 100])
    
    return pd.DataFrame({'x': x, 'y': y})

def interactive_demo_tab():
    st.header("Interactive Demo: Detecting and Handling Outliers")
    
    data = generate_sample_data()
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("1. Sample Data")
        st.write(data.head())
        
        st.subheader("2. Outlier Detection")
        method = st.radio("Select a method to detect outliers", ["Boxplot", "Scatter plot"])
        
        if method == "Boxplot":
            column = st.selectbox("Select a column for boxplot", data.columns)
        
        st.subheader("3. Handling Outliers")
        handling_method = st.radio("Select a method to handle outliers", ["Remove", "Cap"])
        
        st.markdown("""
        **Remove**: Eliminate data points that are considered outliers.
        **Cap**: Set outliers to a specified maximum or minimum value.
        """)
        
        if st.button("Apply Method"):
            Q1 = data.quantile(0.25)
            Q3 = data.quantile(0.75)
            IQR = Q3 - Q1
            if handling_method == "Remove":
                data_clean = data[~((data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))).any(axis=1)]
            else:
                data_clean = data.clip(lower=Q1 - 1.5 * IQR, upper=Q3 + 1.5 * IQR, axis=1)
            
            st.write("Original data shape:", data.shape)
            st.write("Cleaned data shape:", data_clean.shape)
    
    with col2:
        st.subheader("Visualization")
        if method == "Boxplot":
            fig = px.box(data, y=column)
            fig.update_layout(title=f"Boxplot for {column}")
        else:
            fig = px.scatter(data, x='x', y='y')
            fig.update_layout(title="Scatter plot")
        
        st.plotly_chart(fig, use_container_width=True)
        
        if st.button("Show Handled Data"):
            Q1 = data.quantile(0.25)
            Q3 = data.quantile(0.75)
            IQR = Q3 - Q1
            if handling_method == "Remove":
                data_clean = data[~((data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))).any(axis=1)]
            else:
                data_clean = data.clip(lower=Q1 - 1.5 * IQR, upper=Q3 + 1.5 * IQR, axis=1)
            
            fig_clean = px.scatter(data_clean, x='x', y='y', title="Data after handling outliers")
            st.plotly_chart(fig_clean, use_container_width=True)
    
    st.subheader("4. Code")
    st.code("""
    # Handling outliers
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    
    if handling_method == "Remove":
        data_clean = data[~((data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))).any(axis=1)]
    else:
        data_clean = data.clip(lower=Q1 - 1.5 * IQR, upper=Q3 + 1.5 * IQR, axis=1)
    """)

def quiz_tab():
    st.header("Quiz: Outliers")
    
    questions = [
        {
            "question": "What are outliers in data analysis?",
            "options": [
                "Observations that are very similar to other observations",
                "Observations that are very different from other observations",
                "Missing values in the dataset",
                "The mean of the dataset"
            ],
            "correct": 1,
            "explanation": "Outliers are observations which are very different from the other observations in the dataset. They can significantly affect the results of data analysis if not handled properly."
        },
        {
            "question": "Which of the following is NOT a common method to detect outliers?",
            "options": [
                "Boxplot",
                "Scatter plot",
                "Pie chart",
                "Z-score method"
            ],
            "correct": 2,
            "explanation": "Pie charts are not typically used for outlier detection. Boxplots, scatter plots, and statistical methods like the Z-score are common ways to identify outliers in a dataset."
        },
        {
            "question": "Why is it important to handle outliers in data analysis?",
            "options": [
                "Outliers always improve the accuracy of analysis",
                "Outliers can significantly skew statistical measures and affect model performance",
                "Outliers are always errors and should be removed",
                "Handling outliers is not important in data analysis"
            ],
            "correct": 1,
            "explanation": "Handling outliers is crucial because they can significantly skew statistical measures (like mean and standard deviation) and affect the performance of machine learning models. However, not all outliers are errors, and their treatment depends on the specific context of the analysis."
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
            st.success("Perfect score! You have a great understanding of outliers in data analysis!")
        elif score >= len(questions) / 2:
            st.success("Good job! You have a solid grasp of outliers concept.")
        else:
            st.info("Keep learning! Review the content about outliers to improve your understanding.")

if __name__ == "__main__":
    main()
