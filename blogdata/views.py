from django.shortcuts import render
from django.views import View
from .form import Blog

from blog.models import AddUser, Addblog


class BlogAdd(View):

    def get(self, request):
        return render(request, 'blogform.html')
    
    def post(self, request):

        form = Blog(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data['title']
            post = form.cleaned_data['post']
            category = form.cleaned_data['category']
            email = request.session['email']
            file = form.cleaned_data['file']

            obj = AddUser.objects.get(email=email)

            Addblog.objects.create(title=title, post=post, category=category, author=obj, file=file)

            msg = "Blog Uploaded Successfully"
            return render(request, 'blogform.html', {'msg':msg})
        
        else:
            msg = "Invalid Form"
            return render(request, 'blogform.html', {'msg':msg})


def allblog(request):
    objs = Addblog.objects.all()
    
    return render(request, 'blog.html', {'objs':objs})


def myblog(request):
    email = request.session['email']
    obj = AddUser.objects.get(email=email)
    data = Addblog.objects.filter(author=obj)

    return render(request, 'blog.html', {'objs':data})
            

