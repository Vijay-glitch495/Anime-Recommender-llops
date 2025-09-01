import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="🎌 Anime Recommender",
    layout="wide",
    page_icon="🌸"
)

# Initialize pipeline
@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

# Header
st.markdown(
    """
    <h1 style='text-align:center; background: linear-gradient(to right, #FF4B4B, #FF8C42, #6C63FF);
    -webkit-background-clip: text; color: transparent; font-size:50px;'>🎌 Anime Recommender 🌸</h1>
    <p style='text-align:center; color:#FF69B4; font-size:18px;'>Find your perfect anime based on your mood, favorites, and genres! ✨🎥</p>
    """,
    unsafe_allow_html=True
)

# Sidebar
with st.sidebar:
    st.markdown("### 🐱 Anime Mood Selector")
    mood = st.selectbox(
        "Choose a mood:", 
        ["Exciting 🎢", "Relaxing 😌", "Romantic 💖", "Funny 😂", "Thrilling 🔥"]
    )
    st.markdown(f"<p style='color:#FF69B4;'>You selected: **{mood}**</p>", unsafe_allow_html=True)

# CSS to pin input at the bottom
st.markdown(
    """
    <style>
    .chat-input {
        position: fixed;
        bottom: 20px;
        left: 20%;
        width: 60%;
        z-index: 100;
        background-color: #0e1117;
        padding: 10px;
        border-radius: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Placeholder for recommendations above input
output_placeholder = st.container()

# Input pinned at bottom
with st.container():
    st.markdown("<div class='chat-input'>", unsafe_allow_html=True)
    query = st.text_input("", placeholder="Type your message here...")
    st.markdown("</div>", unsafe_allow_html=True)

# Recommendations
if query:
    with output_placeholder:
        with st.spinner("Fetching recommendations for you... ⏳"):
            try:
                response = pipeline.recommend(query)
                st.success("✅ Recommendations fetched successfully!")

                # Show recommendations as a paragraph with white text
                st.markdown("### 🌟 Recommended Anime for You:")
                paragraph_text = " ".join(response.split('\n')) + " 🎉"
                st.markdown(
                    f"<p style='color:#FFFFFF; font-size:16px;'>{paragraph_text}</p>",
                    unsafe_allow_html=True
                )

            except Exception as e:
                st.error(f"❌ Failed to fetch recommendations: {e}")

# Footer
st.markdown("---")
st.markdown(
    """
    <p style='text-align:center; background: linear-gradient(to right, #FF8C42, #FF4B4B, #6C63FF); 
    -webkit-background-clip: text; color: transparent; font-size:16px;'>Made with ❤️ using <b>LangChain & Streamlit</b> 🌸</p>
    """,
    unsafe_allow_html=True
)

# Feedback at the very bottom
st.markdown(
    """
    <p style='text-align:center;'>💌 Feedback?</p>
    <p style='text-align:center;'><a href="mailto:bvkreddy543@gmail.com?subject=Anime Recommender Feedback" 
    style='color:#FF4500;'>Send feedback via Email ✉️</a></p>
    """,
    unsafe_allow_html=True
)

#streamlit run app/app.py
#streamlit run app/app.py --server.port 8000
#streamlit run app/app.py --server.address 0.0.0.0 --server.port 8501

