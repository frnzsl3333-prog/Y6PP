# --- Import required libraries ---
import streamlit as st
import random
import time
import pandas as pd
import altair as alt

# --- Title of the app ---
st.title("Cricket Scoreboard")

# --- Sidebar for inputs ---
st.sidebar.header("Match Settings")
team1 = st.sidebar.text_input("Enter Team 1 name:", "AUS")
team2 = st.sidebar.text_input("Enter Team 2 name:", "IND")
overs = st.sidebar.slider("Pick number of overs between 1 and 20", 1, 20, 5)

# Start button
start_button = st.sidebar.button("Start Match")

# --- Main display ---
score_display = st.empty()

if start_button:
    final_scores = {team1: 0, team2: 0}
    final_wickets = {team1: 0, team2: 0}

    def update_scoreboard(batting_team, total_runs, wickets, current_over=0, current_ball=0):
        """Update the scoreboard display with runs, wickets, and overs.balls."""
        scoreboard_html = f"""
        <div style='background-color:#003366; color:yellow; padding:20px; border-radius:10px; text-align:center;'>
            <h1 style='margin:0; font-size:48px;'><b>{team1}: {final_scores[team1]}/{final_wickets[team1]}  |  {team2}: {final_scores[team2]}/{final_wickets[team2]}</b></h1>
            <h3 style='margin:5px 0 0 0; font-size:24px;'>
                Currently batting: {batting_team} | Runs: {total_runs} | Wickets: {wickets} | Overs: {current_over}.{current_ball}
            </h3>
        </div>
        """
        score_display.markdown(scoreboard_html, unsafe_allow_html=True)

    def play_innings(batting_team):
        """Simulate one innings for the batting team."""
        total_runs = 0
        wickets = 0
        total_balls = overs * 6
        runs_list = []
        outcome_list = []

        for ball in range(1, total_balls + 1):
            run = random.choices(
                [0, 1, 2, 3, 4, 6, "W"],
                weights=[10, 25, 15, 5, 15, 10, 20]
            )[0]

            if run == "W":
                wickets += 1
                outcome_list.append("W")
            else:
                total_runs += run
                outcome_list.append(run)
            runs_list.append(total_runs)

            # Calculate overs and balls like real cricket
            current_over = (ball - 1) // 6
            current_ball = (ball - 1) % 6

            update_scoreboard(batting_team, total_runs, wickets, current_over, current_ball)
            time.sleep(0.2)

            if wickets == 10:
                break

        final_scores[batting_team] = total_runs
        final_wickets[batting_team] = wickets
        update_scoreboard(batting_team, total_runs, wickets, current_over, current_ball)

        return total_runs, wickets, runs_list, outcome_list

    # --- Play both innings ---
    team1_score, team1_wickets, team1_runs, team1_outcomes = play_innings(team1)
    team2_score, team2_wickets, team2_runs, team2_outcomes = play_innings(team2)

    update_scoreboard("Match End", 0, 0)
    st.write("---")

    # --- Match Result ---
    if final_scores[team1] > final_scores[team2]:
        st.markdown(f"<h1 style='color:green; text-align:center;'>🏆 {team1} WINS!</h1>", unsafe_allow_html=True)
    elif final_scores[team2] > final_scores[team1]:
        st.markdown(f"<h1 style='color:green; text-align:center;'>🏆 {team2} WINS!</h1>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h1 style='color:orange; text-align:center;'>🤝 IT'S A TIE!</h1>", unsafe_allow_html=True)

    # --- Line Graph: Runs per Ball ---
    st.subheader("📈 Runs per Ball Graph")
    df1 = pd.DataFrame({'Ball': list(range(1, len(team1_runs)+1)), 'Runs': team1_runs, 'Team': team1})
    df2 = pd.DataFrame({'Ball': list(range(1, len(team2_runs)+1)), 'Runs': team2_runs, 'Team': team2})
    df = pd.concat([df1, df2])
    line_chart = alt.Chart(df).mark_line(point=True).encode(
        x='Ball', y='Runs',
        color=alt.Color('Team', scale=alt.Scale(domain=[team1, team2], range=['#FFD700','#008000'])),
        tooltip=['Ball', 'Runs', 'Team']
    ).interactive()
    st.altair_chart(line_chart, use_container_width=True)

    # --- Bar Chart: Runs per Over ---
    st.subheader("📊 Runs per Over")
    df1['Over'] = ((df1['Ball']-1)//6) + 1
    df2['Over'] = ((df2['Ball']-1)//6) + 1
    over_df = pd.concat([df1, df2])
    over_chart = alt.Chart(over_df).mark_bar().encode(
        x='Over:O', y='Runs',
        color=alt.Color('Team', scale=alt.Scale(domain=[team1, team2], range=['#FFD700','#008000'])),
        tooltip=['Over','Runs','Team']
    )
    st.altair_chart(over_chart, use_container_width=True)
