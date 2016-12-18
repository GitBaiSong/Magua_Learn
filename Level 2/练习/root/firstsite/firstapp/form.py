from django import forms
from django.core.exceptions import ValidationError

def words_validator(comment):
    if len(comment) < 4:
        raise ValidationError("至少4位")

def comment_validator(comment):
    if '习近平' in comment:
        raise ValidationError("包含非法字符")

class CommentForm(forms.Form):
    name = forms.CharField(max_length=50)

    comment = forms.CharField(
        widget = forms.Textarea(),
        error_messages = {
        'required' : "wow, such words"
        },
        validators = [words_validator, comment_validator],
    )
