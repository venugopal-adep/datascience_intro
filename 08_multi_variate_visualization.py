import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide", page_title="Multivariate Visualization")

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
    .stDataFrame {{
        font-size: 14px;
    }}
</style>
""", unsafe_allow_html=True)

def main():
    st.title("Multivariate Visualization")
    st.write('**Developed by : Venugopal Adep**')
    
    st.markdown(f"""
    <p style='font-size: 1.2em; color: {colors['text']}; background-color: white; padding: 15px; border-radius: 5px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
    Multivariate analysis is used to study the interaction between more than two variables. Exploring more
    combination of variables helps to extract deeper insights which could not be observed with univariate or
    bivariate analysis. Examples: Correlation, Regression analysis, etc.
    </p>
    """, unsafe_allow_html=True)

    tabs = st.tabs([
        "Overview",
        "Pair Plot",
        "Heatmap",
        "Quiz"
    ])

    with tabs[0]:
        overview()

    with tabs[1]:
        pair_plot()

    with tabs[2]:
        heatmap()

    with tabs[3]:
        quiz()

def overview():
    st.header("Multivariate Visualization Overview")
    
    data = {
        "Type": ["Multivariate", "Multivariate"],
        "Variables": ["Continuous (more than two)", "Continuous (more than two)"],
        "Purpose of analysis": [
            "How to visualize relationship across multiple combination of variables?",
            "How to visualize the spread of values in the data with color-encoding?"
        ],
        "Type of chart": ["Pair Plot", "Heatmap"],
        "Example": [
            "Relation between three variables - horsepower, weight, and acceleration",
            "Correlation matrix for three variables - horsepower, weight, and acceleration"
        ]
    }
    
    df = pd.DataFrame(data)
    st.table(df)
    
    st.markdown("""
    **Note:** Pair plot and heatmap can also be used with only two variables but are generally preferred and more
    useful for visualizing more than two variables.
    """)

def explain(text):
    st.markdown(f"""
    <div style='background-color: white; padding: 15px; border-radius: 5px; border-left: 5px solid {colors['accent']}; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
        <p style='color: {colors['text']}; margin: 0;'>{text}</p>
    </div>
    """, unsafe_allow_html=True)

def show_code(code):
    st.code(code, language='python')

def pair_plot():
    st.header("Pair Plot")
    col1, col2 = st.columns([1, 1])
    
    with col1:
        explain("Use this to visualize relationships across multiple combinations of variables. It's particularly useful for exploring correlations between multiple continuous variables.")
        
        show_code("""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(0)
n = 100
data = pd.DataFrame({
    'horsepower': np.random.normal(150, 30, n),
    'weight': np.random.normal(3000, 500, n),
    'acceleration': np.random.normal(15, 3, n)
})

# Create pair plot
fig = sns.pairplot(data, height=2)
plt.tight_layout()
plt.show()
        """)
    
    with col2:
        # Generate sample data
        np.random.seed(0)
        n = 100
        data = pd.DataFrame({
            'horsepower': np.random.normal(150, 30, n),
            'weight': np.random.normal(3000, 500, n),
            'acceleration': np.random.normal(15, 3, n)
        })
        
        fig = sns.pairplot(data, height=2)
        plt.tight_layout()
        st.pyplot(fig)
    
    st.markdown("**Example:**")
    st.write("- Relation between three variables - horsepower, weight, and acceleration")

def heatmap():
    st.header("Heatmap")
    col1, col2 = st.columns([1, 1])
    
    with col1:
        explain("Use this to visualize the spread of values in the data with color-encoding. It's particularly useful for showing correlation matrices between multiple variables.")
        
        show_code("""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(0)
n = 100
data = pd.DataFrame({
    'horsepower': np.random.normal(150, 30, n),
    'weight': np.random.normal(3000, 500, n),
    'acceleration': np.random.normal(15, 3, n)
})

# Compute correlation matrix
corr = data.corr()

# Create heatmap
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
ax.set_title("Correlation Heatmap")
plt.tight_layout()
plt.show()
        """)
    
    with col2:
        # Generate sample data
        np.random.seed(0)
        n = 100
        data = pd.DataFrame({
            'horsepower': np.random.normal(150, 30, n),
            'weight': np.random.normal(3000, 500, n),
            'acceleration': np.random.normal(15, 3, n)
        })
        
        # Compute correlation matrix
        corr = data.corr()
        
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
        ax.set_title("Correlation Heatmap")
        plt.tight_layout()
        st.pyplot(fig)
    
    st.markdown("**Example:**")
    st.write("- Correlation matrix for three variables - horsepower, weight, and acceleration")

def quiz():
    st.header("Multivariate Visualization Quiz 📊")
    
    st.markdown(f"""
    <p style='font-size: 1.2em; color: {colors['text']}; background-color: white; padding: 15px; border-radius: 5px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
    Test your understanding of multivariate visualization techniques! Good luck! 🍀
    </p>
    """, unsafe_allow_html=True)

    questions = [
        {
            "question": "Which plot is best for visualizing relationships across multiple combinations of variables?",
            "options": ["Bar plot", "Line plot", "Pair plot", "Pie chart"],
            "correct": "Pair plot",
            "explanation": "Pair plots are ideal for visualizing relationships across multiple combinations of variables, showing scatterplots for each pair of variables."
        },
        {
            "question": "What type of plot is best for visualizing a correlation matrix between multiple variables?",
            "options": ["Scatter plot", "Heatmap", "Box plot", "Histogram"],
            "correct": "Heatmap",
            "explanation": "Heatmaps are excellent for visualizing correlation matrices, using color intensity to represent correlation strength between variables."
        },
        {
            "question": "What is a key advantage of multivariate analysis over univariate or bivariate analysis?",
            "options": [
                "It's simpler to interpret",
                "It requires less data",
                "It can extract deeper insights from interactions between multiple variables",
                "It's always more visually appealing"
            ],
            "correct": "It can extract deeper insights from interactions between multiple variables",
            "explanation": "Multivariate analysis allows us to explore interactions between multiple variables, potentially revealing insights that couldn't be observed with simpler analyses."
        },
        {
            "question": "Which of the following is NOT typically considered a multivariate visualization technique?",
            "options": ["Pair plot", "Heatmap", "Parallel coordinates plot", "Pie chart"],
            "correct": "Pie chart",
            "explanation": "Pie charts are typically used for showing proportions of a whole and are not suited for multivariate analysis. The other options are common multivariate visualization techniques."
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
    Remember, multivariate visualization techniques are powerful tools for exploring complex relationships in your data. Keep practicing and exploring different approaches! 📊
    </p>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
