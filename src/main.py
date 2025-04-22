from reddit_client import RedditClient
from caption_generator import CaptionGenerator
from instagram_client import InstagramClient

def main():
    # Initialize clients
    reddit = RedditClient()
    caption_gen = CaptionGenerator()
    instagram = InstagramClient()
    
    # Get meme and generate caption
    title, url = reddit.get_meme()
    if title and url:
        print("🖼️ Title:", title)
        caption = caption_gen.generate_caption(title)
        print("💬 Caption:", caption)
        
        # Download and upload
        image_path = instagram.download_image(url)
        instagram.upload_post(image_path, caption)
    else:
        print("No suitable meme found.")

if __name__ == "__main__":
    main() 