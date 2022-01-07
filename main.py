import praw

reddit = praw.Reddit(
    client_id="kuSoDC6pdwCn3Jx7xlCXtg",
    client_secret="hs6JeCU0dl98BXxSN7u-enmN2vROJw",
    user_agent="my user agent",
    username="Blue_sharknado",
    password="Elfstein0.",
    check_for_async=False
)

import random
import time
def karma():
  try: 
    messages = ["Upvoted, upvote in return?", "Great post, care to share the upvotes!"]
    for submission in reddit.subreddit("FreeKarma4U+FreeKarma4You").stream.submissions():
      submission.upvote()
      rand = random.randint(0, (len(messages)-1))
      print(submission.title)
      submission.reply(messages[rand])
      time.sleep(30)
    except:
     time.sleep(300)
     karma()
  karma() 
