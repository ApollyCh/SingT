from googletrans import Translator
import langid


def translate(text, target_lang):
    translator = Translator()
    return translator.translate(text, dest=target_lang).text


def detect_lang(text):
    return langid.classify(text)[0]
