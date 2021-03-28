# django-echadmin
Django EchAdmin

- account
- format-admin
- static
- templates
- options.py
- sites.py

settings.py
```
INSTALLED_APPS = [
    'echadmin',
    'echadmin.account',

    ...
]
```

urls.py
```
urlpatterns = [
    ...

    path('account/', include('echadmin.account.urls')),
    path('admin/', echadmin.site.urls),

    ...
]
```