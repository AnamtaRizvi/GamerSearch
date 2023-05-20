from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass
class profile(models.Model):                         
    role=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.role}"
class game(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"
class gamer(models.Model):
    fname=models.CharField(max_length=60,default="")
    gamingname=models.ForeignKey(User,on_delete=models.CASCADE , related_name="gamingname",null=True)
    image=models.ImageField(upload_to='images',default="")
    location=models.CharField(max_length=60)
    level=models.IntegerField(default=0)
    matches=models.IntegerField(default=0)
    win=models.IntegerField(default=0)
    kill=models.IntegerField(default=0)
    damage=models.IntegerField(default=0)
    status=models.CharField(max_length=150,default="")
    g1=models.ForeignKey(game, null=True,on_delete=models.CASCADE , related_name="g1")
    g2=models.ForeignKey(game, null=True,on_delete=models.CASCADE , related_name="g2")
    g3=models.ForeignKey(game, null=True,on_delete=models.CASCADE , related_name="g3")
    r1=models.ForeignKey(profile, null=True,on_delete=models.CASCADE , related_name="r1")
    r2=models.ForeignKey(profile, null=True,on_delete=models.CASCADE , related_name="r2")
    r3=models.ForeignKey(profile, null=True,on_delete=models.CASCADE , related_name="r3")
    def __str__(self):
        return f"{self.fname} {self.location} {self.status} {self.win} {self.kill}{self.matches}{self.damage} {self.gamingname}"
class followers(models.Model):
    page=models.ForeignKey(gamer,on_delete=models.CASCADE , related_name="page",null=True)
    fop=models.ManyToManyField(User, blank=True, related_name="fop")
    def __str__(self):
        return f"{self.name}"
class followings(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE , related_name="followingname",null=True)
    following=models.ManyToManyField(gamer, blank=True, related_name="following")
    def __str__(self):
        return f"{self.name}"
