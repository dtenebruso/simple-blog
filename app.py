from database import Database
from models.post import Post

__author__ = 'pr0c'

Database.initialize()

blog = Blog(author="pr0c",
            title="Sample",
            description="Sample description")

blog.new_post()

blog.save_to_mongo()

Blog.from_mongo()

blog.get_post() # == Post.from_blog(id)