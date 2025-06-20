# keywords-cloud
Create a cloud of keywords for a few programming languages, with optional highlights to specific keywords

![Alt text](/sample_output.png?raw=true "Sample Output")

## Requirements

- [wordcloud](https://github.com/amueller/word_cloud): `pip install wordcloud`
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/) (bs4): `pip install beautifulsoup4`
  - used for HTML parsing

#### Installation notes

wordcloud depends on `numpy` and `pillow`.

To save the wordcloud into a file, `matplotlib` can also be installed.

Please see [wordcloud's GitHub](https://github.com/amueller/word_cloud) for more info on requirements and example usage.

## Using `get_keywords`

The `keywords_cloud` module exposes a helper function `get_keywords(language)` which returns the list of reserved words for the chosen language. For Python, it simply returns `keyword.kwlist`.

```python
from keywords_cloud import get_keywords
print(get_keywords("python"))
```

## Running tests

Install `pytest` and run:

```bash
pytest -q
```