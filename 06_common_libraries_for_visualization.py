import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide", page_title="Common Libraries for Visualization")

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
</style>
""", unsafe_allow_html=True)

def main():
    st.title("Common Libraries for Visualization")
    st.write('**Developed by : Venugopal Adep**')
    
    st.markdown(f"""
    <p style='font-size: 1.2em; color: {colors['text']}; background-color: white; padding: 15px; border-radius: 5px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
    Welcome to the Common Libraries for Visualization demo! This app will help you understand 
    the capabilities of Matplotlib and Seaborn, two popular Python libraries for data visualization.
    </p>
    """, unsafe_allow_html=True)

    tabs = st.tabs([
        "Matplotlib", 
        "Seaborn", 
        "Comparison",
        "Quiz"
    ])

    with tabs[0]:
        matplotlib_tab()

    with tabs[1]:
        seaborn_tab()

    with tabs[2]:
        comparison_tab()

    with tabs[3]:
        quiz_tab()

def explain(text):
    st.markdown(f"""
    <div style='background-color: white; padding: 15px; border-radius: 5px; border-left: 5px solid {colors['accent']}; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
        <p style='color: {colors['text']}; margin: 0;'>{text}</p>
    </div>
    """, unsafe_allow_html=True)

def matplotlib_tab():
    st.header("Matplotlib")
    
    st.markdown("""
    - One of the most popular libraries for data visualizations
    - Provides high-quality graphics and a variety of plots such as histograms, bar charts, pie charts, etc.
    - Some important functions: plot(), hist(), bar(), pie(), scatter(), text(), legend(), etc.
    """)
    
    explain("Matplotlib is a versatile library that gives you fine-grained control over your visualizations.")
    
    # Interactive Matplotlib example
    st.subheader("Interactive Matplotlib Example")
    
    plot_type = st.selectbox("Choose a plot type", ["Line Plot", "Bar Chart", "Scatter Plot", "Histogram"])
    
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    if plot_type == "Line Plot":
        ax.plot(x, y)
        ax.set_title("Sine Wave")
    elif plot_type == "Bar Chart":
        data = {'A': 5, 'B': 7, 'C': 3, 'D': 8}
        ax.bar(data.keys(), data.values())
        ax.set_title("Sample Bar Chart")
    elif plot_type == "Scatter Plot":
        ax.scatter(x, y)
        ax.set_title("Sine Wave Scatter")
    else:  # Histogram
        ax.hist(np.random.normal(0, 1, 1000), bins=30)
        ax.set_title("Normal Distribution Histogram")
    
    st.pyplot(fig)
    
    st.code(f"""
    import matplotlib.pyplot as plt
    import numpy as np

    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Code for {plot_type.lower()}
    {ax.get_lines() if plot_type == "Line Plot" else ax.containers[0] if plot_type in ["Bar Chart", "Histogram"] else ax.collections[0]}
    
    plt.title("{ax.get_title()}")
    plt.show()
    """, language="python")

def seaborn_tab():
    st.header("Seaborn")
    
    st.markdown("""
    - Complementary to Matplotlib and specifically targets statistical data visualizations
    - A saying: "Matplotlib tries to make easy things easier and hard things possible, Seaborn tries to make a well-defined set of hard things easy too."
    - Some important functions: displot(), boxplot(), stripplot(), pairplot()
    """)
    
    explain("Seaborn is built on top of Matplotlib and provides a high-level interface for drawing attractive statistical graphics.")
    
    # Interactive Seaborn example
    st.subheader("Interactive Seaborn Example")
    
    plot_type = st.selectbox("Choose a plot type", ["Distplot", "Boxplot", "Stripplot", "Pairplot"])
    
    # Generate sample data
    data = pd.DataFrame({
        'A': np.random.normal(0, 1, 1000),
        'B': np.random.normal(2, 1, 1000),
        'C': np.random.normal(-1, 1, 1000)
    })
    
    if plot_type != "Pairplot":
        fig, ax = plt.subplots(figsize=(10, 6))
        
        if plot_type == "Distplot":
            sns.histplot(data=data, x='A', kde=True, ax=ax)
            ax.set_title("Distribution Plot")
        elif plot_type == "Boxplot":
            sns.boxplot(data=data, ax=ax)
            ax.set_title("Box Plot")
        elif plot_type == "Stripplot":
            sns.stripplot(data=data, ax=ax)
            ax.set_title("Strip Plot")
        
        st.pyplot(fig)
    else:  # Pairplot
        fig = sns.pairplot(data, height=3)
        st.pyplot(fig)
    
    st.code(f"""
    import seaborn as sns
    import pandas as pd
    import numpy as np

    data = pd.DataFrame({{
        'A': np.random.normal(0, 1, 1000),
        'B': np.random.normal(2, 1, 1000),
        'C': np.random.normal(-1, 1, 1000)
    }})

    # Code for {plot_type.lower()}
    {'fig, ax = plt.subplots(figsize=(10, 6))' if plot_type != "Pairplot" else ''}
    sns.{plot_type.lower()}(data=data{', x="A", kde=True' if plot_type == "Distplot" else ''}{', ax=ax' if plot_type != "Pairplot" else ''})
    {'plt.title("' + ax.get_title() + '")' if plot_type != "Pairplot" else ''}
    plt.show()
    """, language="python")

def comparison_tab():
    st.header("Matplotlib vs Seaborn")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Matplotlib")
        st.write("- More control over plot elements")
        st.write("- Steeper learning curve")
        st.write("- Good for custom visualizations")
    
    with col2:
        st.subheader("Seaborn")
        st.write("- Higher-level interface")
        st.write("- Easier for statistical visualizations")
        st.write("- Built-in themes and color palettes")
    
    explain("Both libraries have their strengths. Matplotlib offers more flexibility, while Seaborn provides convenient functions for common statistical plots.")
    
    # Comparison example
    st.subheader("Comparison Example: Scatter Plot")
    
    data = pd.DataFrame({
        'x': np.random.rand(100),
        'y': np.random.rand(100),
        'size': np.random.rand(100) * 100
    })
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Matplotlib
    ax1.scatter(data['x'], data['y'], s=data['size'])
    ax1.set_title("Matplotlib Scatter")
    
    # Seaborn
    sns.scatterplot(data=data, x='x', y='y', size='size', ax=ax2)
    ax2.set_title("Seaborn Scatter")
    
    st.pyplot(fig)

def quiz_tab():
    st.header("Visualization Libraries Quiz 📊")
    
    st.markdown(f"""
    <p style='font-size: 1.2em; color: {colors['text']}; background-color: white; padding: 15px; border-radius: 5px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
    Test your understanding of Matplotlib and Seaborn! Good luck! 🍀
    </p>
    """, unsafe_allow_html=True)

    questions = [
        {
            "question": "Which library is known for providing high-quality graphics and a variety of plots?",
            "options": ["NumPy", "Pandas", "Matplotlib", "Scikit-learn"],
            "correct": "Matplotlib",
            "explanation": "Matplotlib is one of the most popular libraries for data visualizations, providing high-quality graphics and a variety of plots."
        },
        {
            "question": "Which of the following is NOT a function typically associated with Matplotlib?",
            "options": ["plot()", "hist()", "bar()", "displot()"],
            "correct": "displot()",
            "explanation": "displot() is a function from Seaborn, not Matplotlib. The others (plot(), hist(), bar()) are common Matplotlib functions."
        },
        {
            "question": "What is Seaborn primarily designed for?",
            "options": ["Web development", "Machine learning", "Statistical data visualizations", "Database management"],
            "correct": "Statistical data visualizations",
            "explanation": "Seaborn is complementary to Matplotlib and specifically targets statistical data visualizations."
        },
        {
            "question": "According to the saying, what does Seaborn try to do?",
            "options": [
                "Make easy things easier and hard things possible",
                "Make a well-defined set of hard things easy",
                "Replace Matplotlib entirely",
                "Provide only 3D visualizations"
            ],
            "correct": "Make a well-defined set of hard things easy",
            "explanation": "The saying goes: 'Matplotlib tries to make easy things easier and hard things possible, Seaborn tries to make a well-defined set of hard things easy too.'"
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
    Remember, both Matplotlib and Seaborn have their strengths. Practice with both to become a visualization expert! 📈
    </p>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()