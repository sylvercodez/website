from django.db import models


# Create your models here.
class Base(models.Model):
    home_images = models.ImageField(max_length=200, null=True)
    write_up = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.home_images.name

class About(models.Model):
    headings = models.CharField(default="ABOUT US", max_length=50, null=True)
    small_desc1_headings = models.CharField(max_length=100, null=True, blank=True)
    headings_desc1 = models.TextField(null=True)
    pics_headings = models.CharField(default="MY name", max_length=20, null=True)
    admin_pics = models.ImageField(default=' profilpics.png', max_length=200, null=True)
    desc2_admin = models.TextField(null=True)
    small_desc2_admin = models.CharField(max_length=100, null=True, blank=True)
    partners = models.IntegerField(default="0", max_length=None, null=True)
    projects_done = models.IntegerField(default="0", max_length=None, null=True)
    meetings = models.IntegerField(default="0", max_length=None, null=True)
    happy_clients = models.IntegerField(default="0", max_length=None, null=True)

    def __str__(self):
        return self.headings


class Aboutwork(models.Model):
    works = models.ForeignKey(About, null=True, on_delete=models.SET_NULL)
    good_at = models.TextField(max_length=50, null=True, blank=True)
    good_at_percentage = models.IntegerField(default='20', max_length=None, null=True, blank=True)

    def __str__(self):
        return self.good_at


class Contact(models.Model):
    BackgroundImage3 = models.ImageField(max_length=100, null=True)
    headings = models.CharField(default="CONTACT US", max_length=50, null=True)
    image_banner = models.ImageField(max_length=100, null=True, blank=True)
    small_desc1_headings = models.CharField(default="WHERE I WORK", max_length=100, null=True, blank=True)
    small_desc2_subheadings = models.CharField(default="I'd love your feedback!", max_length=50, null=True, blank=True)
    mymap = models.ImageField(max_length=100,null=True,blank=True)
    location = models.CharField(default="Lagos, NIGERIA", max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return self.headings


class Portfolio(models.Model):
    BackgroundImage2 = models.ImageField(max_length=100, null=True)
    headings = models.CharField(default="PORTFOLIO", max_length=50, null=True)
    small_desc1_headings = models.TextField(default="MY WORK", max_length=100, null=True, blank=True)
    small_desc2_subheadings = models.CharField(default="Here are some of my work.",
                                               max_length=300, null=True, blank=True)
    image_banner = models.ImageField(max_length=100, null=True, blank=True)
    image_banner_alt = models.CharField(max_length=30,null=True, blank=True)

    def __str__(self):
        return self.headings


class PortfolioImages(models.Model):
    portlink = models.ForeignKey(Portfolio, null=True, on_delete=models.SET_NULL,blank=True)
    image_links = models.ImageField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.image_links.name



class Facebookurl(models.Model):
    facebookUrl = models.URLField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.facebookUrl


class InstagramUrl(models.Model):
    instagramUrl = models.URLField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.instagramUrl


class LinkedinUrl(models.Model):
    linkedinUrl = models.URLField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.linkedinUrl


class SnapchatUrl(models.Model):
    snapchatUrl = models.URLField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.snapchatUrl


class PinterestUrl(models.Model):
    pinterestUrl = models.URLField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.pintrestUrl


class TwitterUrl(models.Model):
    twitterUrl = models.URLField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.twitterUrl