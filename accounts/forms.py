from django.contrib.auth.forms import User, AuthenticationForm, UsernameField
from django.shortcuts import render
from django import forms
from django.core.exceptions import ObjectDoesNotExist

# class LoginForm(AuthenticationForm):
#     """ログインフォーム"""

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs['class'] = 'form-control'
    #         field.widget.attrs['placeholder'] = field.label 
class LoginForm(AuthenticationForm):
    username = UsernameField(
        label='ユーザー名',
        max_length=255
    )
    password = forms.CharField(
        label='パスワード',
        strip=False,
        widget=forms.PasswordInput(render_value=True)
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
    # 個別バリデーション
    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 3:
            raise forms.ValidationError(
                '%(min_length)s 文字以上！', params={'min_length': 3}
            )
        return username
    # 総合
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            raise forms.ValidationError(
                '正しくない'
            )
        if not user.check_password(password):
            raise forms.ValidationError('パスワード違う')
        return cleaned_data
