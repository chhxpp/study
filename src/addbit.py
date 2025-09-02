def prepend_one_bit(infile="./src/new.txt", outfile="./src/restored.txt"):
    # 读取文件（以二进制方式）
    with open(infile, "rb") as f:
        data = f.read()
    
    # 转换为二进制字符串
    bit_str = "".join(f"{byte:08b}" for byte in data)
    
    # 在最前面加一个 bit=1
    bit_str = "1" + bit_str
    
    # 如果长度不是8的倍数，补齐到8位
    if len(bit_str) % 8 != 0:
        bit_str = bit_str.ljust((len(bit_str) // 8 + 1) * 8, "0")
    
    # 转回字节
    new_data = bytes(int(bit_str[i:i+8], 2) for i in range(0, len(bit_str), 8))
    
    # 写入新文件
    with open(outfile, "wb") as f:
        f.write(new_data)

prepend_one_bit()
