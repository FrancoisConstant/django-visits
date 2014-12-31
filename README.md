django-visit
============

- Really simple app to count the visits on any Django Model.
- This is not meant to replace any proper tracking analytics tool.
- This app is useful to setup really simple "most popular" widgets.


It's a simplified fork of: https://github.com/thornomad/django-hitcount with 2 main differences:
- the visits/hits are not saved
- I've only kept the AJAX option

INSTALL:
--------
`pip install -e git+https://github.com/goinnn/django-visits#egg=visits`


Set-up:
-------

1.Add it to your "INSTALLED_APPS" settings:

    INSTALLED_APPS = (
        ...
        'visits',
        ...
    )

TODO
----
* doc
* tests


2.Optionally, add a column to cache the result on the concerned model:
3.migrate
4.add tag in template