import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

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
</style>
""", unsafe_allow_html=True)

def explain(text):
    st.markdown(f"""
    <div style='background-color: white; padding: 15px; border-radius: 5px; border-left: 5px solid {colors['accent']}; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
        <p style='color: {colors['text']}; margin: 0;'>{text}</p>
    </div>
    """, unsafe_allow_html=True)

def generate_sample_data(n=100):
    np.random.seed(42)
    x = np.random.normal(10, 2, n)
    y = 2 * x + np.random.normal(0, 5, n)
    # Add some outliers
    x = np.append(x, [20, 22, 25])
    y = np.append(y, [80, 90, 100])
    return pd.DataFrame({'x': x, 'y': y})

def handle_outliers(data, method):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    if method == "Remove":
        # Remove outliers using the IQR method
        data_clean = data[~((data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))).any(axis=1)]
    else:
        # Cap the outliers to the lower and upper bounds
        data_clean = data.clip(lower=Q1 - 1.5 * IQR, upper=Q3 + 1.5 * IQR, axis=1)
    return data_clean

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
        st.write("Outliers are observations that are significantly different from other data points.")
        explain("Detecting and handling outliers is crucial for accurate data analysis and model building.")

    with col2:
        st.header("How to detect outliers?")
        st.write("1. **Boxplot**: Visualize outliers using a boxplot.")
        st.write("2. **Scatter plot**: Identify outliers using scatter plots by locating data points far from other observations.")

def interactive_demo_tab():
    st.header("Interactive Demo: Detecting and Handling Outliers")

    # Explanation for the tab
    explain("This demo allows you to explore different methods of outlier detection and handling. Choose a method to visualize outliers and apply a technique to handle them in real-time.")

    data = generate_sample_data()

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("1. Sample Data")
        st.write(data.head())
        explain("The data contains two columns ('x' and 'y'). Some of these data points are considered outliers, which we'll identify and handle using different methods.")

        st.subheader("2. Outlier Detection")
        method = st.radio("Select a method to detect outliers", ["Boxplot", "Scatter plot"])

        column = st.selectbox("Select a column for boxplot", data.columns) if method == "Boxplot" else None

        st.subheader("3. Handling Outliers")
        handling_method = st.radio("Select a method to handle outliers", ["Remove", "Cap"])
        
        # Explanation for handling methods
        if handling_method == "Remove":
            explain("""
            **Remove Outliers:** Outliers are removed based on the Interquartile Range (IQR) method.
            - **Formula:** An outlier is any value outside the range [Q1 - 1.5 * IQR, Q3 + 1.5 * IQR].
            - **Q1:** 25th percentile of the data.
            - **Q3:** 75th percentile of the data.
            - **IQR:** Interquartile range, calculated as Q3 - Q1.
            """)
        else:
            explain("""
            **Cap Outliers:** Outliers are capped to the boundaries using the IQR method.
            - **Formula:** Values below Q1 - 1.5 * IQR are set to Q1 - 1.5 * IQR. Values above Q3 + 1.5 * IQR are set to Q3 + 1.5 * IQR.
            - **Q1:** 25th percentile of the data.
            - **Q3:** 75th percentile of the data.
            - **IQR:** Interquartile range, calculated as Q3 - Q1.
            """)

    with col2:
        st.subheader("Visualization")

        if method == "Boxplot":
            fig = px.box(data, y=column)
            fig.update_layout(title=f"Boxplot for {column}", annotations=[
                dict(x=0.5, y=max(data[column]), text="Outliers are points outside the whiskers", showarrow=False, font=dict(color="red"))
            ])
        else:
            fig = px.scatter(data, x='x', y='y')
            fig.update_layout(title="Scatter plot", annotations=[
                dict(x=22, y=90, text="Outliers", showarrow=True, arrowhead=2, ax=-40, ay=-40, font=dict(color="red"))
            ])

        st.plotly_chart(fig, use_container_width=True)

        # Handle outliers based on selected method
        data_clean = handle_outliers(data, handling_method)
        fig_clean = px.scatter(data_clean, x='x', y='y', title="Data after handling outliers")
        fig_clean.update_layout(annotations=[
            dict(x=0.5, y=max(data_clean['y']), text=f"Data after {handling_method} handling", showarrow=False, font=dict(color="green"))
        ])
        st.plotly_chart(fig_clean, use_container_width=True)
        explain(f"The plot above shows the data after applying the '{handling_method}' method to handle outliers.")

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
            "explanation": "Outliers are observations that are significantly different from other observations."
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
            "explanation": "Pie charts are not typically used for outlier detection."
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
            "explanation": "Handling outliers is crucial as they can significantly skew statistical measures."
        }
    ]

    score = 0
    for i, q in enumerate(questions):
        st.subheader(f"Question {i+1}")
        st.write(q["question"])
        answer = st.radio(f"Select your answer for question {i+1}:", q["options"], key=f"q{i}")
        if answer == q["options"][q["correct"]]:
            st.success("Correct!")
            score += 1
        else:
            st.error(f"Incorrect. The correct answer is: {q['options'][q['correct']]}")
        st.info(f"Explanation: {q['explanation']}")

    st.write(f"Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    main()
