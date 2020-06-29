from django import forms
from core.models import Entry, Language


class EntryCreationForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['language'].queryset = Language.objects.none()
    #
    #     if 'language' in self.data:
    #         self.fields['language'].queryset = Language.objects.all()
    #
    #     elif self.instance.pk:
    #         self.fields['language'].queryset = Language.objects.all().filter(pk=self.instance.language.pk)