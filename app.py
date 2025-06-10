import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("data/gators_games.csv")

# Title
st.title("🏀 Florida Gators Betting Assistant")

# Team selector
selected_team = st.sidebar.selectbox("Choose your School's Team:", df['Team'].unique())

# Filtered data
team_data = df[df['Team'] == selected_team]

# Show table
st.subheader(f"Recent Games for {selected_team}")
st.dataframe(team_data)

# Placeholder prediction
st.subheader("🤖 AI Prediction (Coming Soon)")
st.text("Model prediction: Pending")
st.text("Confidence: Pending")
