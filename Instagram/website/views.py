from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import FormMixin
from .models import Post, Follows, Comments, Likes, Profile, User
from django.http import JsonResponse, HttpResponseRedirect 
import json
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import (
    CommentForm
)

# Create your views here.

@login_required(login_url='login')
def home(request):
    
    following = Follows.objects.get(follower=request.user)
    following = following.following
    post = Post.objects.filter(userPosted=following)
    like = Likes.objects
    context = {
        'page_name': 'Instagram', # default
        'posts': post,
        'likes': like,
    }
    return render(request,'index.html',context)


class ProfileView(DetailView):
    model = Profile
    template_name = "profile.html"

class ProfileEditView(DetailView):
    model = Profile
    template_name = "edit-profile.html"

    def post(self,request, *args, **kwargs):
        user = User.objects.get(username=request.user.username)
        profile = Profile.objects.get(user=request.user)
        first_name = request.POST['first-name']
        second_name = request.POST['second-name']
        bio = request.POST['biography']
        username = request.POST['user-name']

        profile.biography = bio
        profile.save()

        usernames = User.objects.values_list('username')
        users = []
        for i in range(len(usernames)):
            users.append(usernames[i][0])
        if username in users:
            user.first_name = first_name
            user.last_name = second_name
            user.save()
        else:

            user.first_name = first_name
            user.last_name = second_name
            user.username = username
            user.save()

        url = '/profile/'+profile.slug
            
        return redirect(url)
    

@login_required(login_url='login')
def explore(request):
    context = {
        'page_name': 'Explore',
    }
    return render(request, 'explore.html', context)

@login_required(login_url='login')
def activity(request):
    context = {
        'page_name': 'activity',
    }
    return render(request, 'activity.html', context)

@login_required(login_url='login')
def comments(request):
    context = {
        'page_name': 'Comments',
    }
    return render(request, 'comments.html', context)

class ImageView(FormMixin, DetailView):
    model = Post
    template_name = 'single-image-page.html'
    form_class = CommentForm
    success_url = '/'
    
    def post(self,request, *args, **kwargs):
        user = request.user
        message = request.POST['message']
        postID = request.POST['postID']
        post = Post.objects.get(postID=postID)
        print('\n\nhello ',post,'\n\n')
        commented = Comments.objects.create(
            commentedOn=post,
            comment=message,
            commentBy=user
        )
        print('\nsuccess\n')
        return redirect('/')

    '''
    def post(self, request, *args, **kwargs):

        # user = request.user
        # message = request.POST['message']
        # image = model.postID
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(ParticularPost, self).form_valid(form)

    '''
    

@login_required(login_url='login')
def lists(request):
    if request.method == 'POST':
        search = request.POST['search']
        search_results = User.objects.filter(username__contains=search)

        context = {
            'list': search_results,

        }
    else:
        context = {}
    return render(request, 'lists.html', context)

@login_required(login_url='login')
def single(request):
    context = {
        'page_name': 'username',
    }
    return render(request, 'single-image-page.html', context)


def login_logic(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':

        context = {
                'message': 'hello',
            }


        userName = request.POST['username']
        PassWord = request.POST['password']
        user = authenticate(request, username=userName, password=PassWord)
        

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/login/')

    else:
        return render(request, 'login.html')
    


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    context = {}
    return render(request, 'login.html', context)
    
    

@login_required(login_url='login')
def updateLike(request):

    if request.method == "POST":
        data = json.loads(request.body)
        postId = data['postID']

        user = request.user  #change to get user
        post = Post.objects.get(postID=postId)

        like, create = Likes.objects.get_or_create(onPost=post, user=user)

        if create:
            like.save()

        else:
            like.delete()

        

        return JsonResponse(data, safe=False)

    
    else:
        return JsonResponse('error', safe=False)
    

@login_required(login_url='login')
def updateFollow(request):
    if request.method == "POST":
        data = json.loads(request.body)
        followee = data['Followee'] # being followed
        follower = request.user # doing the following

        followeeID = User.objects.get(username=followee)

        follow, create = Follows.objects.get_or_create(follower=follower, following=followeeID)

        if create:
            follow.save()
        else:
            follow.delete()
        return JsonResponse(data, safe=False)
    
    else:
        return JsonResponse('error', safe=False)

'''
# comment and delete comment

def comment(request, slug):
    user = 
    post = 

    if NEW_COMMENT:
        comment = 
        # add to model
    else REMOVE_COMMENT:
        commentNumber = 
        # remove from model
    return # do nothing



# space for new function
'''