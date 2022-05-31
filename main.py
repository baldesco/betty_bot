from datetime import datetime as dt
import os
import tweepy
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())

API_KEY = os.getenv("api_key")
API_SECRET_KEY = os.getenv("api_secret_key")
ACCESS_TOKEN = os.getenv("access_token")
ACCESS_TOKEN_SECRET = os.getenv("access_token_secret")

auth = tweepy.OAuth1UserHandler(
    API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


video_path = 'nomina.mp4'

if dt.today().weekday() in (0, 1, 2):
    upload_result = api.media_upload(video_path)
    api.update_status(status="", media_ids=[
        upload_result.media_id_string])
