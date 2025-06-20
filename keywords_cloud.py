import re
import keyword

try:  # Optional imports for non-python languages
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
except Exception:  # pragma: no cover - only needed when dependencies missing
    BeautifulSoup = None  # type: ignore
    urlopen = None  # type: ignore

# List of usable urls to extract the keywords
urls = {
    'c#': {
        "url": "https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/",
        "tag": "code"
    },
    'c++': {
        "url": "https://learn.microsoft.com/en-us/cpp/cpp/keywords-cpp",
        "tag": "code"
    },
    't-sql': {
        "url": "https://learn.microsoft.com/en-us/sql/t-sql/language-elements/reserved-keywords-transact-sql",
        "tag": "p"
    },
    'javascript': {
        "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#keywords",
        "tag": "code"
    },
    'java': {
        "url": "https://docs.oracle.com/javase/tutorial/java/nutsandbolts/_keywords.html",
        "tag": "code"
    }
}

def get_keywords(language: str):
    """Return a list of keywords for the given language."""
    lang = language.lower()

    # Python keywords can be retrieved directly
    if lang == 'python':
        return keyword.kwlist

    match_word = lambda x: len(re.findall(r'\w+', str(x)))

    if lang in urls and BeautifulSoup and urlopen:
        page = urlopen(urls[lang]['url'])
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        return [
            c.string
            for c in soup.find_all(urls[lang]['tag'])
            if (match_word(c.string) == 1 and c.string is not None)
        ]

    return []
