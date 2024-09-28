import streamlit as st
import random

st.set_page_config(page_title="NumPy & Pandas Explorer", layout="wide")

st.title("Key Libraries for Data Manipulation - NumPy & Pandas")

# Define the concepts
numpy_concepts = [
    "Numerical Python",
    "Fundamental package for scientific computing",
    "A powerful N-dimensional array object - ndarray",
    "Useful in linear algebra, vector calculus, and random number capabilities, etc."
]

pandas_concepts = [
    "Extremely useful for data manipulation and exploratory analysis",
    "Offers two major data structures - Series & DataFrame",
    "A DataFrame is made up of several Series - Each column of a DataFrame is a Series",
    "In a DataFrame, each column can have its own data type unlike NumPy array which creates all entries with the same data type"
]

# Session state to keep track of the game state
if 'game_state' not in st.session_state:
    st.session_state.game_state = {
        'concepts': numpy_concepts + pandas_concepts,
        'score': 0,
        'total_concepts': len(numpy_concepts) + len(pandas_concepts),
        'current_concept': None
    }

# Function to check if the concept belongs to NumPy or Pandas
def check_concept(concept, library):
    if library == "NumPy" and concept in numpy_concepts:
        return True
    elif library == "Pandas" and concept in pandas_concepts:
        return True
    return False

# Main game logic
if st.session_state.game_state['concepts']:
    if not st.session_state.game_state['current_concept']:
        st.session_state.game_state['current_concept'] = random.choice(st.session_state.game_state['concepts'])
    
    st.write("Select the correct library for this concept:")
    st.info(st.session_state.game_state['current_concept'])
    
    col1, col2 = st.columns(2)
    with col1:
        numpy_selected = st.button("NumPy", key="numpy_button", use_container_width=True)
    with col2:
        pandas_selected = st.button("Pandas", key="pandas_button", use_container_width=True)
    
    if numpy_selected or pandas_selected:
        selected_library = "NumPy" if numpy_selected else "Pandas"
        if check_concept(st.session_state.game_state['current_concept'], selected_library):
            st.success("Correct! Well done!")
            st.session_state.game_state['score'] += 1
        else:
            st.error(f"Oops! This concept belongs to {'NumPy' if selected_library == 'Pandas' else 'Pandas'}.")
        
        # Remove the concept from the game state
        st.session_state.game_state['concepts'].remove(st.session_state.game_state['current_concept'])
        st.session_state.game_state['current_concept'] = None
        st.rerun()
else:
    st.success(f"Congratulations! You've completed the game. Your score: {st.session_state.game_state['score']}/{st.session_state.game_state['total_concepts']}")
    if st.button("Play Again"):
        st.session_state.game_state = {
            'concepts': numpy_concepts + pandas_concepts,
            'score': 0,
            'total_concepts': len(numpy_concepts) + len(pandas_concepts),
            'current_concept': None
        }
        st.rerun()

# Display current score
st.sidebar.write(f"Current Score: {st.session_state.game_state['score']}/{st.session_state.game_state['total_concepts']}")

# Styling
st.markdown("""
<style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    h1, h2 {
        color: #0066CC;
    }
    .stButton>button {
        height: 60px;
        font-size: 20px;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)
