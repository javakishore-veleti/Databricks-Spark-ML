import tweepy
from tweepy.auth import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json
import os


def initialize_twitter_api_access_token() -> dict:
    return {
        "consumer_key": os.getenv("TWITTER_API_CONSUMER_KEY", "undefined_consumer_key"),
        "consumer_secret": os.getenv("TWITTER_API_CONSUMER_SECRET", "undefined_consumer_secret"),
        "access_token": os.getenv("TWITTER_API_ACCESS_TOKEN", "undefined_access_token"),
        "access_secret": os.getenv("TWITTER_API_ACCESS_SECRET", "undefined_access_secret"),
    }
