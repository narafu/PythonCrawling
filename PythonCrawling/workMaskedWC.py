from PIL import Image
import numpy as np
import matplotlib.font_manager as fm
from wordCloud import WordCloud

# 폰트 검색 & 찾기
# for font in fm.fontManager.ttflist:
    # if 'Nanum' in font.name:
        # print(font.name, font.fname)

font_path = "NanumGothic C:/Windows/Fonts/NanumGothicExtraBold.ttf"

text = ""
with open("KakaoTalk_20201011_1908_31_544_최윤희.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        if '] [' in line:
            text += line.split('] ')[2]

mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path=font_path, background_color="white", mask=mask)
wc.generate(text)
wc.to_file("homework_masked.png")
