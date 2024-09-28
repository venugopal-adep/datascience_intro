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
        'numpy_concepts': numpy_concepts.copy(),
        'pandas_concepts': pandas_concepts.copy(),
        'score': 0,
        'total_concepts': len(numpy_concepts) + len(pandas_concepts)
    }

# Function to check if the concept belongs to NumPy or Pandas
def check_concept(concept, library):
    if library == "NumPy" and concept in numpy_concepts:
        return True
    elif library == "Pandas" and concept in pandas_concepts:
        return True
    return False

# Main game logic
col1, col2 = st.columns(2)

with col1:
    st.header("NumPy")
    numpy_drop = st.empty()

with col2:
    st.header("Pandas")
    pandas_drop = st.empty()

# Display a random concept
if st.session_state.game_state['numpy_concepts'] or st.session_state.game_state['pandas_concepts']:
    all_concepts = st.session_state.game_state['numpy_concepts'] + st.session_state.game_state['pandas_concepts']
    current_concept = random.choice(all_concepts)
    
    st.write("Drag and drop this concept to the correct library:")
    st.info(current_concept)
    
    numpy_clicked = numpy_drop.button("Drop to NumPy")
    pandas_clicked = pandas_drop.button("Drop to Pandas")
    
    if numpy_clicked or pandas_clicked:
        if (numpy_clicked and check_concept(current_concept, "NumPy")) or (pandas_clicked and check_concept(current_concept, "Pandas")):
            st.success("Correct! Well done!")
            st.session_state.game_state['score'] += 1
        else:
            st.error("Oops! That's not the right library for this concept.")
        
        # Remove the concept from the game state
        if current_concept in st.session_state.game_state['numpy_concepts']:
            st.session_state.game_state['numpy_concepts'].remove(current_concept)
        else:
            st.session_state.game_state['pandas_concepts'].remove(current_concept)
        
        # Force a rerun to update the game state
        st.experimental_rerun()
else:
    st.success(f"Congratulations! You've completed the game. Your score: {st.session_state.game_state['score']}/{st.session_state.game_state['total_concepts']}")
    if st.button("Play Again"):
        st.session_state.game_state = {
            'numpy_concepts': numpy_concepts.copy(),
            'pandas_concepts': pandas_concepts.copy(),
            'score': 0,
            'total_concepts': len(numpy_concepts) + len(pandas_concepts)
        }
        st.experimental_rerun()

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
        width: 100%;
        height: 100px;
        font-size: 20px;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)
