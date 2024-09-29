import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide", page_title="Common Libraries for Visualization")

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

def main():
    st.title("Common Libraries for Visualization")
    st.write('**Developed by : Venugopal Adep**')
    
    st.markdown(f"""
    <p style='font-size: 1.2em; color: {colors['text']}; background-color: white; padding: 15px; border-radius: 5px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
    Welcome to the Common Libraries for Visualization demo! This app will help you understand 
    the capabilities of Matplotlib and Seaborn, two popular Python libraries for data visualization.
    </p>
    """, unsafe_allow_html=True)

    tabs = st.tabs([
        "Overview",
        "Matplotlib", 
        "Seaborn", 
        "Quiz"
    ])

    with tabs[0]:
        overview_tab()

    with tabs[1]:
        matplotlib_tab()

    with tabs[2]:
        seaborn_tab()

    with tabs[3]:
        quiz_tab()

def explain(text):
    st.markdown(f"""
    <div style='background-color: white; padding: 15px; border-radius: 5px; border-left: 5px solid {colors['accent']}; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
        <p style='color: {colors['text']}; margin: 0;'>{text}</p>
    </div>
    """, unsafe_allow_html=True)

def overview_tab():
    st.header("Overview of Visualization Libraries")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Matplotlib")
        st.markdown("""
        - One of the most popular libraries for data visualizations
        - Provides high-quality graphics and a variety of plots such as histograms, bar charts, pie charts, etc.
        - Some important functions: plot(), hist(), bar(), pie(), scatter(), text(), legend(), etc.
        """)

    with col2:
        st.subheader("Seaborn")
        st.markdown("""
        - Complementary to Matplotlib and specifically targets statistical data visualizations
        - A saying: "Matplotlib tries to make easy things easier and hard things possible, Seaborn tries to make a well-defined set of hard things easy too."
        - Some important functions: displot(), boxplot(), stripplot(), pairplot()
        """)

def matplotlib_tab():
    st.header("Matplotlib")
    
    explain("Matplotlib is a versatile library that gives you fine-grained control over your visualizations.")
    
    st.subheader("Matplotlib Examples")
    
    plot_type = st.selectbox("Choose a plot type", ["Line Plot", "Bar Chart", "Scatter Plot", "Histogram", "Pie Chart"])
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if plot_type == "Line Plot":
            code = """
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(5, 4))
plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.show()
            """
            st.code(code, language="python")
        
        elif plot_type == "Bar Chart":
            code = """
import matplotlib.pyplot as plt

data = {'A': 5, 'B': 7, 'C': 3, 'D': 8}

plt.figure(figsize=(5, 4))
plt.bar(data.keys(), data.values())
plt.title("Sample Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
            """
            st.code(code, language="python")
        
        elif plot_type == "Scatter Plot":
            code = """
import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)

plt.figure(figsize=(5, 4))
plt.scatter(x, y)
plt.title("Sample Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
            """
            st.code(code, language="python")
        
        elif plot_type == "Histogram":
            code = """
import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(0, 1, 1000)

plt.figure(figsize=(5, 4))
plt.hist(data, bins=30)
plt.title("Normal Distribution Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
            """
            st.code(code, language="python")
        
        else:  # Pie Chart
            code = """
import matplotlib.pyplot as plt

sizes = [30, 20, 25, 15, 10]
labels = ['A', 'B', 'C', 'D', 'E']

plt.figure(figsize=(5, 4))
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Sample Pie Chart")
plt.axis('equal')
plt.show()
            """
            st.code(code, language="python")
    
    with col2:
        fig, ax = plt.subplots(figsize=(5, 4))
        
        if plot_type == "Line Plot":
            x = np.linspace(0, 10, 100)
            y = np.sin(x)
            ax.plot(x, y)
            ax.set_title("Sine Wave")
            ax.set_xlabel("x")
            ax.set_ylabel("sin(x)")
        
        elif plot_type == "Bar Chart":
            data = {'A': 5, 'B': 7, 'C': 3, 'D': 8}
            ax.bar(data.keys(), data.values())
            ax.set_title("Sample Bar Chart")
            ax.set_xlabel("Categories")
            ax.set_ylabel("Values")
        
        elif plot_type == "Scatter Plot":
            x = np.random.rand(50)
            y = np.random.rand(50)
            ax.scatter(x, y)
            ax.set_title("Sample Scatter Plot")
            ax.set_xlabel("X")
            ax.set_ylabel("Y")
        
        elif plot_type == "Histogram":
            data = np.random.normal(0, 1, 1000)
            ax.hist(data, bins=30)
            ax.set_title("Normal Distribution Histogram")
            ax.set_xlabel("Value")
            ax.set_ylabel("Frequency")
        
        else:  # Pie Chart
            sizes = [30, 20, 25, 15, 10]
            labels = ['A', 'B', 'C', 'D', 'E']
            ax.pie(sizes, labels=labels, autopct='%1.1f%%')
            ax.set_title("Sample Pie Chart")
            ax.axis('equal')
        
        st.pyplot(fig, use_container_width=True)

