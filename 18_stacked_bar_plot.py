import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", page_title="Stacked Bar Plot Exploration")

# Custom color palette
colors = {
    "primary": "#0066CC",
    "secondary": "#FF9900", 
    "accent": "#66CC99",
    "background": "#F0F8FF",
    "text": "#333333"
}

# Custom CSS for background and text styling
st.markdown(f"""
<style>
    .stApp {{
        background-color: {colors['background']};
    }}
    .block-container {{
        padding: 1rem;
        max-width: 100%;
    }}
    h1, h2, h3, h4 {{
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

def generate_sample_data():
    fitness_levels = ['Very Poor', 'Poor', 'Good', 'Very Good']
    smoker_percentages = [0.8, 0.27, 0.25, 0.48]
    non_smoker_percentages = [0.2, 0.73, 0.75, 0.52]
    return pd.DataFrame({'Fitness': fitness_levels, 'Smoker': smoker_percentages, 'Non-smoker': non_smoker_percentages})

def interactive_demo_tab():
    st.header("Interactive Stacked Bar Plot Demo")
    
    # Create two columns: left for explanation and input elements, right for plots
    left_col, right_col = st.columns([1, 2])
    
    data = generate_sample_data()
    
    with left_col:
        st.subheader("Sample Data")
        st.write(data)
        
        st.subheader("Customize the Plot")
        orientation = st.radio("Bar Orientation", ["Vertical", "Horizontal"])
        percentage_display = st.checkbox("Show Percentages", value=True)
        
        explain("This plot shows the percentage of smokers and non-smokers for different fitness levels. We can observe that the percentage of smokers is very high for people with very poor fitness.")
    
    with right_col:
        st.subheader("Stacked Bar Plot: Smoking Habits by Fitness Level")
        if orientation == "Vertical":
            fig = px.bar(data, x="Fitness", y=["Smoker", "Non-smoker"], 
                         title="Percentage of Smokers and Non-smokers by Fitness Level",
                         labels={"value": "Percentage", "variable": "Smoking Status"},
                         color_discrete_map={"Smoker": "#1E90FF", "Non-smoker": "#4B0082"})
        else:
            fig = px.bar(data, y="Fitness", x=["Smoker", "Non-smoker"], 
                         title="Percentage of Smokers and Non-smokers by Fitness Level",
                         labels={"value": "Percentage", "variable": "Smoking Status"},
                         color_discrete_map={"Smoker": "#1E90FF", "Non-smoker": "#4B0082"},
                         orientation='h')
        
        if percentage_display:
            fig.update_traces(texttemplate='%{y:.0%}', textposition='inside')
        
        fig.update_layout(yaxis_title="Percentage" if orientation == "Vertical" else "Fitness Level",
                          xaxis_title="Fitness Level" if orientation == "Vertical" else "Percentage")
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Full-width code block at the bottom
    st.subheader("Code Used for the Plot")
    st.code("""
    import plotly.express as px
    
    # Create a stacked bar plot
    fig = px.bar(data, x="Fitness", y=["Smoker", "Non-smoker"], 
                 title="Percentage of Smokers and Non-smokers by Fitness Level",
                 labels={"value": "Percentage", "variable": "Smoking Status"},
                 color_discrete_map={"Smoker": "#1E90FF", "Non-smoker": "#4B0082"})
    
    # Optionally, change orientation to horizontal
    # fig = px.bar(data, y="Fitness", x=["Smoker", "Non-smoker"], 
    #              title="Percentage of Smokers and Non-smokers by Fitness Level",
    #              labels={"value": "Percentage", "variable": "Smoking Status"},
    #              color_discrete_map={"Smoker": "#1E90FF", "Non-smoker": "#4B0082"},
    #              orientation='h')
    
    # Optionally, display percentages
    # fig.update_traces(texttemplate='%{y:.0%}', textposition='inside')
    
    fig.show()
    """)

def quiz_tab():
    st.header("Quiz: Stacked Bar Plots")
    
    questions = [
        {
            "question": "What is the main purpose of a stacked bar plot?",
            "options": [
                "To show trends over time",
                "To compare total amounts and composition within categories",
                "To display the distribution of a continuous variable",
                "To show the correlation between two variables"
            ],
            "correct": 1,
            "explanation": "Stacked bar plots are primarily used to compare total amounts across categories and show the composition within each category."
        },
        {
            "question": "In the example stacked bar plot, which fitness level has the highest percentage of smokers?",
            "options": [
                "Very Good",
                "Good",
                "Poor",
                "Very Poor"
            ],
            "correct": 3,
            "explanation": "The plot shows that the 'Very Poor' fitness level has the highest percentage of smokers, with about 80% of individuals in this category being smokers."
        },
        {
            "question": "What advantage does a stacked bar plot have over a simple bar plot?",
            "options": [
                "It can show more categories",
                "It displays part-to-whole relationships within each category",
                "It's better for comparing exact values",
                "It always looks more visually appealing"
            ],
            "correct": 1,
            "explanation": "A key advantage of stacked bar plots is their ability to display part-to-whole relationships within each category, showing both the total and the breakdown simultaneously."
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
            st.success("Perfect score! You have a great understanding of stacked bar plots!")
        elif score >= len(questions) / 2:
            st.success("Good job! You have a solid grasp of stacked bar plot concepts.")
        else:
            st.info("Keep learning! Review the content about stacked bar plots to improve your understanding.")

def main():
    st.title("Stacked Bar Plot Exploration")
    st.write('**Developed by: Venugopal Adep**')
    
    tabs = st.tabs(["Learn", "Interactive Demo", "Quiz"])
    
    with tabs[0]:
        st.header("Stacked Bar Plot")
        st.markdown("""
        - Stacked Bar plots are used to show how a larger category is divided into smaller categories and what relationship each category of one variable has with each category of another variable.
        - They allow for comparison of total amounts across categories as well as the composition within each category.
        - Stacked bar plots are particularly useful for displaying part-to-whole relationships.
        """)
        explain("Stacked bar plots help visualize the composition of different groups and how they compare to each other. They're excellent for showing both the total and the breakdown of categories simultaneously.")
    
    with tabs[1]:
        interactive_demo_tab()
    
    with tabs[2]:
        quiz_tab()

if __name__ == "__main__":
    main()
