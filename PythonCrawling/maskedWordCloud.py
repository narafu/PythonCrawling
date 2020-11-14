from PIL import Image
import numpy as np
from wordcloud import WordCloud

font_path = "Malgun Gothic C:/Windows/Fonts/malgunsl.ttf"

text = ""
with open("kakaotalk.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        if '] [' in line:
            text += line.split('] ')[2].replace('ㅋ', '').replace('ㅜ', '').replace('ㅠ', '').replace('ㅇ', '') \
                .replace('ㅎ', '').replace('사진\n', '').replace('이모티콘\n', '').replace('삭제된 메시지입니다', '')

mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path=font_path, background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked.png")
