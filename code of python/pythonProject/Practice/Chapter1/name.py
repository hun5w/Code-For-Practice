name = "ada"
print(name.title())
print(name.upper())
print(name.lower())

name = "ADA"
print(name.title())

name = "Ada"
print(name.title())

'''
title(),是将字符串中的每个单词的首字母大写
upper(),是将字符串中的每个字母大写
lower(),是将字符串中的每个字母小写
'''
last_name = "lovelace"
first_name = "ada"
full_name = f"{first_name } {last_name}"
print(f"Hello,{full_name.title()}!")

filename = "python_notes.txt"
filename = filename.removesuffix(".txt")
print(filename)