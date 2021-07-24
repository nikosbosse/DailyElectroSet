from create_api import create_api
from randomset import randomset
import tempfile

def post_tweet(event="", context=""):
    api = create_api()
    dailyset = randomset()
    dailyset.get_random_set()
    dailyset.download_title()
    filename = tempfile.NamedTemporaryFile()
    #dailyset.download_title_image(filename.name)

    tweet = dailyset.write_tweet()
    try:
        #api.update_with_media(filename.name, status=tweet)
        api.update_status(status=tweet)
    except Exception as e:
        raise e

post_tweet()