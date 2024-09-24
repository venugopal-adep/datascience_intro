import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide", page_title="Swarm Plot Exploration")

# Custom color palette (same as original)
colors = {
    "primary": "#0066CC",
    "secondary": "#FF6347", 
    "accent": "#32CD32",
    "background": "#F0F8FF",
    "text": "#333333"
}

# Custom CSS (same as original)
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
    st.title("Swarm Plot Exploration")
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
    st.header("Swarm Plot")
    
    st.markdown("""
    A swarm plot is like a categorical scatterplot with non-overlapping points. The data points are adjusted so that they don't overlap. This gives a better representation of the distribution and spread of values.

    Key features of a swarm plot:
    - Each point represents an individual data point
    - Points are grouped by categories (in this case, days of the week)
    - Points are spread out horizontally to avoid overlap
    - The vertical position of each point represents its value

    Swarm plots are particularly useful for visualizing the distribution of data across categories and identifying patterns or outliers.
    """)
    
    explain("Swarm plots provide a detailed view of data distribution, allowing you to see every individual data point while still getting a sense of the overall pattern for each category.")

def generate_sample_data():
    np.random.seed(42)
    days = ['Thu', 'Fri', 'Sat', 'Sun']
    tips = []
    for day in days:
        if day in ['Sat', 'Sun']:
            tips.extend(np.random.normal(4, 1.5, 50))
        else:
            tips.extend(np.random.normal(3, 1, 30))
    return pd.DataFrame({'day': np.repeat(days, [30, 30, 50, 50]), 'tip': tips})

def plot_swarmplot(data, title):
    fig = px.strip(data, x="day", y="tip", title=title)
    fig.update_traces(jitter=1, marker=dict(size=5))
    return fig

def interactive_demo_tab():
    st.header("Interactive Swarm Plot Demo")
    
    data = generate_sample_data()
    
    st.subheader("Sample Data")
    st.write(data.groupby('day').describe())
    
    st.subheader("Swarm Plot: Restaurant Tips by Day")
    fig = plot_swarmplot(data, "Distribution of Tips for Each Day")
    st.plotly_chart(fig)
    
    explain("This plot shows the amount of tip for each day in the data. "
            "We can see that the most number of tips are on Saturday and Sunday. "
            "The amount of tips is maximum on Saturday. "
            "The most common tip on all days is around 2-4 dollars.")
    
    st.subheader("Customize the Plot")
    jitter = st.slider("Adjust point spread", 0.0, 2.0, 1.0, 0.1)
    point_size = st.slider("Adjust point size", 1, 10, 5)
    
    fig = px.strip(data, x="day", y="tip", title="Customized Swarm Plot of Restaurant Tips")
    fig.update_traces(jitter=jitter, marker=dict(size=point_size))
    st.plotly_chart(fig)

def restaurant_tip_simulator_tab():
    st.header("Restaurant Tip Simulator")
    
    st.write("Simulate a week of tipping in your restaurant and see how it affects the distribution!")
    
    base_data = generate_sample_data()
    
    num_customers = st.number_input("Number of New Customers per Day", min_value=10, max_value=100, value=30)
    
    weekday_mean = st.slider("Average Weekday Tip", 1.0, 5.0, 3.0, 0.1)
    weekend_mean = st.slider("Average Weekend Tip", 1.0, 7.0, 4.0, 0.1)
    
    if st.button("Simulate Tips"):
        new_weekday_tips = np.random.normal(weekday_mean, 1, num_customers * 2)
        new_weekend_tips = np.random.normal(weekend_mean, 1.5, num_customers * 2)
        
        new_data = pd.DataFrame({
            'day': np.repeat(['Thu', 'Fri', 'Sat', 'Sun'], num_customers),
            'tip': np.concatenate([new_weekday_tips, new_weekend_tips])
        })
        
        simulated_data = pd.concat([base_data, new_data])
        
        fig = plot_swarmplot(simulated_data, f"Simulated Tips Distribution (Total Customers: {len(simulated_data)})")
        st.plotly_chart(fig)
        
        st.write("Summary Statistics:")
        st.write(simulated_data.groupby('day').describe())
        
        explain(f"After simulating tips from {num_customers * 4} new customers, you can see how the distribution of tips has changed. "
                f"This simulation helps understand how changes in tipping patterns can affect the overall distribution of tips for each day.")

def quiz_tab():
    st.header("Quiz: Swarm Plots")
    
    questions = [
        {
            "question": "What does each point in a swarm plot represent?",
            "options": [
                "An average value",
                "A median value",
                "An individual data point",
                "A range of values"
            ],
            "correct": 2,
            "explanation": "In a swarm plot, each point represents an individual data point, allowing you to see the full distribution of the data."
        },
        {
            "question": "Based on the example swarm plot, which days tend to have higher tips?",
            "options": [
                "Thursday and Friday",
                "Saturday and Sunday",
                "All days are the same",
                "It's impossible to tell from a swarm plot"
            ],
            "correct": 1,
            "explanation": "The swarm plot shows that Saturday and Sunday tend to have higher tips, with more points clustered at higher values."
        },
        {
            "question": "What is the main advantage of a swarm plot over a simple scatter plot?",
            "options": [
                "It shows the mean and median",
                "It avoids overlapping points",
                "It's faster to create",
                "It uses less screen space"
            ],
            "correct": 1,
            "explanation": "A key advantage of swarm plots is that they adjust point positions to avoid overlap, giving a clearer view of the data distribution, especially when there are many points with similar values."
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
            st.success("Perfect score! You have a great understanding of swarm plots!")
        elif score >= len(questions) / 2:
            st.success("Good job! You have a solid grasp of swarm plot concepts.")
        else:
            st.info("Keep learning! Review the content about swarm plots to improve your understanding.")

if __name__ == "__main__":
    main()