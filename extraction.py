from konlpy.tag import Okt
from konlpy.utils import pprint
from newspaper import Article
import re

url = "http://www.bloter.net/archives/335773"

news = Article(url, language = 'ko')
news.download()
news.parse()

sentence = re.findall(r"([^.]*?투자[^.]*\.)",news.text)
okt = Okt()

for line in sentence:
    print(okt.pos(line))