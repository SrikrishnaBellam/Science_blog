from django.db import models
from django.contrib.auth.models import User
from django.db.models import CheckConstraint

STATUS =(
    (0,"Draft"),
    (1,"Publish")
)


class Post(models.Model):
    Primary_key = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices = STATUS, default = 0)
    
    class Meta:
        ordering = ['-created_on']
        
    def __str__(self):
        return self.title


class steps(models.Model):
    step_number = models.IntegerField()
    image = models.ImageField(upload_to="images/")
    step_desc = models.TextField()
    exp_step = models.ForeignKey(Post, on_delete=models.CASCADE )
    
    
class mat_and_content(models.Model):
    Material = models.TextField()
    Quantity = models.IntegerField()
    Mat_and_cont_Key = models.ForeignKey(Post, on_delete=models.CASCADE )
    class Meta:
        constraints = [
            CheckConstraint(check=models.Q(Quantity__gte=0), name='non_negative')
        ]
    