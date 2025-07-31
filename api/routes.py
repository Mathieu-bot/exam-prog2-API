import base64

from fastapi import APIRouter, Request, Response, HTTPException
from starlette.responses import PlainTextResponse, JSONResponse
from models.post import Post, serialized_posts, post_list, serialized_posts

router = APIRouter()

@router.get("/ping") # Q1
def get_ping():
    return PlainTextResponse(f"pong", status_code=200)

@router.get("/home") # Q2
def get_home():
    with open("templates/home.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return Response(content=html_content, status_code=200, media_type="text/html")

@router.get("/{unknown}") # Q3
def get_unknown(unknown: str):
    with open("templates/not_found.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return Response(content=html_content, status_code=200, media_type="text/html")


@router.post("/posts", status_code=201) # Q4
def post_posts(new_post: list[Post]):
    post_list.extend(new_post)
    return {"post": serialized_posts()}

@router.get("/posts") # Q5
def get_posts():
    return JSONResponse({"posts": serialized_posts()}, status_code=200)

@router.put("/posts") # Q6
def put_posts(new_posts: list[Post]):
    for new_post in new_posts:
        for i, post in enumerate(post_list):
            if post.title == new_post.title:
                post_list[i] = new_post
                break
        else:
            post_list.append(new_post)
    return JSONResponse({"posts": serialized_posts()}, status_code=200)

"""bonus"""
@router.get("/ping/auth")
def get_ping_auth(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return PlainTextResponse("No authorization header provided", status_code=401)

    if not auth_header.startswith("Basic "):
        return PlainTextResponse("Invalid authentication scheme. Use Basic Authentication", status_code=401)

    credentials_base64 = auth_header[len("Basic "):].strip()
    try:
        credentials = base64.b64decode(credentials_base64).decode("utf-8")
        username, password = credentials.split(":", 1)
    except (base64.binascii.Error, UnicodeDecodeError, ValueError):
        return PlainTextResponse("Invalid authorization credentials", status_code=401)

    expected_credentials = "user:secret"
    if credentials != expected_credentials:
        return PlainTextResponse("Invalid username or password", status_code=403)
    return PlainTextResponse("pong", status_code=200)
