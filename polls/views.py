from django.http import HttpResponse
from django.shortcuts import render

from polls.forms import BlogForm
from polls.models import Blog


# Create your views here.
def blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            return render(request, "blog.html", {"title": title, "content": content})
    else:
        form = BlogForm()
        return render(request, "blog1.html", {"form": form})
