from django import forms

from bookmark.models import Bookmark


class BookmarkCreationForm(forms.ModelForm):
    url = forms.CharField(label='링크', widget=forms.TextInput)
    class Meta:
        model = Bookmark
        fields = ['name', 'url']

    def save(self, commit=True):
        new_bookmark = Bookmark.objects.create(
            name=self.cleaned_data.get('name')
        )
        return new_bookmark