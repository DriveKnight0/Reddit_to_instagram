import os
import praw
import requests
import google.generativeai as genai
from instagrapi import Client

# Reddit API credentials
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password

# Google AI credentialssk
GOOGLE_API_KEY=your_google_api_key

# Instagram credentials
INSTAGRAM_USERNAME=your_instagram_username
INSTAGRAM_PASSWORD=your_instagram_password 

def setup_reddit():
    """Initialize Reddit API client"""
    return praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        username=REDDIT_USERNAME,
        password=REDDIT_PASSWORD,
        user_agent="reddit-to-instagram-bot"
    )

def get_meme(reddit):
    """Fetch a meme from Reddit"""
    subreddit = reddit.subreddit("memes+darkmemes+brainrot")
    for post in subreddit.hot(limit=15):
        if post.url.endswith((".jpg", ".jpeg", ".png")):
            return post.title, post.url
    return None, None

def generate_caption(meme_title):
    """Generate a caption using Google's Gemini AI"""
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = f"Write a short and funny Instagram caption for a meme titled: '{meme_title}'. Only give me one caption, no explanations."
    response = model.generate_content(prompt)
    return response.text.strip().split('\n')[0]

def download_image(url, filename="meme.jpg"):
    """Download image from URL"""
    img_data = requests.get(url).content
    with open(filename, 'wb') as f:
        f.write(img_data)
    return filename

def upload_to_instagram(image_path, caption):
    """Upload image to Instagram"""
    cl = Client()
    try:
        cl.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
        print("✅ Logged in successfully.")
    except Exception as e:
        print("⚠️ Login failed:", e)
        return

    try:
        cl.photo_upload(image_path, caption)
        print("✅ Meme posted successfully!")
    except Exception as e:
        print("⚠️ Upload failed:", e)

def main():
    # Initialize Reddit client
    reddit = setup_reddit()
    
    # Get meme and generate caption
    title, url = get_meme(reddit)
    if title and url:
        print("🖼️ Title:", title)
        caption = generate_caption(title)
        print("💬 Caption:", caption)
        
        # Download and upload
        image_path = download_image(url)
        upload_to_instagram(image_path, caption)
    else:
        print("No suitable meme found.")

if __name__ == "__main__":
    main() 
