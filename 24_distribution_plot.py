import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy.stats import gaussian_kde

st.set_page_config(layout="wide", page_title="Distribution Plot Exploration")

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
    car_types = ['Sedan', 'SUV', 'Sports Car']
    data = []
    for car_type in car_types:
        if car_type == 'Sedan':
            horsepower = np.random.normal(120, 20, 1000)
        elif car_type == 'SUV':
            horsepower = np.random.normal(200, 30, 1000)
        else:
            horsepower = np.random.normal(300, 50, 1000)
        data.extend(zip([car_type] * 1000, horsepower))
    return pd.DataFrame(data, columns=['car_type', 'horsepower'])

def plot_distribution(data, title, bin_size=20, show_kde=True):
    fig = make_subplots(rows=1, cols=1)
    
    for car_type in data['car_type'].unique():
        car_data = data[data['car_type'] == car_type]['horsepower']
        
        # Add histogram
        fig.add_trace(
            go.Histogram(
                x=car_data,
                name=car_type,
                opacity=0.75,
                nbinsx=int((car_data.max() - car_data.min()) / bin_size)
            )
        )
        
        # Add KDE if selected
        if show_kde:
            kde_x = np.linspace(car_data.min(), car_data.max(), 100)
            kde = gaussian_kde(car_data)
            fig.add_trace(
                go.Scatter(
                    x=kde_x,
                    y=kde(kde_x) * len(car_data) * (car_data.max() - car_data.min()) / bin_size,
                    name=f"{car_type} KDE",
                    mode='lines'
                )
            )
    
    fig.update_layout(
        title=title,
        xaxis_title="Horsepower",
        yaxis_title="Count",
        barmode='overlay'
    )
    
    return fig

def learn_tab():
    st.header("Distribution Plot")
    
    st.markdown("""
    A distribution plot is a method for visualizing the distribution of observations in data. Relative to a histogram, a
    distribution plot can produce a graph that is less cluttered and more interpretable, especially when drawing
    multiple distributions.

    Key features of a distribution plot:
    - It shows the probability density of the data
    - The area under the curve sums to 1
    - It can reveal the shape of the distribution (e.g., normal, skewed, multimodal)
    - It's useful for comparing multiple distributions on the same plot
    """)
    
    explain("Distribution plots provide a smooth representation of the data distribution, making it easier to identify patterns, skewness, and compare multiple datasets.")

def interactive_demo_tab():
    st.header("Interactive Distribution Plot Demo")
    
    data = generate_sample_data()
    
    st.subheader("Sample Data")
    st.write(data.groupby('car_type').describe())
    
    st.subheader("Distribution Plot: Car Horsepower by Type")
    fig = plot_distribution(data, "Distribution of Horsepower for Different Types of Cars")
    st.plotly_chart(fig)
    
    explain("This plot shows the distribution of horsepower for different types of cars. "
            "We can see that the distribution is slightly right-skewed. "
            "Majority of values are less than 300. "
            "The range of values is high, it varies from less than 50 to approx 450.")
    
    st.subheader("Customize the Plot")
    bin_size = st.slider("Adjust bin size", 5, 50, 20)
    show_kde = st.checkbox("Show KDE (Kernel Density Estimation)", value=True)
    
    fig = plot_distribution(data, "Customized Distribution Plot of Car Horsepower", bin_size, show_kde)
    st.plotly_chart(fig)

def car_horsepower_simulator_tab():
    st.header("Car Horsepower Simulator")
    
    st.write("Simulate new car models and see how they affect the horsepower distribution!")
    
    base_data = generate_sample_data()
    
    num_cars = st.number_input("Number of New Cars per Type", min_value=10, max_value=500, value=100)
    
    sedan_mean = st.slider("Average Sedan Horsepower", 50, 200, 120)
    suv_mean = st.slider("Average SUV Horsepower", 100, 300, 200)
    sports_car_mean = st.slider("Average Sports Car Horsepower", 200, 500, 300)
    
    if st.button("Simulate Cars"):
        new_sedans = np.random.normal(sedan_mean, 20, num_cars)
        new_suvs = np.random.normal(suv_mean, 30, num_cars)
        new_sports_cars = np.random.normal(sports_car_mean, 50, num_cars)
        
        new_data = pd.DataFrame({
            'car_type': ['Sedan'] * num_cars + ['SUV'] * num_cars + ['Sports Car'] * num_cars,
            'horsepower': np.concatenate([new_sedans, new_suvs, new_sports_cars])
        })
        
        simulated_data = pd.concat([base_data, new_data])
        
        fig = plot_distribution(simulated_data, f"Simulated Horsepower Distribution (Total Cars: {len(simulated_data)})")
        st.plotly_chart(fig)
        
        st.write("Summary Statistics:")
        st.write(simulated_data.groupby('car_type').describe())
        
        explain(f"After simulating {num_cars * 3} new cars, you can see how the distribution of horsepower has changed. "
                f"This simulation helps understand how introducing new car models can affect the overall distribution of horsepower across different car types.")

def quiz_tab():
    st.header("Quiz: Distribution Plots")
    
    questions = [
        {
            "question": "What does the y-axis typically represent in a distribution plot?",
            "options": [
                "The actual count of observations",
                "The probability density",
                "The cumulative frequency",
                "The standard deviation"
            ],
            "correct": 1,
            "explanation": "In a distribution plot, the y-axis typically represents the probability density, which shows the relative likelihood of different values occurring in the dataset."
        },
        {
            "question": "Based on the example distribution plot, which statement is true?",
            "options": [
                "The distribution is perfectly symmetric",
                "The distribution is slightly left-skewed",
                "The distribution is slightly right-skewed",
                "The distribution is bimodal"
            ],
            "correct": 2,
            "explanation": "The distribution plot in the example shows a slightly right-skewed distribution, with a longer tail extending to the right."
        },
        {
            "question": "What is an advantage of using a distribution plot over a histogram?",
            "options": [
                "It shows exact counts of each value",
                "It's less cluttered and more interpretable for multiple distributions",
                "It always uses less memory to generate",
                "It can only be used for continuous data"
            ],
            "correct": 1,
            "explanation": "A key advantage of distribution plots over histograms is that they can produce graphs that are less cluttered and more interpretable, especially when comparing multiple distributions."
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
            st.success("Perfect score! You have a great understanding of distribution plots!")
        elif score >= len(questions) / 2:
            st.success("Good job! You have a solid grasp of distribution plot concepts.")
        else:
            st.info("Keep learning! Review the content about distribution plots to improve your understanding.")

def main():
    st.title("Distribution Plot Exploration")
    st.write('**Developed by : Venugopal Adep**')
    
    tabs = st.tabs(["Learn", "Interactive Demo", "Car Horsepower Simulator", "Quiz"])
    
    with tabs[0]:
        learn_tab()
    
    with tabs[1]:
        interactive_demo_tab()
    
    with tabs[2]:
        car_horsepower_simulator_tab()
    
    with tabs[3]:
        quiz_tab()

if __name__ == "__main__":
    main()