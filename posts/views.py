from django.shortcuts import render

import json
import requests

# POSTS VIEW ENDPOINT
def posts(request): 
    api_request=requests.get("https://jsonplaceholder.typicode.com/posts")
    try:
        api=json.loads(api_request.content)
    except Exception as e:
        api= "error"
    return render(request, 'blog-listing.html',{'api':api})


# POST DETAILS VIEW ENDPOINT
def post_details(request,id):
    api_request=requests.get(f"https://jsonplaceholder.typicode.com/posts/{id}")
    comments=requests.get(f"https://jsonplaceholder.typicode.com/posts/{id}/comments")
    try:
        api=json.loads(api_request.content)
        comment=json.loads(comments.content)
    except Exception as e:
        api= "error"
        comment= "error"
    return render(request, 'blog-post.html',{'api':api,'comment':comment})