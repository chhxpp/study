# 生成一个乱码文件
# 这个程序会创建一个用GBK编码的中文文件
# 当用错误的编码(如UTF-8)打开时就会显示乱码

# 中文内容
chinese_text = "这是一段中文文本，用于测试字符编码和解码问题。"

# 用GBK编码写入文件
with open(".\src\t1.txt", "w", encoding="utf-16") as f:
    f.write(chinese_text)

print("已生成乱码文件: garbled_text.txt")
print("提示: 这个文件实际是用GBK编码的中文文本")
    