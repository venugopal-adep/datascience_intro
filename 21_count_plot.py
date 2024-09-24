import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(layout="wide", page_title="Count Plot Exploration")

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
    st.title("Count Plot Exploration")
    st.write('**Developed by : Venugopal Adep**')
    
    tabs = st.tabs(["Learn", "Interactive Demo", "Employee Simulator", "Quiz"])
    
    with tabs[0]:
        learn_tab()
    
    with tabs[1]:
        interactive_demo_tab()
    
    with tabs[2]:
        employee_simulator_tab()
    
    with tabs[3]:
        quiz_tab()

def learn_tab():
    st.header("Count Plot")
    
    st.markdown("""
    - A count plot shows the count of observations in each category of a categorical variable using bars.
    - It can be thought of as a histogram across a categorical, instead of continuous, variable.
    - Count plots are useful for visualizing the distribution of categorical data.
    - They help in quickly identifying the most common and least common categories in a dataset.
    """)
    
    explain("Count plots are excellent for displaying the frequency of different categories in a dataset. They provide a clear visual representation of how data is distributed across various groups or categories.")

def generate_sample_data():
    degrees = ['Master', 'Bachelor', 'PhD', 'Secondary']
    counts = [76, 88, 62, 19]
    return pd.DataFrame({'Degree': degrees, 'Count': counts})

def plot_count(data, title, orientation='v'):
    if orientation == 'v':
        fig = px.bar(data, x='Degree', y='Count', title=title, color='Degree')
    else:
        fig = px.bar(data, y='Degree', x='Count', title=title, color='Degree', orientation='h')
    fig.update_layout(showlegend=False)
    return fig

def interactive_demo_tab():
    st.header("Interactive Count Plot Demo")
    
    data = generate_sample_data()
    
    st.subheader("Sample Data")
    st.write(data)
    
    st.subheader("Count Plot: Employee Degrees")
    fig = plot_count(data, "Count of Employees by Degree")
    st.plotly_chart(fig)
    
    explain("This plot shows the count of employees for each type of degree in an organization. "
            "We can see that the majority of the employees have a bachelor's degree, followed by master's.")
    
    st.subheader("Customize the Plot")
    orientation = st.radio("Bar Orientation", ["Vertical", "Horizontal"])
    sort_bars = st.checkbox("Sort Bars by Count")
    show_percentages = st.checkbox("Show Percentages")
    
    if sort_bars:
        data = data.sort_values('Count', ascending=False)
    
    fig = plot_count(data, "Customized Count Plot of Employee Degrees", 
                     orientation='v' if orientation == "Vertical" else 'h')
    
    if show_percentages:
        total = data['Count'].sum()
        percentages = (data['Count'] / total * 100).round(1)
        if orientation == "Vertical":
            fig.update_traces(text=percentages.astype(str) + '%', textposition='outside')
        else:
            fig.update_traces(text=percentages.astype(str) + '%', textposition='inside')
    
    st.plotly_chart(fig)

def employee_simulator_tab():
    st.header("Employee Degree Simulator")
    
    st.write("Simulate hiring new employees and see how it affects the degree distribution!")
    
    data = generate_sample_data()
    total_employees = data['Count'].sum()
    
    new_hires = st.number_input("Number of New Hires", min_value=1, max_value=100, value=10)
    
    st.write("Set the probability of hiring for each degree:")
    master_prob = st.slider("Master's Degree", 0.0, 1.0, 0.3, 0.1)
    bachelor_prob = st.slider("Bachelor's Degree", 0.0, 1.0, 0.4, 0.1)
    phd_prob = st.slider("PhD", 0.0, 1.0, 0.2, 0.1)
    secondary_prob = 1 - (master_prob + bachelor_prob + phd_prob)
    st.write(f"Secondary Degree: {secondary_prob:.1f}")
    
    if st.button("Simulate Hiring"):
        new_employees = np.random.choice(data['Degree'], new_hires, p=[master_prob, bachelor_prob, phd_prob, secondary_prob])
        for degree in new_employees:
            data.loc[data['Degree'] == degree, 'Count'] += 1
        
        fig = plot_count(data, f"Updated Employee Degree Distribution (After Hiring {new_hires} New Employees)")
        st.plotly_chart(fig)
        
        st.write("Updated Employee Counts:")
        st.write(data)
        
        explain(f"After simulating the hiring of {new_hires} new employees, you can see how the distribution of degrees has changed. "
                f"This simulation helps understand how hiring decisions can impact the overall composition of employee qualifications.")

def quiz_tab():
    st.header("Quiz: Count Plots")
    
    questions = [
        {
            "question": "What type of data is best represented by a count plot?",
            "options": [
                "Continuous data",
                "Categorical data",
                "Time series data",
                "Geographical data"
            ],
            "correct": 1,
            "explanation": "Count plots are best suited for representing categorical data, showing the frequency of each category."
        },
        {
            "question": "In the example count plot, which degree is most common among employees?",
            "options": [
                "Master's",
                "Bachelor's",
                "PhD",
                "Secondary"
            ],
            "correct": 1,
            "explanation": "The count plot shows that the Bachelor's degree has the highest count, making it the most common degree among employees."
        },
        {
            "question": "How does a count plot differ from a histogram?",
            "options": [
                "Count plots use lines instead of bars",
                "Count plots are for categorical data, histograms for continuous data",
                "Count plots show percentages, histograms show counts",
                "There is no difference"
            ],
            "correct": 1,
            "explanation": "While both show frequencies, count plots are used for categorical data, whereas histograms are used for continuous data divided into bins."
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
            st.success("Perfect score! You have a great understanding of count plots!")
        elif score >= len(questions) / 2:
            st.success("Good job! You have a solid grasp of count plot concepts.")
        else:
            st.info("Keep learning! Review the content about count plots to improve your understanding.")

if __name__ == "__main__":
    main()