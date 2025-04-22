# Reddit to Instagram Bot

A Python bot that automatically fetches memes from Reddit and posts them to Instagram with AI-generated captions.

## Features

- Fetches trending memes from multiple Reddit subreddits
- Generates creative captions using Google's Gemini AI
- Automatically posts to Instagram
- Handles image downloading and formatting

## Setup

1. Clone this repository:
```bash
git clone https://github.com/yourusername/reddit-to-instagram.git
cd reddit-to-instagram
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your credentials:
```env
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password
GOOGLE_API_KEY=your_google_api_key
INSTAGRAM_USERNAME=your_instagram_username
INSTAGRAM_PASSWORD=your_instagram_password
```

4. Run the bot:
```bash
python src/main.py
```

## Requirements

- Python 3.8+
- Reddit API credentials
- Google AI API key
- Instagram account

## Project Structure

```
reddit-to-instagram/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── reddit_client.py
│   ├── instagram_client.py
│   └── caption_generator.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details. 