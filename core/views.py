from django.shortcuts import render

posts = [
    {
        "author": "Pawel",
        "title": "First Blog Post",
        "content": "First Post Content",
        "date_posted": "7 May, 2025",
    },
    {
        "author": "Mod",
        "title": "Second Blog Post",
        "content": "Second Post Content",
        "date_posted": "8 May, 2025",
    },
]


def home(request):
    context = {
        "posts": posts,
    }
    return render(request, "core/home.html", context)


def about(request):
    return render(request, "core/about.html")
