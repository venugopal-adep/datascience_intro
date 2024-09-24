import streamlit as st
import pandas as pd
import plotly.express as px
import io

st.set_page_config(layout="wide", page_title="Interactive Pandas Explorer")

# Custom color palette
colors = {
    "primary": "#4A4E69",
    "secondary": "#9A8C98",
    "accent": "#C9ADA7",
    "background": "#F2E9E4",
    "text": "#22223B"
}

# Custom CSS (same as before)
st.markdown("""
<style>
    ... (CSS styles remain the same)
</style>
""", unsafe_allow_html=True)

def main():
    st.title("🐼 Pandas Key Operations")
    st.write('**Developed by : Venugopal Adep**')

    st.markdown(f"""
    <p style='font-size: 1.2em; color: {colors['text']}; background-color: white; padding: 15px; border-radius: 5px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
    Welcome to the Interactive Pandas Explorer! This app lets you dive into the powerful world of Pandas, 
    a data manipulation library built on top of NumPy. Experiment with various Pandas functions and 
    see the results in real-time. Let's make data analysis fun and colorful! 🌈
    </p>
    """, unsafe_allow_html=True)

    tabs = st.tabs([
        "Data Loading 📊", "Data Info 🔍", "Data Description 📈", 
        "Data Merging 🔗", "Data Grouping 👥", "Pandas Pop Quiz 🧠"
    ])

    with tabs[0]:
        data_loading_tab()

    with tabs[1]:
        data_info_tab()

    with tabs[2]:
        data_description_tab()

    with tabs[3]:
        data_merging_tab()

    with tabs[4]:
        data_grouping_tab()

    with tabs[5]:
        quiz_tab()

def show_code(code):
    st.code(code, language='python')

def explain(text):
    st.markdown(f"""
    <div style='background-color: white; padding: 15px; border-radius: 5px; border-left: 5px solid {colors['accent']}; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
        <p style='color: {colors['text']}; margin: 0;'>{text}</p>
    </div>
    """, unsafe_allow_html=True)

def data_loading_tab():
    st.header("Data Loading 📊")
    
    st.subheader("Load data from different sources/formats")
    
    file_format = st.selectbox("Choose a file format", ["CSV", "Excel", "JSON", "HTML"])
    
    if file_format == "CSV":
        uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.write(df)
            show_code("pd.read_csv('your_file.csv')")
    elif file_format == "Excel":
        uploaded_file = st.file_uploader("Upload an Excel file", type="xlsx")
        if uploaded_file is not None:
            df = pd.read_excel(uploaded_file)
            st.write(df)
            show_code("pd.read_excel('your_file.xlsx')")
    elif file_format == "JSON":
        uploaded_file = st.file_uploader("Upload a JSON file", type="json")
        if uploaded_file is not None:
            df = pd.read_json(uploaded_file)
            st.write(df)
            show_code("pd.read_json('your_file.json')")
    elif file_format == "HTML":
        url = st.text_input("Enter a URL with HTML tables")
        if url:
            dfs = pd.read_html(url)
            st.write(f"Found {len(dfs)} tables. Showing the first one:")
            st.write(dfs[0])
            show_code("pd.read_html('url_with_tables')")
    
    explain(f"Pandas makes it easy to load data from various sources. The `read_{file_format.lower()}()` function is used to load data from {file_format} files or URLs.")

def data_info_tab():
    st.header("Data Info 🔍")
    
    st.subheader("Get information about the data")
    
    # Create a sample DataFrame for demonstration
    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': ['a', 'b', 'c', 'd', 'e'],
        'C': [1.1, 2.2, 3.3, 4.4, 5.5],
        'D': [True, False, True, True, False]
    })
    
    st.write("Sample DataFrame:")
    st.write(df)
    
    if st.button("Show DataFrame Info"):
        buffer = io.StringIO()
        df.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)
        show_code("df.info()")
    
    explain("The `info()` method provides a concise summary of the DataFrame, including the column names, non-null counts, and data types. It's a great way to get a quick overview of your data structure and memory usage.")

def data_description_tab():
    st.header("Data Description 📈")
    
    st.subheader("View basic statistical details of numeric data")
    
    # Create a sample DataFrame for demonstration
    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': [1.1, 2.2, 3.3, 4.4, 5.5]
    })
    
    st.write("Sample DataFrame:")
    st.write(df)
    
    if st.button("Show DataFrame Description"):
        st.write(df.describe())
        show_code("df.describe()")
    
    explain("The `describe()` method generates various summary statistics of the numeric columns in the DataFrame. It includes count, mean, standard deviation, minimum, 25th percentile (Q1), median (50th percentile), 75th percentile (Q3), and maximum.")

