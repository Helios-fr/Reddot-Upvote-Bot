import praw

reddit = praw.Reddit(
    client_id='2mKgUn1q9GgjJYXwQ19v_A',
    client_secret='zl225Z7pdRFK43749vz2iaVwNAXvXg',
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
    username='177954',
    password='4P."f7ybqKrStjE'
)

post = reddit.submission(id='14hazbi')

post.upvote()

