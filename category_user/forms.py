from django import forms

from category_user.models import Comment, TVShow


class CommentForm(forms.ModelForm):
    shows = forms.ModelChoiceField(widget=forms.HiddenInput(),
                                   disabled=True,
                                   required=False,
                                   queryset=TVShow.objects.all())

    class Meta:
        model = Comment
        fields = [
            'text',
            'shows'
        ]
