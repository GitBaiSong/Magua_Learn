from django import forms

def word_validator(name):
    if len(name)  < 2:
        raise forms.ValidationError("请输入2位以上的名字")

def comment_validator(comment):
    if len(comment) < 8:
        raise forms.ValidationError("请输入8位以上的评论")


class CommentForm(forms.Form):
    name = forms.CharField(max_length=50,
        error_messages={"required":"Wow, Such Words!"},
        validators = [word_validator],
    )
    comment = forms.CharField(
        widget= forms.Textarea(),
        error_messages={"required": "Wow, Such Words!"},
        validators = [comment_validator],
    )