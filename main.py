from create_api import create_api
from randomset import randomset

def post_tweet(event="", context=""):
    api = create_api()
    dailyset = randomset()
    dailyset.get_random_set()
    tweet = dailyset.write_tweet()
    try:
        api.update_status(status=tweet)
    except Exception as e:
        raise e

post_tweet()