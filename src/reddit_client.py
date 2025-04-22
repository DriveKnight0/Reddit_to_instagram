import os
import praw
from dotenv import load_dotenv

load_dotenv()

class RedditClient:
    def __init__(self):
        self.client = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            username=os.getenv("REDDIT_USERNAME"),
            password=os.getenv("REDDIT_PASSWORD"),
            user_agent="reddit-to-instagram-bot"
        )

    def get_meme(self):
        """Fetch a meme from Reddit"""
        subreddit = self.client.subreddit("memes+darkmemes+brainrot")
        for post in subreddit.hot(limit=15):
            if post.url.endswith((".jpg", ".jpeg", ".png")):
                return post.title, post.url
        return None, None 