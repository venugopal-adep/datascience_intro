import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide", page_title="Data Visualization Explorer")

# Custom color palette
colors = {
    "primary": "#3366CC",
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
</style>
""", unsafe_allow_html=True)

def main():
    st.title("Data Visualization Explorer")
    st.write('**Developed by : Venugopal Adep**')

    st.markdown(f"""
    <p style='font-size: 1.2em; color: {colors['text']}; background-color: white; padding: 15px; border-radius: 5px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
    Welcome to the Data Visualization Explorer! This app demonstrates some of the most commonly used
    visualization techniques and libraries in Python. Let's explore these powerful tools!
    </p>
    """, unsafe_allow_html=True)

    tabs = st.tabs([
        "Importance of Data Viz", "Visualization Libraries", "Choosing Visualizations", 
        "Interactive Plotting", "Advanced Techniques", "Visualization Quiz"
    ])

    with tabs[0]:
        importance_of_data_viz_tab()

    with tabs[1]:
        visualization_libraries_tab()

    with tabs[2]:
        choosing_visualizations_tab()

    with tabs[3]:
        interactive_plotting_tab()

    with tabs[4]:
        advanced_techniques_tab()

    with tabs[5]:
        quiz_tab()

def show_code(code):
    st.code(code, language='python')

def explain(text):
    st.markdown(f"""
    <div style='background-color: white; padding: 15px; border-radius: 5px; border-left: 5px solid {colors['accent']}; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
        <p style='color: {colors['text']}; margin: 0;'>{text}</p>
    </div>
    """, unsafe_allow_html=True)

def importance_of_data_viz_tab():
    st.header("Importance of Data Visualization")
    
    st.subheader("Why Data Visualization Matters")
    
    benefits = [
        "Quickly identify patterns and trends",
        "Communicate complex information effectively",
        "Make data-driven decisions",
        "Spot outliers and anomalies",
        "Understand relationships between variables"
    ]
    
    for benefit in benefits:
        st.markdown(f"- {benefit}")
    
    explain("Data visualization transforms raw data into meaningful visual representations, making it easier to understand and analyze large amounts of information.")
    
    # Example visualization
    data = pd.DataFrame({
        'category': ['A', 'B', 'C', 'D', 'E'],
        'value': [23, 48, 12, 35, 19]
    })
    
    fig = px.bar(data, x='category', y='value', title='Simple Bar Chart Example')
    st.plotly_chart(fig)
    
    show_code("""
    import plotly.express as px
    import pandas as pd

    data = pd.DataFrame({
        'category': ['A', 'B', 'C', 'D', 'E'],
        'value': [23, 48, 12, 35, 19]
    })
    
    fig = px.bar(data, x='category', y='value', title='Simple Bar Chart Example')
    fig.show()
    """)

def visualization_libraries_tab():
    st.header("Popular Visualization Libraries in Python")
    
    libraries = {
        "Matplotlib": "The foundational library for plotting in Python. Offers fine-grained control over plot elements.",
        "Seaborn": "Built on top of Matplotlib, provides a high-level interface for statistical graphics.",
        "Plotly": "Creates interactive, publication-quality graphs. Great for web-based visualizations.",
        "Bokeh": "Focuses on interactive visualization for modern web browsers.",
        "Altair": "Declarative statistical visualization library based on Vega and Vega-Lite."
    }
    
    for lib, desc in libraries.items():
        st.subheader(lib)
        st.write(desc)
        
    st.subheader("Comparison Example: Line Plot")
    
    # Generate sample data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    # Matplotlib
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("Matplotlib Line Plot")
    st.pyplot(fig)
    
    # Seaborn
    fig, ax = plt.subplots()
    sns.lineplot(x=x, y=y)
    ax.set_title("Seaborn Line Plot")
    st.pyplot(fig)
    
    # Plotly
    fig = px.line(x=x, y=y, title="Plotly Line Plot")
    st.plotly_chart(fig)
    
    explain("Each library has its strengths. Choose based on your specific needs, such as interactivity, statistical analysis, or publication-quality static images.")

def choosing_visualizations_tab():
    st.header("Choosing the Right Visualization")
    
    st.write("The choice of visualization depends on the type of data and the story you want to tell.")
    
    viz_types = {
        "Bar Charts": "Compare quantities across categories",
        "Line Charts": "Show trends over time",
        "Scatter Plots": "Explore relationships between two variables",
        "Pie Charts": "Show composition of a whole",
        "Heatmaps": "Visualize patterns in a matrix of data",
        "Box Plots": "Display distribution and identify outliers"
    }
    
    for viz, desc in viz_types.items():
        st.subheader(viz)
        st.write(desc)
    
    # Interactive example
    st.subheader("Interactive Example: Choose Your Visualization")
    
    data = pd.DataFrame({
        'date': pd.date_range(start='2023-01-01', periods=100),
        'value': np.random.randn(100).cumsum(),
        'category': np.random.choice(['A', 'B', 'C'], 100)
    })
    
    viz_choice = st.selectbox("Select a visualization type", ["Line Chart", "Bar Chart", "Scatter Plot"])
    
    if viz_choice == "Line Chart":
        fig = px.line(data, x='date', y='value', title='Line Chart Example')
    elif viz_choice == "Bar Chart":
        fig = px.bar(data.groupby('category').mean().reset_index(), x='category', y='value', title='Bar Chart Example')
    else:
        fig = px.scatter(data, x='date', y='value', color='category', title='Scatter Plot Example')
    
    st.plotly_chart(fig)
    
    explain("Consider your audience, the complexity of your data, and the key insights you want to convey when choosing a visualization type.")

def interactive_plotting_tab():
    st.header("Interactive Plotting with Plotly")
    
    st.write("Plotly allows you to create interactive visualizations that users can explore.")
    
    # Generate sample data
    np.random.seed(0)
    data = pd.DataFrame({
        'x': np.random.rand(100),
        'y': np.random.rand(100),
        'size': np.random.rand(100) * 30,
        'color': np.random.rand(100)
    })
    
    fig = px.scatter(data, x='x', y='y', size='size', color='color',
                     title='Interactive Scatter Plot',
                     labels={'color': 'Color Value'},
                     hover_data=['x', 'y', 'size'])
    
    st.plotly_chart(fig)
    
    show_code("""
    import plotly.express as px
    import pandas as pd
    import numpy as np

    np.random.seed(0)
    data = pd.DataFrame({
        'x': np.random.rand(100),
        'y': np.random.rand(100),
        'size': np.random.rand(100) * 30,
        'color': np.random.rand(100)
    })
    
    fig = px.scatter(data, x='x', y='y', size='size', color='color',
                     title='Interactive Scatter Plot',
                     labels={'color': 'Color Value'},
                     hover_data=['x', 'y', 'size'])
    fig.show()
    """)
    
    explain("Interactive plots allow users to zoom, pan, and hover over data points to get more information. This can be particularly useful for exploring complex datasets.")

def advanced_techniques_tab():
    st.header("Advanced Visualization Techniques")
    
    st.subheader("Faceting")
    
    # Generate sample data
    data = pd.DataFrame({
        'x': np.random.rand(200),
        'y': np.random.rand(200),
        'category': np.random.choice(['A', 'B', 'C', 'D'], 200)
    })
    
    fig = px.scatter(data, x='x', y='y', color='category', facet_col='category',
                     title='Faceted Scatter Plot')
    st.plotly_chart(fig)
    
    st.subheader("3D Plotting")
    
    # Generate 3D data
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))
    
    fig = go.Figure(data=[go.Surface(z=Z, x=x, y=y)])
    fig.update_layout(title='3D Surface Plot', autosize=False,
                      width=500, height=500,
                      margin=dict(l=65, r=50, b=65, t=90))
    st.plotly_chart(fig)
    
    explain("Advanced techniques like faceting and 3D plotting can help reveal complex patterns and relationships in your data.")

def quiz_tab():
    st.header("Data Visualization Quiz 🎨")
    
    st.markdown(f"""
    <p style='font-size: 1.2em; color: {colors['text']}; background-color: white; padding: 15px; border-radius: 5px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
    Test your knowledge of data visualization concepts! Good luck! 🍀
    </p>
    """, unsafe_allow_html=True)

    questions = [
        {
            "question": "Which type of plot is best for showing trends over time?",
            "options": ["Bar chart", "Pie chart", "Line chart", "Scatter plot"],
            "correct": "Line chart",
            "explanation": "Line charts are ideal for showing how values change over time, making trends easily visible."
        },
        {
            "question": "Which Python library is known for its statistical visualizations?",
            "options": ["Matplotlib", "Seaborn", "Plotly", "Bokeh"],
            "correct": "Seaborn",
            "explanation": "Seaborn is built on top of Matplotlib and provides a high-level interface for drawing attractive statistical graphics."
        },
        {
            "question": "What type of plot would you use to show the distribution of a continuous variable?",
            "options": ["Bar chart", "Histogram", "Pie chart", "Scatter plot"],
            "correct": "Histogram",
            "explanation": "Histograms are used to show the distribution of a continuous variable by dividing it into bins and showing the frequency of each bin."
        },
        {
            "question": "Which library is best for creating interactive, web-based visualizations?",
            "options": ["Matplotlib", "Seaborn", "Plotly", "Pandas"],
            "correct": "Plotly",
            "explanation": "Plotly is designed for creating interactive, publication-quality graphs that work well in web-based environments."
        },
        {
            "question": "What type of plot is best for showing the relationship between two continuous variables?",
            "options": ["Bar chart", "Line chart", "Scatter plot", "Pie chart"],
            "correct": "Scatter plot",
            "explanation": "Scatter plots are ideal for visualizing the relationship between two continuous variables, showing patterns, correlations, or clusters in the data."
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
    Remember, effective data visualization is both an art and a science. Keep practicing and exploring different techniques! 📊
    </p>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()