import os

def create_typical_garbled_file():
    # 内容包含：常用中文（GB2312支持）+ 生僻字（GB2312不支持）+ 数字符号
    content = """这是一段包含生僻字的测试文本：
常用字：你好、世界、123、!@#$%
生僻字：𪚥、𠀎、𠑥、𡃁、𣗥（这些字GB2312不支持）
用GB2312编码保存后，生僻字会变成乱码，适合练习解码。
"""
    
    # 关键：用GB2312编码保存（不支持部分生僻字，自然产生乱码）
    file_name = "./src/t1.txt"  # 直接生成你要的t1.txt
    with open(file_name, "w", encoding="gb2312", errors="xmlcharrefreplace") as f:
        f.write(content)
    
    full_path = os.path.abspath(file_name)
    print(f"典型乱码文件已生成：{full_path}")
    print("提示：用记事本打开会看到生僻字变成乱码（如&#172133;），符合真实场景")

if __name__ == "__main__":
    create_typical_garbled_file()
    
    