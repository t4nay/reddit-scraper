import requests
import json
import re
import time
import pprint
from addict import Dict
import random
import pathlib
import string
import uuid



data = requests.get("https://api.pushshift.io/reddit/search/submission/?subreddit=<subreddit>&sort=desc&size=1000")
ad = Dict(data.json())
binary = data.content
output = json.loads(binary)
points = 0
data = output['data']
for selftext in output['data']:
        randomstr = str(uuid.uuid4());
        filename = randomstr + ".txt"
        news = output['data'][points]['selftext']
        title = output['data'][points]['title']
        points = points + 1
        with open(filename, "w") as text_file:
            text_file.write(" %s \n %s" % (title, news))
