# DNS-Libcomp

Vibe Finder

Welcome to Vibe Finder! Our website helps users who may have trouble choosing songs at karaoke by allowing them to select from a list of keywords that resonate with their current mood and vibe. Based on these selections, Vibe Finder generates a list of song recommendations to enhance your karaoke experience.

Features
Mood-Based Song Recommendations: Choose keywords that match your current mood and vibe to get a list of curated song recommendations.
Spotify Integration: Powered by the Spotify API to provide a vast selection of songs.
User-Friendly Interface: Easy-to-navigate UI/UX to ensure a seamless user experience.
Project Structure
General Framework and Structure

Idea and UI/UX Design
Chloe planned out the idea and concepts of the karaoke recommendation system. She managed and created the UI/UX, thinking through all the functions that the website offers to ensure an intuitive and engaging user experience.

Felicia took care of the main general framework and the overall structure of our project, ensuring a solid foundation for development.

Back-End Development
Han and Stella developed the back-end algorithms behind the recommendation system. They also implemented the Spotify API to fetch and recommend songs.


Installation
To run Vibe Finder locally, follow these steps:

Clone the repository:
git clone https://github.com/your-username/vibe_finder.git
Navigate to the project directory:
cd vibe_finder

Activate Venv:
myenv\Scripts\activate

Install the necessary dependencies:
npm install

Set up your environment variables for the Spotify API (create a .env file in the root directory and add your Spotify API credentials):

SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret

Run the development server:
python -m streamlit run vibe_finder.py

Usage
Open your web browser and navigate to http://localhost:3000.
Select keywords that match your current mood and vibe.
Browse the generated list of song recommendations.
Enjoy your karaoke session with perfectly matched songs!
Contributing
We welcome contributions to Vibe Finder! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgements
Special thanks to all team members for their contributions:

Felicia: Main framework and project structure.

Han and Stella: Back-end algorithms and Spotify API integration.

Chloe: Idea planning, UI/UX design, and functionality planning.

