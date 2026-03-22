import streamlit as st
import pickle
from googleapiclient.discovery import build

# Load model
model = pickle.load(open("model.pkl", "rb"))

# YouTube API key
API_KEY = "AIzaSyD7eOyDSUk4ZSrs3Kmjud1yntEY3QXsKrQ"

youtube = build('youtube', 'v3', developerKey=API_KEY)

st.title("📺 YouTube Popularity Predictor (URL Based)")

url = st.text_input("Paste YouTube Video URL")

def get_video_id(url):
    return url.split("v=")[-1]

if st.button("Analyze"):
    try:
        video_id = get_video_id(url)

        request = youtube.videos().list(
            part="snippet,statistics",
            id=video_id
        )
        response = request.execute()

        data = response['items'][0]

        title = data['snippet']['title']
        likes = int(data['statistics'].get('likeCount', 0))
        comments = int(data['statistics'].get('commentCount', 0))
        views = int(data['statistics'].get('viewCount', 0))

        title_length = len(title)

        st.write(f"🎬 Title: {title}")
        st.write(f"👍 Likes: {likes}")
        st.write(f"💬 Comments: {comments}")
        st.write(f"👁️ Current Views: {views}")

        # Prediction
        prediction = model.predict([[likes, comments, title_length]])

        st.success(f"🔥 Predicted Views: {int(prediction[0])}")

    except:
        st.error("Invalid URL or API issue")