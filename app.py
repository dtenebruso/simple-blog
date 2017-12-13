from database import Database
from models.post import Post

__author__ = 'pr0c'

Database.initialize()

post = Post(blog_id="123",
            title="Another Post",
            content="Some Content",
            author="pr0c")

post.save_to_mongo()

post2 = Post(blog_id="123",
             title="Gamify Your Life",
             content="This week on lifeWire we're discussing how to Gamify your life\n")