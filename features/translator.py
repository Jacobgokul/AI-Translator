from deep_translator import GoogleTranslator

class Translator:
    def __init__(self):
        self.translator = GoogleTranslator()

    def list_of_lang(self):
        return self.translator._languages

    def text_translator(self, source_text, target_lang):
        self.translator.target = target_lang
        return self.translator.translate(source_text)
