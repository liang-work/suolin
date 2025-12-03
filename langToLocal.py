import readFile

class LangLocal:
    def __init__(self, lang_code):
        self.lang_code = lang_code
        self.translations = self.load_translations()
    def load_translations(self):
        file_path = f"lang/{self.lang_code}.json"
        return readFile.LoadJson(file_path)
    
    def get_tarnslation(self, key):
        return self.translations.get(key, key)