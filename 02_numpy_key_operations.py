import streamlit as st
import numpy as np
import plotly.graph_objects as go

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

def show_code(code):
    st.code(code, language='python')

def explain(text):
    st.markdown(f"""
    <div style='background-color: white; padding: 15px; border-radius: 5px; border-left: 5px solid #90CAF9; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
        <p style='color: #0D47A1; margin: 0;'>{text}</p>
    </div>
    """, unsafe_allow_html=True)

# Call the function to display the tab
matrix_operations_tab()
