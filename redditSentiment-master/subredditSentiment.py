import praw
from textblob import TextBlob
import math


reddit = praw.Reddit(client_id='CdD87eBK0UUwdg',
                     client_secret='N0toFnW5SeXfLSW3DuuhPVMLW94',
                     user_agent='subSentiment')

# opens file with subreddit names
with open('sb.txt') as f:

    for line in f:
        subreddit = reddit.subreddit(line.strip())
        # write web agent to get converter for datetime to epoch on a daily basis for updates
        day_start = 1548979200
        day_end = 1550188800
		
		#sub_submissions = subreddit.submissions(day_start, day_end)
		
        sub_sentiment = 0
        num_comments = 0

        for submission in subreddit.hot(limit=100):
            if not submission.stickied:
                submission.comments.replace_more(limit=0)
                for comment in submission.comments.list():
                        blob = TextBlob(comment.body)

                        #adds comment sentiment to overall sentiment for subreddit
                        comment_sentiment = blob.sentiment.polarity
                        sub_sentiment += comment_sentiment
                        num_comments += 1
		
                        #prints comment and polarity
                        #print(str(comment.body.encode('utf-8')) + ': ' + str(blob.sentiment.polarity))

        print('/r/' + str(subreddit.display_name))
        try:
            print('Ratio: ' + str(math.floor(sub_sentiment/num_comments*100)) + '\n')
        except:
            print('No comment sentiment.' + '\n')
            ZeroDivisionError

# add key:value subredditname:sentiment to dict
# order dictionary by sentiment value
# output dictionary key + ' sentiment: ' + sentiment value


