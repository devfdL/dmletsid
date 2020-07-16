from django import forms

class kltrcmntForm(forms.Form):

    comment    = forms.CharField(
        max_length=255,
        label = '',
        widget = forms.TextInput(
            attrs={
                'class':'inpt-ssmdcomment',
                'placeholder':'Comment...'
            }
        )
    )