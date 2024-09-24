import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(layout="wide", page_title="Box Plot Exploration")

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

def main():
    st.title("Box Plot Exploration")
    st.write('**Developed by : Venugopal Adep**')
    
    tabs = st.tabs(["Learn", "Interactive Demo", "Restaurant Tip Simulator", "Quiz"])
    
    with tabs[0]:
        learn_tab()
    
    with tabs[1]:
        interactive_demo_tab()
    
    with tabs[2]:
        restaurant_tip_simulator_tab()
    
    with tabs[3]:
        quiz_tab()

def learn_tab():
    st.header("Box Plot")
    
    st.markdown("""
    A box plot is a type of chart often used in exploratory data analysis to visualize the distribution of numerical data and get an idea about the skewness and outliers in the data by displaying the items included in the five point summary. The five point summary includes:

    - The minimum
    - Q1 (the first quartile, or the 25% mark)
    - The median (the second quartile, or the 50% mark)
    - Q3 (the third quartile, or the 75% mark)
    - The maximum

    Box plots are particularly useful for comparing distributions between several groups or datasets.
    """)
    
    explain("Box plots provide a concise summary of a dataset's distribution, making it easy to spot outliers, skewness, and differences between groups at a glance.")

def generate_sample_data():
    np.random.seed(42)
    lunch_tips = np.random.normal(2.5, 1, 100)
    dinner_tips = np.random.normal(3, 1.5, 100)
    return pd.DataFrame({'Lunch': lunch_tips, 'Dinner': dinner_tips})

def plot_boxplot(data, title):
    fig = go.Figure()
    for column in data.columns:
        fig.add_trace(go.Box(y=data[column], name=column))
    fig.update_layout(title=title)
    return fig

def interactive_demo_tab():
    st.header("Interactive Box Plot Demo")
    
    data = generate_sample_data()
    
    st.subheader("Sample Data")
    st.write(data.describe())
    
    st.subheader("Box Plot: Restaurant Tips")
    fig = plot_boxplot(data, "Distribution of Tips at Lunch and Dinner")
    st.plotly_chart(fig)
    
    explain("This plot shows how tip varies at lunch and dinner times in a restaurant. "
            "We can see that the median value of tip is larger at the time of dinner.")
    
    st.subheader("Customize the Plot")
    show_points = st.checkbox("Show All Data Points")
    show_mean = st.checkbox("Show Mean")
    notched = st.checkbox("Use Notched Boxes")
    
    fig = go.Figure()
    for column in data.columns:
        fig.add_trace(go.Box(
            y=data[column],
            name=column,
            boxpoints='all' if show_points else False,
            notched=notched,
            boxmean=show_mean
        ))
    
    fig.update_layout(title="Customized Box Plot of Restaurant Tips")
    st.plotly_chart(fig)

def restaurant_tip_simulator_tab():
    st.header("Restaurant Tip Simulator")
    
    st.write("Simulate a day of tipping in your restaurant and see how it affects the distribution!")
    
    base_data = generate_sample_data()
    
    num_customers = st.number_input("Number of Customers", min_value=10, max_value=200, value=50)
    
    lunch_mean = st.slider("Average Lunch Tip", 1.0, 5.0, 2.5, 0.1)
    dinner_mean = st.slider("Average Dinner Tip", 1.0, 5.0, 3.0, 0.1)
    
    if st.button("Simulate Tips"):
        new_lunch_tips = np.random.normal(lunch_mean, 1, num_customers // 2)
        new_dinner_tips = np.random.normal(dinner_mean, 1.5, num_customers - num_customers // 2)
        
        simulated_data = pd.DataFrame({
            'Lunch': np.concatenate([base_data['Lunch'], new_lunch_tips]),
            'Dinner': np.concatenate([base_data['Dinner'], new_dinner_tips])
        })
        
        fig = plot_boxplot(simulated_data, f"Simulated Tips Distribution (Total Customers: {len(simulated_data)})")
        st.plotly_chart(fig)
        
        st.write("Summary Statistics:")
        st.write(simulated_data.describe())
        
        explain(f"After simulating tips from {num_customers} new customers, you can see how the distribution of tips has changed. "
                f"This simulation helps understand how changes in tipping patterns can affect the overall distribution of tips for lunch and dinner.")

def quiz_tab():
    st.header("Quiz: Box Plots")
    
    questions = [
        {
            "question": "What does the box in a box plot represent?",
            "options": [
                "The range from minimum to maximum",
                "The interquartile range (IQR) from Q1 to Q3",
                "The standard deviation",
                "The mean ± 1 standard deviation"
            ],
            "correct": 1,
            "explanation": "The box in a box plot represents the interquartile range (IQR), which is the range between the first quartile (Q1) and the third quartile (Q3)."
        },
        {
            "question": "In the example box plot, which meal time tends to have higher tips?",
            "options": [
                "Lunch",
                "Dinner",
                "They are exactly the same",
                "It's impossible to tell from a box plot"
            ],
            "correct": 1,
            "explanation": "The box plot shows that dinner tends to have higher tips, as the median (middle line in the box) for dinner is higher than for lunch."
        },
        {
            "question": "What do the whiskers in a standard box plot typically represent?",
            "options": [
                "The full range of the data",
                "One standard deviation above and below the mean",
                "The range of data within 1.5 times the IQR beyond the box",
                "The 95% confidence interval"
            ],
            "correct": 2,
            "explanation": "In a standard box plot, the whiskers typically extend to the lowest and highest data points within 1.5 times the IQR beyond the box. Points beyond this are usually plotted as individual outliers."
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
            st.success("Perfect score! You have a great understanding of box plots!")
        elif score >= len(questions) / 2:
            st.success("Good job! You have a solid grasp of box plot concepts.")
        else:
            st.info("Keep learning! Review the content about box plots to improve your understanding.")

if __name__ == "__main__":
    main()