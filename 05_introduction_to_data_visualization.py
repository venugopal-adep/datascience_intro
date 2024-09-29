import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(layout="wide", page_title="Introduction to Data Visualization")

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

def main():
    st.title("Introduction to Data Visualization")
    st.write('**Developed by : Venugopal Adep**')

    st.markdown(f"""
    <p style='font-size: 1.2em; color: {colors['text']}; background-color: white; padding: 15px; border-radius: 5px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
    Welcome to the Introduction to Data Visualization! This app will help you understand 
    what data visualization is and why it's important in data science.
    </p>
    """, unsafe_allow_html=True)

    tabs = st.tabs([
        "Introduction",
        "What is Data Visualization?", 
        "Why is it Important?", 
        "Interactive Example",
        "Quiz"
    ])

    with tabs[0]:
        introduction_tab()

    with tabs[1]:
        what_is_data_viz_tab()

    with tabs[2]:
        why_data_viz_important_tab()

    with tabs[3]:
        interactive_example_tab()

    with tabs[4]:
        quiz_tab()

def explain(text):
    st.markdown(f"""
    <div style='background-color: white; padding: 15px; border-radius: 5px; border-left: 5px solid {colors['accent']}; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
        <p style='color: {colors['text']}; margin: 0;'>{text}</p>
    </div>
    """, unsafe_allow_html=True)

def introduction_tab():
    st.header("Introduction to Visualization")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("What is Data Visualization?")
        st.markdown("""
        - Visual representation of data
        - Helps to observe and communicate patterns & trends with naked eye
        """)

    with col2:
        st.subheader("Why Data Visualization is important?")
        st.markdown("""
        - Data visualization helps to communicate information in a manner that is universal, fast, and effective
        - Communicating insights to non-technical decision makers is one of the most critical phases in a data science project
        """)

def what_is_data_viz_tab():
    st.header("What is Data Visualization?")
    
    st.markdown("""
    Data visualization is:
    - Visual representation of data
    - Helps to observe and communicate patterns & trends with naked eye
    """)
    
    explain("Data visualization transforms raw data into graphical representations, making it easier for humans to understand complex information at a glance.")
    
    # Example visualization
    data = pd.DataFrame({
        'category': ['A', 'B', 'C', 'D', 'E'],
        'value': [23, 48, 12, 35, 19]
    })
    
    fig = px.bar(data, x='category', y='value', title='Simple Bar Chart Example')
    st.plotly_chart(fig)
    
    st.write("This bar chart is a simple example of data visualization. It represents the values for different categories visually, making it easy to compare them.")

def why_data_viz_important_tab():
    st.header("Why is Data Visualization Important?")
    
    st.markdown("""
    - Data visualization helps to communicate information in a manner that is universal, fast, and effective
    - Communicating insights to non-technical decision makers is one of the most critical phases in a data science project
    """)
    
    explain("Effective data visualization bridges the gap between complex data analysis and decision-making, making insights accessible to all stakeholders.")
    
    # Example of before and after visualization
    st.subheader("Before and After Visualization")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("Raw Data:")
        data = pd.DataFrame({
            'Date': pd.date_range(start='2023-01-01', periods=10),
            'Value': [10, 15, 13, 18, 20, 21, 19, 25, 28, 30]
        })
        st.dataframe(data)
    
    with col2:
        st.write("Visualized Data:")
        fig = px.line(data, x='Date', y='Value', title='Trend Over Time')
        st.plotly_chart(fig)
    
    st.write("Notice how the trend is much easier to spot in the line chart compared to the raw data.")

def interactive_example_tab():
    st.header("Interactive Visualization Example")
    
    st.write("Let's create a scatter plot with some random data. You can adjust the number of points and the range of values.")
    
    col1, col2 = st.columns([1, 3])  # Create two columns with a 1:3 width ratio
    
    with col1:
        num_points = st.slider("Number of data points", min_value=10, max_value=1000, value=100, step=10)
        value_range = st.slider("Range of values", min_value=0, max_value=100, value=(0, 50))
    
    data = pd.DataFrame({
        'x': np.random.rand(num_points) * (value_range[1] - value_range[0]) + value_range[0],
        'y': np.random.rand(num_points) * (value_range[1] - value_range[0]) + value_range[0],
        'category': np.random.choice(['A', 'B', 'C'], num_points)
    })
    
    with col2:
        fig = px.scatter(data, x='x', y='y', color='category', title='Interactive Scatter Plot')
        st.plotly_chart(fig, use_container_width=True)
    
    explain("This interactive example demonstrates how data visualization can help you explore and understand patterns in your data. Try adjusting the sliders to see how the visualization changes!")

def quiz_tab():
    st.header("Data Visualization Quiz 📊")
    
    st.markdown(f"""
    <p style='font-size: 1.2em; color: {colors['text']}; background-color: white; padding: 15px; border-radius: 5px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
    Test your understanding of data visualization concepts! Good luck! 🍀
    </p>
    """, unsafe_allow_html=True)

    questions = [
        {
            "question": "What is the primary purpose of data visualization?",
            "options": [
                "To make data look pretty",
                "To visual represent data and communicate patterns & trends",
                "To hide complex information",
                "To confuse non-technical stakeholders"
            ],
            "correct": "To visual represent data and communicate patterns & trends",
            "explanation": "Data visualization aims to represent data visually, making it easier to observe and communicate patterns and trends."
        },
        {
            "question": "Why is data visualization important in a data science project?",
            "options": [
                "It's not important",
                "It helps to make the project longer",
                "It's crucial for communicating insights to non-technical decision makers",
                "It's only used to impress clients"
            ],
            "correct": "It's crucial for communicating insights to non-technical decision makers",
            "explanation": "Communicating insights to non-technical decision makers is one of the most critical phases in a data science project, and data visualization is key to this process."
        },
        {
            "question": "Which of the following best describes how data visualization communicates information?",
            "options": [
                "Slowly and ineffectively",
                "In a complex, technical manner",
                "Universal, fast, and effective",
                "Only for technical audiences"
            ],
            "correct": "Universal, fast, and effective",
            "explanation": "Data visualization helps to communicate information in a manner that is universal, fast, and effective, making it accessible to a wide audience."
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
    Remember, effective data visualization is a powerful tool in data science. Keep practicing and exploring different techniques! 📈
    </p>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
