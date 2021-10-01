# p21_5.py
from p21_3 import Filter, FilterChain

import re
# 引入規則運算式庫

class SensitiveFilter(Filter):
    """敏感詞過濾"""
    def __init__(self):
        self.__sensitives = ["黃色", "反動", "貪污"]
    def doFilter(self, elements):
        # 敏感詞列表轉換成規則運算式
        regex = ""
        for word in self.__sensitives:
            regex += word + "|"
        regex = regex[0: len(regex) - 1]
        # 對每個元素進行過濾
        newElements = []
        for element in elements:
            item, num = re.subn(regex, "", element)
            newElements.append(item)
        return newElements

class HtmlFilter(Filter):
    """HTML特殊字元轉換"""
    def __init__(self):
        self.__wordMap = {
            "&": "&amp;",
            "'": " &apos;",
            ">": "&gt;",
            "<": "&lt;",
            "\"": " &quot;",
        }
    def doFilter(self, elements):
        newElements = []
        for element in elements:
            for key, value in self.__wordMap.items():
                element = element.replace(key, value)
            newElements.append(element)
        return newElements

def testFiltercontent():
    contents = [
        '有人出售黃色書：<黃情味道>',
        '有人企圖搞反動活動, —"造謠資訊"',
    ]
    print("過濾前的內容：", contents)
    filterChain = FilterChain()
    filterChain.addFilter(SensitiveFilter())
    filterChain.addFilter(HtmlFilter())
    newContents = filterChain.doFilter(contents)
    print("過濾後的內容：", newContents)

testFiltercontent()
