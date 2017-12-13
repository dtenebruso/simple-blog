import uuid

from models.post import Post

__author__ = 'pr0c'

class Blog(object):
    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4.hex() if id is None else id

    def new_post(self):
        title = input("Enter post title: ")
        content = input("Enter post content: ")
        date = input("Enter post date, or leave blank for today (DDMMYY): ")
        post = Post(blog_id=self.id,
                    title=title,
                    content=content,
                    author=self.author,
                    date=date)

    def get_posts(self):
        pass

    def save_to_mongo(self):
        pass

    def json(self):
        pass

    def get_from_mongo(self):
        pass