from django.forms import (
    Form,
    ModelForm,
    CharField,
    TextInput,
    Textarea,
    EmailField,
    EmailInput
)


class CommentForm(Form):
    name = CharField(widget=TextInput(attrs={
        'placeholder': 'Name',
        'class': 'main_text'
    }))
    email = EmailField(widget=EmailInput(attrs={
        'placeholder': 'Your Email',
        'class': 'mail_text'
    }))
    phone = CharField(widget=TextInput(attrs={
        'placeholder': 'Phone Number',
        'class': 'mail_text'
    }))
    message = CharField(widget=Textarea(attrs={
        'placeholder': 'Message',
        'class': 'message-bt',
        'rows': 5,
        'id': 'comment'
    }))


class CategoryForm(Form):
    category = CharField(widget=TextInput(attrs={
        'placeholder': 'Category',
        'class': 'mail_text'
    }))
