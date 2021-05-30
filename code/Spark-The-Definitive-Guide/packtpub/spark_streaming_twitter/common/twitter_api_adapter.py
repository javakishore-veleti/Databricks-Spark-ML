import json
import logging

from tweepy import StreamListener


class TweetsListener(StreamListener):

    def __init__(self, csocket):
        self.client_socket = csocket

    def on_data(self, raw_data):
        try:
            msg = json.loads(raw_data)
            self.client_socket.send(msg['text'].encode('utf-8'))
        except BaseException as e:
            logging.error(f"Error {e}")
        return True

    def on_error(self, status_code):
        logging.error(f"Exception occured {status_code}")
        return True
