from typing import List, Dict, Any

class I18n:
  """I18n class"""

  def __init__(self, locale: str, fallback_locale: str, translations: Dict[str, Dict[str, Any]], show_warning = False):
    """Initializer"""

    self._locale = locale
    self._fallback_locale = fallback_locale
    self._show_warning = show_warning
    self._translations = {
      lang: self._flatten(messages) for lang, messages in translations.items()
    }

    for lang in [locale, fallback_locale]:
      if lang not in self._translations:
        self._translations[lang] = {}

  @property
  def locale(self):
    """Active locale"""
    return self._locale

  @locale.setter
  def locale(self, value: str):
    """Set active locale"""
    self._locale = value
    
  @property
  def fallback_locale(self):
    """Fallback locale"""
    return self._fallback_locale

  @fallback_locale.setter
  def fallback_locale(self, value: str):
    """Set active locale"""
    self._fallback_locale = value

  @property
  def available_locales(self):
    """Available locales"""
    return self._translations.keys()
  
  def _flatten(self, input_object: dict):
    result = {}

    for key in input_object:
      value = input_object[key]
      
      if type(value) == dict or type(value) == list:
        self._flatten_deep(value, key, result)
      else:
        result[key] = value
    
    return result
  
  def _flatten_deep(self, input_object: dict, base_key: str, result: dict):
    for key in input_object:
      prop = f'{base_key}.{key}' if base_key else key
      value = input_object[key]
      
      if type(value) == dict or type(value) == list:
        self._flatten(value, prop, result)
      else:
        result[prop] = value
    
    return result

  def _get_message_variant(self, message: str, **params):
    count = params.get('count', 0)
    message = message.split('|')
    
    if len(message) == 2:
      message = [message[0]] + message

    if count == 0:
      return message[0]
    
    return message[1] if count == 1 else message[2]
    
  def _translate(self, path: str, translations: dict, **params):
    if path in translations:
      response = self._get_message_variant(translations[path], **params).strip() if '|' in translations[path] else translations[path]

      for param in params:
        response = response.replace("{" + str(param) + "}", str(params[param]))

      return response
    
    return None

  def tr(self, path: str, **params):
    """Get the translate text for the given path"""
    
    response = self._translate(path, self._translations[self._locale], **params)

    if response is None:
      response = self._translate(path, self._translations[self._fallback_locale], **params)
    else:
      return response

    if response is None:
      if self._show_warning:
        print("Translation missing for {key}".format(key=path))

      return path

    return response
