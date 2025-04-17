import streamlit as st
import pandas as pd
from datetime import datetime
from io import BytesIO

st.set_page_config(page_title="Growth Mindset Tracker", layout="centered")
st.title("Growth Mindset Tracker")

st.markdown("Track your goals, reflect on your growth, and embrace the mindset to keep improving every day! 🚀")

if 'logs' not in st.session_state:
    st.session_state.logs = []

with st.form("mindset_form"):
    st.subheader("Daily Entry")

    date = st.date_input("Date", value=datetime.today())
    goal = st.text_input("What is your goal for today?")
    challenge = st.text_area("What challenge did you face today?")
    learning = st.text_area("What did you learn from it?")
    mood = st.slider("How are you feeling today?", 1, 10, 5)

    submitted = st.form_submit_button("Add Entry")
    if submitted:
        st.session_state.logs.append({
            "Date": date,
            "Goal": goal,
            "Challenge": challenge,
            "Learning": learning,
            "Mood": mood
        })
        st.success("Entry added successfully!")

if st.session_state.logs:
    df = pd.DataFrame(st.session_state.logs)
    st.subheader("Journal Summary")
    st.dataframe(df)

    st.subheader("Mood Over Time")
    mood_chart = df[['Date', 'Mood']].sort_values("Date")
    st.line_chart(mood_chart.set_index("Date"))

    buffer = BytesIO()
    df.to_csv(buffer, index=False)
    buffer.seek(0)

    st.download_button(
        label="Download Journal as CSV",
        data=buffer,
        file_name="growth_mindset_journal.csv",
        mime="text/csv"
    )
else:
    st.info("No entries yet. Start tracking your mindset by filling the form above!")
