import streamlit as st
import random

st.set_page_config(page_title="NumPy & Pandas Explorer", layout="wide")

# Custom CSS for a more appealing look
st.markdown("""
<style>
    .stApp {
        max-width: 1000px;
        margin: 0 auto;
        background-color: #f0f8ff;
    }
    h1, h2 {
        color: #0066CC;
        text-align: center;
    }
    .concept-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .stButton>button {
        height: 60px;
        font-size: 20px;
        font-weight: bold;
        border-radius: 30px;
    }
    .score-box {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        padding: 10px;
        background-color: #e6f3ff;
        border-radius: 10px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.title("NumPy & Pandas Concept Challenge")

# Define the concepts
concepts = {
    "NumPy": [
        "Numerical Python",
        "Fundamental package for scientific computing",
        "A powerful N-dimensional array object - ndarray",
        "Useful in linear algebra, vector calculus, and random number capabilities, etc."
    ],
    "Pandas": [
        "Extremely useful for data manipulation and exploratory analysis",
        "Offers two major data structures - Series & DataFrame",
        "A DataFrame is made up of several Series - Each column of a DataFrame is a Series",
        "In a DataFrame, each column can have its own data type unlike NumPy array which creates all entries with the same data type"
    ]
}

# Initialize session state
if 'game_state' not in st.session_state:
    st.session_state.game_state = {
        'concepts': [(concept, library) for library, concept_list in concepts.items() for concept in concept_list],
        'score': 0,
        'total_concepts': sum(len(concept_list) for concept_list in concepts.values()),
        'current_concept': None,
        'feedback': None
    }

# Main game logic
if st.session_state.game_state['concepts']:
    if not st.session_state.game_state['current_concept']:
        st.session_state.game_state['current_concept'] = random.choice(st.session_state.game_state['concepts'])
        st.session_state.game_state['feedback'] = None

    # Display live score
    st.markdown(f"""
    <div class="score-box">
        Score: {st.session_state.game_state['score']} / {st.session_state.game_state['total_concepts']}
    </div>
    """, unsafe_allow_html=True)

    # Display the concept
    st.markdown(f"""
    <div class="concept-box">
        <h2>Which library does this concept belong to?</h2>
        <p style="font-size: 18px; font-style: italic;">{st.session_state.game_state['current_concept'][0]}</p>
    </div>
    """, unsafe_allow_html=True)

    # Buttons for selection
    col1, col2 = st.columns(2)
    with col1:
        numpy_selected = st.button("NumPy", key="numpy_button", use_container_width=True)
    with col2:
        pandas_selected = st.button("Pandas", key="pandas_button", use_container_width=True)

    # Check answer and provide feedback
    if numpy_selected or pandas_selected:
        selected_library = "NumPy" if numpy_selected else "Pandas"
        correct_library = st.session_state.game_state['current_concept'][1]
        
        if selected_library == correct_library:
            st.session_state.game_state['score'] += 1
            st.session_state.game_state['feedback'] = f"✅ Correct! This concept belongs to {correct_library}."
        else:
            st.session_state.game_state['feedback'] = f"❌ Oops! This concept actually belongs to {correct_library}."
        
        st.session_state.game_state['concepts'].remove(st.session_state.game_state['current_concept'])
        st.session_state.game_state['current_concept'] = None
        st.rerun()

    # Display feedback
    if st.session_state.game_state['feedback']:
        st.markdown(f"""
        <div style="padding: 10px; border-radius: 5px; text-align: center; font-size: 18px; font-weight: bold; background-color: {'#d4edda' if '✅' in st.session_state.game_state['feedback'] else '#f8d7da'};">
            {st.session_state.game_state['feedback']}
        </div>
        """, unsafe_allow_html=True)

else:
    final_score = st.session_state.game_state['score']
    total_concepts = st.session_state.game_state['total_concepts']
    percentage = (final_score / total_concepts) * 100

    st.markdown(f"""
    <div style="text-align: center; padding: 20px; background-color: #e6f3ff; border-radius: 10px;">
        <h2>🎉 Congratulations! You've completed the challenge! 🎉</h2>
        <p style="font-size: 24px;">Your final score: {final_score} / {total_concepts}</p>
        <p style="font-size: 20px;">Accuracy: {percentage:.1f}%</p>
    </div>
    """, unsafe_allow_html=True)

    if percentage == 100:
        st.balloons()

    if st.button("Play Again", key="play_again"):
        st.session_state.game_state = {
            'concepts': [(concept, library) for library, concept_list in concepts.items() for concept in concept_list],
            'score': 0,
            'total_concepts': sum(len(concept_list) for concept_list in concepts.values()),
            'current_concept': None,
            'feedback': None
        }
        st.rerun()

# Brief explanation
st.markdown("""
---
<div style="text-align: center; font-style: italic;">
    Test your knowledge of NumPy and Pandas concepts!<br>
    Select the library you think each concept belongs to and see how well you know these key data manipulation tools.
</div>
""", unsafe_allow_html=True)
