from django.db import models
from apps.login_reg_app.models import User

class Message(models.Model):
    user = models.ForeignKey(User, related_name="messages", on_delete=models.PROTECT)
    message = models.TextField(default="message*")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    message = models.ForeignKey(Message, related_name="comments", on_delete=models.PROTECT)
    user = models.ForeignKey(User, related_name="comment", on_delete=models.PROTECT)
    comment = models.TextField(default="comment*")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