def data_merging_tab():
    st.header("Data Merging 🔗")
    
    st.subheader("Merge two DataFrames")
    
    # Create two sample DataFrames
    df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'], 'value1': [1, 2, 3, 4]})
    df2 = pd.DataFrame({'key': ['B', 'D', 'E', 'F'], 'value2': [20, 40, 50, 60]})
    
    st.write("DataFrame 1:")
    st.write(df1)
    st.write("DataFrame 2:")
    st.write(df2)
    
    merge_type = st.selectbox("Choose merge type", ["Inner Join", "Left Join", "Right Join", "Full Outer Join"])
    
    if st.button("Merge DataFrames"):
        if merge_type == "Inner Join":
            result = pd.merge(df1, df2, on='key', how='inner')
            show_code("pd.merge(df1, df2, on='key', how='inner')")
        elif merge_type == "Left Join":
            result = pd.merge(df1, df2, on='key', how='left')
            show_code("pd.merge(df1, df2, on='key', how='left')")
        elif merge_type == "Right Join":
            result = pd.merge(df1, df2, on='key', how='right')
            show_code("pd.merge(df1, df2, on='key', how='right')")
        else:
            result = pd.merge(df1, df2, on='key', how='outer')
            show_code("pd.merge(df1, df2, on='key', how='outer')")
        
        st.write("Merged DataFrame:")
        st.write(result)
    
    explain(f"The `merge()` function combines two DataFrames based on a common column or index. The '{merge_type.lower()}' option determines how to handle rows that don't have matches in both DataFrames.")

def data_grouping_tab():
    st.header("Data Grouping 👥")
    
    st.subheader("Group data and apply summary functions")
    
    # Create a sample DataFrame
    df = pd.DataFrame({
        'Category': ['A', 'B', 'A', 'B', 'A', 'C', 'C', 'B'],
        'Value': [10, 20, 30, 40, 50, 60, 70, 80]
    })
    
    st.write("Sample DataFrame:")
    st.write(df)
    
    if st.button("Group by Category and Sum Values"):
        result = df.groupby('Category')['Value'].sum()
        st.write("Grouped Result:")
        st.write(result)
        show_code("df.groupby('Category')['Value'].sum()")
    
    explain("The `groupby()` function allows you to split the data into groups based on some criteria. You can then apply various aggregation functions like sum(), mean(), count(), etc., to these groups. It's a powerful way to summarize and analyze your data.")

def quiz_tab():
    st.header("Pandas Pop Quiz 🧠")
    
    st.markdown(f"""
    <p style='font-size: 1.2em; color: {colors['text']}; background-color: white; padding: 15px; border-radius: 5px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
    Test your Pandas knowledge with these questions! Good luck! 🍀
    </p>
    """, unsafe_allow_html=True)

    questions = [
        {
            "question": "Which Pandas function is used to load data from a CSV file?",
            "options": ["pd.load_csv()", "pd.read_csv()", "pd.import_csv()", "pd.csv_reader()"],
            "correct": "pd.read_csv()",
            "explanation": "pd.read_csv() is the correct function to load data from a CSV file in Pandas."
        },
        {
            "question": "What function would you use to read data from an Excel file?",
            "options": ["pd.read_excel()", "pd.load_excel()", "pd.excel_reader()", "pd.import_excel()"],
            "correct": "pd.read_excel()",
            "explanation": "pd.read_excel() is used to read data from Excel files in Pandas."
        },
        {
            "question": "Which function allows you to read HTML tables from a webpage?",
            "options": ["pd.read_webpage()", "pd.read_html()", "pd.import_html()", "pd.html_reader()"],
            "correct": "pd.read_html()",
            "explanation": "pd.read_html() is used to read HTML tables from webpages in Pandas."
        },
        {
            "question": "What function would you use to read JSON data?",
            "options": ["pd.read_json()", "pd.load_json()", "pd.json_reader()", "pd.import_json()"],
            "correct": "pd.read_json()",
            "explanation": "pd.read_json() is used to read JSON data in Pandas."
        },
        {
            "question": "Which method provides a concise summary of a DataFrame, including column types and non-null counts?",
            "options": ["summary()", "info()", "describe()", "details()"],
            "correct": "info()",
            "explanation": "The info() method provides a concise summary of the DataFrame, including column types and non-null counts."
        },
        {
            "question": "What method generates descriptive statistics of a DataFrame's numeric columns?",
            "options": ["summarize()", "stats()", "describe()", "analyze()"],
            "correct": "describe()",
            "explanation": "The describe() method generates descriptive statistics of a DataFrame's numeric columns, including count, mean, std, min, and max."
        },
        {
            "question": "Which function is used to combine two DataFrames based on a common column or index?",
            "options": ["combine()", "join()", "merge()", "concat()"],
            "correct": "merge()",
            "explanation": "The merge() function is used to combine two DataFrames based on a common column or index."
        },
        {
            "question": "What method is used to split the data into groups based on some criteria?",
            "options": ["split()", "groupby()", "categorize()", "segment()"],
            "correct": "groupby()",
            "explanation": "The groupby() method is used to split the data into groups based on some criteria, allowing for aggregate operations on these groups."
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
    Remember, the key to mastering Pandas is practice and experimentation. 
    Keep exploring the other tabs to learn more about Pandas' powerful features! 💪
    </p>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()