import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide", page_title="How to deal with outliers?")

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
    st.title("How to Deal with Outliers")
    st.write('**Developed by : Venugopal Adep**')
    
    tabs = st.tabs(["Learn", "Interactive Demo", "Quiz"])
    
    with tabs[0]:
        learn_tab()
    
    with tabs[1]:
        interactive_demo_tab()
    
    with tabs[2]:
        quiz_tab()

def learn_tab():
    st.header("Dealing with Outliers")
    
    st.write("Handling outliers is subjective to the business problem we are trying to solve but some general practices are as follows:")
    
    st.markdown("""
    - We should analyze outliers before treating them
    - If an outlier represents the general trend, then there is no need to treat it
        - Example: Income is generally a skewed variable but all extreme points might not be outliers
    - If we decide to treat outlier after analyzing it, then:
        - We can drop them but we would lose information in other columns of the data
        - We can cap outliers at certain values, say 5th percentile or 95th percentile
        - We can set a threshold using IQR and remove the outliers greater than that threshold value
    """)
    
    explain("The approach to handling outliers depends on the specific context of your data and the problem you're trying to solve.")

def generate_sample_data(n=1000):
    np.random.seed(42)
    income = np.random.lognormal(mean=10, sigma=1, size=n)
    age = np.random.normal(40, 10, n)
    age = np.clip(age, 18, 80).astype(int)
    
    # Add some outliers
    income = np.append(income, [1e6, 2e6, 3e6])
    age = np.append(age, [90, 95, 100])
    
    return pd.DataFrame({'Income': income, 'Age': age})

def interactive_demo_tab():
    st.header("Interactive Demo: Dealing with Outliers")
    
    data = generate_sample_data()
    
    st.subheader("Sample Data")
    st.write(data.describe())
    
    st.subheader("Visualize Outliers")
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.box(data, y="Income", title="Income Distribution")
        st.plotly_chart(fig1)
    with col2:
        fig2 = px.scatter(data, x="Age", y="Income", title="Age vs Income")
        st.plotly_chart(fig2)
    
    st.subheader("Dealing with Outliers")
    method = st.radio("Select a method to deal with outliers", ["No treatment", "Drop outliers", "Cap outliers", "IQR method"])
    
    if method == "No treatment":
        data_cleaned = data
    elif method == "Drop outliers":
        Q1 = data['Income'].quantile(0.25)
        Q3 = data['Income'].quantile(0.75)
        IQR = Q3 - Q1
        data_cleaned = data[(data['Income'] >= Q1 - 1.5 * IQR) & (data['Income'] <= Q3 + 1.5 * IQR)]
    elif method == "Cap outliers":
        lower = data['Income'].quantile(0.05)
        upper = data['Income'].quantile(0.95)
        data_cleaned = data.copy()
        data_cleaned['Income'] = data_cleaned['Income'].clip(lower, upper)
    else:  # IQR method
        Q1 = data['Income'].quantile(0.25)
        Q3 = data['Income'].quantile(0.75)
        IQR = Q3 - Q1
        threshold = Q3 + 1.5 * IQR
        data_cleaned = data[data['Income'] <= threshold]
    
    st.write("Original data shape:", data.shape)
    st.write("Cleaned data shape:", data_cleaned.shape)
    
    col3, col4 = st.columns(2)
    with col3:
        fig3 = px.box(data_cleaned, y="Income", title="Income Distribution (After Treatment)")
        st.plotly_chart(fig3)
    with col4:
        fig4 = px.scatter(data_cleaned, x="Age", y="Income", title="Age vs Income (After Treatment)")
        st.plotly_chart(fig4)
    
    st.code(f"""
    # Dealing with outliers
    if method == "Drop outliers":
        Q1 = data['Income'].quantile(0.25)
        Q3 = data['Income'].quantile(0.75)
        IQR = Q3 - Q1
        data_cleaned = data[(data['Income'] >= Q1 - 1.5 * IQR) & (data['Income'] <= Q3 + 1.5 * IQR)]
    elif method == "Cap outliers":
        lower = data['Income'].quantile(0.05)
        upper = data['Income'].quantile(0.95)
        data_cleaned = data.copy()
        data_cleaned['Income'] = data_cleaned['Income'].clip(lower, upper)
    elif method == "IQR method":
        Q1 = data['Income'].quantile(0.25)
        Q3 = data['Income'].quantile(0.75)
        IQR = Q3 - Q1
        threshold = Q3 + 1.5 * IQR
        data_cleaned = data[data['Income'] <= threshold]
    else:
        data_cleaned = data
    """)

def quiz_tab():
    st.header("Quiz: Dealing with Outliers")
    
    questions = [
        {
            "question": "What should be the first step when dealing with outliers?",
            "options": [
                "Always remove them",
                "Analyze them before treating",
                "Cap them at the 95th percentile",
                "Ignore them completely"
            ],
            "correct": 1,
            "explanation": "We should analyze outliers before treating them. This helps us understand if the outliers represent a genuine trend or if they are truly anomalous."
        },
        {
            "question": "When might we decide not to treat an outlier?",
            "options": [
                "If it's more than 3 standard deviations from the mean",
                "If it represents the general trend of the data",
                "If it's in the top 1% of values",
                "If it's a negative value"
            ],
            "correct": 1,
            "explanation": "If an outlier represents the general trend of the data, there might be no need to treat it. For example, income data is often skewed, and extreme values might be valid data points."
        },
        {
            "question": "Which of the following is NOT a common method for dealing with outliers?",
            "options": [
                "Dropping the outliers",
                "Capping outliers at certain percentiles",
                "Using the IQR method to set a threshold",
                "Multiplying all outliers by 2"
            ],
            "correct": 3,
            "explanation": "Common methods for dealing with outliers include dropping them, capping them at certain percentiles (e.g., 5th and 95th), or using the IQR method to set a threshold. Multiplying outliers by 2 is not a standard practice and would actually amplify the outlier effect."
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
            st.success("Perfect score! You have a great understanding of how to deal with outliers!")
        elif score >= len(questions) / 2:
            st.success("Good job! You have a solid grasp of dealing with outliers.")
        else:
            st.info("Keep learning! Review the content about dealing with outliers to improve your understanding.")

if __name__ == "__main__":
    main()