import streamlit as st

st.set_page_config(page_title="NumPy & Pandas Explorer", layout="wide")

st.title("Key Libraries for Data Manipulation - NumPy & Pandas")

col1, col2 = st.columns(2)

with col1:
    st.header("NumPy")
    st.markdown("""
    - Numerical Python
    - Fundamental package for scientific computing
    - A powerful N-dimensional array object - ndarray
    - Useful in linear algebra, vector calculus, and random number capabilities, etc.
    """)

with col2:
    st.header("Pandas")
    st.markdown("""
    - Extremely useful for data manipulation and exploratory analysis
    - Offers two major data structures - Series & DataFrame
    - A DataFrame is made up of several Series - Each column of a DataFrame is a Series
    - In a DataFrame, each column can have its own data type unlike NumPy array which creates all entries with the same data type
    """)

st.markdown("""
<style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    h1 {
        color: #0066CC;
    }
    h3 {
        color: #0066CC;
    }
</style>
""", unsafe_allow_html=True)
