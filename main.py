from random import randrange
from typing import Optional
from fastapi import FastAPI, Response,status
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

my_posts = []
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
    else:
        return {}

@app.get('/')
def root():
    return {"message": "Hello World! From Dexter"}

@app.get('/posts')
def get_posts():
    return {"data": my_posts}

@app.post('/posts')
def create_posts(post: Post):
    post_dict  = post.dict()
    post_dict['id'] = randrange(0,100000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if post:
        return {"post_detail": f"Here is the data : {post}"}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"post_detail": None}

# title str, content str, category, Bool published