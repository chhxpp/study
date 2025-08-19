import re

def proper_title(s):
    """更符合自然语言的标题转换：只将单词（纯字母开头）的首字母大写"""
    # 正则规则：匹配单词开头的小写字母（前面是字符串开头或非字母字符）
    return re.sub(r"(^|[^a-zA-Z])([a-z])", lambda m: m.group(1) + m.group(2).upper(), s.lower())

# 测试对比
original = "hello WORLD! 2nd DAY"
print("str.title() 结果：", original.title())  # Hello World! 2Nd Day
print("自定义 proper_title 结果：", proper_title(original))  # Hello World! 2nd Day

import re

def proper_title(s):
    """修正版：数字后的字母不会被大写，仅非字母非数字分隔符后的字母大写"""
    # 正则规则：只把「字符串开头」或「非字母非数字字符」后面的小写字母大写
    # [^a-zA-Z0-9] 表示：不是字母也不是数字的字符（如空格、感叹号、逗号等）
    return re.sub(r"(^|[^a-zA-Z0-9])([a-z])", lambda m: m.group(1) + m.group(2).upper(), s.lower())

# 测试对比
original = "hello WORLD! 2nd DAY"
print("str.title() 结果：", original.title())  # Hello World! 2Nd Day
print("修正后 proper_title 结果：", proper_title(original))  # Hello World! 2nd Day
