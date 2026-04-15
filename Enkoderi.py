alfabeti_dhe_numrat = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
def bytes_to_bits(data: bytes) -> str:
    bits = ""
    for byte in data:
        bits += f"{byte:08b}"
    return bits
def split_bits(bits: str):
    chunks = []
    for i in range(0, len(bits), 5):
        chunk = bits[i:i+5]
        if len(chunk) < 5:
            chunk = chunk.ljust(5, "0")
        chunks.append(chunk)
    return chunks

def chunks_to_base32(chunks):
    result = ""
    for chunk in chunks:
        index = int(chunk, 2)
        result += alfabeti_dhe_numrat[index]
    return result

