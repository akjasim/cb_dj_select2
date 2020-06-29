# Django Select2 Integration


## Usage

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