def seaborn_tab():
    st.header("Seaborn")
    
    explain("Seaborn is built on top of Matplotlib and provides a high-level interface for drawing attractive statistical graphics.")
    
    st.subheader("Seaborn Examples")
    
    plot_type = st.selectbox("Choose a plot type", ["Distplot", "Boxplot", "Stripplot", "Pairplot"])
    
    col1, col2 = st.columns([1, 1])
    
    # Generate sample data
    data = pd.DataFrame({
        'A': np.random.normal(0, 1, 1000),
        'B': np.random.normal(2, 1, 1000),
        'C': np.random.normal(-1, 1, 1000)
    })
    
    with col1:
        if plot_type == "Distplot":
            code = """
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'A': np.random.normal(0, 1, 1000)
})

plt.figure(figsize=(5, 4))
sns.histplot(data=data, x='A', kde=True)
plt.title("Distribution Plot")
plt.show()
            """
            st.code(code, language="python")
        
        elif plot_type == "Boxplot":
            code = """
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'A': np.random.normal(0, 1, 1000),
    'B': np.random.normal(2, 1, 1000),
    'C': np.random.normal(-1, 1, 1000)
})

plt.figure(figsize=(5, 4))
sns.boxplot(data=data)
plt.title("Box Plot")
plt.show()
            """
            st.code(code, language="python")
        
        elif plot_type == "Stripplot":
            code = """
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'A': np.random.normal(0, 1, 1000),
    'B': np.random.normal(2, 1, 1000),
    'C': np.random.normal(-1, 1, 1000)
})

plt.figure(figsize=(5, 4))
sns.stripplot(data=data)
plt.title("Strip Plot")
plt.show()
            """
            st.code(code, language="python")
        
        else:  # Pairplot
            code = """
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'A': np.random.normal(0, 1, 1000),
    'B': np.random.normal(2, 1, 1000),
    'C': np.random.normal(-1, 1, 1000)
})

sns.pairplot(data, height=2)
plt.show()
            """
            st.code(code, language="python")
    
    with col2:
        if plot_type != "Pairplot":
            fig, ax = plt.subplots(figsize=(5, 4))
            
            if plot_type == "Distplot":
                sns.histplot(data=data, x='A', kde=True, ax=ax)
                ax.set_title("Distribution Plot")
            elif plot_type == "Boxplot":
                sns.boxplot(data=data, ax=ax)
                ax.set_title("Box Plot")
            elif plot_type == "Stripplot":
                sns.stripplot(data=data, ax=ax)
                ax.set_title("Strip Plot")
            
            st.pyplot(fig, use_container_width=True)
        else:  # Pairplot
            fig = sns.pairplot(data, height=2)
            st.pyplot(fig, use_container_width=True)

def quiz_tab():
    st.header("Visualization Libraries Quiz 📊")
    
    st.markdown(f"""
    <p style='font-size: 1.2em; color: {colors['text']}; background-color: white; padding: 15px; border-radius: 5px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
    Test your understanding of Matplotlib and Seaborn! Good luck! 🍀
    </p>
    """, unsafe_allow_html=True)

    questions = [
        {
            "question": "Which library is one of the most popular for data visualizations?",
            "options": ["NumPy", "Pandas", "Matplotlib", "Scikit-learn"],
            "correct": "Matplotlib",
            "explanation": "Matplotlib is one of the most popular libraries for data visualizations, providing high-quality graphics and a variety of plots."
        },
        {
            "question": "Which of the following is NOT a function typically associated with Matplotlib?",
            "options": ["plot()", "hist()", "bar()", "displot()"],
            "correct": "displot()",
            "explanation": "displot() is a function from Seaborn, not Matplotlib. The others (plot(), hist(), bar()) are common Matplotlib functions."
        },
        {
            "question": "What is Seaborn primarily designed for?",
            "options": ["Web development", "Machine learning", "Statistical data visualizations", "Database management"],
            "correct": "Statistical data visualizations",
            "explanation": "Seaborn is complementary to Matplotlib and specifically targets statistical data visualizations."
        },
        {
            "question": "According to the saying, what does Seaborn try to do?",
            "options": [
                "Make easy things easier and hard things possible",
                "Make a well-defined set of hard things easy",
                "Replace Matplotlib entirely",
                "Provide only 3D visualizations"
            ],
            "correct": "Make a well-defined set of hard things easy",
            "explanation": "The saying goes: 'Matplotlib tries to make easy things easier and hard things possible, Seaborn tries to make a well-defined set of hard things easy too.'"
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
    Remember, both Matplotlib and Seaborn have their strengths. Practice with both to become a visualization expert! 📈
    </p>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
