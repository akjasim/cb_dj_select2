# Django Select2 Integration


## Usage

### select2 css
```html
<link href="https://cdn.jsdelivr.net/npm/select2@4.1.0-beta.1/dist/css/select2.min.css" rel="stylesheet"/>
```

### select2 js & jQuery
```html
<script src="https://code.jquery.com/jquery-3.5.1.min.js"
        integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/select2@4.1.0-beta.1/dist/js/select2.min.js"></script>
```


### select2 AJAX script

```html
<script>
    $(document).ready(function () {
        $('#id_language').select2({
            ajax: {
                url: '{% url 'home' %}',
                dataType: 'json',
                processResults: function (data) {
                    return {
                        results: $.map(data, function (item) {
                            return {id: item.id, text: item.title};
                        })
                    };
                }
            },
            minimumInputLength: 1
        });
    });
</script>
```

### forms.py logic
```python
def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['language'].queryset = Language.objects.none()

    if 'language' in self.data:
        self.fields['language'].queryset = Language.objects.all()

    elif self.instance.pk:
        self.fields['language'].queryset = Language.objects.all().filter(pk=self.instance.language.pk)
```
