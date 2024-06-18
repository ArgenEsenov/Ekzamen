from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    nickname = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images')
    website = models.URLField()
    followers = models.IntegerField()

    def __str__(self):
        return f'{self.user} {self.bio}'


class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='following')
    created_at = models.DateTimeField()

    def __str__(self):
        return f'{self.followerUp} {self.followingUP}'


class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_post')
    image = models.ImageField(null=True, blank=True)
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField()
    hashtag = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.user} {self.hashtag}'


class PostLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_post_like')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} {self.post}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='user_comment')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField()

    def __str__(self):
        return f'{self.user} {self.post}'


class CommentLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_comment_like')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} {self.comment}'


class Story(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_story')
    image = models.ImageField(null=True, blank=True)
    video = models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return f'{self.user} {self.created_at}'


class Group(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='creator')
    members = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='members')
    join_key = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name} {self.description}'
