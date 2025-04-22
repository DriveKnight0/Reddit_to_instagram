import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class CaptionGenerator:
    def __init__(self):
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel("gemini-2.0-flash")

    def generate_caption(self, meme_title):
        """Generate a caption using Google's Gemini AI"""
        prompt = f"Write a short and funny Instagram caption for a meme titled: '{meme_title}'. Only give me one caption, no explanations."
        response = self.model.generate_content(prompt)
        return response.text.strip().split('\n')[0] 