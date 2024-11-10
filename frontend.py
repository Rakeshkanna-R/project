# Streamlit UI setup
st.set_page_config(page_title="Travel Planner", page_icon=":earth_africa:")

# Login and Signup page layout
if not st.session_state.authenticated:
    st.sidebar.title("Login / Signup")
    option = st.sidebar.selectbox("Choose option", ["Login", "Signup"])

    if option == "Login":
        st.sidebar.subheader("Login")
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")
        if st.sidebar.button("Login"):
            login(username, password)

    elif option == "Signup":
        st.sidebar.subheader("Signup")
        new_username = st.sidebar.text_input("Create Username")
        new_password = st.sidebar.text_input("Create Password", type="password")
        if st.sidebar.button("Signup"):
            signup(new_username, new_password)
else:
    st.sidebar.write(f"Welcome, {st.session_state.username}")
    if st.sidebar.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.username = ""
        st.rerun()

# Travel planner UI
if st.session_state.authenticated:
    st.title("Your Personalized Trip Planner")
    st.header("Let AI Create the Perfect Trip for You")

    destination = st.text_input("Enter your travel destination:")
    number_of_days = st.text_input("Enter number of days for the trip:")
    budget = st.text_input("Enter your budget (e.g., $2000):")

    if st.button("Generate Travel Plan") and destination and number_of_days and budget:
        with st.spinner("Generating travel plan..."):
            response = generate_response(destination, number_of_days, budget)
            st.markdown(response)
else:
    st.title("Please log in to access the Trip Planner.")
