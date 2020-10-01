from django import forms


class LinkForm(forms.Form):
    link = forms.URLField()
    link.widget.attrs.update(
        {'class': 'form-control', 'placeHolder': "Please enter link"})
