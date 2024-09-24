import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import io

st.set_page_config(layout="wide", page_title="NumPy & Pandas Explorer")

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
</style>
""", unsafe_allow_html=True)

def explain(text):
    st.markdown(f"""
    <div style='background-color: white; padding: 15px; border-radius: 5px; border-left: 5px solid {colors['accent']}; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
        <p style='color: {colors['text']}; margin: 0;'>{text}</p>
    </div>
    """, unsafe_allow_html=True)

def main():
    st.title("NumPy & Pandas Explorer")
    st.write('**Developed by : Venugopal Adep**')
    
    tabs = st.tabs(["Learn", "NumPy Demo", "Pandas Demo", "Quiz"])
    
    with tabs[0]:
        learn_tab()
    
    with tabs[1]:
        numpy_demo_tab()
    
    with tabs[2]:
        pandas_demo_tab()
    
    with tabs[3]:
        quiz_tab()

def learn_tab():
    st.header("Key Libraries for Data Manipulation - NumPy & Pandas")
    
    st.subheader("NumPy")
    st.markdown("""
    - Numerical Python
    - Fundamental package for scientific computing
    - A powerful N-dimensional array object - ndarray
    - Useful in linear algebra, vector calculus, and random number capabilities, etc.
    """)
    
    st.subheader("Pandas")
    st.markdown("""
    - Extremely useful for data manipulation and exploratory analysis
    - Offers two major data structures - Series & DataFrame
    - A DataFrame is made up of several Series - Each column of a DataFrame is a Series
    - In a DataFrame, each column can have its own data type unlike NumPy array which creates all entries with the same data type
    """)
    
    explain("Both NumPy and Pandas are essential libraries for data manipulation in Python, with NumPy focusing on numerical operations and Pandas excelling in data analysis and manipulation.")

def numpy_demo_tab():
    st.header("NumPy Demo")
    
    st.subheader("Create a NumPy Array")
    dimensions = st.slider("Select dimensions for the array", 1, 3, 2)
    size = st.number_input("Enter size for each dimension", 1, 10, 3)
    
    arr = None  # Initialize arr outside the button click scope

    if st.button("Generate NumPy Array"):
        if dimensions == 1:
            arr = np.random.rand(size)
        elif dimensions == 2:
            arr = np.random.rand(size, size)
        else:
            arr = np.random.rand(size, size, size)
        
        st.write("Generated NumPy Array:")
        st.write(arr)
        
        st.write(f"Array Shape: {arr.shape}")
        st.write(f"Array Dimensions: {arr.ndim}")
        st.write(f"Array Size: {arr.size}")
        
        if dimensions == 2:
            fig = px.imshow(arr, color_continuous_scale='viridis')
            st.plotly_chart(fig)
    
    st.subheader("NumPy Operations")
    operation = st.selectbox("Select an operation", ["Sum", "Mean", "Standard Deviation", "Matrix Multiplication"])
    
    if arr is not None:  # Only show the "Perform Operation" button if arr is defined
        if operation == "Matrix Multiplication" and dimensions < 2:
            st.warning("Matrix multiplication requires at least 2 dimensions.")
        elif st.button("Perform Operation"):
            if operation == "Sum":
                result = np.sum(arr)
            elif operation == "Mean":
                result = np.mean(arr)
            elif operation == "Standard Deviation":
                result = np.std(arr)
            elif operation == "Matrix Multiplication" and dimensions >= 2:
                result = np.matmul(arr, arr)
            
            st.write(f"Result of {operation}:")
            st.write(result)
    else:
        st.info("Please generate a NumPy array first before performing operations.")

def pandas_demo_tab():
    st.header("Pandas Demo")
    
    st.subheader("Create a Pandas DataFrame")
    num_rows = st.slider("Number of rows", 5, 20, 10)
    
    if st.button("Generate DataFrame"):
        df = pd.DataFrame({
            'A': np.random.randn(num_rows),
            'B': np.random.choice(['X', 'Y', 'Z'], num_rows),
            'C': np.random.randint(1, 100, num_rows),
            'D': pd.date_range(start='2023-01-01', periods=num_rows)
        })
        
        st.write("Generated Pandas DataFrame:")
        st.write(df)
        
        st.write("DataFrame Info:")
        buffer = io.StringIO()
        df.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)
        
        st.subheader("DataFrame Operations")
        operation = st.selectbox("Select an operation", ["Describe", "Group By", "Filter", "Sort"])
        
        if operation == "Describe":
            st.write(df.describe())
        elif operation == "Group By":
            st.write(df.groupby('B').mean())
        elif operation == "Filter":
            st.write(df[df['C'] > 50])
        elif operation == "Sort":
            st.write(df.sort_values('A', ascending=False))

def quiz_tab():
    st.header("Quiz: NumPy & Pandas")
    
    questions = [
        {
            "question": "What is the primary data structure in NumPy?",
            "options": ["List", "Dictionary", "ndarray", "Series"],
            "correct": 2,
            "explanation": "The primary data structure in NumPy is the ndarray (N-dimensional array)."
        },
        {
            "question": "Which of these is NOT a major data structure in Pandas?",
            "options": ["Series", "DataFrame", "Panel", "Matrix"],
            "correct": 3,
            "explanation": "Pandas primarily offers two data structures: Series and DataFrame. Matrix is not a major Pandas data structure."
        },
        {
            "question": "In a Pandas DataFrame, can different columns have different data types?",
            "options": ["Yes", "No"],
            "correct": 0,
            "explanation": "Yes, in a Pandas DataFrame, each column can have its own data type, unlike NumPy arrays where all elements typically have the same data type."
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
            st.success("Perfect score! You have a great understanding of NumPy and Pandas!")
        elif score >= len(questions) / 2:
            st.success("Good job! You have a solid grasp of NumPy and Pandas concepts.")
        else:
            st.info("Keep learning! Review the content about NumPy and Pandas to improve your understanding.")

if __name__ == "__main__":
    main()