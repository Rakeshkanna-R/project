from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import os

# Set up Google API credentials
os.environ["GOOGLE_API_KEY"] = "AIzaSyC96ELnaWIN_3kHSzykc--ZISfgm04lVxI"

# Initialize the user database in session state if it doesn't exist
if "user_db" not in st.session_state:
    st.session_state.user_db = {}  # Default user

# Session state initialization for authentication
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "username" not in st.session_state:
    st.session_state.username = ""


# Define the function to generate the travel plan
def generate_response(destination, number_of_days, budget):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful assistant that plans trips based on the user's destination, number of days, and budget.",
            ),
            (
                "human",
                f"Plan my trip to {destination}. I want to stay for {number_of_days} days and my budget is {budget}. Please suggest for Accommodation,Food,Transportation,Tips for Saving Money.  Please suggest some activities to do and places to visit with a suitable title.",
            ),
        ]
    )
    chain = prompt | llm
    ai_response = chain.invoke({"destination": destination, "number_of_days": number_of_days, "budget": budget})
    return ai_response.content

# Authentication functions
def login(username, password):
    if st.session_state.user_db.get(username) == password:
        st.session_state.authenticated = True
        st.session_state.username = username
        st.success("Login successful!")
    else:
        st.error("Invalid username or password.")

def signup(username, password):
    if username in st.session_state.user_db:
        st.error("Username already exists. Please choose a different one.")
    else:
        st.session_state.user_db[username] = password
        st.success("Signup successful! Please log in.")
