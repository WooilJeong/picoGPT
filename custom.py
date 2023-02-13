"""

번역기

"""
from googletrans import Translator
trans = Translator()

def kor_to_eng(text):
    result = trans.translate(text, 
                             src="ko", 
                             dest="en")
    return result.text

def eng_to_kor(text):
    result = trans.translate(text, 
                             src="en", dest="ko")
    return result.text