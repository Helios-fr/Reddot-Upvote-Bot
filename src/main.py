import praw

# id = KEKQZGzx776gn9JhwTfBtw
# secret = 	tMBzrgwQHg7XEegMBFXnqpx0h5jAGQ

# Create a Reddit instance
reddit = praw.Reddit(
    client_id='KEKQZGzx776gn9JhwTfBtw',
    client_secret='tMBzrgwQHg7XEegMBFXnqpx0h5jAGQ',
    user_agent='testscript by /u/fakebot3',
    username='177954',
    password='4P."f7ybqKrStjE'
)

# Fetch the post to upvote
post = reddit.submission(id='14g1cwy')

# Upvote the post
post.upvote()
