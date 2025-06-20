import keyword
from keywords_cloud import get_keywords

def test_get_python_keywords():
    assert get_keywords("python") == keyword.kwlist
