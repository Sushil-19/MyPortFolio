from django.db import models

# Create your models here.


class Services(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.TextField()
    clas = models.CharField(max_length = 100)


class Pricing(models.Model):
    name = models.CharField(max_length = 100)
    cost = models.IntegerField()
    span = models.IntegerField()
    projectcount = models.IntegerField()
    projectsize = models.CharField(max_length = 100)
    domain = models.IntegerField()
    usercount = models.IntegerField()


class Blogs(models.Model):
    img = models.ImageField(upload_to = 'blog_pics')
    name = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    firstpara = models.TextField()
    secondpara = models.TextField()
    link = models.CharField(max_length = 200)

class MyInfo(models.Model):
    profileDesc = models.CharField(max_length = 300)
    skillDesc = models.CharField(max_length = 300)
    cv = models.FileField(upload_to='resume_files')
    birthdate = models.CharField(max_length = 100)
    emailid = models.CharField(max_length = 100)
    contactno = models.CharField(max_length = 100)
    skypeid = models.CharField(max_length = 100)
    address = models.CharField(max_length = 200)

class Expertise(models.Model):
    clas = models.CharField(max_length = 100)
    field = models.CharField(max_length = 200)
    desc = models.TextField()

class Education(models.Model):
    years = models.CharField(max_length = 100)
    degree = models.CharField(max_length = 300)
    details = models.TextField()


class Experiance(models.Model):
    years = models.CharField(max_length = 100)
    title = models.CharField(max_length = 300)
    details = models.TextField()

class Skills(models.Model):
    title = models.CharField(max_length = 100)
    percent = models.CharField(max_length = 20)

class Language(models.Model):
    name = models.CharField(max_length = 100)
    percent = models.CharField(max_length = 20)

class Project(models.Model):
    img = models.ImageField(upload_to = 'project_pics')
    name = models.CharField(max_length = 200)
    author = models.CharField(max_length = 100)
    desc = models.TextField()
    technologies =  models.TextField()
    link =  models.CharField(max_length = 200)
