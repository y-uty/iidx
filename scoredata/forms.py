from django import forms
from .models import CsvUpload, VersionList

class CsvUploadForm(forms.ModelForm):

    class Meta:
        model = CsvUpload
        fields = ('iidx_id', 'uploaded',)


class VersionChoice(forms.Form):
    ''' お試し
        ver_list = forms.fields.ChoiceField(
        choices = (
            (26, 'Rootage'),
            (27, 'HEROIC VERSE'),
            (28, 'BISROVER')
        ),
        required=True,
        widget=forms.widgets.Select
        )
    '''
    ver_list = forms.ModelChoiceField(
                                label='バージョン',
                                queryset=VersionList.objects.filter(ver_name__isnull=False),
                                empty_label='選択してください',
                                to_field_name='ver_no'
                                )