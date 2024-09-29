import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide", page_title="Bar Plot Exploration")

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
</style>
""", unsafe_allow_html=True)

def explain(text):
    st.markdown(f"""
    <div style='background-color: white; padding: 15px; border-radius: 5px; border-left: 5px solid {colors['accent']}; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
        <p style='color: {colors['text']}; margin: 0;'>{text}</p>
    </div>
    """, unsafe_allow_html=True)

def main():
    st.title("Bar Plot Exploration")
    st.write('**Developed by : Venugopal Adep**')
    
    tabs = st.tabs(["Learn", "Interactive Demo", "Quiz"])
    
    with tabs[0]:
        learn_tab()
    
    with tabs[1]:
        interactive_demo_tab()
    
    with tabs[2]:
        quiz_tab()

def learn_tab():
    st.header("Bar Plot")
    
    st.markdown("""
    - A bar chart is a chart that presents categorical data with rectangular bars with heights or lengths proportional to the values that they represent.
    - The bars can be plotted vertically or horizontally.
    - Bar plots are used to compare quantities across different categories.
    """)
    
    explain("Bar plots are effective for displaying and comparing discrete, categorical data. They make it easy to see patterns, trends, and differences between categories at a glance.")

def generate_sample_data():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    students = [3, 4, 2, 3, 8, 10, 6, 1, 7, 8, 4, 7]
    return pd.DataFrame({'Month': months, 'Number of Students': students})

def interactive_demo_tab():
    st.header("Interactive Bar Plot Demo")
    
    # Create two columns: left for controls and explanation, right for plots
    left_col, right_col = st.columns([1, 2])
    
    data = generate_sample_data()
    
    with left_col:
        st.subheader("Sample Data")
        st.write(data)
        
        st.subheader("Customize the Plot")
        orientation = st.radio("Bar Orientation", ["Vertical", "Horizontal"])
        color_bars = st.checkbox("Color Bars by Value")
        
        explain("This plot shows the distribution of student birthdays across different months. We can easily compare the number of students born in each month.")
        
        st.code("""
        import plotly.express as px
        
        # Create a bar plot
        fig = px.bar(data, x="Month", y="Number of Students", 
                     title="Birthday of Students by Month",
                     labels={"Month": "Month", "Number of Students": "Number of Students"})
        
        # Optionally, change orientation to horizontal
        # fig = px.bar(data, y="Month", x="Number of Students",
        #              title="Birthday of Students by Month",
        #              labels={"Month": "Month", "Number of Students": "Number of Students"},
        #              orientation='h')
        
        # Optionally, color bars by value
        # fig = px.bar(data, x="Month", y="Number of Students",
        #              title="Birthday of Students by Month",
        #              labels={"Month": "Month", "Number of Students": "Number of Students"},
        #              color="Number of Students")
        
        fig.show()
        """)
    
    with right_col:
        st.subheader("Bar Plot: Birthday of Students by Month")
        if orientation == "Vertical":
            fig = px.bar(data, x="Month", y="Number of Students",
                         title="Birthday of Students by Month",
                         labels={"Month": "Month", "Number of Students": "Number of Students"},
                         color="Number of Students" if color_bars else None)
        else:
            fig = px.bar(data, y="Month", x="Number of Students",
                         title="Birthday of Students by Month",
                         labels={"Month": "Month", "Number of Students": "Number of Students"},
                         color="Number of Students" if color_bars else None,
                         orientation='h')
        
        st.plotly_chart(fig, use_container_width=True)

def quiz_tab():
    st.header("Quiz: Bar Plots")
    
    questions = [
        {
            "question": "What type of data is best represented by a bar plot?",
            "options": [
                "Continuous data",
                "Categorical data",
                "Time series data",
                "Multidimensional data"
            ],
            "correct": 1,
            "explanation": "Bar plots are best suited for representing categorical data, where each bar represents a distinct category."
        },
        {
            "question": "In the example bar plot, which month had the most student birthdays?",
            "options": [
                "January",
                "May",
                "June",
                "October"
            ],
            "correct": 2,
            "explanation": "The bar plot shows that June had the highest number of student birthdays, with 10 students."
        },
        {
            "question": "What is an advantage of using a horizontal bar plot instead of a vertical one?",
            "options": [
                "It can display more categories",
                "It's better for comparing exact values",
                "It's easier to read long category names",
                "It always looks more visually appealing"
            ],
            "correct": 2,
            "explanation": "Horizontal bar plots are particularly useful when category names are long, as they can be easily read along the y-axis without overlapping or requiring rotation."
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
            st.success("Perfect score! You have a great understanding of bar plots!")
        elif score >= len(questions) / 2:
            st.success("Good job! You have a solid grasp of bar plot concepts.")
        else:
            st.info("Keep learning! Review the content about bar plots to improve your understanding.")

if __name__ == "__main__":
    main()
