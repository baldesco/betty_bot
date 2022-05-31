import calendar
import os
import tweepy
from datetime import datetime as dt
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())

# Define constants
API_KEY = os.getenv("api_key")
API_SECRET_KEY = os.getenv("api_secret_key")
ACCESS_TOKEN = os.getenv("access_token")
ACCESS_TOKEN_SECRET = os.getenv("access_token_secret")
VIDEO_PATH = 'nomina.mp4'

# Authentication in Twitter API
auth = tweepy.OAuth1UserHandler(
    API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# Aux function to determine if today is a pay day


def is_payday():
    today = dt.today()
    t_day = today.day
    t_weekday = today.weekday()
    month_end = calendar.monthrange(today.year, today.month)[1]
    # Condition to determine of it is mid-month pay day
    cond_mid_month = (t_day == 15 and t_weekday not in [5, 6]) or (
        t_day in (13, 14) and t_weekday == 4)
    # Condition to determine of it is end-of-month pay day
    cond_end_month = (t_day == month_end and t_weekday not in [5, 6]) or (
        t_day in (month_end - 1, month_end - 2) and t_weekday == 4)
    # Check combined conditions and return
    return cond_mid_month or cond_end_month


if is_payday():
    upload_result = api.media_upload(VIDEO_PATH)
    api.update_status(status="", media_ids=[
        upload_result.media_id_string])
