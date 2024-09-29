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
        "Summary Table",
        "Univariate Continuous",
        "Univariate Categorical",
        "Bivariate Continuous",
        "Bivariate Time Series",
        "Bivariate Continuous-Categorical",
        "Bivariate Categorical-Categorical",
    ])

    with tabs[0]:
        summary_table()
    with tabs[1]:
        univariate_continuous()
    with tabs[2]:
        univariate_categorical()
    with tabs[3]:
        bivariate_continuous()
    with tabs[4]:
        bivariate_time_series()
    with tabs[5]:
        bivariate_continuous_categorical()
    with tabs[6]:
        bivariate_categorical_categorical()

def explain(text):
    st.markdown(f"""
    <div style='background-color: white; padding: 15px; border-radius: 5px; border-left: 5px solid {colors['accent']}; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
        <p style='color: {colors['text']}; margin: 0;'>{text}</p>
    </div>
    """, unsafe_allow_html=True)

def show_code(code):
    st.code(code, language='python')

def summary_table():
    st.header("Summary of Visualization Types")
    
    data = {
        "Type": ["Univariate", "Univariate", "Bivariate", "Bivariate", "Bivariate", "Bivariate"],
        "X Variable": ["Continuous", "Categorical", "Continuous", "Time Related (months, hours, etc.)", "Continuous", "Categorical"],
        "Y Variable": ["-", "-", "Continuous", "Continuous", "Categorical", "Categorical"],
        "Purpose of analysis": [
            "How the values of the X variable are distributed?",
            "What is the count of observations in each category of X variable?",
            "How Y is correlated with X?",
            "How Y changes over time?",
            "How range of X varies for various category levels?",
            "What is the number or % of records of X which falls under each category of Y?"
        ],
        "Type of chart": ["Histogram, Distribution plot", "Count Plot", "Scatter plot", "Line Plot", "Box plot, Swarm Plot", "Stacked Bar plot"],
        "Example": [
            "Distribution of cholesterol ranges\nDistribution of horsepower of cars",
            "What is the count of employees for each type of degree in an organization?",
            "How tip varies with the total bill?",
            "How sales varies on different days?",
            "How tip varies at lunch and dinner?\nHow tips varies with day of the week?",
            "What is the percentage of smokers and non-smokers across fitness levels?"
        ]
    }
    
    df = pd.DataFrame(data)
    st.table(df)

def univariate_continuous():
    st.header("Univariate Continuous Visualization")
    explain("Use this when you want to show how the values of a single continuous variable are distributed.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        show_code("""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate sample data
data = np.random.normal(0, 1, 1000)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# Histogram
sns.histplot(data, kde=True, ax=ax1)
ax1.set_title("Histogram with KDE")

# Distribution plot
sns.kdeplot(data, fill=True, ax=ax2)
ax2.set_title("Distribution Plot")

plt.tight_layout()
plt.show()
        """)
    
    with col2:
        # Generate sample data
        data = np.random.normal(0, 1, 1000)
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
        
        # Histogram
        sns.histplot(data, kde=True, ax=ax1)
        ax1.set_title("Histogram with KDE")
        
        # Distribution plot
        sns.kdeplot(data, fill=True, ax=ax2)
        ax2.set_title("Distribution Plot")
        
        plt.tight_layout()
        st.pyplot(fig)
    
    st.markdown("**Examples:**")
    st.write("- Distribution of cholesterol ranges")
    st.write("- Distribution of horsepower of cars")

def univariate_categorical():
    st.header("Univariate Categorical Visualization")
    explain("Use this when you want to show the count of observations in each category of a categorical variable.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        show_code("""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate sample data
categories = ['A', 'B', 'C', 'D']
counts = np.random.randint(10, 100, size=len(categories))

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=categories, y=counts)
ax.set_title("Count Plot")

plt.tight_layout()
plt.show()
        """)
    
    with col2:
        # Generate sample data
        categories = ['A', 'B', 'C', 'D']
        counts = np.random.randint(10, 100, size=len(categories))
        
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.barplot(x=categories, y=counts)
        ax.set_title("Count Plot")
        
        plt.tight_layout()
        st.pyplot(fig)
    
    st.markdown("**Example:**")
    st.write("- What is the count of employees for each type of degree in an organization?")

def bivariate_continuous():
    st.header("Bivariate Continuous Visualization")
    explain("Use this when you want to show how two continuous variables are correlated.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        show_code("""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate sample data
