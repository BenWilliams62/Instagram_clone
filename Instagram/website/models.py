from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
import datetime

# choice lists



class Profile(models.Model):
    user = models.OneToOneField(User, null=False, on_delete = models.CASCADE, primary_key=True)
    biography = models.CharField(max_length=200, null=True, blank=True)
    pic = models.ImageField(upload_to='pp/',null=True, blank=True)
    slug = models.SlugField(unique=True, editable=True, null=True, default='')
    

    def get_absolute_url(self):
        return reverse("profile", kwargs={
            'slug': self.slug
        })
    
    def get_edit_url(self):
        return reverse("profile-edit", kwargs={
            'slug': self.slug
        })
    
    def save(self, **kwargs):
        slug_str = str(self.user)
        self.slug = slugify(slug_str)
        super(Profile, self).save(**kwargs)

    def profile_pics(self):
        posts = Post.objects.filter(userPosted=self.user)
        return posts
    
    def following(self):
        following = Follows.objects.filter(follower=self.user)
        return following
    
    def followers(self):
        followers = Follows.objects.filter(following=self.user)
        return followers


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()



class Post(models.Model):
    postID = models.AutoField(primary_key = True)
    image = models.ImageField(upload_to='images/', null=False, blank=False)
    userPosted = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    caption = models.CharField(max_length=200, null=False, blank=True)
    timePosted = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(editable=False, null=True, default='')

    class Meta:
        ordering = ['-timePosted']

    def save(self, **kwargs):
        slug_user_str = str(self.userPosted)
        slug_year_str = str(datetime.datetime.now().strftime("%Y"))
        slug_month_str = str(datetime.datetime.now().strftime("%m"))
        slug_day_str = str(datetime.datetime.now().strftime("%d"))
        slug_hour_str = str(datetime.datetime.now().strftime("%H"))
        slug_minute_str = str(datetime.datetime.now().strftime("%M"))
        slug_second_str = str(datetime.datetime.now().strftime("%S"))
        slug_str = slug_user_str + '-' + slug_year_str+slug_month_str+slug_day_str+slug_hour_str+slug_minute_str+slug_second_str
        self.slug = slugify(slug_str)
        super(Post, self).save(**kwargs)

    def get_absolute_url(self):
        return reverse("image", kwargs={
            'slug': self.slug
        })

    def __str__(self):
        return str(self.postID)

    def get_likes(self):
        likes = Likes.objects.filter(onPost=self.postID)
        return likes
    
    def get_comments(self):
        comments = Comments.objects.filter(commentedOn=self.postID)
        return comments

    def upload_time(self):
        now = datetime.datetime.now()
        year_now = now.strftime('%Y')
        month_now = now.strftime('%m')
        day_now = now.strftime('%d')
        hour_now = now.strftime('%H')
        minute_now = now.strftime('%M')
        second_now = now.strftime('%S')

        then = self.timePosted
        year_then = then.strftime('%Y')
        month_then = then.strftime('%m')
        day_then = then.strftime('%d')
        hour_then = then.strftime('%H')
        minute_then = then.strftime('%M')
        second_then = then.strftime('%S')

        

        years = int(year_now) - int(year_then)
        months = int(month_now) - int(month_then)
        days = int(day_now) - int(day_then)
        hours = int(hour_now) - int(hour_then)
        minutes = int(minute_now) - int(minute_then)
        seconds = int(second_now) - int(second_then)
  

        if years == 0:
            if months == 0:
                if days == 0:
                    if hours == 0:
                        if minutes == 0:
                            if seconds <= 5:
                                return 'just now'
                            elif 5 < seconds < 30:
                                return 'a few seconds ago'
                            else:
                                return 'less than a minute ago'
                        elif minutes == 1:
                            return 'a minutes ago'
                        elif 1 < minutes <=2 :
                            return '2 minutes ago'
                        elif 2 < minutes <=3:
                            return '3 minutes ago'
                        elif 3 < minutes <= 4:
                            return '4 minutes ago'
                        elif 4 < minutes <= 5:
                            return '5 minutes ago'
                        elif 5 < minutes < 30:
                            return 'a few minutes ago'
                        else:
                            return 'less than an hour ago'
                    elif hours == 1:
                        return 'an hour ago'
                    else:
                        return str(hours) + ' hours ago'
                elif days == 1:
                    return 'a day ago'
                else:
                    return str(days) + ' days ago'
            elif months == 1:
                return 'a month ago'
            else:
                return str(months) + ' months ago'
        elif years == 1:
            return 'a year ago'
        
        else:
            return str(years) + ' years ago'


     


class Likes(models.Model):
    likeID = models.AutoField(primary_key=True)
    onPost = models.ForeignKey(Post, on_delete=models.CASCADE, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return str(self.user)


class Follows(models.Model):
    followNumber = models.AutoField(primary_key=True)
    follower = models.ForeignKey(User, related_name="follower", on_delete=models.CASCADE, null=False, blank=False) # person who is following
    following = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE, null=False, blank=False) # person being followed

    def __str__(self):
        return str(self.follower)

class Comments(models.Model):
    commentedOn = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False)
    commentNumber = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=250, null=False)
    commentBy = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False,default='')
    timeCommented = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timeCommented']

    def __str__(self):
        return str(self.commentNumber)


