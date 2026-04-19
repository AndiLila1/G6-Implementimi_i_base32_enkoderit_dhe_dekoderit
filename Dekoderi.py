alfabeti_dhe_numrat = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
def base32_to_bits(text: str) -> str:
  bits = ""
  for char in text:
    index = alfabeti_dhe_numrat.index(char)
    bits += f"{index:05b}"
  return bits

def bits_to_bytes(bits: str) -> bytes:
    rezultat = bytearray()
    for i in range(0, len(bits), 8):
        byte_chunk = bits[i:i+8]
        if len(byte_chunk) == 8:
            rezultat.append(int(byte_chunk, 2))
    return bytes(rezultat)
    
def decode_base32(text: str) -> bytes:
  text = text.strip().replace(" ","").upper().rstrip("=")  
  bits = base32_to_bits(text)
  bits = bits[:len(bits) - (len(bits) % 8)]               
  return bits_to_bytes(bits)
  
