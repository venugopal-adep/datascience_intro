import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

st.set_page_config(layout="wide", page_title="Line Plot Exploration")

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
    .stApp {{
        background-color: {colors['background']};
    }}
    .block-container {{
        padding: 1rem;
        max-width: 100%;
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
</style>
""", unsafe_allow_html=True)

def explain(text):
    st.markdown(f"""
    <div style='background-color: white; padding: 15px; border-radius: 5px; border-left: 5px solid {colors['accent']}; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
        <p style='color: {colors['text']};'>{text}</p>
    </div>
    """, unsafe_allow_html=True)

def main():
    st.title("Line Plot Exploration")
    st.write('**Developed by: Venugopal Adep**')
    
    tabs = st.tabs(["Learn", "Interactive Demo", "Sales Predictor", "Quiz"])
    
    with tabs[0]:
        learn_tab()
    
    with tabs[1]:
        interactive_demo_tab()
    
    with tabs[2]:
        sales_predictor_tab()
    
    with tabs[3]:
        quiz_tab()

def learn_tab():
    st.header("Line Plot")
    
    st.markdown("""
    - A line graph is a graphical display of information that changes continuously over time.
    - It's ideal for showing trends and patterns in data over a continuous interval.
    - Line plots are excellent for visualizing time series data and comparing multiple series.
    """)
    
    explain("Line plots help in identifying trends, patterns, and fluctuations in data over time. They're particularly useful for forecasting and understanding the overall direction of data.")

def generate_sample_data():
    days = list(range(1, 11))
    sales = [220, 330, 320, 400, 360, 620, 760, 500, 550, 330]
    return pd.DataFrame({'Day': days, 'Sales': sales})

def interactive_demo_tab():
    st.header("Interactive Line Plot Demo")
    
    data = generate_sample_data()
    
    st.subheader("Sample Data")
    st.write(data)
    
    st.subheader("Line Plot: Sales Over Time")
    fig = px.line(data, x="Day", y="Sales", 
                  title="Sales Trend Over 10 Days",
                  labels={"Day": "Day", "Sales": "Sales Amount"},
                  line_shape="linear", render_mode="svg")
    fig.update_traces(line_color=colors['secondary'])
    st.plotly_chart(fig)
    
    explain("""
    Line shapes:
    - **linear**: Straight lines connecting data points.
    - **spline**: Smooth curved lines connecting data points.
    - **hv**: Horizontal-Vertical step lines, moving horizontally first and then vertically.
    - **vh**: Vertical-Horizontal step lines, moving vertically first and then horizontally.
    - **hvh**: Horizontal-Vertical-Horizontal, creating a staircase effect.
    - **vhv**: Vertical-Horizontal-Vertical, creating a staircase effect in the reverse order.
    """)
    
    st.subheader("Customize the Plot")
    line_shape = st.selectbox("Line Shape", ["linear", "spline", "hv", "vh", "hvh", "vhv"])
    show_markers = st.checkbox("Show Markers", value=True)
    highlight_max = st.checkbox("Highlight Maximum Sales", value=False)
    
    fig = px.line(data, x="Day", y="Sales", 
                  title="Sales Trend Over 10 Days",
                  labels={"Day": "Day", "Sales": "Sales Amount"},
                  line_shape=line_shape, render_mode="svg")
    fig.update_traces(line_color=colors['secondary'])
    
    if show_markers:
        fig.update_traces(mode="lines+markers")
    
    if highlight_max:
        max_sales_day = data.loc[data['Sales'].idxmax()]
        fig.add_trace(go.Scatter(x=[max_sales_day['Day']], y=[max_sales_day['Sales']],
                                 mode='markers', marker=dict(size=12, color=colors['accent'], symbol='star'),
                                 name='Max Sales'))
    
    st.plotly_chart(fig)
    
    st.code(f"""
    import plotly.express as px
    import plotly.graph_objects as go
    
    # Create a line plot
    fig = px.line(data, x="Day", y="Sales", 
                  title="Sales Trend Over 10 Days",
                  labels={{"Day": "Day", "Sales": "Sales Amount"}},
                  line_shape="{line_shape}", render_mode="svg")
    fig.update_traces(line_color="{colors['secondary']}")
    
    # Optionally, add markers
    {"fig.update_traces(mode='lines+markers')" if show_markers else ""}
    
    # Optionally, highlight maximum sales point
    {"max_sales_day = data.loc[data['Sales'].idxmax()]" if highlight_max else ""}
    {"fig.add_trace(go.Scatter(x=[max_sales_day['Day']], y=[max_sales_day['Sales']]," if highlight_max else ""}
    {"                         mode='markers', marker=dict(size=12, color='green', symbol='star')," if highlight_max else ""}
    {"                         name='Max Sales'))" if highlight_max else ""}
    
    fig.show()
    """)

def sales_predictor_tab():
    st.header("Sales Predictor")
    
    st.write("Based on our historical data, let's try to predict sales for a future day!")
    
    day = st.slider("Select a future day", min_value=11, max_value=20, value=15)
    
    # Simple linear regression for prediction (this is a very basic model for demonstration purposes)
    data = generate_sample_data()
    X = data['Day'].values.reshape(-1, 1)
    y = data['Sales'].values
    model = LinearRegression().fit(X, y)
    
    predicted_sales = model.predict([[day]])[0]
    
    st.write(f"Predicted sales for day {day}: ${predicted_sales:.2f}")
    
    # Visualization
    future_days = list(range(1, 21))
    future_sales = model.predict([[d] for d in future_days])
    future_data = pd.DataFrame({'Day': future_days, 'Sales': future_sales})
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Day'], y=data['Sales'], mode='lines+markers', name='Historical Data'))
    fig.add_trace(go.Scatter(x=future_data['Day'][10:], y=future_data['Sales'][10:], mode='lines', line=dict(dash='dash'), name='Predicted Data'))
    fig.add_trace(go.Scatter(x=[day], y=[predicted_sales], mode='markers', marker=dict(size=12, color=colors['accent'], symbol='star'), name='Predicted Point'))
    
    fig.update_layout(title="Sales Prediction", xaxis_title="Day", yaxis_title="Sales Amount")
    st.plotly_chart(fig)
    
    explain("This prediction is based on a simple linear regression model. In real-world scenarios, more complex models and additional factors would be considered for accurate forecasting.")

def quiz_tab():
    st.header("Quiz: Line Plots")
    
    questions = [
        {
            "question": "What type of data is best represented by a line plot?",
            "options": [
                "Categorical data",
                "Time series data",
                "Nominal data",
                "Unordered data"
            ],
            "correct": 1,
            "explanation": "Line plots are best suited for representing time series data or any data that changes continuously over an interval."
        },
        {
            "question": "In the example line plot, on which day were sales the highest?",
            "options": [
                "Day 5",
                "Day 6",
                "Day 7",
                "Day 8"
            ],
            "correct": 2,
            "explanation": "The plot shows that sales peaked on day 7, reaching the highest point on the graph."
        },
        {
            "question": "What advantage does a line plot have over a bar plot for time series data?",
            "options": [
                "It can show more categories",
                "It's better for comparing exact values",
                "It clearly shows trends and patterns over time",
                "It always looks more visually appealing"
            ],
            "correct": 2,
            "explanation": "Line plots excel at showing trends and patterns over time, making it easy to visualize the overall direction and fluctuations in the data."
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
            st.success("Perfect score! You have a great understanding of line plots!")
        elif score >= len(questions) / 2:
            st.success("Good job! You have a solid grasp of line plot concepts.")
        else:
            st.info("Keep learning! Review the content about line plots to improve your understanding.")

if __name__ == "__main__":
    main()
