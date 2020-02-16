#!/usr/bin/env python

"""Tests for `agify` package."""

import pytest
from connapi.api import agify

@pytest.mark.parametrize(
    "names_list, country, api_key, expected",
    [(['random'],None,None,"random"),
     ([''],"","","Error"),
     (['randome1','random2'],"US",None,"randome1")
     ]
)
def test_get_age(names_list, country, api_key, expected):
    result = agify.Agify.get_age(names_list,country_code=country,api_key=api_key)
    assert expected in str(result)

@pytest.mark.parametrize(
    "names_list, country, api_key, expected",
    [(['random'],None,None,"random"),
     ([''],"","","Error"),
     (['randome1','random2'],"US",None,"randome1")
     ]
)
def test_get_gender(names_list, country, api_key, expected):
    result = agify.Agify.get_gender(names_list,country_code=country,api_key=api_key)
    assert expected in str(result)
    if("Error" not in expected):
        assert 'probability' in str(result)


@pytest.mark.parametrize(
    "names_list, api_key, expected",
    [(['random'],None,"random"),
     ([''],"","Error"),
     (['randome1','random2'],None,"randome1")
     ]
)
def test_get_nationality(names_list, api_key, expected):
    result = agify.Agify.get_nationality(names_list,api_key=api_key)
    assert expected in str(result)
