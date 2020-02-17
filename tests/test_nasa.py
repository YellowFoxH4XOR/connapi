import pytest
from connapi.api import nasa

@pytest.mark.parametrize(
    "api_key, date, hd, save",
    [(None,None,None,False),
     (None,"2020-1-23",True,False),
     ]
)
def test_get_apod(api_key, date, hd, save):
    result = nasa.Nasa.get_apod(api_key=api_key, date=date, hd=hd, save=save)
    assert "url" in result.keys()


@pytest.mark.parametrize(
    "api_key, start_date, end_date",
    [(None,None,None)
     ]
)
def test_get_neows(api_key, start_date, end_date):
    result = nasa.Nasa.get_neows(api_key=api_key)
    assert "links" in result.keys()