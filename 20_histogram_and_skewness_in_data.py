import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from scipy.stats import skew

st.set_page_config(layout="wide", page_title="Histogram and Skewness Exploration")

# Custom color palette
colors = {
    "primary": "#0066CC",
    "secondary": "#FF6347", 
    "accent": "#32CD32",
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
    st.title("Histogram and Skewness Exploration")
    st.write('**Developed by : Venugopal Adep**')
    
    tabs = st.tabs(["Learn", "Interactive Demo", "Skewness Generator", "Quiz"])
    
    with tabs[0]:
        learn_tab()
    
    with tabs[1]:
        interactive_demo_tab()
    
    with tabs[2]:
        skewness_generator_tab()
    
    with tabs[3]:
        quiz_tab()

def learn_tab():
    st.header("Histogram and Skewness")
    
    st.markdown("""
    - A histogram is a graphical display of data using bars of different heights.
    - In a histogram, each bar groups numbers into ranges.
    - Skewness refers to distortion or asymmetry in a symmetrical bell curve in a set of data.
    - If the curve is shifted to the left, it is called left skewed (negative skew).
    - If the curve is shifted to the right, it is called right skewed (positive skew).
    """)
    
    explain("Histograms help visualize the distribution of data, while skewness measures the asymmetry of the distribution. Understanding both concepts is crucial for data analysis and interpretation.")

def generate_sample_data(skew_type="no"):
    if skew_type == "negative":
        return np.random.beta(5, 2, 1000) * 100 + 40
    elif skew_type == "positive":
        return np.random.beta(2, 5, 1000) * 50 + 10
    else:
        return np.random.normal(150, 20, 1000)

def plot_histogram(data, title):
    fig = go.Figure(data=[go.Histogram(x=data, nbinsx=30)])
    fig.update_layout(title=title, xaxis_title="Value", yaxis_title="Frequency")
    return fig

def interactive_demo_tab():
    st.header("Interactive Histogram Demo")
    
    skew_type = st.selectbox("Select Skew Type", ["Negative Skew", "No Skew", "Positive Skew"])
    
    if skew_type == "Negative Skew":
        data = generate_sample_data("negative")
    elif skew_type == "Positive Skew":
        data = generate_sample_data("positive")
    else:
        data = generate_sample_data("no")
    
    fig = plot_histogram(data, f"Histogram with {skew_type}")
    st.plotly_chart(fig)
    
    skewness = skew(data)
    st.write(f"Skewness: {skewness:.2f}")
    
    explain(f"This histogram shows a distribution with {skew_type.lower()}. "
            f"The skewness value is {skewness:.2f}, where negative values indicate left skew, "
            f"positive values indicate right skew, and values close to 0 indicate symmetry.")
    
    st.subheader("Customize the Plot")
    num_bins = st.slider("Number of Bins", min_value=5, max_value=100, value=30)
    show_kde = st.checkbox("Show KDE (Kernel Density Estimation)")
    
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=data, nbinsx=num_bins, name="Histogram"))
    
    if show_kde:
        kde = np.histogram(data, bins=num_bins, density=True)[0]
        x = np.linspace(min(data), max(data), num_bins)
        fig.add_trace(go.Scatter(x=x, y=kde, mode='lines', name='KDE'))
    
    fig.update_layout(title=f"Customized Histogram with {skew_type}", xaxis_title="Value", yaxis_title="Frequency")
    st.plotly_chart(fig)

def skewness_generator_tab():
    st.header("Skewness Generator")
    
    st.write("Adjust the parameters to generate distributions with different skewness!")
    
    alpha = st.slider("Alpha", min_value=0.1, max_value=10.0, value=2.0, step=0.1)
    beta = st.slider("Beta", min_value=0.1, max_value=10.0, value=5.0, step=0.1)
    
    data = np.random.beta(alpha, beta, 1000) * 100
    
    fig = plot_histogram(data, f"Generated Distribution (Alpha: {alpha}, Beta: {beta})")
    st.plotly_chart(fig)
    
    skewness = skew(data)
    st.write(f"Skewness: {skewness:.2f}")
    
    if skewness < -0.5:
        st.write("This distribution is negatively skewed (left-skewed).")
    elif skewness > 0.5:
        st.write("This distribution is positively skewed (right-skewed).")
    else:
        st.write("This distribution is approximately symmetric.")
    
    explain("The Beta distribution is versatile for generating skewed distributions. "
            "Adjust alpha and beta to create different shapes: "
            "alpha > beta produces negative skew, alpha < beta produces positive skew, "
            "and alpha ≈ beta produces more symmetric distributions.")

def quiz_tab():
    st.header("Quiz: Histograms and Skewness")
    
    questions = [
        {
            "question": "What does a histogram represent?",
            "options": [
                "Trends over time",
                "Categorical data comparison",
                "Distribution of numerical data",
                "Correlation between variables"
            ],
            "correct": 2,
            "explanation": "A histogram represents the distribution of numerical data, grouping numbers into ranges and displaying them as bars."
        },
        {
            "question": "In a left-skewed (negatively skewed) distribution, where is the tail of the distribution?",
            "options": [
                "On the left side",
                "On the right side",
                "In the middle",
                "There is no tail in a left-skewed distribution"
            ],
            "correct": 0,
            "explanation": "In a left-skewed (negatively skewed) distribution, the tail of the distribution is on the left side, with the bulk of the data on the right."
        },
        {
            "question": "What does a skewness value close to 0 indicate?",
            "options": [
                "Strong positive skew",
                "Strong negative skew",
                "Approximate symmetry",
                "Bimodal distribution"
            ],
            "correct": 2,
            "explanation": "A skewness value close to 0 indicates that the distribution is approximately symmetric, with little or no skew."
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
            st.success("Perfect score! You have a great understanding of histograms and skewness!")
        elif score >= len(questions) / 2:
            st.success("Good job! You have a solid grasp of histogram and skewness concepts.")
        else:
            st.info("Keep learning! Review the content about histograms and skewness to improve your understanding.")

if __name__ == "__main__":
    main()