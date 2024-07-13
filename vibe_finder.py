import streamlit as st
import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import base64
from datetime import datetime
import csvReader  # Import the custom CSV reader

# Initialize Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id='db38a7c36dca4c9fb354f6daf9be019a', client_secret='0e64f105beb84d8db19ad4672eca99e3')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Initialize session state variables
if 'page' not in st.session_state:
    st.session_state.page = 0
if 'selected_keywords' not in st.session_state:
    st.session_state.selected_keywords = []

# Define keyword options
keyword_options = [
    ["Light", "Dark", "Neutral"],
    ["Sprint", "Stroll", "Nostalgic"],
    ["Nostalgia", "Nature", "City"],
    ["Foreign", "Comfortable", "Discover"],
    ["Dreamy", "Flirty", "Lonely"]
]

# Define background images for all pages
background_images = [
    f"assets/images/page{i}_background.jpg"
    for i in range(6)  # 0 to 5
]

# Add the results page background
results_background = "assets/images/results_background.jpg"

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

def next_page():
    st.session_state.page += 1

def select_keyword(keyword):
    st.session_state.selected_keywords.append(keyword)
    next_page()

def reset():
    st.session_state.page = 0
    st.session_state.selected_keywords = []

def get_spotify_recommendations(keywords):
    seed_genres = [keyword.lower() for keyword in keywords if keyword.lower() in sp.recommendation_genre_seeds()]
    if not seed_genres:
        seed_genres = ['pop']
    results = sp.recommendations(seed_genres=seed_genres, limit=5)
    return [track['name'] + ' - ' + track['artists'][0]['name'] for track in results['tracks']]

def save_to_csv(keywords, recommendations):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('vibe_finder_data.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csvReader.writer(file)  # Using custom CSV writer
        writer.writerow([timestamp] + keywords + recommendations)

def main():
    # Set background image
    if 0 <= st.session_state.page <= 5:
        set_png_as_page_bg(background_images[st.session_state.page])
    else:
        set_png_as_page_bg(results_background)  # Use the new results background

    st.title("Vibe Finder")

    if st.session_state.page == 0:
        st.write("Welcome to Vibe Finder! Click the button below to start your journey.")
        if st.button("Find Your Vibe"):
            next_page()
    elif 1 <= st.session_state.page <= 5:
        st.write(f"Step {st.session_state.page} of 5")
        st.write("Choose a keyword that resonates with you:")
        for keyword in keyword_options[st.session_state.page - 1]:
            if st.button(keyword):
                select_keyword(keyword)
    else:
        st.write("Here are your selected vibes:")
        st.write(", ".join(st.session_state.selected_keywords))

        st.write("Based on your choices, we recommend:")
        recommendations = get_spotify_recommendations(st.session_state.selected_keywords)
        for song in recommendations:
            st.write(f"- {song}")

        # Save the data to CSV
        save_to_csv(st.session_state.selected_keywords, recommendations)

        if st.button("Start Over"):
            reset()

if __name__ == "__main__":
    main()
