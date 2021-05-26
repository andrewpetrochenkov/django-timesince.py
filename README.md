[![](https://img.shields.io/badge/released-2021.5.8-green.svg?longCache=True)](https://pypi.org/project/django-timesince/)
[![](https://img.shields.io/badge/license-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)

### Installation
```bash
$ pip install django-timesince
```

### Examples
```html
{% load timesince %}

{{ created_at|timesince }} ago
```

`default`|`django_timesince`
-|-
`1 hour 5 minutes ago`|`1 hour ago`
`1 year 2 months ago`|`1 year ago`

