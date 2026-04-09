alfabeti_dhe_numrat = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
def encode_i_base32(data: bytes)-> str:
    bits = ""
    for byte in data:
        bits += f"{byte:08b}"
    result = ""