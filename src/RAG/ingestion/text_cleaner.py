import re

class TextCleaner:
    def remove_extra_whitespace(self, text):
        return re.sub(r'\s+', " ", text)

    def remove_page_number(self, text):
        text = re.sub(r'Page \d+', '', text)
        text = re.sub(r'page \d+', '', text)
        return text

    def remove_citations(self, text):
        return re.sub(r'\[\d+\]', '', text)

    def clean(self, text):
        """Apply all cleaning steps in one call."""
        text = self.remove_page_number(text)
        text = self.remove_citations(text)
        text = self.remove_extra_whitespace(text)
        return text.strip()
