from database import Database
from models.blog import Blog
#from models.post import Post

__author__ = 'pr0c'

Database.initialize()

blog = Blog(author="pr0c",
            title="Sample",
            description="Sample description")

blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

print(blog.get_posts())