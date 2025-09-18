# 极简版编码测试工具
hex_str = (
    "FF FE 27 59 77 6D 4A 55 0C FF 60 4F 68 51 2F 66 "
    "00 00 34 6C 0D 00 0A 00 8F 9A 6C 9A 4A 55 0C FF 60 4F "
    "DB 56 61 67 7F 81 0D 00 0A 00 44 51 1F 5F 4A 55 "
    "0C FF 60 4F 65 55 FD 90 0D 4E 1A 4F 0D 00 0A 00 "
    "68 51 60 97 40 77 0C FF A3 90 20 6B 53 62 84 76 "
    "34 56"
)

data = bytes.fromhex(hex_str.replace(" ", ""))

# 在这里修改编码名称试试
encoding = "utf-16-le"

result = data.decode(encoding, errors='ignore')
print(f"{encoding}：\n{result}")