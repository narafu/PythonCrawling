f = open("text1.txt", "w", encoding="utf-8")
f.write("안녕 파이썬\n")
f.write("안녕 파이썬\n")
f.write("안녕 파이썬\n")
f.close()

# -----------------------------------------------------

with open("text2.txt", "w", encoding="utf-8") as f:
    for i in [1, 2, 3, 4, 5]:
        f.write(f"{i}번째 줄입니다.\n");

# -----------------------------------------------------

with open("text2.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line)

# -----------------------------------------------------

text = ""
with open("kakaotalk.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        text += line

print(text)

