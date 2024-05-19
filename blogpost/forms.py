from django.forms import ModelForm

from blogpost.models import BlogPost


class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        exclude = ("number_of_views",)