from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Todo(models.Model):
    status_choices= [
    ('C', 'Completed'),
    ('P', 'Pending'),
    ]
    priority_choices= [
    ('1', '1️⃣First Priority'),
    ('2', '2️⃣Less than first prority'),
    ('3', '3️⃣urgent'),
    ('4', '4️⃣not urgent but do'),
    ('5', '5️⃣ Last priority'),
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    status=models.CharField(max_length=1,choices=status_choices)
    date=models.DateTimeField(auto_now_add=True)
    priority=models.CharField(max_length=1,choices=priority_choices)

