import matplotlib.font_manager as fm
from wordcloud import WordCloud

# 폰트 검색 & 찾기
# for font in fm.fontManager.ttflist:
#     if 'Gothic' in font.name:
#         print(font.name, font.fname)

text = ""
with open("kakaotalk.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        if '] [' in line:
            text += line.split('] ')[2].replace('ㅋ', '').replace('ㅜ', '').replace('ㅠ', '').replace('ㅇ', '') \
                .replace('ㅎ', '').replace('사진\n', '').replace('이모티콘\n', '').replace('삭제된 메시지입니다', '')
    # print(text)

font_path = "Malgun Gothic C:/Windows/Fonts/malgunsl.ttf"

wc = WordCloud(font_path=font_path, background_color="white", width=600, height=400)
wc.generate(text)
wc.to_file("result.png")
