from django import forms

from .models import Post, Comment, GameUser


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'message']


class GameUserSignupForm(forms.ModelForm):
    class Meta:
        model = GameUser
        fields = ['server', 'username']
    
    def clean_username(self):
        '''
        값 변환은 clean 함수에서만 가능합니다.
        validator에서는 지원하지 않습니다.
        '''
        return self.cleaned_data.get('username','').strip()
