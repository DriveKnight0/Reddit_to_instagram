import os
import requests
from instagrapi import Client
from dotenv import load_dotenv

load_dotenv()

class InstagramClient:
    def __init__(self):
        self.client = Client()

    def download_image(self, url, filename="meme.jpg"):
        """Download image from URL"""
        img_data = requests.get(url).content
        with open(filename, 'wb') as f:
            f.write(img_data)
        return filename

    def upload_post(self, image_path, caption):
        """Upload image to Instagram"""
        try:
            self.client.login(
                os.getenv("INSTAGRAM_USERNAME"),
                os.getenv("INSTAGRAM_PASSWORD")
            )
            print("✅ Logged in successfully.")
        except Exception as e:
            print("⚠️ Login failed:", e)
            return

        try:
            self.client.photo_upload(image_path, caption)
            print("✅ Meme posted successfully!")
        except Exception as e:
            print("⚠️ Upload failed:", e) 