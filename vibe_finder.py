import streamlit as st
import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import base64
import os

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
    ["Energetic", "Calm", "Mysterious"],
    ["Happy", "Sad", "Nostalgic"],
    ["Romantic", "Angry", "Peaceful"],
    ["Epic", "Intimate", "Quirky"],
    ["Uplifting", "Melancholic", "Intense"]
]

# Define background image for home page
home_background = os.path.join("assets", "images", "home_background.jpg")

# Define background videos for keyword pages
background_videos = [
    os.path.join("assets", "videos", f"page{i}_background.mp4")
    for i in range(1, 6)
]

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

def set_mp4_as_page_bg(mp4_file):
    video_html = """
    <style>
    #myVideo {
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100%;
        min-height: 100%;
        object-fit: cover;
    }
    .content {
        position: relative;
        z-index: 10;
    }
    </style>
    <video autoplay muted loop id="myVideo">
        <source src="%s" type="video/mp4">
    </video>
    """ % mp4_file
    st.markdown(video_html, unsafe_allow_html=True)
    st.markdown('<div class="content">', unsafe_allow_html=True)

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

def main():
    if st.session_state.page == 0:
        set_png_as_page_bg(home_background)
    elif 1 <= st.session_state.page <= 5:
        set_mp4_as_page_bg(background_videos[st.session_state.page - 1])
    else:
        # For the results page, you can either use a static image or one of the videos
        set_png_as_page_bg(home_background)  # or use any other background

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
        
        if st.button("Start Over"):
            reset()

    # Close the content div if using video background
    if 1 <= st.session_state.page <= 5:
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()