x = np.random.rand(100)
y = 2 * x + np.random.normal(0, 0.1, 100)

fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(x=x, y=y)
ax.set_title("Scatter Plot")

plt.tight_layout()
plt.show()
        """)
    
    with col2:
        # Generate sample data
        x = np.random.rand(100)
        y = 2 * x + np.random.normal(0, 0.1, 100)
        
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.scatterplot(x=x, y=y)
        ax.set_title("Scatter Plot")
        
        plt.tight_layout()
        st.pyplot(fig)
    
    st.markdown("**Example:**")
    st.write("- How tip varies with the total bill?")

def bivariate_time_series():
    st.header("Bivariate Time Series Visualization")
    explain("Use this when you want to show how a continuous variable changes over time.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        show_code("""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Generate sample data
dates = pd.date_range(start='2023-01-01', periods=100)
values = np.cumsum(np.random.randn(100))

fig, ax = plt.subplots(figsize=(8, 5))
sns.lineplot(x=dates, y=values)
ax.set_title("Line Plot")

plt.tight_layout()
plt.show()
        """)
    
    with col2:
        # Generate sample data
        dates = pd.date_range(start='2023-01-01', periods=100)
        values = np.cumsum(np.random.randn(100))
        
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.lineplot(x=dates, y=values)
        ax.set_title("Line Plot")
        
        plt.tight_layout()
        st.pyplot(fig)
    
    st.markdown("**Example:**")
    st.write("- How sales varies on different days?")

def bivariate_continuous_categorical():
    st.header("Bivariate Continuous-Categorical Visualization")
    explain("Use this when you want to show how the range of a continuous variable varies for different categories.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        show_code("""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate sample data
categories = ['A', 'B', 'C', 'D']
data = [np.random.normal(i, 1, 100) for i in range(len(categories))]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# Box plot
sns.boxplot(data=data, ax=ax1)
ax1.set_title("Box Plot")

# Swarm plot
sns.swarmplot(data=data, ax=ax2)
ax2.set_title("Swarm Plot")

plt.tight_layout()
plt.show()
        """)
    
    with col2:
        # Generate sample data
        categories = ['A', 'B', 'C', 'D']
        data = [np.random.normal(i, 1, 100) for i in range(len(categories))]
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
        
        # Box plot
        sns.boxplot(data=data, ax=ax1)
        ax1.set_title("Box Plot")
        
        # Swarm plot
        sns.swarmplot(data=data, ax=ax2)
        ax2.set_title("Swarm Plot")
        
        plt.tight_layout()
        st.pyplot(fig)
    
    st.markdown("**Examples:**")
    st.write("- How tip varies at lunch and dinner?")
    st.write("- How tips varies with day of the week?")

def bivariate_categorical_categorical():
    st.header("Bivariate Categorical-Categorical Visualization")
    explain("Use this when you want to show the number or percentage of records of one categorical variable which falls under each category of another categorical variable.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        show_code("""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate sample data
categories1 = ['A', 'B', 'C']
categories2 = ['X', 'Y']
data = np.random.randint(10, 100, size=(len(categories1), len(categories2)))

fig, ax = plt.subplots(figsize=(8, 5))
sns.heatmap(data, annot=True, fmt='d', cmap='YlGnBu')
ax.set_title("Stacked Bar Plot (Heatmap representation)")
ax.set_xlabel("Category 2")
ax.set_ylabel("Category 1")

plt.tight_layout()
plt.show()
        """)
    
    with col2:
        # Generate sample data
        categories1 = ['A', 'B', 'C']
        categories2 = ['X', 'Y']
        data = np.random.randint(10, 100, size=(len(categories1), len(categories2)))
        
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.heatmap(data, annot=True, fmt='d', cmap='YlGnBu')
        ax.set_title("Stacked Bar Plot (Heatmap representation)")
        ax.set_xlabel("Category 2")
        ax.set_ylabel("Category 1")
        
        plt.tight_layout()
        st.pyplot(fig)
    
    st.markdown("**Example:**")
    st.write("- What is the percentage of smokers and non-smokers across fitness levels?")

if __name__ == "__main__":
    main()
