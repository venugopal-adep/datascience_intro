import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide", page_title="Scatter Plot Exploration")

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
    st.title("Scatter Plot Exploration")
    st.write('**Developed by : Venugopal Adep**')
    
    tabs = st.tabs(["Learn", "Interactive Demo", "Quiz"])
    
    with tabs[0]:
        learn_tab()
    
    with tabs[1]:
        interactive_demo_tab()
    
    with tabs[2]:
        quiz_tab()

def learn_tab():
    st.header("Scatter Plot")
    
    st.markdown("""
    - A scatter plot uses dots to represent values for two different numeric variables.
    - The position of each dot on the horizontal and vertical axis indicates values for an individual data point.
    - Scatter plots are used to observe relationships between continuous variables.
    """)
    
    explain("Scatter plots are powerful tools for visualizing the relationship between two continuous variables and can help identify patterns, trends, or outliers in the data.")

def generate_sample_data(n=200):
    np.random.seed(42)
    tip = np.random.uniform(1, 10, n)
    total_bill = 3 * tip + np.random.normal(5, 2, n)
    return pd.DataFrame({'tip': tip, 'total_bill': total_bill})

def interactive_demo_tab():
    st.header("Interactive Scatter Plot Demo")
    
    data = generate_sample_data()
    
    st.subheader("Sample Data")
    st.write(data.head())
    
    st.subheader("Scatter Plot: Tip vs Total Bill")
    fig = px.scatter(data, x="tip", y="total_bill", 
                     title="Relationship between Tip and Total Bill",
                     labels={"tip": "Tip", "total_bill": "Total Bill"})
    st.plotly_chart(fig)
    
    explain("This plot shows the relationship between the tip and the total bill. We can observe that as the total bill increases, the tip also tends to increase.")
    
    st.subheader("Customize the Plot")
    color_by = st.checkbox("Color by Tip Amount")
    add_trendline = st.checkbox("Add Trendline")
    
    if color_by:
        fig = px.scatter(data, x="tip", y="total_bill", color="tip",
                         title="Relationship between Tip and Total Bill (Colored by Tip)",
                         labels={"tip": "Tip", "total_bill": "Total Bill"})
    else:
        fig = px.scatter(data, x="tip", y="total_bill",
                         title="Relationship between Tip and Total Bill",
                         labels={"tip": "Tip", "total_bill": "Total Bill"})
    
    if add_trendline:
        fig.add_traces(px.scatter(data, x="tip", y="total_bill", trendline="ols").data[1])
    
    st.plotly_chart(fig)
    
    st.code("""
    import plotly.express as px
    
    # Create a scatter plot
    fig = px.scatter(data, x="tip", y="total_bill", 
                     title="Relationship between Tip and Total Bill",
                     labels={"tip": "Tip", "total_bill": "Total Bill"})
    
    # Optionally, color by tip amount
    # fig = px.scatter(data, x="tip", y="total_bill", color="tip",
    #                  title="Relationship between Tip and Total Bill (Colored by Tip)",
    #                  labels={"tip": "Tip", "total_bill": "Total Bill"})
    
    # Optionally, add a trendline
    # fig.add_traces(px.scatter(data, x="tip", y="total_bill", trendline="ols").data[1])
    
    fig.show()
    """)

def quiz_tab():
    st.header("Quiz: Scatter Plots")
    
    questions = [
        {
            "question": "What do the dots in a scatter plot represent?",
            "options": [
                "Categories of data",
                "Values for two different numeric variables",
                "Time series data",
                "Percentage distribution"
            ],
            "correct": 1,
            "explanation": "In a scatter plot, each dot represents values for two different numeric variables, with its position indicating the values on both axes."
        },
        {
            "question": "What type of relationship can be observed using scatter plots?",
            "options": [
                "Categorical relationships",
                "Time-based trends",
                "Relationships between continuous variables",
                "Hierarchical structures"
            ],
            "correct": 2,
            "explanation": "Scatter plots are primarily used to observe relationships between continuous variables, showing how one variable changes with respect to another."
        },
        {
            "question": "In the example scatter plot, what can we conclude about the relationship between tip and total bill?",
            "options": [
                "There is no relationship",
                "As the total bill increases, the tip tends to decrease",
                "As the total bill increases, the tip tends to increase",
                "The tip is always exactly 15% of the total bill"
            ],
            "correct": 2,
            "explanation": "From the scatter plot, we can observe that as the total bill increases, the tip also tends to increase, indicating a positive relationship between these two variables."
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
            st.success("Perfect score! You have a great understanding of scatter plots!")
        elif score >= len(questions) / 2:
            st.success("Good job! You have a solid grasp of scatter plot concepts.")
        else:
            st.info("Keep learning! Review the content about scatter plots to improve your understanding.")

if __name__ == "__main__":
    main()