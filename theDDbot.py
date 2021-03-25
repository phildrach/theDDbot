import os
import praw
import time
from datetime import date
from keep_alive import keep_alive

#Here is where I create an instance of the Reddit API and log in with my bot credentials
def main():
    reddit = praw.Reddit(
        client_id=os.getenv('client_id'),
        client_secret=os.getenv('client_secret'),
        username=os.getenv('username'),
        password=os.getenv('password'),
        user_agent="<console:theDDbot:1.0>",
    )
#Here is where I assign my target subreddit and issue replies to submissions
    keep_alive()
    subreddit = reddit.subreddit("RobinHoodPennyStocks")
    for post in subreddit.stream.submissions():
        process_post(post)

#Here is where I filter submissions by 'flair' and compose my reply comment
def process_post(post):
    if post.link_flair_text == "DD/Research" or post.link_flair_text == "Research/DD" or post.link_flair_text == "DD + Research":
        post.reply((str(post.author) + "'s account was created " + "**" + str(date.fromtimestamp(post.author.created_utc)) 
                    + "** " "\n\nThis redditor has " + "**" + str(post.author.link_karma) + "**" + " post karma" 
                    + "\n\nThis redditor has " + "**" + str(post.author.comment_karma) + "**" + " comment karma"))
        time.sleep(660)

if __name__ == "__main__":
    main()
