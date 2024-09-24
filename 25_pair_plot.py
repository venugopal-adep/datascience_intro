import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(layout="wide", page_title="Pair Plot Exploration")

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
    .plot-container {{
        display: flex;
        justify-content: center;
        align-items: center;
    }}
</style>
""", unsafe_allow_html=True)

def explain(text):
    st.markdown(f"""
    <div style='background-color: white; padding: 15px; border-radius: 5px; border-left: 5px solid {colors['accent']}; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
        <p style='color: {colors['text']}; margin: 0;'>{text}</p>
    </div>
    """, unsafe_allow_html=True)

def generate_sample_data():
    np.random.seed(42)
    n = 150
    sepal_length = np.random.normal(5.5, 1, n)
    sepal_width = np.random.normal(3.5, 0.5, n)
    petal_length = np.random.normal(4, 1.5, n)
    petal_width = np.random.normal(1.3, 0.5, n)
    species = np.random.choice(['setosa', 'versicolor', 'virginica'], n)
    return pd.DataFrame({
        'sepal_length': sepal_length,
        'sepal_width': sepal_width,
        'petal_length': petal_length,
        'petal_width': petal_width,
        'species': species
    })

def plot_pair(data):
    fig = make_subplots(rows=4, cols=4, shared_xaxes=True, shared_yaxes=True)
    
    variables = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    
    for i, var1 in enumerate(variables):
        for j, var2 in enumerate(variables):
            row = i + 1
            col = j + 1
            
            if var1 == var2:
                # Histogram on diagonal
                fig.add_trace(go.Histogram(x=data[var1], name=var1), row=row, col=col)
            else:
                # Scatter plot on off-diagonal
                fig.add_trace(go.Scatter(x=data[var2], y=data[var1], mode='markers', name=f'{var1} vs {var2}', 
                                         marker=dict(color=data['species'].astype('category').cat.codes, colorscale='Viridis')), 
                              row=row, col=col)
    
    fig.update_layout(height=800, width=800, title="Pair Plot of Iris Dataset")
    
    # Update axes labels
    for i, var in enumerate(variables):
        fig.update_xaxes(title_text=var, row=4, col=i+1)
        fig.update_yaxes(title_text=var, row=i+1, col=1)
    
    return fig

def learn_tab():
    st.header("Pair Plot")
    
    st.markdown("""
    A pair plot is a grid of scatter plots showing the relationship between pairs of variables in a dataset. It's an excellent tool for exploratory data analysis, allowing you to visualize:

    1. The distribution of each variable (on the diagonal)
    2. The relationship between each pair of variables (off-diagonal)
    3. Patterns or clusters in the data

    Key features of a pair plot:
    - It shows multiple scatter plots in a grid layout
    - The diagonal often shows histograms or kernel density estimates
    - It's useful for identifying correlations and patterns across multiple variables
    - Color coding can be used to distinguish different categories in the data
    """)
    
    explain("Pair plots provide a comprehensive view of relationships between multiple variables, making it easy to identify patterns, correlations, and potential clusters in your data.")

def interactive_demo_tab():
    st.header("Interactive Pair Plot Demo")
    
    data = generate_sample_data()
    
    st.subheader("Sample Data")
    st.write(data.head())
    
    st.subheader("Pair Plot: Iris Dataset")
    fig = plot_pair(data)
    st.plotly_chart(fig)
    
    explain("This pair plot shows the relationships between sepal length, sepal width, petal length, and petal width in the Iris dataset. "
            "The diagonal shows the distribution of each variable, while the off-diagonal plots show the relationships between pairs of variables. "
            "The colors represent different Iris species.")
    
    st.subheader("Customize the Plot")
    numeric_columns = data.select_dtypes(include=[np.number]).columns.tolist()
    selected_vars = st.multiselect("Select variables to plot", numeric_columns, default=numeric_columns)
    color_by = st.checkbox("Color by species", value=True)
    
    if selected_vars:
        fig = make_subplots(rows=len(selected_vars), cols=len(selected_vars), shared_xaxes=True, shared_yaxes=True)
        
        for i, var1 in enumerate(selected_vars):
            for j, var2 in enumerate(selected_vars):
                row = i + 1
                col = j + 1
                
                if var1 == var2:
                    fig.add_trace(go.Histogram(x=data[var1], name=var1), row=row, col=col)
                else:
                    scatter = go.Scatter(
                        x=data[var2], 
                        y=data[var1], 
                        mode='markers', 
                        name=f'{var1} vs {var2}',
                        marker=dict(
                            color=data['species'].astype('category').cat.codes if color_by else None,
                            colorscale='Viridis' if color_by else None
                        )
                    )
                    fig.add_trace(scatter, row=row, col=col)
        
        fig.update_layout(height=800, width=800, title="Customized Pair Plot of Iris Dataset")
        
        for i, var in enumerate(selected_vars):
            fig.update_xaxes(title_text=var, row=len(selected_vars), col=i+1)
            fig.update_yaxes(title_text=var, row=i+1, col=1)
        
        st.plotly_chart(fig)

def iris_species_analyzer_tab():
    st.header("Iris Species Analyzer")
    
    st.write("Analyze the characteristics of Iris flowers and predict their species!")
    
    data = generate_sample_data()
    
    sepal_length = st.slider("Sepal Length", float(data['sepal_length'].min()), float(data['sepal_length'].max()), float(data['sepal_length'].mean()))
    sepal_width = st.slider("Sepal Width", float(data['sepal_width'].min()), float(data['sepal_width'].max()), float(data['sepal_width'].mean()))
    petal_length = st.slider("Petal Length", float(data['petal_length'].min()), float(data['petal_length'].max()), float(data['petal_length'].mean()))
    petal_width = st.slider("Petal Width", float(data['petal_width'].min()), float(data['petal_width'].max()), float(data['petal_width'].mean()))
    
    if st.button("Analyze Iris"):
        new_iris = pd.DataFrame({
            'sepal_length': [sepal_length],
            'sepal_width': [sepal_width],
            'petal_length': [petal_length],
            'petal_width': [petal_width]
        })
        
        # Simple prediction based on petal length (just for demonstration)
        if petal_length < 2.5:
            prediction = 'setosa'
        elif petal_length < 4.9:
            prediction = 'versicolor'
        else:
            prediction = 'virginica'
        
        st.write(f"Based on these characteristics, this Iris is likely to be: **{prediction}**")
        
        fig = plot_pair(pd.concat([data, new_iris]))
        fig.add_trace(go.Scatter(x=[sepal_length], y=[sepal_width], mode='markers', marker=dict(color='red', size=15, symbol='star'), name='New Iris'), row=2, col=1)
        fig.add_trace(go.Scatter(x=[petal_length], y=[petal_width], mode='markers', marker=dict(color='red', size=15, symbol='star'), name='New Iris'), row=4, col=3)
        st.plotly_chart(fig)
        
        explain(f"The red star shows where your analyzed Iris falls in relation to the existing data. "
                f"This visual comparison can help understand why it was classified as {prediction}.")

def quiz_tab():
    st.header("Quiz: Pair Plots")
    
    questions = [
        {
            "question": "What does each scatter plot in a pair plot represent?",
            "options": [
                "The relationship between a variable and itself",
                "The relationship between two different variables",
                "The overall distribution of the dataset",
                "The average values of each variable"
            ],
            "correct": 1,
            "explanation": "Each scatter plot in a pair plot represents the relationship between two different variables, allowing you to see how they correlate or interact."
        },
        {
            "question": "What is typically shown on the diagonal of a pair plot?",
            "options": [
                "A scatter plot",
                "A histogram or kernel density plot",
                "A box plot",
                "A line plot"
            ],
            "correct": 1,
            "explanation": "The diagonal of a pair plot typically shows a histogram or kernel density plot of each variable, providing a view of its distribution."
        },
        {
            "question": "How can color be used effectively in a pair plot?",
            "options": [
                "To make the plot more visually appealing",
                "To represent a third variable, often a categorical one",
                "To highlight outliers",
                "To separate different plots"
            ],
            "correct": 1,
            "explanation": "Color in a pair plot is often used to represent a third variable, typically a categorical one, allowing you to see how different categories behave across the various relationships."
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
            st.success("Perfect score! You have a great understanding of pair plots!")
        elif score >= len(questions) / 2:
            st.success("Good job! You have a solid grasp of pair plot concepts.")
        else:
            st.info("Keep learning! Review the content about pair plots to improve your understanding.")

def main():
    st.title("Pair Plot Exploration")
    st.write('**Developed by : Venugopal Adep**')
    
    tabs = st.tabs(["Learn", "Interactive Demo", "Iris Species Analyzer", "Quiz"])
    
    with tabs[0]:
        learn_tab()
    
    with tabs[1]:
        interactive_demo_tab()
    
    with tabs[2]:
        iris_species_analyzer_tab()
    
    with tabs[3]:
        quiz_tab()

if __name__ == "__main__":
    main()