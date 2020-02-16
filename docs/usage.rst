=====
Usage
=====

To use connapi in a project::

    import connapi
    resutl = connapi.Agify.get_age(['randomname']

Output::
    {'name': 'randomname', 'age': 33, 'count': 0} -> dict


========
Packages
========

AGIFY ::

    def get_age(names, country_code, api_key)

Here names is a list of names example - ['name1','name2']  -- Mandatory feild (minimum one value)

country_code takes a upper case String of Country code example - "US","IN"

api_key takes the api_key which you generated in case of more requests. You can generate the `api_key`_ from here.

.. _api_key: https://store.agify.io/
