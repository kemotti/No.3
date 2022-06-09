import chardet
e = input("入力してください：").encode('utf-8')



result = chardet.detect(e)
print(result)

print("ASCII文字か", e.isascii())
print("半角か" ,e.isupper())
print("全角か" ,e.islower())
print("数字か", e.isdigit())


d = input("入力")

with open('d', 'r', encoding='utf-8') as a_file:
  txt = a_file.read()


txt = txt.replace('\r', '')
