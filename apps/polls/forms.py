#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 9:53
# @Author  : tanxw
# @Desc    : 表单
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    error_css_class = 'error'
    required_css_class = 'required'