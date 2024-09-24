import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide", page_title="Which Visualization to Use")

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
    st.title("Which Visualization to Use")
    st.write('**Developed by : Venugopal Adep**')
    
    st.markdown(f"""
    <p style='font-size: 1.2em; color: {colors['text']}; background-color: white; padding: 15px; border-radius: 5px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
    There are numerous types of plots available in Matplotlib and Seaborn, each has its own usage with 
    certain specific data. Choosing the right visualization for the right purpose is very important.
    </p>
    """, unsafe_allow_html=True)

    tabs = st.tabs([
        "Univariate Continuous",
        "Univariate Categorical",
        "Bivariate Continuous",
        "Bivariate Time Series",
        "Bivariate Continuous-Categorical",
        "Bivariate Categorical-Categorical",
        "Quiz"
    ])

    with tabs[0]:
        univariate_continuous()
    with tabs[1]:
        univariate_categorical()
    with tabs[2]:
        bivariate_continuous()
    with tabs[3]:
        bivariate_time_series()
    with tabs[4]:
        bivariate_continuous_categorical()
    with tabs[5]:
        bivariate_categorical_categorical()
    with tabs[6]:
        quiz()

def explain(text):
    st.markdown(f"""
    <div style='background-color: white; padding: 15px; border-radius: 5px; border-left: 5px solid {colors['accent']}; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
        <p style='color: {colors['text']}; margin: 0;'>{text}</p>
    </div>
    """, unsafe_allow_html=True)

def show_code(code):
    st.code(code, language='python')

def univariate_continuous():
    st.header("Univariate Continuous Visualization")
    explain("Use this when you want to show how the values of a single continuous variable are distributed.")
    
    # Generate sample data
    data = np.random.normal(0, 1, 1000)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Histogram
    sns.histplot(data, kde=True, ax=ax1)
    ax1.set_title("Histogram with KDE")
    
    # Distribution plot
    sns.kdeplot(data, shade=True, ax=ax2)
    ax2.set_title("Distribution Plot")
    
    st.pyplot(fig)
    
    show_code("""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate sample data
data = np.random.normal(0, 1, 1000)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Histogram
sns.histplot(data, kde=True, ax=ax1)
ax1.set_title("Histogram with KDE")

# Distribution plot
sns.kdeplot(data, shade=True, ax=ax2)
ax2.set_title("Distribution Plot")

plt.show()
    """)
    
    st.markdown("**Examples:**")
    st.write("- Distribution of cholesterol ranges")
    st.write("- Distribution of horsepower of cars")

def univariate_categorical():
    st.header("Univariate Categorical Visualization")
    explain("Use this when you want to show the count of observations in each category of a categorical variable.")
    
    # Generate sample data
    categories = ['A', 'B', 'C', 'D']
    counts = np.random.randint(10, 100, size=len(categories))
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=categories, y=counts)
    ax.set_title("Count Plot")
    
    st.pyplot(fig)
    
    show_code("""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate sample data
categories = ['A', 'B', 'C', 'D']
counts = np.random.randint(10, 100, size=len(categories))

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=categories, y=counts)
ax.set_title("Count Plot")

plt.show()
    """)
    
    st.markdown("**Example:**")
    st.write("- What is the count of employees for each type of degree in an organization?")

def bivariate_continuous():
    st.header("Bivariate Continuous Visualization")
    explain("Use this when you want to show how two continuous variables are correlated.")
    
    # Generate sample data
    x = np.random.rand(100)
    y = 2 * x + np.random.normal(0, 0.1, 100)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=x, y=y)
    ax.set_title("Scatter Plot")
    
    st.pyplot(fig)
    
    show_code("""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate sample data
x = np.random.rand(100)
y = 2 * x + np.random.normal(0, 0.1, 100)

fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x=x, y=y)
ax.set_title("Scatter Plot")

plt.show()
    """)
    
    st.markdown("**Example:**")
    st.write("- How tip varies with the total bill?")

def bivariate_time_series():
    st.header("Bivariate Time Series Visualization")
    explain("Use this when you want to show how a continuous variable changes over time.")
    
    # Generate sample data
    dates = pd.date_range(start='2023-01-01', periods=100)
    values = np.cumsum(np.random.randn(100))
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x=dates, y=values)
    ax.set_title("Line Plot")
    
    st.pyplot(fig)
    
    show_code("""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Generate sample data
dates = pd.date_range(start='2023-01-01', periods=100)
values = np.cumsum(np.random.randn(100))

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x=dates, y=values)
ax.set_title("Line Plot")

plt.show()
    """)
    
    st.markdown("**Example:**")
    st.write("- How sales varies on different days?")

