import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import random

st.set_page_config(layout="wide", page_title="NumPy Key Operations Explorer")

# Custom color palette
colors = {
    "primary": "#2962FF",
    "secondary": "#1565C0", 
    "accent": "#90CAF9",
    "background": "#E3F2FD",
    "text": "#0D47A1"
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
    .stTextInput>div>div>input,
    .stSelectbox>div>div>select {{
        background-color: white;
        color: {colors['text']};
        border-radius: 5px;
        border: 1px solid {colors['secondary']};
    }}
    .styled-table {{
        width: 100%;
        border-collapse: collapse;
        margin: 25px 0;
        font-size: 0.9em;
        font-family: sans-serif;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
    }}
    .styled-table thead tr {{
        background-color: {colors['primary']};
        color: #ffffff;
        text-align: left;
    }}
    .styled-table th,
    .styled-table td {{
        padding: 12px 15px;
    }}
    .styled-table tbody tr {{
        border-bottom: 1px solid #dddddd;
    }}
    .styled-table tbody tr:nth-of-type(even) {{
        background-color: #f3f3f3;
    }}
    .styled-table tbody tr:last-of-type {{
        border-bottom: 2px solid {colors['primary']};
    }}
</style>
""", unsafe_allow_html=True)

def main():
    st.title("NumPy Key Operations")
    st.write('**Developed by : Venugopal Adep**')

    st.markdown(f"""
    <p style='font-size: 1.2em; color: {colors['text']}; background-color: white; padding: 15px; border-radius: 5px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
    Welcome to the NumPy Key Operations Explorer! This app demonstrates some of the most commonly used
    operations and functions in NumPy for data manipulation. Let's explore these powerful tools!
    </p>
    """, unsafe_allow_html=True)

    tabs = st.tabs([
        "NumPy Overview",
        "Array Creation", "Array Reshaping", "Array Concatenation", 
        "Evenly Spaced Elements", "Matrix Operations", "NumPy Quiz"
    ])

    with tabs[0]:
        numpy_overview_tab()

    with tabs[1]:
        array_creation_tab()

    with tabs[2]:
        array_reshaping_tab()

    with tabs[3]:
        array_concatenation_tab()

    with tabs[4]:
        evenly_spaced_elements_tab()

    with tabs[5]:
        matrix_operations_tab()

    with tabs[6]:
        quiz_tab()

def show_code(code):
    st.code(code, language='python')

def explain(text):
    st.markdown(f"""
    <div style='background-color: white; padding: 15px; border-radius: 5px; border-left: 5px solid {colors['accent']}; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
        <p style='color: {colors['text']}; margin: 0;'>{text}</p>
    </div>
    """, unsafe_allow_html=True)

def numpy_overview_tab():
    st.header("NumPy Overview")
    
    st.markdown("""
    NumPy provides many useful operations for data manipulation. Some of the most commonly used
    operations and functions of NumPy are:
    """)

    data = {
        "Operation": [
            "Declare a NumPy array or convert a list into a NumPy array",
            "Reshape an n-dimensional array without changing the data inside the array",
            "Concatenate two or more arrays along a specified axis",
            "Create evenly spaced elements in an interval, particularly useful while working with loops",
            "Working with matrices and perform different operations on them"
        ],
        "Numpy Function": [
            "array()",
            "reshape()",
            "concatenate()",
            "arange(), linspace()",
            "dot(), transpose(), eye()"
        ]
    }

    df = pd.DataFrame(data)

    st.markdown(df.to_html(index=False, classes='styled-table'), unsafe_allow_html=True)

def array_creation_tab():
    st.header("Array Creation with np.array()")
    
    st.subheader("Convert a list into a NumPy array")
    list_input = st.text_input("Enter comma-separated values", "1,2,3,4,5")
    try:
        arr = np.array([float(x) for x in list_input.split(',')])
        st.write("Resulting array:", arr)
        show_code(f"np.array({list_input.split(',')})")
        explain("The np.array() function is used to create a NumPy array from a list or other iterable.")
    except:
        st.error("Invalid input. Please enter comma-separated numbers.")

def array_reshaping_tab():
    st.header("Array Reshaping with np.reshape()")
    
    st.subheader("Reshape an n-dimensional array")
    arr = np.arange(12)
    st.write("Original array:", arr)
    
    new_shape = st.text_input("Enter new shape (e.g., 3,4)", "3,4")
    try:
        new_shape = tuple(map(int, new_shape.split(',')))
        result = arr.reshape(new_shape)
        st.write("Reshaped array:")
        st.write(result)
        show_code(f"arr.reshape({new_shape})")
        explain("The reshape() function changes the shape of an array without altering its data.")
    except:
        st.error("Invalid shape. Please enter comma-separated integers.")

def array_concatenation_tab():
    st.header("Array Concatenation with np.concatenate()")
    
    st.subheader("Concatenate two or more arrays")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Array 1:")
        arr1 = np.array([1, 2, 3])
        st.write(arr1)
    with col2:
        st.write("Array 2:")
        arr2 = np.array([4, 5, 6])
        st.write(arr2)
    
    result = np.concatenate((arr1, arr2))
    st.write("Concatenated array:", result)
    show_code("np.concatenate((arr1, arr2))")
    explain("The concatenate() function joins two or more arrays along a specified axis.")

def evenly_spaced_elements_tab():
    st.header("Evenly Spaced Elements with np.arange() and np.linspace()")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("np.arange()")
        start = st.number_input("Start", value=0)
        stop = st.number_input("Stop", value=10)
        step = st.number_input("Step", value=1)
        arr_arange = np.arange(start, stop, step)
        st.write("Resulting array:", arr_arange)
        show_code(f"np.arange({start}, {stop}, {step})")
        explain("np.arange() creates an array with evenly spaced values within a given interval.")
    
    with col2:
        st.subheader("np.linspace()")
        start = st.number_input("Start", value=0, key="linspace_start")
        stop = st.number_input("Stop", value=10, key="linspace_stop")
        num = st.number_input("Number of points", value=5, min_value=2)
        arr_linspace = np.linspace(start, stop, num)
        st.write("Resulting array:", arr_linspace)
        show_code(f"np.linspace({start}, {stop}, {num})")
        explain("np.linspace() creates an array with a specified number of evenly spaced points between two values.")

def matrix_operations_tab():
    st.header("Matrix Operations")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Matrix A")
        A = np.array([[1, 2], [3, 4]])
        st.write(A)
    
    with col2:
        st.subheader("Matrix B")
        B = np.array([[5, 6], [7, 8]])
        st.write(B)
    
    with col3:
        st.subheader("A · B")
        result = np.dot(A, B)
        st.write(result)
    
    st.subheader("Calculations")
    st.write("(1 * 5 + 2 * 7) = 19")
    st.write("(1 * 6 + 2 * 8) = 22")
    st.write("(3 * 5 + 4 * 7) = 43")
    st.write("(3 * 6 + 4 * 8) = 50")
    
    show_code("np.dot(A, B)")
    explain("The dot() function computes the matrix product of two arrays.")
    
    st.subheader("Matrix Transpose")
    A = np.array([[1, 2, 3], [4, 5, 6]])
    st.write("Original matrix:")
    st.write(A)
    result = A.T
    st.write("Transposed matrix:")
    st.write(result)
    show_code("A.T")
    explain("The .T attribute returns the transpose of the array.")

    st.subheader("Identity Matrix with np.eye()")
    n = st.number_input("Enter the size of the identity matrix", min_value=1, value=3)
    identity_matrix = np.eye(n)
    st.write(f"{n}x{n} Identity Matrix:")
    st.write(identity_matrix)
    show_code(f"np.eye({n})")
    explain("np.eye() creates an identity matrix, which is a square matrix with 1s on the main diagonal and 0s elsewhere.")

def quiz_tab():
    st.header("NumPy Quiz 🧠")
    
    st.markdown(f"""
    <p style='font-size: 1.2em; color: {colors['text']}; background-color: white; padding: 15px; border-radius: 5px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
    Test your NumPy knowledge with these questions! Good luck! 🍀
    </p>
    """, unsafe_allow_html=True)

    questions = [
        {
            "question": "Which NumPy function is used to create an array from a list?",
            "options": ["np.create()", "np.array()", "np.make()", "np.list_to_array()"],
            "correct": "np.array()",
            "explanation": "np.array() is used to create a NumPy array from a list or other iterable."
        },
        {
            "question": "Which function is used to change the shape of an array without changing its data?",
            "options": ["np.resize()", "np.reshape()", "np.rearrange()", "np.reformat()"],
            "correct": "np.reshape()",
            "explanation": "np.reshape() changes the shape of an array without altering its data."
        },
        {
            "question": "Which function is used to join two or more arrays?",
            "options": ["np.join()", "np.merge()", "np.concatenate()", "np.combine()"],
            "correct": "np.concatenate()",
            "explanation": "np.concatenate() joins two or more arrays along a specified axis."
        },
        {
            "question": "Which function creates an array with evenly spaced values within a given interval?",
            "options": ["np.space()", "np.interval()", "np.arange()", "np.range()"],
            "correct": "np.arange()",
            "explanation": "np.arange() creates an array with evenly spaced values within a given interval."
        },
        {
            "question": "Which function computes the matrix product of two arrays?",
            "options": ["np.multiply()", "np.dot()", "np.matmul()", "np.product()"],
            "correct": "np.dot()",
            "explanation": "np.dot() computes the matrix product of two arrays."
        },
        {
            "question": "What attribute is used to get the transpose of an array?",
            "options": [".transpose", ".T", ".flip", ".rotate"],
            "correct": ".T",
            "explanation": "The .T attribute returns the transpose of an array."
        },
        {
            "question": "Which function creates an identity matrix?",
            "options": ["np.identity()", "np.ones()", "np.eye()", "np.diagonal()"],
            "correct": "np.eye()",
            "explanation": "np.eye() creates an identity matrix, which is a square matrix with 1s on the main diagonal and 0s elsewhere."
        }
    ]

    for i, q in enumerate(questions, 1):
        st.subheader(f"Question {i}")
        st.markdown(f"<p style='font-size: 1.1em; color: {colors['primary']};'>{q['question']}</p>", unsafe_allow_html=True)
        
        user_answer = st.radio(f"Select your answer for Question {i}", q["options"], key=f"q{i}")
        
        if st.button(f"Check Answer for Question {i}"):
            if user_answer == q["correct"]:
                st.success("Correct! Great job! 🎉")
            else:
                st.error("Oops! That's not quite right. Try again! 🔄")
            
            explain(f"Explanation: {q['explanation']}")
        
        st.markdown("---")

    st.markdown(f"""
    <p style='font-size: 1.2em; color: {colors['text']}; background-color: white; padding: 15px; border-radius: 5px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
    Remember, the key to mastering NumPy is practice and experimentation. 
    Keep exploring the other tabs to learn more about NumPy's powerful features! 💪
    </p>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
