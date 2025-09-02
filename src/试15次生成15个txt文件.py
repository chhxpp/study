import os

def generate_shifted_files(infile="new.txt", outdir="./src/txt/"):
    # 确保输出目录存在
    os.makedirs(outdir, exist_ok=True)

    # 读取文件二进制
    with open(infile, "rb") as f:
        data = f.read()

    # 转成二进制字符串
    bit_str = "".join(f"{b:08b}" for b in data)

    # 依次删除首 0 ~ 15 位
    for shift in range(0, 16):
        shifted_bits = bit_str[shift:]
        # 补齐到字节边界
        pad_len = (-len(shifted_bits)) % 8
        if pad_len:
            shifted_bits += "0" * pad_len

        # 转回字节
        new_data = bytes(int(shifted_bits[i:i+8], 2) for i in range(0, len(shifted_bits), 8))

        # 保存文件
        outfile = os.path.join(outdir, f"{shift}.txt")
        with open(outfile, "wb") as f:
            f.write(new_data)

    print(f"已生成 1.txt ~ 24.txt 到 {outdir}")

# 执行
generate_shifted_files("./src/txt/new.txt", "./src/txt/")
