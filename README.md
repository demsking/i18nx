# I18n for Python

[![pypi version](https://badge.fury.io/py/pi18n.svg)](https://pypi.org/project/pi18n/)

Lightweight i18n for Python

## Install

```sh
pip install pi18n
```

## Usage

```python
from pi18n import I18n

i18n = I18n(
  locale = 'en',
  fallback = 'fr',
  translations = {
    'en': { 'message': { 'hello': 'Hello World!' } },
    'fr': { 'message': { 'hello': 'Bonjour le monde !' } },
  },
)

print(i18n.tr("message.hello")) # Hello World!
```

## Message Format Syntax

**Interpolation**

`pi18n` use the Mustache like placeholders `{}` syntax for interpolation.

```python
from pi18n import I18n

i18n = I18n(
  locale = 'en',
  fallback = 'fr',
  translations = {
    'en': { 'message': { 'hello': 'Hello {name}!' } },
    'fr': { 'message': { 'hello': 'Bonjour {name} !' } },
  },
)

print(i18n.tr("message.hello", name = 'Mario')) # Hello Mario!
```

**Pluralization**

Use a pipe `|` separator in combination with the param `count` to define 
plurals on the locale translations.

```python
from pi18n import I18n

i18n = I18n(
  locale = 'en',
  fallback = 'fr',
  translations = {
    'en': {
      'car': 'car | cars',
      'apple': 'no apples | one apple | {count} apples',
    },
  },
)

print(i18n.tr("car")) # 'car'
print(i18n.tr("car", count = 0)) # 'car'
print(i18n.tr("car", count = 1)) # 'car'
print(i18n.tr("car", count = 2)) # 'cars'
print(i18n.tr("apple", count = 0)) # 'no apples'
print(i18n.tr("apple", count = 1)) # 'one apple'
print(i18n.tr("apple", count = 15)) # '15 apples'
```

## I18n API

```coffee
interface class I18n:
  constructor(locale: str, fallback_locale: str, translations: Dict[str, Dict[str, Any]], show_warning = False)

  @property locale: str    
  @property fallback_locale: str
  @property available_locales: List[str]

  @method tr(path: str, **params) -> str
```

## Development Setup

1. [Install Nix Package Manager](https://nixos.org/manual/nix/stable/installation/installing-binary.html)

2. [Install `direnv` with your OS package manager](https://direnv.net/docs/installation.html#from-system-packages)

3. [Hook it `direnv` into your shell](https://direnv.net/docs/hook.html)

4. At the top-level of your project run:

   ```sh
   direnv allow
   ```

   The next time your launch your terminal and enter the top-level of your
   project, `direnv` will check for changes.

## License

Under the MIT license.
See [LICENSE](https://gitlab.com/demsking/pi18n/blob/main/LICENSE) file for
more details.
