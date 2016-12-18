from django import forms

class CommentForm(forms.Form):
    comment = forms.CharField(
        widget= forms.Textarea(),
        error_messages= {
            "required":"客官，打赏下吧~",
        },
        validators=[],
    )