def bivariate_continuous_categorical():
    st.header("Bivariate Continuous-Categorical Visualization")
    explain("Use this when you want to show how the range of a continuous variable varies for different categories.")
    
    # Generate sample data
    categories = ['A', 'B', 'C', 'D']
    data = [np.random.normal(i, 1, 100) for i in range(len(categories))]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Box plot
    sns.boxplot(data=data, ax=ax1)
    ax1.set_title("Box Plot")
    
    # Swarm plot
    sns.swarmplot(data=data, ax=ax2)
    ax2.set_title("Swarm Plot")
    
    st.pyplot(fig)
    
    show_code("""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate sample data
categories = ['A', 'B', 'C', 'D']
data = [np.random.normal(i, 1, 100) for i in range(len(categories))]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Box plot
sns.boxplot(data=data, ax=ax1)
ax1.set_title("Box Plot")

# Swarm plot
sns.swarmplot(data=data, ax=ax2)
ax2.set_title("Swarm Plot")

plt.show()
    """)
    
    st.markdown("**Examples:**")
    st.write("- How tip varies at lunch and dinner?")
    st.write("- How tips varies with day of the week?")

def bivariate_categorical_categorical():
    st.header("Bivariate Categorical-Categorical Visualization")
    explain("Use this when you want to show the number or percentage of records of one categorical variable which falls under each category of another categorical variable.")
    
    # Generate sample data
    categories1 = ['A', 'B', 'C']
    categories2 = ['X', 'Y']
    data = np.random.randint(10, 100, size=(len(categories1), len(categories2)))
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(data, annot=True, fmt='d', cmap='YlGnBu')
    ax.set_title("Stacked Bar Plot (Heatmap representation)")
    ax.set_xlabel("Category 2")
    ax.set_ylabel("Category 1")
    
    st.pyplot(fig)
    
    show_code("""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate sample data
categories1 = ['A', 'B', 'C']
categories2 = ['X', 'Y']
data = np.random.randint(10, 100, size=(len(categories1), len(categories2)))

fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(data, annot=True, fmt='d', cmap='YlGnBu')
ax.set_title("Stacked Bar Plot (Heatmap representation)")
ax.set_xlabel("Category 2")
ax.set_ylabel("Category 1")

plt.show()
    """)
    
    st.markdown("**Example:**")
    st.write("- What is the percentage of smokers and non-smokers across fitness levels?")

def quiz():
    st.header("Visualization Selection Quiz 📊")
    
    st.markdown(f"""
    <p style='font-size: 1.2em; color: {colors['text']}; background-color: white; padding: 15px; border-radius: 5px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
    Test your understanding of which visualization to use for different types of data! Good luck! 🍀
    </p>
    """, unsafe_allow_html=True)

    questions = [
        {
            "question": "Which plot is best for showing the distribution of a single continuous variable?",
            "options": ["Bar plot", "Line plot", "Histogram", "Scatter plot"],
            "correct": "Histogram",
            "explanation": "Histograms are ideal for showing the distribution of a single continuous variable."
        },
        {
            "question": "What type of plot would you use to show the count of observations in each category of a categorical variable?",
            "options": ["Scatter plot", "Line plot", "Count plot", "Box plot"],
            "correct": "Count plot",
            "explanation": "Count plots (or bar plots) are used to show the count of observations in each category of a categorical variable."
        },
        {
            "question": "Which plot is best for showing how two continuous variables are correlated?",
            "options": ["Bar plot", "Line plot", "Scatter plot", "Box plot"],
            "correct": "Scatter plot",
            "explanation": "Scatter plots are excellent for showing the correlation between two continuous variables."
        },
        {
            "question": "What type of plot would you use to show how a continuous variable changes over time?",
            "options": ["Bar plot", "Line plot", "Scatter plot", "Box plot"],
            "correct": "Line plot",
            "explanation": "Line plots are ideal for showing how a continuous variable changes over time."
        },
        {
            "question": "Which plot is best for showing how the range of a continuous variable varies for different categories?",
            "options": ["Scatter plot", "Line plot", "Bar plot", "Box plot"],
            "correct": "Box plot",
            "explanation": "Box plots are great for showing how the range and distribution of a continuous variable varies across different categories."
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
        



if __name__ == "__main__":
    main()