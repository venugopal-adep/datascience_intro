import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(layout="wide", page_title="Heatmap Exploration")

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
    n = 100
    horsepower = np.random.normal(200, 30, n)
    weight = horsepower * 15 + np.random.normal(0, 100, n)
    acceleration = -0.05 * horsepower - 0.01 * weight + np.random.normal(0, 1, n)
    return pd.DataFrame({'horsepower': horsepower, 'weight': weight, 'acceleration': acceleration})

def plot_heatmap(data, title):
    corr = data.corr()
    
    fig = go.Figure(data=go.Heatmap(
        z=corr.values,
        x=corr.columns,
        y=corr.columns,
        colorscale='RdBu_r',
        zmin=-1,
        zmax=1,
        text=corr.values,
        texttemplate='%{text:.2f}',
        textfont={'size':14}
    ))
    
    fig.update_layout(
        title=title,
        height=500,
        width=600
    )
    
    return fig

def learn_tab():
    st.header("Heatmap")
    
    st.markdown("""
    A heatmap is used to visualize the spread of values as a rectangular table using color-encoding to highlight very low and very high values.

    Key features of a heatmap:
    - It represents data in a 2-dimensional grid
    - Colors are used to represent values
    - It's useful for showing relationships between variables
    - It can reveal patterns and correlations in complex datasets
    """)
    
    explain("Heatmaps provide a visual representation of numerical data, making it easy to spot patterns, correlations, and anomalies across multiple variables.")

def interactive_demo_tab():
    st.header("Interactive Heatmap Demo")
    
    data = generate_sample_data()
    
    st.subheader("Sample Data")
    st.write(data.head())
    
    st.subheader("Correlation Heatmap: Car Features")
    fig = plot_heatmap(data, "Correlation Heatmap of Car Features")
    st.plotly_chart(fig)
    
    explain("This heatmap shows the correlation coefficient between three variables - horsepower, weight, and acceleration. "
            "The plot shows that acceleration is negatively correlated with horsepower and weight. "
            "The variable horsepower is positively correlated with weight.")
    
    st.subheader("Customize the Heatmap")
    color_scale = st.selectbox("Choose a color scale", ['RdBu_r', 'Viridis', 'Plasma', 'Inferno', 'Magma'])
    show_values = st.checkbox("Show correlation values", value=True)
    
    corr = data.corr()
    
    fig = go.Figure(data=go.Heatmap(
        z=corr.values,
        x=corr.columns,
        y=corr.columns,
        colorscale=color_scale,
        zmin=-1,
        zmax=1,
        text=corr.values,
        texttemplate='%{text:.2f}' if show_values else None,
        textfont={'size':14}
    ))
    
    fig.update_layout(
        title="Customized Correlation Heatmap of Car Features",
        height=500,
        width=600
    )
    
    st.plotly_chart(fig)

def car_feature_simulator_tab():
    st.header("Car Feature Simulator")
    
    st.write("Simulate new car models and see how it affects the correlation heatmap!")
    
    base_data = generate_sample_data()
    
    num_cars = st.number_input("Number of New Cars", min_value=10, max_value=500, value=50)
    
    hp_weight_correlation = st.slider("Horsepower-Weight Correlation", -1.0, 1.0, 0.8, 0.1)
    hp_accel_correlation = st.slider("Horsepower-Acceleration Correlation", -1.0, 1.0, -0.6, 0.1)
    
    if st.button("Simulate Cars"):
        new_horsepower = np.random.normal(200, 30, num_cars)
        new_weight = hp_weight_correlation * new_horsepower + np.random.normal(0, np.sqrt(1 - hp_weight_correlation**2), num_cars)
        new_acceleration = hp_accel_correlation * new_horsepower + np.random.normal(0, np.sqrt(1 - hp_accel_correlation**2), num_cars)
        
        new_data = pd.DataFrame({
            'horsepower': new_horsepower,
            'weight': new_weight,
            'acceleration': new_acceleration
        })
        
        simulated_data = pd.concat([base_data, new_data])
        
        fig = plot_heatmap(simulated_data, f"Simulated Correlation Heatmap (Total Cars: {len(simulated_data)})")
        st.plotly_chart(fig)
        
        st.write("Correlation Matrix:")
        st.write(simulated_data.corr())
        
        explain(f"After simulating {num_cars} new cars with specified correlations, you can see how the overall correlation heatmap has changed. "
                f"This simulation helps understand how introducing new car models with different characteristics can affect the relationships between variables.")

def quiz_tab():
    st.header("Quiz: Heatmaps")
    
    questions = [
        {
            "question": "What does each cell in a correlation heatmap represent?",
            "options": [
                "The actual value of a variable",
                "The correlation coefficient between two variables",
                "The sum of two variables",
                "The difference between two variables"
            ],
            "correct": 1,
            "explanation": "In a correlation heatmap, each cell represents the correlation coefficient between two variables, ranging from -1 (perfect negative correlation) to 1 (perfect positive correlation)."
        },
        {
            "question": "Based on the example heatmap, which statement is true?",
            "options": [
                "Acceleration is positively correlated with horsepower",
                "Weight is negatively correlated with horsepower",
                "Acceleration is negatively correlated with weight",
                "There is no correlation between any variables"
            ],
            "correct": 2,
            "explanation": "The heatmap shows that acceleration is negatively correlated with both horsepower and weight, as indicated by the dark colors in those cells."
        },
        {
            "question": "What is an advantage of using a heatmap for correlation analysis?",
            "options": [
                "It can only show positive correlations",
                "It's limited to two variables",
                "It provides a quick visual summary of relationships between multiple variables",
                "It always uses less memory than other plots"
            ],
            "correct": 2,
            "explanation": "A key advantage of heatmaps for correlation analysis is that they provide a quick visual summary of relationships between multiple variables, making it easy to identify patterns and strong correlations at a glance."
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
            st.success("Perfect score! You have a great understanding of heatmaps!")
        elif score >= len(questions) / 2:
            st.success("Good job! You have a solid grasp of heatmap concepts.")
        else:
            st.info("Keep learning! Review the content about heatmaps to improve your understanding.")

def main():
    st.title("Heatmap Exploration")
    st.write('**Developed by : Venugopal Adep**')
    
    tabs = st.tabs(["Learn", "Interactive Demo", "Car Feature Simulator", "Quiz"])
    
    with tabs[0]:
        learn_tab()
    
    with tabs[1]:
        interactive_demo_tab()
    
    with tabs[2]:
        car_feature_simulator_tab()
    
    with tabs[3]:
        quiz_tab()

if __name__ == "__main__":
    main()