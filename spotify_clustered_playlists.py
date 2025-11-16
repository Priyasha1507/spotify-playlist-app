import streamlit as st
import pandas as pd

st.title("🎶 Clustered Spotify Playlist Explorer")
st.markdown("Select a cluster to explore your personalized playlist!")

playlist_files = {
    "Cluster 0": "Playlist_0.csv",
    "Cluster 1": "Playlist_1.csv",
    "Cluster 2": "Playlist_2.csv",
    "Cluster 3": "Playlist_3.csv"
}

selected_label = st.selectbox("Choose a cluster", list(playlist_files.keys()))
selected_file = playlist_files[selected_label]
df = pd.read_csv(selected_file)

st.subheader("Playlist Stats")
st.write(f"**Number of Tracks:** {len(df)}")
if 'duration_ms' in df.columns:
    st.write(f"**Average Duration (sec):** {df['duration_ms'].mean() / 1000:.2f}")
if 'popularity' in df.columns:
    st.write(f"**Average Popularity:** {df['popularity'].mean():.2f}")

st.subheader("Tracks in Playlist")
for _, row in df.iterrows():
    st.markdown(f"**{row['track_name']}** by *{row['artist']}*")
    st.caption(f"Album: {row['album']}")

st.download_button("Download This Playlist", df.to_csv(index=False), file_name=selected_file)