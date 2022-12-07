# module imports with specific functions

from django.shortcuts import render

posts = [
    {
        'author': 'Oscar Spencer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'august 27th'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'august 28th'
    }

]



def home(request):

    context = {
        'posts': posts
    }

    return render(request,'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html', {'title': 'About'})
