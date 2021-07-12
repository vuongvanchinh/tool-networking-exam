
def crc(data: str, generator: str, base=2):
    """
    len(data) > len(generate)
    """
    if base != 2:
        data = bin(int(data, base))[2:]
    n = len(generator)
    data += '0'*(n - 1) # shift left (n - 1) bits
    g_number = int(generator, 2)
    t = data[:n]
    i = n
    while i <= len(data):
        t = bin(int(t, 2) ^ g_number)[2:]
        offset = n - len(t)
        t += data[i: i + offset]
        i += offset
        
    return '0' * (n - 1 - len(t)) + t # make sure result has n - 1 bits "t.zfill(n-1)

def checksum(data: list, length=16, base = 2):
    """
    input: list of operands in binary format is default: eg: "10010010"
        length: 
    Chú ý: Để tính checksum, kích thước khối dữ liệu cần tính phải có chiều dài là bội nguyên của 16, hối
    vì vậy dữ liệu thiếu sẽ được gắn thêm các bit 0 vào cuối (zero-padding)
    """
    if base == 16:
        data = map(lambda x: bin(int(x, base))[2:], data)
    rs = 0
    for item in data:
        rs += int(item, 2)
    rs = bin(rs)[2:]
    while len(rs) > length:
        offset = len(rs) - length
        rs = bin(
            int(rs[: offset], 2) + int(rs[offset:], 2)
        )[2:]
    
    rs = rs.zfill(length)
    #đảo bit
    rs = map(lambda x: '0' if x == '1' else '1', rs)
    return ''.join(rs)

if __name__ == '__main__':
    # CRC
    d = 'A0B1'
    g = '1001'
    base = 16
    print("CRC", crc(d, g, base))

    # Check sum
    data = ['10011001', '11100010', '00100100', '10000100']
    print('Check sum: ', checksum(data, length=8, base=2))
    hex_data = ['1200', '0100', 'A000']
    print('CheckSum Hex', hex(int(checksum(hex_data, length= 16, base=16), 2))[2:].upper())
