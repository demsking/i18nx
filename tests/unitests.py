# pylint: disable=missing-module-docstring,wrong-import-position,missing-function-docstring,protected-access,invalid-name

import sys
sys.path.append('../i18nx')

from i18nx import I18n

def test_init():
  i18n = I18n('en', 'fr', {
    'en': { 'hello': 'Hello' },
    'fr': { 'hello': 'Salut' },
  })

  assert i18n.locale == 'en'
  assert i18n.fallback_locale == 'fr'
  assert 'en' in i18n.available_locales
  assert 'fr' in i18n.available_locales

def test_setters():
  i18n = I18n('en', 'fr', {
    'en': { 'hello': 'Hello' },
    'fr': { 'hello': 'Salut' },
  })

  assert i18n.locale == 'en'
  assert i18n.fallback_locale == 'fr'

  i18n.locale = 'fr'
  i18n.fallback_locale = 'en'

  assert i18n.locale == 'fr'
  assert i18n.fallback_locale == 'en'

def test_nested():
  i18n = I18n('en', 'fr', {
    'en': { 'hello': { 'world': 'Hello World!' } },
    'fr': { 'hello': { 'world': 'Bonjour le monde!' } },
  })

  assert 'hello.world' in i18n._translations['en']
  assert 'hello.world' in i18n._translations['fr']
  assert i18n._translations['en']['hello.world'] == 'Hello World!'
  assert i18n._translations['fr']['hello.world'] == 'Bonjour le monde!'

def test_deep():
  i18n = I18n('en', 'fr', {
    'en': { 'hello': { 'world': { 'cameroon': 'Continent' } } },
  })

  assert i18n._translations['en']['hello.world.cameroon'] == 'Continent'

def test_translation():
  i18n = I18n(
    locale = 'en',
    fallback_locale = 'fr',
    translations = {
      'en': { 'message': { 'hello': 'Hello World!' } },
      'fr': { 'message': { 'hello': 'Bonjour le monde !' } },
    },
  )

  assert i18n.tr("message.hello") == 'Hello World!'

def test_translation_fallback():
  i18n = I18n(
    locale = 'en',
    fallback_locale = 'fr',
    translations = {
      'fr': { 'message': { 'hello': 'Bonjour le monde !' } },
    },
  )

  assert i18n.tr("message.hello") == 'Bonjour le monde !'

def test_missing_translation():
  i18n = I18n(
    locale = 'en',
    fallback_locale = 'fr',
    translations = {},
  )

  assert i18n.tr("message.hello") == 'message.hello'

def test_missing_translation_with_warning():
  i18n = I18n(
    locale = 'en',
    fallback_locale = 'fr',
    translations = {},
    show_warning = True
  )

  assert i18n.tr("message.hello") == 'message.hello'

def test_interpolation():
  i18n = I18n(
    locale = 'en',
    fallback_locale = 'fr',
    translations = {
      'en': { 'message': { 'hello': 'Hello {name}!' } },
      'fr': { 'message': { 'hello': 'Bonjour {name} !' } },
    },
  )

  assert i18n.tr("message.hello", name = 'Mario') == 'Hello Mario!'

def test_plurals():
  i18n = I18n(
    locale = 'en',
    fallback_locale = 'fr',
    translations = {
      'en': {
        'car': 'car | cars',
        'apple': 'no apples | one apple | {count} apples'
      },
    },
  )

  assert i18n.tr("car") == 'car'
  assert i18n.tr("car", count = 0) == 'car'
  assert i18n.tr("car", count = 1) == 'car'
  assert i18n.tr("car", count = 2) == 'cars'
  assert i18n.tr("apple", count = 0) == 'no apples'
  assert i18n.tr("apple", count = 1) == 'one apple'
  assert i18n.tr("apple", count = 15) == '15 apples'

def test_list():
  i18n = I18n(
    locale = 'en',
    fallback_locale = 'fr',
    translations = {
      'en': {
        "greetings": [
          "Hey {firtname}!",
          "Hi {firtname}!",
        ],
      },
    },
  )

  assert i18n.tr("greetings.0", firtname = 'Mario') == 'Hey Mario!'
  assert i18n.tr("greetings.1", firtname = 'Mario') == 'Hi Mario!'

def test_raw():
  greetings = [
    "Hey {firtname}!",
    "Hi {firtname}!",
  ]

  i18n = I18n(
    locale = 'en',
    fallback_locale = 'fr',
    translations = {
      'en': {
        "greetings": greetings,
      },
    },
  )

  assert isinstance(i18n.raw["greetings"], list)
  assert i18n.raw['greetings'] == greetings
