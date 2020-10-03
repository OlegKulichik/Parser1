import re


class Parser:


    def __init__(self, file_name: str):
        self._file_name = file_name
        self._single_tag = '<{0}.*?>'
        self._double_tag = '<{0}.*?{1}.*?>*?<{0}.*?>'
        self._triple_tag = '<{0}.*?{1}.*?{2}.*?>*?</{0}.*?>'


    def read_file(self):
        with open(self._file_name, "r",) as file:
            result = file.read()
        return result


    def paty_maker(self, tag: str,atrr: str = None, atrr1: str =None):

        if atrr is None and atrr1 is not None:
            raise RuntimeError ("Не ну ты дурак?")

        if atrr is not None and atrr1 is None:
            ttm = re.findall(self._double_tag.format(tag,atrr),self.read_file())
        elif atrr is not None and atrr1 is not None:
            ttm = re.findall(self._triple_tag.format(tag,atrr,atrr1),self.read_file())
        elif tag:
            ttm = re.findall(self._single_tag.format(tag),self.read_file())
        return ttm



pt = Parser("myfin.html")

print(pt.paty_maker("meta"))
print(pt.paty_maker("span", atrr="class"))
print(pt.paty_maker("span", atrr="class", atrr1="data-bind"))