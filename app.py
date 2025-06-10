import streamlit as st
import pandas as pd

#Load game data from CSV
df = pd.read_csv("data/gators_games.csv")

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Set app title
st.title("Florida Gators Betting Assistant")

# Sidebar team selector
selected_team = st.sidebar.selectbox("Choose Your Team:", df['Team'].unique())

# Filter data for the selected team
team_data = df[df['Team'] == selected_team]

# Sort games by most recent date
team_data = team_data.sort_values(by='Date', ascending=False)

# Calculate summary statistics
total_games = len(team_data)
wins = (team_data['Result'] == 'Win').sum()
losses = (team_data['Result'] == 'Loss').sum()
recent_form = ' - '.join(team_data['Result'].head(5).tolist())  # e.g., Win - Loss - Win
avg_team_score = team_data['Team Score'].mean()
avg_opponent_score = team_data['Opponent Score'].mean()

# Display summary section
st.subheader(f"Summary for {selected_team}")
st.markdown(f"""
- Record: {wins} Wins / {losses} Losses  
- Recent Form: {recent_form}  
- Average Points Scored: {avg_team_score:.1f}  
- Average Points Allowed: {avg_opponent_score:.1f}
""")

# Show table of recent games
st.subheader("Game History")
st.dataframe(team_data)

# AI Prediction section (placeholder for now)
st.subheader("AI Prediction (Coming Soon)")
st.markdown("""
- Predicted Outcome: Pending  
- Confidence Level: Pending  
- Next Opponent: Pending
""")
