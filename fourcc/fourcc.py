def decode_fourcc(cc):
    """convert fourcc number to str"""
    return "".join([chr((int(cc) >> 8 * i) & 0xFF) for i in range(4)])