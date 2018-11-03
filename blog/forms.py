# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 00:25:53 2018

@author: Vartika Sharma
"""

from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)